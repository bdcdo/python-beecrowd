#!/usr/bin/env python3
"""Download missing HTML files from resources.beecrowd.com."""
import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path

BASE_DIR = Path("/home/brunodcdo/Desktop/dev/2026/23_URI")
HTML_DIR = BASE_DIR / "html_raw"
PROBLEMS_FILE = BASE_DIR / "problems_list.json"

RESOURCE_URL = "https://resources.beecrowd.com/repository/UOJ_{pid}.html"


def get_missing_ids():
    """Return list of problem IDs that don't have an HTML file."""
    with open(PROBLEMS_FILE) as f:
        problems = json.load(f)
    all_ids = {p["id"] for p in problems}
    existing = {f.replace(".html", "") for f in os.listdir(HTML_DIR) if f.endswith(".html")}
    return sorted(all_ids - existing, key=int)


def download_html(pid):
    """Try to download HTML for a problem ID. Returns True on success."""
    url = RESOURCE_URL.format(pid=pid)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read()
            if len(html) < 100:
                return False
            out_path = HTML_DIR / f"{pid}.html"
            out_path.write_bytes(html)
            return True
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return False


def main():
    missing = get_missing_ids()
    print(f"[*] {len(missing)} problemas faltantes para baixar")

    success = 0
    failed = []

    for i, pid in enumerate(missing):
        print(f"  [{i+1}/{len(missing)}] Baixando {pid}...", end=" ")
        if download_html(pid):
            print("OK")
            success += 1
        else:
            print("FALHOU")
            failed.append(pid)
        time.sleep(0.3)

    print(f"\n[*] Baixados: {success}, Falharam: {len(failed)}")
    if failed:
        print(f"[*] IDs que falharam: {failed}")
        # Save failed IDs for Playwright fallback
        failed_path = BASE_DIR / "scripts" / "failed_downloads.json"
        with open(failed_path, "w") as f:
            json.dump(failed, f)
        print(f"[*] IDs salvos em {failed_path}")


if __name__ == "__main__":
    main()
