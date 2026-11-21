# Run 01：從課程資料到 RoomQuest 教學簡報

- 執行日期：2026-11-21
- 目標：ingest 至少 5 份資料，建立可追溯的 Wiki 與 10 頁教學 HTML 簡報
- 實際 ingest：6 份資料

## 執行結果

| 節點 | 輸入 | 檢查 | 結果 |
|---|---|---|---|
| Ingest | 3 PDF + 3 Notebook | 檔案可讀、數量 >= 5 | 通過 |
| Normalize v1 | PDF 全文、Notebook markdown | 中文完整、流程概念完整 | 不通過 |
| Normalize v2 | 概念段落 + Notebook code cells | 標題、正文、來源 ID、核心流程 | 通過 |
| Build Wiki | 6 份正規化資料 | 每頁有來源、限制、檢查問題 | 通過，產出 W01–W06 |
| Outline | 6 個 Wiki 條目 | 初學者可依序理解 | 通過，產出 10 頁結構 |
| Trace Check | slide-map.json | 每頁至少有 1 個 wiki_id，ID 皆存在 | 通過 |
| HTML Review | 4 個 HTML 頁面 | 連結、互動、手機版、JS 語法 | 通過 |

## 發現的問題

1. PDF 轉純文字後，某些中文字會因投影片排版而斷裂。全文仍適合定位概念，但不適合直接複製成 Wiki。
2. Reflection 與 Two-Stage CoT notebook 的 markdown 只說明任務；作者、審查者及兩階段呼叫的具體流程在 code cells 裡。只讀 markdown 會得到不完整知識。

## 調整

- 將 Source Check 從「簡報完成後」前移到「Normalize 後」。
- Notebook 同時核對 markdown 與 code cells。
- Wiki 每頁加入 `source_ids`；簡報另以 `slide-map.json` 記錄每頁對應。
- 驗證腳本拒絕不存在的來源或 Wiki ID，也拒絕沒有知識對應的投影片。

## 反思

最常出錯的節點是 Normalize，而不是最後的 HTML。來源資料若在一開始就斷字或漏掉程式邏輯，後續生成得再漂亮也只是放大錯誤。因此 workflow 增加前置的 Source Check，並讓錯誤回到 Normalize，而不是整份 Wiki 與簡報一起重做。

