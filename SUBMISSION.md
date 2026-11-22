# 第十週作業繳交內容

## 繳交標題

長庚 B1228010 AI四 李怡萱 RoomQuest Agent Wiki

## 1. LLM Wiki 主題與簡短介紹

我的 LLM Wiki 主題是「RoomQuest Agent Wiki：AI 如何把真實空間變成可驗證的解謎遊戲」。

我以 RoomQuest 期末專案為案例，整理生成式 AI Agent 需要的六個核心概念：Context 與 Grounding、結構化場景資料、兩階段規劃、Python Verifier、Reflection Loop，以及人工核准與可追溯性。Wiki 的目的不是複製課堂講義，而是把分散在 PDF 與 Notebook 的概念重新整理成可供簡報查詢與重組的知識單元。

本次共 ingest 6 份課程資料：

1. 07 讓 AI 看懂你的世界
2. 08 教 AI 做事的方法
3. 09 換你當老闆
4. Demo07a AI 代理設計模式：Reflection
5. Demo07c Two-Stage CoT
6. RAG 01：打造你的 RAG 系統

正式生成 Wiki 前，我先和 AI 討論題目定位、來源選擇、條目拆分以及哪些內容應捨棄或延後。原本有 8 個候選條目，討論後把「照片解析」併入場景資料、把 Harness 落實到 Verifier 與人工核准，最後收斂為 6 個條目。完整紀錄位於 `logs/discussion-01.md`。

## 2. LLM Wiki 連結或成果

- LLM Wiki：https://lyixuan0718.github.io/roomquest-agent-wiki/wiki/
- GitHub Repository：https://github.com/lyixuan0718/roomquest-agent-wiki
- 來源登記：Repository 內的 `data/source-register.json`
- 生成前討論：https://github.com/lyixuan0718/roomquest-agent-wiki/blob/main/logs/discussion-01.md

Wiki 共包含 6 個條目，每個條目都有來源編號、核心概念、RoomQuest 應用、限制與檢查問題。投影片和 Wiki 的對應另外記錄在 `data/slide-map.json`，可由投影片回到 Wiki，再由 Wiki 回到 ingest 的資料。

## 3. 教學 HTML 簡報連結

https://lyixuan0718.github.io/roomquest-agent-wiki/slides.html

簡報主題為「AI 出題、程式驗題：認識可驗證的生成式 AI Agent」，共 10 頁，內容依序介紹直接生成的問題、AI Model＋Harness、場景 JSON、兩階段規劃、Python 驗證、Reflection、完整 graph、條件唯一性案例與系統限制。可以使用按鈕、方向鍵及空白鍵翻頁或逐步揭示內容。

## 4. Loop / Graph 流程說明

完整流程圖：https://lyixuan0718.github.io/roomquest-agent-wiki/workflow.html

流程為：

> 先討論與收斂 → Ingest 資料 → Normalize 內容 → Source Check → 建立 Wiki → 查詢 Wiki → 規劃簡報大綱 → Traceability Check → 產生與檢查 HTML 簡報

有兩個會重複執行的 loop：

1. 如果 Source Check 發現 PDF 斷字、正文缺失或 Notebook 流程不完整，就回到 Normalize，調整擷取方式後重新檢查。
2. 如果 Traceability Check 發現投影片無法對回 Wiki 或來源，就先回到 Outline 修正；若 Wiki 本身缺少必要概念，再回到 Build Wiki 補充。

這樣設計是因為錯誤越晚發現，重做範圍越大。把資料檢查移到 Wiki 生成前，可以避免錯誤資料一路進入最後的簡報。

## 5. 一次實際執行結果與檢查紀錄

本次先完成一份生成前討論紀錄，再 ingest 3 份 PDF 與 3 份 Notebook，共 6 份資料。第一次 Normalize 時發現兩個問題：PDF 轉成純文字後，出現「換你當　闆」「AI　作現場」「我們做事的　法」等斷裂片段；Notebook 的 Markdown 已說明 writer 寫初稿、reviewer 給建議、writer 產出第二版的流程，但「把第一版和建議組成新的 prompt 再交給 writer」的具體做法只出現在 code cells 裡。

第二次執行改成先定位 PDF 中的概念段落，並同時核對 Notebook 的 Markdown 與 code cells。修正後產生 6 個 Wiki 條目與 10 張投影片。專案驗證程式最後檢查：來源數是否至少 5 份、Wiki 是否包含 source_ids、所有來源與 Wiki ID 是否存在、每張投影片是否至少對應一個 Wiki 條目，以及 4 個 HTML 頁面是否完整。檢查結果為：`PASS sources=6 wiki=6 slides=10 pages=4`。

完整原始片段與修正方式記錄於 `logs/run-01.md`；公開 workflow 頁面列出 9 筆主要紀錄，包含原本缺少的 Retrieve 節點。

## 6. 反思與流程調整

最常出錯的節點是 Normalize，而不是最後的 HTML 生成。PDF 的版面可能造成斷字，Notebook 的知識又分散在說明文字與程式碼中；如果一開始沒有發現，後面的 Wiki 和簡報即使排版完整，內容仍可能缺漏。

因此我把檢查從「簡報完成後」往前移到「Normalize 後、Build Wiki 前」，新增 Source Check，要求每份資料必須具有可讀正文、來源 ID 與可使用的概念。另外新增 Traceability Check，要求每張投影片都能對應到 Wiki 與來源。修改後的 workflow 可以讓錯誤回到負責的前一個節點，而不需要重新生成整份成果。
