regex_patterns = [
    # AddExtParam
    (
        r'(.*?)local\s+([A-Za-z_]\w*)\s*=\s*(-?\d+)',
        lambda indent, var_name, value: f"{indent}宣告變數 {var_name} 的值為 {value}"
    ),
    # AddExtParam
    (
        r'(.*?)AddExtParam\(0,\s*(\d+),\s*([^)]+)\)',
        lambda indent, param_value, value: f"{indent}{param_value}參數 + ( {value} )"
    ),
    # 體型抗性
    (
        r'(.*?)SubDamage_Size\(0, (\d+),\s*(-?\d+)\)',
        lambda indent, size, value: f"{indent}對 {size}體型 的物理抗性 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)SubMDamage_Size\(0, (\d+),\s*(-?\d+)\)',
        lambda indent, size, value: f"{indent}對 {size}體型 的魔法抗性 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)AddDamage_Size\(0, (\d+),\s*(-?\d+)\)',
        lambda indent, size, value: f"{indent}對 {size}體型 的物理抗性 {'-' if int(value) >= 0 else '+'} {abs(int(value))}%"
    ),
    (
        r'(.*?)AddMDamage_Size\(0, (\d+),\s*(-?\d+)\)',
        lambda indent, size, value: f"{indent}對 {size}體型 的魔法抗性 {'-' if int(value) >= 0 else '+'} {abs(int(value))}%"
    ),
    # 屬性抗性
    (
        r'(.*?)AddAttrTolerace\((\d+),\s*(-?\d+)\)',
        lambda indent, element, value: f"{indent}對 {element}屬性 的抗性 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)SubAttrTolerace\((\d+),\s*(-?\d+)\)',
        lambda indent, element, value: f"{indent}對 {element}屬性 的抗性 {'-' if int(value) >= 0 else '+'} {abs(int(value))}%"
    ),
    # 體型抗性
    (
        r'(.*?)AddRaceTolerace\((\d+),\s*(-?\d+)\)',
        lambda indent, race, value: f"{indent}對 {race}種族 的抗性 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    # 技能傷害
    (
        r'(.*?)AddDamage_SKID\(1, (\d+),\s*(-?\d+)\)',
        lambda indent, skill_id, value: f"{indent}技能 {skill_id} 的傷害 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    # 體型傷害
    (
        r'(.*?)AddDamage_Size\(1, (\d+),\s*(-?\d+)\)',
        lambda indent, size, value: f"{indent}對 {size}體型 的物理傷害 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)AddMDamage_Size\(1, (\d+),\s*(-?\d+)\)',
        lambda indent, size, value: f"{indent}對 {size}體型 的魔法傷害 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    # 對敵人屬性傷害
    # 種族傷害
    (
        r'(.*?)RaceAddDamage\((\d+),\s*(-?\d+)\)',
        lambda indent, race, value: f"{indent}對 {race}種族 的物理傷害 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)AddMdamage_Race\((\d+),\s*(-?\d+)\)',
        lambda indent, race, value: f"{indent}對 {race}種族 的魔法傷害 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    # 反射
    (
        r'(.*?)AddMeleeAttackReflect\((\d+)\)',
        lambda indent, value: f"{indent}反射 {value}% 受到的近距離物理傷害"
    ),
    (
        r'(.*?)AddReflectMagic\((\d+)\)',
        lambda indent, value: f"{indent}有 {value}% 的機率反射魔法"
    ),
    # 經驗 掉寶
    (
        r'(.*?)AddEXPPercent_KillRace\((\d+),\s*(-?\d+)\)',
        lambda indent, race, value: f"{indent}打倒 {race}種族 取得的經驗值 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
    (
        r'(.*?)AddNeverknockback\(1\)',
        lambda indent: f"{indent}不會被擊退"
    ),
    # 其他
    (
        r'(.*?)AddSPconsumption\((\d+)\)',
        lambda indent, value: f"{indent}SP 消耗 {'+' if int(value) >= 0 else '-'} {abs(int(value))}%"
    ),
]

ext_param_table = {
    '41參數': 'ATK',
    '45參數': 'DEF',
    '47參數': 'MDEF',
    '109參數': 'MHP',
    '113參數': 'HP 自然恢復力',
    '114參數': 'SP 自然恢復力',
    '200參數': 'MATK',
}

get_table = {
    'get(11)': '裝備者的基本等級',
}

size_table = {
    '0體型': '小型體型',
    '1體型': '中型體型',
    '2體型': '大型體型',
}

class_table = {
    '0階級': '一般階級',
    '1階級': 'Boss 階級',
    '2階級': '護衛階級',
}

element_table = {
    '999屬性': '未知屬性(NeverUse)',
    '0屬性': '無屬性',
    '1屬性': '水屬性',
    '2屬性': '地屬性',
    '3屬性': '火屬性',
    '4屬性': '風屬性',
    '5屬性': '毒屬性',
    '6屬性': '聖屬性',
    '7屬性': '暗屬性',
    '8屬性': '念屬性',
    '9屬性': '不死屬性',
    '10屬性': '所有屬性',
}

race_table = {
    '9999種族': '所有種族',
    '0種族': '無形種族',
    '1種族': '不死種族',
    '2種族': '動物種族',
    '3種族': '植物種族',
    '4種族': '昆蟲種族',
    '5種族': '魚貝種族',
    '6種族': '惡魔種族',
    '7種族': '人形種族',
    '8種族': '天使種族',
    '9種族': '龍族種族',
    '10種族': '人形玩家種族',
    '11種族': '動物玩家種族',
}