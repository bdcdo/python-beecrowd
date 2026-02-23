#!/usr/bin/env python3
"""Download missing HTML files using Playwright (for problems not available via direct HTTP)."""
import json
import os
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE_DIR = Path("/home/brunodcdo/Desktop/dev/2026/23_URI")
HTML_DIR = BASE_DIR / "html_raw"
PROBLEMS_FILE = BASE_DIR / "problems_list.json"

EMAIL = os.environ.get("BEECROWD_EMAIL", "")
SENHA = os.environ.get("BEECROWD_SENHA", "")

RESOURCE_URL = "https://resources.beecrowd.com/repository/UOJ_{pid}.html"


def get_missing_ids():
    with open(PROBLEMS_FILE) as f:
        problems = json.load(f)
    all_ids = {p["id"] for p in problems}
    existing = {f.replace(".html", "") for f in os.listdir(HTML_DIR) if f.endswith(".html")}
    return sorted(all_ids - existing, key=int)


def login(page):
    print("[*] Fazendo login...")
    page.goto("https://judge.beecrowd.com/pt/login", wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(3000)

    if "login" not in page.url:
        print("[+] Já logado!")
        return True

    page.fill('input[name="email"]', EMAIL)
    page.fill('input[name="password"]', SENHA)
    page.click("#submit-btn")
    page.wait_for_timeout(5000)

    if "login" not in page.url:
        print("[+] Login OK!")
        return True
    else:
        print("[-] Login falhou!")
        return False


def main():
    missing = get_missing_ids()
    print(f"[*] {len(missing)} problemas faltantes")

    if not missing:
        print("[+] Nenhum problema faltante!")
        return

    if not EMAIL or not SENHA:
        print("[-] Defina BEECROWD_EMAIL e BEECROWD_SENHA")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        if not login(page):
            browser.close()
            return

        success = 0
        failed = []

        for i, pid in enumerate(missing):
            url = RESOURCE_URL.format(pid=pid)
            out_path = HTML_DIR / f"{pid}.html"
            print(f"  [{i+1}/{len(missing)}] {pid}...", end=" ", flush=True)

            try:
                page.goto(url, wait_until="domcontentloaded", timeout=15000)
                page.wait_for_timeout(1000)
                html = page.content()

                if len(html) > 500 and "problem" in html:
                    out_path.write_text(html, encoding="utf-8")
                    print("OK")
                    success += 1
                else:
                    print("SEM CONTEUDO")
                    failed.append(pid)
            except Exception as e:
                print(f"ERRO: {e}")
                failed.append(pid)

            time.sleep(0.5)

        browser.close()

    print(f"\n[*] Baixados: {success}, Falharam: {len(failed)}")
    if failed:
        print(f"[*] IDs que falharam: {failed}")
        failed_path = BASE_DIR / "scripts" / "failed_downloads.json"
        with open(failed_path, "w") as f:
            json.dump(failed, f)


if __name__ == "__main__":
    main()
