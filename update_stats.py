import re
import sys
from datetime import datetime, timezone, timedelta
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

# 여기에 본인 CodeUp 아이디를 넣으세요 (예: fcode)
USERNAME = "fcode"

README_PATH = "README.md"
SVG_PATH = "codeup-stats.svg"
START_MARKER = "<!-- CODEUP-STATS:START -->"
END_MARKER = "<!-- CODEUP-STATS:END -->"

GREEN = "#2da44e"


def fetch_stats(username: str) -> dict:
    url = f"https://codeup.kr/userinfo.php?user={quote(username)}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    stats = {}
    for row in soup.select("table.table tr"):
        cells = row.find_all("td")
        if len(cells) != 2:
            continue
        label = cells[0].get_text(strip=True)
        value = cells[1].get_text(strip=True)
        stats[label] = value

    level_tag = soup.select_one("#lv")
    if level_tag:
        stats["레벨"] = level_tag.get_text(strip=True)

    required = ["순위", "푼 문제 수"]
    missing = [key for key in required if key not in stats]
    if missing:
        raise RuntimeError(
            f"페이지 구조가 바뀐 것 같습니다(또는 아이디가 존재하지 않습니다). 못 찾은 항목: {missing}"
        )

    return stats


def build_svg(username: str, stats: dict) -> str:
    level_match = re.search(r"Lv\.(\d+)", stats.get("레벨", ""))
    level = level_match.group(1) if level_match else "-"

    rank_raw = stats.get("순위", "-위")
    rank_num = rank_raw[:-1] if rank_raw.endswith("위") else rank_raw

    solved_raw = stats.get("푼 문제 수", "0")
    try:
        solved = f"{int(solved_raw.replace(',', '')):,}"
    except ValueError:
        solved = solved_raw

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="700" height="226" viewBox="0 0 700 226" xmlns="http://www.w3.org/2000/svg" font-family="'Apple SD Gothic Neo','Segoe UI','Pretendard',sans-serif">
  <rect x="0.5" y="0.5" width="699" height="225" rx="20" fill="#ffffff" stroke="#000000" stroke-width="1"/>

  <text x="24" y="30" font-size="14" font-weight="600" fill="#1f2328">{username} <tspan fill="#57606a">· CodeUp Stats</tspan></text>

  <line x1="233.33" y1="50" x2="233.33" y2="212" stroke="#d0d7de" stroke-width="1.25"/>
  <line x1="466.67" y1="50" x2="466.67" y2="212" stroke="#d0d7de" stroke-width="1.25"/>

  <text x="116.67" y="132" font-size="38" font-weight="800" fill="{GREEN}" text-anchor="middle">{solved}</text>
  <text x="116.67" y="200" font-size="13" font-weight="600" fill="#57606a" text-anchor="middle" letter-spacing="1.5">SOLVED</text>

  <circle cx="350" cy="120" r="44" fill="none" stroke="{GREEN}" stroke-width="4"/>
  <circle cx="350" cy="69" r="4" fill="{GREEN}"/>
  <text x="350" y="132" font-size="32" font-weight="800" fill="{GREEN}" text-anchor="middle">{level}</text>
  <text x="350" y="200" font-size="13" font-weight="600" fill="#57606a" text-anchor="middle" letter-spacing="1.5">LEVEL</text>

  <text x="583.33" y="132" font-size="38" font-weight="800" fill="{GREEN}" text-anchor="middle">{rank_num}</text>
  <text x="583.33" y="200" font-size="13" font-weight="600" fill="#57606a" text-anchor="middle" letter-spacing="1.5">RANK</text>
</svg>
'''


def build_readme_block() -> str:
    kst = timezone(timedelta(hours=9))
    now = datetime.now(kst).strftime("%Y-%m-%d %H:%M KST")
    return "\n".join(
        [
            START_MARKER,
            f'<img src="{SVG_PATH}" width="480" alt="CodeUp Stats" />',
            "",
            f"_마지막 업데이트: {now}_",
            END_MARKER,
        ]
    )


def update_readme(block: str):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if START_MARKER not in content or END_MARKER not in content:
        raise RuntimeError(
            f"README.md에 {START_MARKER} ~ {END_MARKER} 마커가 없습니다. 먼저 추가해주세요."
        )

    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    new_content = pattern.sub(block, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    username = sys.argv[1] if len(sys.argv) > 1 else USERNAME
    stats = fetch_stats(username)

    svg = build_svg(username, stats)
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg)

    block = build_readme_block()
    update_readme(block)

    print("README.md, codeup-stats.svg 업데이트 완료")
    print(stats)


if __name__ == "__main__":
    main()
