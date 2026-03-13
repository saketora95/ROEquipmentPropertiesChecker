from console_printer import print_by_indent as pbi
import os
import sys
import datetime
import file
import different_process as diff
import effect_explain

DEFAULT_FILE_NAME = 'equipmentproperties.txt'
DATETIME_TEXT = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
EXECUTE_PATH = os.path.abspath(os.path.dirname(__file__)) + '\\'
if getattr(sys, 'frozen', False):
    EXECUTE_PATH = os.path.dirname(sys.executable) + '\\'
INPUT_PATH = EXECUTE_PATH + 'Input\\'
TEMP_PATH = EXECUTE_PATH + 'Temp\\'
OUTPUT_PATH = EXECUTE_PATH + 'Output\\'

indent_number = 0
pbi(indent_number, '# 程式開始執行')

indent_number += 1
pbi(indent_number, '- 程式正常執行時，視窗不會主動關閉。')
pbi(indent_number, '- 若視窗突然消失，表示有地方執行失敗而導致程式自動關閉。\n')

#region 建置必要目錄
pbi(indent_number, '# 建置必要目錄')
indent_number += 1
if not os.path.exists(INPUT_PATH):
    os.makedirs(INPUT_PATH)
    pbi(indent_number, f'- 建立缺少的 Input 資料夾。')
if not os.path.exists(TEMP_PATH):
    os.makedirs(TEMP_PATH)
    pbi(indent_number, f'- 建立缺少的 Temp 資料夾。')
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
    pbi(indent_number, f'- 建立缺少的 Output 資料夾。')
pbi(indent_number, '- 建置必要目錄 : 完成\n')
indent_number -= 1
#endregion

#region 處理新增資料
pbi(indent_number, '# 處理新增資料')
indent_number += 1
if file.is_file_exist(INPUT_PATH, DEFAULT_FILE_NAME):
    pbi(indent_number, f'- 已發現 {DEFAULT_FILE_NAME} 檔案，將其複製至 Temp 資料夾。')
    file.copy_to(
        INPUT_PATH + DEFAULT_FILE_NAME,
        TEMP_PATH + DATETIME_TEXT + '.txt'
    )
else:
    pbi(indent_number, f'- 未發現 {DEFAULT_FILE_NAME} 檔案，無法處理新增資料。')
pbi(indent_number, '- 處理新增資料 : 完成\n')
indent_number -= 1
#endregion

#region 清理舊有資料
pbi(indent_number, '# 清理舊有資料')
indent_number += 1
temp_file_list = file.get_file_list(TEMP_PATH, '.txt')
pbi(indent_number, f'- 於 Temp 資料夾中發現 {len(temp_file_list)} 個 txt 檔案: {temp_file_list}')
if len(temp_file_list) > 5:
    output_file_list = file.remove_old_file(TEMP_PATH, temp_file_list, 5)
pbi(indent_number, '- 清理舊有資料 : 完成\n')
indent_number -= 1
#endregion

#region 進行資料比對
pbi(indent_number, '# 進行資料比對')
indent_number += 1
existCompareResult = False
if len(temp_file_list) >= 2:
    pbi(indent_number, f'- 於 Temp 資料夾中具備 {len(temp_file_list)} 個檔案，準備進行資料比對。')
    old_prop_file_data = diff.prop_file_to_dict(TEMP_PATH, temp_file_list[-2])
    new_prop_file_data = diff.prop_file_to_dict(TEMP_PATH, temp_file_list[-1])

    pbi(indent_number, f'- 資料前處理完成，開始進行資料比對。')
    indent_number += 1
    diff.dict_compare(old_prop_file_data, new_prop_file_data, OUTPUT_PATH, indent_number)
    existCompareResult = True
else:
    pbi(indent_number, f'- 於 Temp 資料夾中內的檔案數量不足，無法進行資料比對。')
pbi(indent_number, '- 進行資料比對 : 完成\n')
indent_number -= 1
#endregion

#region 進行資料註釋
pbi(indent_number, '# 進行資料註釋')
indent_number += 1
if existCompareResult:
    effect_explain.effect_explain(OUTPUT_PATH, 'RawCompareResult.txt', 'ExplainedCompareResult.txt')
else:
    pbi(indent_number, f'- 未執行資料比對，略過資料註釋。')
pbi(indent_number, '- 進行資料註釋 : 完成\n')
indent_number -= 1
#endregion

indent_number = 0
pbi(indent_number, '# 程式結束執行')

os.system('pause')