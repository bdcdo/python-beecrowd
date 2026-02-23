#!/usr/bin/env python3
"""Parse downloaded Beecrowd HTML files into clean Markdown."""
import json
import re
import textwrap
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

BASE_DIR = Path("/home/brunodcdo/Desktop/dev/2026/23_URI")
HTML_DIR = BASE_DIR / "html_raw"
MD_DIR = BASE_DIR / "beecrowd_iniciante"
PROBLEMS_FILE = BASE_DIR / "problems_list.json"


def clean_text(text):
    """Clean up whitespace in extracted text."""
    if not text:
        return ""
    # Normalize whitespace but preserve intentional newlines
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned.append(line)
    return "\n".join(cleaned)


def extract_text_with_formatting(element):
    """Extract text from an element, converting <strong> to **bold** and <em> to *italic*."""
    if element is None:
        return ""

    parts = []
    for child in element.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif child.name == "strong" or child.name == "b":
            inner = extract_text_with_formatting(child)
            parts.append(f"**{inner.strip()}**")
        elif child.name == "em" or child.name == "i":
            inner = extract_text_with_formatting(child)
            parts.append(f"*{inner.strip()}*")
        elif child.name == "br":
            parts.append("\n")
        elif child.name == "sub":
            parts.append(f"_{child.get_text()}")
        elif child.name == "sup":
            parts.append(f"^{child.get_text()}")
        elif child.name == "img":
            alt = child.get("alt", "")
            src = child.get("src", "")
            if src and "flags" not in src:
                parts.append(f"![{alt}]({src})")
        elif child.name in ("p", "div"):
            inner = extract_text_with_formatting(child)
            parts.append(inner.strip())
            parts.append("\n\n")
        elif child.name == "ul":
            for li in child.find_all("li", recursive=False):
                inner = extract_text_with_formatting(li)
                parts.append(f"- {inner.strip()}\n")
        elif child.name == "ol":
            for idx, li in enumerate(child.find_all("li", recursive=False), 1):
                inner = extract_text_with_formatting(li)
                parts.append(f"{idx}. {inner.strip()}\n")
        else:
            parts.append(extract_text_with_formatting(child))

    return "".join(parts)


