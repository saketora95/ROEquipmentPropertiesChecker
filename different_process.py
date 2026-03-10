from console_printer import print_by_indent as pbi

def prop_file_to_dict(file_path, file_name, encoding='utf-8', indent_number=3):
    prop_file_lines = open(file_path + file_name, 'r', encoding=encoding).readlines()

    data_dict = {}
    item_id = ''
    in_target_area = False
    for i in range(0, len(prop_file_lines)):
        if prop_file_lines[i] == 'Item = {\n':
            in_target_area = True
            continue
        
        if not in_target_area:
            continue

        if prop_file_lines[i].startswith('SkillGroup'):
            break

        front_brackets_index = prop_file_lines[i].find('[')
        if front_brackets_index != -1:
            item_id = prop_file_lines[i][front_brackets_index + 1:prop_file_lines[i].find(']')]
            if item_id in data_dict:
                pbi(indent_number, f'- 警告 ! 檔案 {file_name} 中的 Item ID {item_id} 於第 {i} 行重複出現 !')
            else:
                data_dict[item_id] = ''
    
        data_dict[item_id] += prop_file_lines[i]
    
    pbi(indent_number, f'- 檔案 {file_name} 整理出 {len(data_dict)} 筆資料。')
    return data_dict

def dict_compare(old_data_dict, new_data_dict, output_file_path, indent_number=3):
    output_file = open(output_file_path + 'RawCompareResult.txt', 'w', encoding='utf-8')

    for old_key in old_data_dict:
        if old_key not in new_data_dict:
            output_file.write(f'# {old_key} (資料移除)\n{old_data_dict[old_key]}\n')
            pbi(indent_number, f'- 發現 資料移除 : {old_key}')

    for new_key in new_data_dict:
        if new_key in old_data_dict and old_data_dict[new_key] != new_data_dict[new_key]:
            output_file.write(f'# {new_key} (內容調整)\n{new_data_dict[new_key]}\n')
            pbi(indent_number, f'- 發現 內容調整 : {new_key}')
            continue

        if new_key not in old_data_dict:
            output_file.write(f'# {new_key} (新增資料)\n{new_data_dict[new_key]}\n')
            pbi(indent_number, f'- 發現 新增資料 : {new_key}')
            continue
