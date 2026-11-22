# Discussion 01：先討論、後生成

- 討論時間：2026-11-21，Wiki 生成前
- 討論目標：先確認主題、資料範圍與知識架構，再開始產生 Wiki 條目
- 最終主題：RoomQuest Agent Wiki——AI 如何把真實空間變成可驗證的解謎遊戲

## 1. 為什麼選 RoomQuest

一開始曾比較「RoomQuest」與「斷捨離助手」兩個生活化題目。最後選 RoomQuest，原因是它除了能做成可展示的作品，也能明確對應課堂的 Context Engineering、Planning、Tool Use、Reflection 與 Harness；核心流程還能延伸到其他需要多模態理解與輸出驗證的專案。

討論中也先排除「做一個成熟產品的簡化版」。因此 Wiki 不以介紹密室逃脫產品功能為主，而是集中回答一個技術問題：

> 生成式 AI 如何利用真實場景出題，同時讓結果可以被程式檢查？

## 2. 為什麼選這 6 份資料

| 來源 | 選擇原因 |
|---|---|
| 07 讓 AI 看懂你的世界 | 支撐 Context、RAG、Grounding 與「只使用已取得資料」的概念。 |
| 08 教 AI 做事的方法 | 同時包含 Tool Use、JSON、Planning 與 Reflection，是 RoomQuest 流程的主要課程依據。 |
| 09 換你當老闆 | 提供「AI Agent = AI Model + Harness」及 loop／graph 的整體定位。 |
| Demo07a Reflection | 有作者、審查者、依建議重寫的可執行範例。 |
| Demo07c Two-Stage CoT | 提供「先拆解、後執行」的兩階段規劃範例。 |
| RAG 01 | 提供資料擷取、metadata、完整性檢查與可追溯保存的實作原則。 |

選擇原則不是「資料越多越好」，而是每份資料都必須對應到 RoomQuest 的一個必要節點。其他週次的神經網路、機率生成與一般聊天機器人講義雖然相關，但無法直接支撐這份簡報的主線，因此沒有 ingest。

## 3. Wiki 條目如何決定

討論初稿曾列出 8 個候選條目：

1. 照片解析
2. Context 與 Grounding
3. 場景 JSON
4. 兩階段規劃
5. Python Verifier
6. Reflection Loop
7. Harness
8. 人工核准與可追溯性

最後收斂成 6 個條目：

| 最終條目 | 討論決定 |
|---|---|
| W01 Context 與 Grounding | 保留；回答模型可以使用哪些資料。 |
| W02 結構化場景資料 | 將「照片解析」合併進來；課堂沒有提供特定 VLM 實作，不另外寫成看似已完成的能力。 |
| W03 兩階段規劃 | 保留；先規劃結構，再撰寫線索。 |
| W04 Python Verifier | 將 Harness 的規則、工具與停止條件放進實際驗證器，不另做抽象條目。 |
| W05 Reflection Loop | 保留；說明錯誤原因如何回到指定關卡重寫。 |
| W06 人工核准與可追溯性 | 合併 Harness 的人工出口與 RAG metadata／保存概念。 |

## 4. 捨棄或延後的內容

- **Embedding 模擬玩家**：有趣，但相似度不是正確率，容易讓初學者誤以為 embedding 可以直接保證線索品質，因此不放入主教學線。
- **拍照作答與 bounding box**：屬於 RoomQuest 的未來功能，尚未實作，不寫成現有能力。
- **RAG 謎題類型庫**：可以作為延伸，但不是本次說明「可驗證生成」的必要節點。
- **多模型投票**：需要額外實驗才能說明效果，這次不做沒有紀錄的結論。

## 5. 討論後才開始生成

確認上述範圍後，才建立 W01–W06 的 Markdown。每個條目固定包含「核心概念、RoomQuest 應用、限制、檢查問題」，並以 `source_ids` 連回來源。簡報則在 Wiki 完成後再產生，不直接由六份原始資料跳到投影片。

