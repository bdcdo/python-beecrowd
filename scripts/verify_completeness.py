#!/usr/bin/env python3
"""Verify completeness of parsed markdown files against problems_list.json."""
import json
import re
import unicodedata
from pathlib import Path

BASE_DIR = Path("/home/brunodcdo/Desktop/dev/2026/23_URI")
MD_DIR = BASE_DIR / "beecrowd_iniciante"
PROBLEMS_FILE = BASE_DIR / "problems_list.json"


def slugify(name):
    slug = name.lower().replace(" ", "_")
    slug = unicodedata.normalize("NFKD", slug).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9_]", "_", slug)
    slug = re.sub(r"_+", "_", slug)
    return slug.strip("_")


def main():
    with open(PROBLEMS_FILE) as f:
        problems = json.load(f)

    print(f"[*] Verificando {len(problems)} problemas...\n")

    complete = []
    incomplete = []
    missing_file = []

    for prob in sorted(problems, key=lambda p: int(p["id"])):
        pid = prob["id"]
        name = prob["name"]
        slug = slugify(name)
        md_path = MD_DIR / f"{pid}_{slug}.md"

        if not md_path.exists():
            missing_file.append((pid, name))
            continue

        content = md_path.read_text(encoding="utf-8")

        has_desc = "## Descricao" in content or "## Descrição" in content
        has_entrada = "## Entrada" in content
        has_saida = "## Saida" in content or "## Saída" in content
        has_exemplo = "## Exemplo" in content

        if has_desc or (has_entrada and has_saida):
            complete.append(pid)
        else:
            incomplete.append((pid, name, has_desc, has_entrada, has_saida, has_exemplo))

    print(f"  Completos:       {len(complete)}/{len(problems)}")
    print(f"  Incompletos:     {len(incomplete)}")
    print(f"  Arquivo ausente: {len(missing_file)}")

    if missing_file:
        print(f"\n[!] Arquivos ausentes:")
        for pid, name in missing_file:
            print(f"  - {pid}: {name}")

    if incomplete:
        print(f"\n[!] Problemas incompletos (sem Descricao/Entrada/Saida):")
        for pid, name, d, e, s, ex in incomplete:
            flags = []
            if not d: flags.append("sem descricao")
            if not e: flags.append("sem entrada")
            if not s: flags.append("sem saida")
            if not ex: flags.append("sem exemplo")
            print(f"  - {pid}: {name} ({', '.join(flags)})")

    if not missing_file and not incomplete:
        print("\n[+] Todos os 334 problemas estao completos!")

    return len(complete), len(incomplete), len(missing_file)


if __name__ == "__main__":
    main()
