---
id: W05
title: Reflection Loop
source_ids: [S02, S04]
status: 教學整理
---

# Reflection Loop

## 核心概念

Reflection 的典型流程是：產生第一版、審查、提供具體建議、再修改。審查不應只說「不好」，而要指出可被修正的問題。

## RoomQuest 應用

Python 將錯誤整理成例如 `AMBIGUOUS_TARGET: obj_03, obj_08 都符合`，AI 只重寫未通過的關卡。迴圈最多兩次；超過上限便交由主持人修改，避免無限重試。

## 限制

Reflection 不代表模型一定會修對。原始規格與程式驗證優先於 Reviewer 的建議，修改後必須重新走同一套檢查。

## 檢查問題

- 回饋是否具體到可修改？
- 是否只修改失敗部分？
- 是否設定重試上限與人工出口？
