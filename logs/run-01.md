# Run 01：從課程資料到 RoomQuest 教學簡報

- 執行日期：2026-11-21
- 目標：ingest 至少 5 份資料，建立可追溯的 Wiki 與 10 頁教學 HTML 簡報
- 實際 ingest：6 份資料

## 執行結果

| 節點 | 輸入 | 檢查 | 結果 |
|---|---|---|---|
| Discuss | 主題需求與候選資料 | 題目是否生活化、能對應課程、不是成熟產品的簡化版 | 通過；收斂為 6 個條目 |
| Ingest | 3 PDF + 3 Notebook | 檔案可讀、數量 >= 5 | 通過 |
| Normalize v1 | PDF 全文、Notebook markdown | 中文完整、流程概念完整 | 不通過 |
| Normalize v2 | 概念段落 + Notebook code cells | 標題、正文、來源 ID、核心流程 | 通過 |
| Build Wiki | 6 份正規化資料 | 每頁有來源、限制、檢查問題 | 通過，產出 W01–W06 |
| Retrieve | 教學問題 + 6 個 Wiki 條目 | 取回內容是否能回答目前投影片的教學目標 | 通過；每頁取用 1–5 個條目 |
| Outline | 6 個 Wiki 條目 | 初學者可依序理解 | 通過，產出 10 頁結構 |
| Trace Check | slide-map.json | 每頁至少有 1 個 wiki_id，ID 皆存在 | 通過 |
| HTML Review | 4 個 HTML 頁面 | 連結、互動、手機版、JS 語法 | 通過 |

## 發現的問題

1. PDF 轉純文字後，某些中文字會因投影片排版而斷裂。全文仍適合定位概念，但不適合直接複製成 Wiki。
2. Reflection Notebook 的 Markdown 已列出 writer 初稿、reviewer 建議、writer 第二版等 5 步概念流程；但「把第一版和建議組成新的 prompt，再交給 writer」的具體串接方式在 code cells 裡。Two-Stage CoT 的 Markdown 也說明了先思考、後產文，但 code cells 才能核對兩次模型呼叫如何傳遞結果。

## 原始片段（保留第一次失敗的證據）

PDF 第一次抽出的片段不是可直接使用的完整句子，例如：

```text
換你當   闆：Agentic Work 與 AI   作現場
老
            工
回憶我們 AI Agents 的定義
就是教 AI「我們做事的 法」做事情。
AI Agent = AI Model + Harness
```

可以看出英文關鍵詞仍在，但「老闆」「工作」「方法」被版面拆散。因此 v2 不直接摘要整份純文字，而是用關鍵詞定位段落，再回到原始頁面核對。

Notebook 的 Markdown 已說明完整 5 步流程，也包含「設定作者和審查員」標題；但沒有呈現第一版文字與 reviewer 建議如何被組成下一次呼叫的 prompt。檢查 code cells 後才確認具體串接方式。

以下為節錄、簡化版本，用來保留資料流，並非逐字複製完整函式參數與 prompt：

```python
# Step 2: Reviewer 給建議
suggestion = reply(system_reviewer, first_version, ...)

# Step 3: Writer 根據建議產出第二版
second_prompt = f"這是我剛剛寫的貼文：\n{first_version}\n\n這是修改建議：\n{suggestion}\n\n請根據這些建議產出第二版。"
```

這個差異使 Source Check 必須在建立 Wiki 之前完成。

## 調整

- 將 Source Check 從「簡報完成後」前移到「Normalize 後」。
- Notebook 同時核對 markdown 與 code cells。
- Wiki 每頁加入 `source_ids`；簡報另以 `slide-map.json` 記錄每頁對應。
- 驗證腳本拒絕不存在的來源或 Wiki ID，也拒絕沒有知識對應的投影片。

## 反思

最常出錯的節點是 Normalize，而不是最後的 HTML。來源資料若在一開始就斷字或漏掉程式邏輯，後續生成得再漂亮也只是放大錯誤。因此 workflow 增加前置的 Source Check，並讓錯誤回到 Normalize，而不是整份 Wiki 與簡報一起重做。

