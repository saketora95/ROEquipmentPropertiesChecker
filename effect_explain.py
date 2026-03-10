from console_printer import print_by_indent as pbi
import re

test_list = [
    '			AddReceiveItem_Equip(7)',
    '			AddEXPPercent_KillRace(9999, 15)',
    '			RaceAddDamage(0, 10)',
]

patterns = [
    (
        r'(.*?)RaceAddDamage\((\d+),\s*(-?\d+)\)',
        lambda indent, race, value: f"{indent}對 {race}種族 的物理傷害 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)AddReceiveItem_Equip\((\d+)\)',
        lambda indent, value: f"{indent}掉寶率 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)AddEXPPercent_KillRace\((\d+),\s*(-?\d+)\)',
        lambda indent, race, value: f"{indent}打倒 {race}種族 取得的經驗值 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
]

def convert_line(line):
    for pattern, formatter in patterns:
        m = re.search(pattern, line)
        if m:
            groups = m.groups()
            return formatter(*groups)

    return line

def line_effect_explain(input_line, output_vestion=0):
    # Output Version 0: 只輸出轉換後的字句
    # Output Version 1: 輸出轉換前與轉換後的字句
    for pattern, formatter in patterns:
        m = re.search(pattern, input_line)
        if m:
            groups = m.groups()
            return formatter(*groups)

    return input_line

for item in test_list:
    print(convert_line(item))

