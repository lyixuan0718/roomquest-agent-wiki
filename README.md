# RoomQuest Agent Wiki

第十週作業：以 6 份課堂講義與 notebook 建立 LLM Wiki，再把 Wiki 整理成可直接瀏覽的教學型 HTML 簡報。

## 公開成果

- 專案入口：https://lyixuan0718.github.io/roomquest-agent-wiki/
- LLM Wiki：https://lyixuan0718.github.io/roomquest-agent-wiki/wiki/
- 教學 HTML 簡報：https://lyixuan0718.github.io/roomquest-agent-wiki/slides.html
- Loop / Graph 與執行紀錄：https://lyixuan0718.github.io/roomquest-agent-wiki/workflow.html

## 本次知識流程

1. Ingest：讀取 6 份課程資料。
2. Normalize：擷取標題、正文與可追溯的來源編號。
3. Check：確認每筆資料有內容、來源和可用概念。
4. Build Wiki：整理成 6 個可重複使用的知識條目。
5. Retrieve & Outline：依教學問題挑選條目並規劃投影片。
6. Traceability Check：檢查每張投影片都能對回 Wiki 與來源。
7. Generate & Review：產生 HTML 簡報，檢查順序、可讀性與互動。

## 本機檢查

```bash
python scripts/validate_project.py
node --check assets/app.js
```

## 資料誠信

本 repository 不重新上傳課堂 PDF。`data/source-register.json` 僅記錄課程提供的資料名稱、類型、用途與可公開的原始 notebook 連結。Wiki 是本作業針對 RoomQuest 主題重新整理的教學摘要，不宣稱是講義原文。

