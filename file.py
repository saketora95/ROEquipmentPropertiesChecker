import os
import shutil
from console_printer import print_by_indent as pbi

def is_file_exist(file_path, file_name):
    return os.path.exists(file_path + file_name)

def copy_to(input_file, target_file):
    shutil.copy(input_file, target_file)

def get_file_list(file_path, specific_end=None):
    file_list = []
    for f in os.listdir(file_path):
        full_path = os.path.join(file_path, f)
        if os.path.isfile(full_path):
            if specific_end is None or f.lower().endswith(specific_end):
                file_list.append(full_path.split('\\')[-1])

    return file_list

def remove_old_file(file_path, file_name_list, max_file_number, pbi_indent=2):
    if len(file_name_list) <= max_file_number:
        pbi(pbi_indent, f'- 於 Output 資料夾內的檔案數量，目前低於 {max_file_number} 個，略過清理步驟。')
        return file_name_list
    
    pbi(pbi_indent, f'- 於 Output 資料夾內的檔案數量，目前多於 {max_file_number} 個，執行清理步驟。')
    pbi_indent += 1
    while len(file_name_list) > max_file_number:
        full_file_path = file_path + file_name_list[0]
        if os.path.exists(full_file_path):
            os.remove(full_file_path)
            pbi(pbi_indent, f'- 刪除檔案: {full_file_path}')
        del file_name_list[0]
    pbi_indent -= 1
    pbi(pbi_indent, f'- 於 Output 資料夾內的檔案數量，已經等於 {max_file_number} 個，結束清理步驟。')
    return file_name_list