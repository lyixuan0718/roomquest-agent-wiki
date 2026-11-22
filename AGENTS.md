# AGENTS.md

## 專案目的

這是一個以 RoomQuest 為案例的生成式 AI Agent 教學網站。它必須同時呈現三件事：可追溯的 LLM Wiki、適合初學者的 HTML 簡報，以及可重現的 loop / graph 與執行紀錄。

## 內容原則

- 建立新一輪 Wiki 前，先在 `logs/discussion-XX.md` 記錄主題範圍、來源選擇、條目拆分與捨棄內容；討論完成後才能生成。
- 先讀 `data/source-register.json`，只使用登記過的來源。
- Wiki 條目不得冒充講義原文；必須標示為針對本專案整理的摘要。
- 每個 Wiki 條目最少對應一個 `source_id`。
- 每張投影片最少對應一個 Wiki 條目；對應關係寫在 `data/slide-map.json`。
- 不把「檢索相似」寫成「內容正確」，也不把規則驗證寫成百分之百保證。
- RoomQuest 尚未完成的功能一律標示為「設計」或「示意」，不得寫成已完成。

## 頁面結構

- `index.html`：入口與成果總覽。
- `wiki/index.html`：六個 Wiki 條目與來源追蹤。
- `slides.html`：十頁教學 HTML 簡報。
- `workflow.html`：loop / graph、執行紀錄與反思。
- `wiki/*.md`：可供 AI 讀取與重組的知識單元。
- `logs/*.md`：每次實際執行的紀錄。
- `logs/discussion-*.md`：生成前的討論與收斂決策。

## 新增 Wiki 條目

1. 檔名使用兩位數編號與英文小寫，例如 `07-answer-normalization.md`。
2. 開頭必須包含 `id`、`title`、`source_ids`、`status`。
3. 內文固定包含：核心概念、RoomQuest 應用、限制與檢查問題。
4. 在 `wiki/index.md` 增加索引。
5. 在 `data/source-register.json` 的 `used_in` 登記條目。

## 新增或修改投影片

1. 每頁只教一個主要概念。
2. 先修改 `data/slide-map.json`，再修改 `slides.html`。
3. 每頁應有「這頁要懂什麼」與來源標籤；案例頁要清楚區分輸入、判斷與輸出。
4. 簡報維持 16:9 的單頁閱讀感；桌機與手機都不能水平溢出。
5. 不使用假統計、假使用者回饋或無來源的技術結論。

## 視覺與互動規則

- 米白紙張、深藍文字、芥末黃與珊瑚紅為主色，不使用漸層。
- 避免 AI 儀表板風格、發光特效、大量膠囊標籤和無意義圖示。
- 互動必須幫助理解：翻頁、逐步揭示、來源對照與模式切換。
- 正文至少 16px；按鈕需有清楚文字與鍵盤 focus 樣式。

## 完成定義

- `python scripts/validate_project.py` 通過。
- `node --check assets/app.js` 通過。
- 來源數不少於 5，且每張投影片可追溯到 Wiki。
- 至少有一份生成前討論紀錄，並在 workflow 與繳交說明中連結。
- 四個 HTML 頁面可直接由相對路徑開啟。
- 沒有 `TODO`、假連結或未標示的未完成功能。

