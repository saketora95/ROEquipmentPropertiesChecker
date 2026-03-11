from console_printer import print_by_indent as pbi
import explain_table as ex_table
import re

test_list = [
    '			local temp = 0',
    '			local temp2 = 0',
    '			temp = get(11)',
    '			SetEquipTempValue(0, temp)',
    '			temp2 = math.floor(temp / 10)',
    '			AddReceiveItem_Equip(7)',
    '			AddEXPPercent_KillRace(9999, 15)',
    '			RaceAddDamage(0, 10)',
    '			AddMdamage_Race(3, 10)',
    '			AddDamage_Size(1, 0, 10)',
    '			AddDamage_Size(1, 1, 10)',
    '			AddDamage_Size(1, 2, 10)',
    '			AddMDamage_Size(1, 0, 10)',
    '			AddMDamage_Size(1, 1, 10)',
    '			AddMDamage_Size(1, 2, 10)',
    '			if temp2 > 20 then',
    '				temp2 = 20',
    '			end',
    '			AddExtParam(0, 47, temp2 * 1)',
    '			AddExtParam(0, 45, temp2 * 3)',
    '			AddExtParam(0, 41, temp2 * 10)',
]

def explain_line(line):
    for pattern, formatter in ex_table.regex_patterns:
        m = re.search(pattern, line)
        if m:
            groups = m.groups()
            return replace_key_word(formatter(*groups)) + '\n', True

    return replace_key_word(line), False

def replace_key_word(input_line: str):
    for key in ex_table.ext_param_table:
        input_line = input_line.replace(key, ex_table.ext_param_table[key])

    for key in ex_table.get_table:
        input_line = input_line.replace(key, ex_table.get_table[key])

    for key in ex_table.class_table:
        input_line = input_line.replace(key, ex_table.class_table[key])

    for key in ex_table.size_table:
        input_line = input_line.replace(key, ex_table.size_table[key])

    for key in ex_table.element_table:
        input_line = input_line.replace(key, ex_table.element_table[key])

    for key in ex_table.race_table:
        input_line = input_line.replace(key, ex_table.race_table[key])
    
    return input_line

def effect_explain(
        file_path,
        input_file_name,
        output_file_name='ExplainedCompareResult.txt'):
    
    output_file = open(file_path + output_file_name, 'w', encoding='utf-8')
    for line in open(file_path + input_file_name, 'r', encoding='utf-8').readlines():
        explained_line, existPattern = explain_line(line)

        if existPattern:
            output_file.write(explained_line)

        else:
            output_file.write(line)
    output_file.close()
