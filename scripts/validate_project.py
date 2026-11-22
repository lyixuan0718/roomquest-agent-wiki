from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str):
    with (ROOT / relative).open(encoding="utf-8") as handle:
        return json.load(handle)


def fail(message: str) -> None:
    raise AssertionError(message)


sources_data = load_json("data/source-register.json")
slides_data = load_json("data/slide-map.json")
sources = sources_data.get("sources", [])
slides = slides_data.get("slides", [])

if len(sources) < 5:
    fail("至少需要 ingest 5 份資料")
if sources_data.get("ingest_count") != len(sources):
    fail("ingest_count 與 sources 數量不一致")

source_ids = {item["id"] for item in sources}
if len(source_ids) != len(sources):
    fail("來源 ID 重複")

wiki_files = sorted((ROOT / "wiki").glob("[0-9][0-9]-*.md"))
if not wiki_files:
    fail("找不到 Wiki Markdown")

wiki_ids: set[str] = set()
for path in wiki_files:
    text = path.read_text(encoding="utf-8")
    id_match = re.search(r"^id:\s*(W\d+)\s*$", text, re.MULTILINE)
    source_match = re.search(r"^source_ids:\s*\[([^]]+)\]", text, re.MULTILINE)
    if not id_match or not source_match:
        fail(f"{path.name} 缺少 id 或 source_ids")
    wiki_id = id_match.group(1)
    wiki_ids.add(wiki_id)
    referenced = {item.strip() for item in source_match.group(1).split(",")}
    unknown = referenced - source_ids
    if unknown:
        fail(f"{path.name} 引用不存在的來源：{sorted(unknown)}")
    for heading in ("## 核心概念", "## RoomQuest 應用", "## 限制", "## 檢查問題"):
        if heading not in text:
            fail(f"{path.name} 缺少固定段落：{heading}")

if len(slides) != 10:
    fail("教學簡報必須有 10 張投影片")

for expected, slide in enumerate(slides, start=1):
    if slide.get("number") != expected:
        fail(f"投影片編號不連續：預期 {expected}")
    if not slide.get("wiki_ids"):
        fail(f"第 {expected} 頁沒有 Wiki 對應")
    if set(slide["wiki_ids"]) - wiki_ids:
        fail(f"第 {expected} 頁引用不存在的 Wiki ID")
    if set(slide.get("source_ids", [])) - source_ids:
        fail(f"第 {expected} 頁引用不存在的來源 ID")

required_pages = ["index.html", "wiki/index.html", "slides.html", "workflow.html"]
for relative in required_pages:
    path = ROOT / relative
    if not path.exists():
        fail(f"缺少頁面：{relative}")
    text = path.read_text(encoding="utf-8")
    if "<title>" not in text:
        fail(f"頁面沒有 title：{relative}")
    if "TODO" in text:
        fail(f"頁面仍有 TODO：{relative}")

discussion = ROOT / "logs/discussion-01.md"
if not discussion.exists():
    fail("缺少生成前討論紀錄 logs/discussion-01.md")
discussion_text = discussion.read_text(encoding="utf-8")
for heading in ("為什麼選 RoomQuest", "為什麼選這 6 份資料", "Wiki 條目如何決定", "捨棄或延後的內容"):
    if heading not in discussion_text:
        fail(f"討論紀錄缺少段落：{heading}")

workflow_text = (ROOT / "workflow.html").read_text(encoding="utf-8")
for required_term in ("Discuss", "Retrieve", "discussion-01.md"):
    if required_term not in workflow_text:
        fail(f"workflow.html 缺少：{required_term}")

slide_html = (ROOT / "slides.html").read_text(encoding="utf-8")
slide_sections = re.findall(r'<section class="slide(?: active)?">', slide_html)
if len(slide_sections) != 10:
    fail("slides.html 的投影片 section 數量不是 10")

print(f"PASS sources={len(sources)} wiki={len(wiki_files)} slides={len(slides)} pages={len(required_pages)}")