def extract_example_text(td):
    """Extract example input/output text from a table cell."""
    if td is None:
        return ""
    # Get text preserving <br> as newlines
    for br in td.find_all("br"):
        br.replace_with("\n")
    text = td.get_text()
    # Clean up: strip each line, remove blank lines
    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def parse_html(html_path, problem_info):
    """Parse a single HTML file and return markdown content."""
    with open(html_path, encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Extract header info
    header = soup.find("div", class_="header")
    title = ""
    author = ""
    timelimit = ""

    if header:
        h1 = header.find("h1")
        title = h1.get_text().strip() if h1 else ""

        author_p = header.find("p")
        if author_p:
            # Remove flag images from author text
            for img in author_p.find_all("img"):
                img.decompose()
            author = author_p.get_text().strip()

        strong = header.find("strong")
        timelimit = strong.get_text().strip() if strong else ""

    # Extract problem content
    problem_div = soup.find("div", class_="problem")
    if not problem_div:
        return None

    # Description
    desc_div = problem_div.find("div", class_="description")
    description = ""
    if desc_div:
        description = extract_text_with_formatting(desc_div).strip()

    # Input
    input_div = problem_div.find("div", class_="input")
    input_text = ""
    if input_div:
        input_text = extract_text_with_formatting(input_div).strip()

    # Output
    output_div = problem_div.find("div", class_="output")
    output_text = ""
    if output_div:
        output_text = extract_text_with_formatting(output_div).strip()

    # Examples (from tables)
    examples = []
    tables = problem_div.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 2:
                # Skip header rows
                cell0_text = cells[0].get_text().strip()
                if "Exemplo" in cell0_text and "Entrada" in cell0_text:
                    continue
                inp = extract_example_text(cells[0])
                out = extract_example_text(cells[1])
                if inp or out:
                    examples.append({"input": inp, "output": out})

    # Build markdown
    pid = problem_info["id"]
    name = problem_info["name"]
    subject = problem_info.get("subject", "")
    level = problem_info.get("level", "")

    md = []
    md.append(f"# {pid} - {title or name}")
    md.append("")
    md.append(f"**Categoria:** Iniciante")
    if subject:
        md.append(f"**Assunto:** {subject}")
    if level:
        md.append(f"**Nivel:** {level}")
    if author:
        md.append(f"**Autor:** {author}")
    if timelimit:
        md.append(f"**{timelimit}**")
    md.append("")
    md.append("---")
    md.append("")

    if description:
        md.append("## Descricao")
        md.append("")
        md.append(description)
        md.append("")

    if input_text:
        md.append("## Entrada")
        md.append("")
        md.append(input_text)
        md.append("")

    if output_text:
        md.append("## Saida")
        md.append("")
        md.append(output_text)
        md.append("")

    if examples:
        for i, ex in enumerate(examples):
            label = f" {i+1}" if len(examples) > 1 else ""
            md.append(f"## Exemplo{label}")
            md.append("")
            if ex["input"]:
                md.append("**Entrada:**")
                md.append("```")
                md.append(ex["input"])
                md.append("```")
                md.append("")
            if ex["output"]:
                md.append("**Saida:**")
                md.append("```")
                md.append(ex["output"])
                md.append("```")
                md.append("")

    return "\n".join(md)


def slugify(name):
    """Convert problem name to filename-safe slug."""
    slug = name.lower()
    slug = slug.replace(" ", "_")
    # Remove accents (simple approach)
    replacements = {
        "a": "a", "e": "e", "i": "i", "o": "o", "u": "u",
        "a": "a", "e": "e", "o": "o",
        "a": "a", "e": "e", "i": "i", "o": "o", "u": "u",
        "c": "c", "n": "n",
    }
    import unicodedata
    slug = unicodedata.normalize("NFKD", slug).encode("ascii", "ignore").decode("ascii")
    # Keep only alphanumeric and underscores
    slug = re.sub(r"[^a-z0-9_]", "_", slug)
    slug = re.sub(r"_+", "_", slug)
    slug = slug.strip("_")
    return slug


def main():
    MD_DIR.mkdir(parents=True, exist_ok=True)

    # Load problem list
    with open(PROBLEMS_FILE) as f:
        problems = json.load(f)

    # Build lookup
    problems_by_id = {p["id"]: p for p in problems}

    # Process each HTML file
    html_files = sorted(HTML_DIR.glob("*.html"))
    print(f"[*] Found {len(html_files)} HTML files to parse")

    success = 0
    failed = []

    for html_path in html_files:
        pid = html_path.stem
        prob_info = problems_by_id.get(pid, {"id": pid, "name": pid})

        try:
            md_content = parse_html(html_path, prob_info)
            if md_content:
                slug = slugify(prob_info.get("name", pid))
                md_filename = f"{pid}_{slug}.md"
                md_path = MD_DIR / md_filename
                md_path.write_text(md_content, encoding="utf-8")
                success += 1
            else:
                print(f"  [-] {pid}: No problem content found")
                failed.append(pid)
        except Exception as e:
            print(f"  [-] {pid}: Error: {e}")
            failed.append(pid)

    print(f"\n[*] Parsed {success} problems, {len(failed)} failed")
    if failed:
        print(f"[*] Failed: {failed}")

    # Generate README
    print("[*] Generating README.md...")
    readme_lines = []
    readme_lines.append("# Beecrowd - Problemas Iniciantes")
    readme_lines.append("")
    readme_lines.append(f"Total de problemas: {success}")
    readme_lines.append("")
    readme_lines.append("| ID | Nome | Assunto | Nivel | Arquivo |")
    readme_lines.append("|---:|------|---------|:-----:|---------|")

    for prob in sorted(problems, key=lambda p: int(p["id"])):
        pid = prob["id"]
        name = prob["name"]
        subject = prob.get("subject", "-")
        level = prob.get("level", "-")
        slug = slugify(name)
        filename = f"{pid}_{slug}.md"
        if (MD_DIR / filename).exists():
            readme_lines.append(f"| {pid} | {name} | {subject} | {level} | [{filename}]({filename}) |")

    readme_path = MD_DIR / "README.md"
    readme_path.write_text("\n".join(readme_lines), encoding="utf-8")
    print(f"[+] README.md generated at {readme_path}")


if __name__ == "__main__":
    main()
