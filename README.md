# 功能摘要
處理 `equipmentproperties` 檔案在更新前後的差異，將其挑選出來並輸出成 `txt` 檔案以利於閱讀。

# 前置準備
1. 安裝 `GRF Editor` 或具備類似功能的軟體
2. 使用上述軟體，將 `equipmentproperties` 檔案以 `txt` 格式輸出
    - 原本慣用的 lub 轉 lua 工具可能因為太舊了，沒辦法正確轉換 `equipmentproperties` 檔案。
    - 一時之間我也沒找到新版本的轉換工具，所以此處一律以 `GRF Editor` 等工具手動處理。
3. 在 `main.py` 所在的目錄中，建立 `Input` 資料夾，並將前一步驟得到的 `equipmentproperties.txt` 放入。

# 操作流程
1. 執行 `main.py`
2. 沒了

執行時 `Input/equipmentproperties.txt` 會以當下的電腦時間命名，複製一份相同檔案至 `Temp/` 當中；若 `Temp/` 底下包含 `5` 份以上的檔案，會先進行一次整理，把較舊的檔案移除。

若經過複製後，`Temp/` 至少有 `2` 份檔案時，程式會讀取最新的兩份檔案並進行比對，最終輸出至 `Output` 資料夾中。

# 輸出結果
## `RawCompareResult.txt`
比對檔案中，是否有刪除、變更或新增。

若為變更，僅會列出有發現不同的項目，不會告知何處不同。

## `ExplainedCompareResult.txt` (實驗性功能)
基於 Regex 的判斷，進行局部的功能註釋以利使用者較容易閱讀。

不過內容中仍有很多 Regex 尚未建置或不明原文語法的意義，因此僅是個實驗性功能。