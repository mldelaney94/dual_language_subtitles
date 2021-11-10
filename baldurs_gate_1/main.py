from read_lang_file import *
import jieba
from materials.cc_cedict_materials import cc_cedict_parser

do_not_parse = {'？', '，', '！', '。', '；', '“', '”', '：', '–', '—', '＊',
        '…', '、', '～', '－', '（', '）', '─', '＜', '＞', '．', '《', '》',
        '％', '·', '>', '’', 'CHARNAME', 'BROTHERSISTER', 'DAYANDMONTH',
        'DAYNIGHT', 'DAYNIGHTALL', 'GABBER', 'GAMEDAY', 'GAMEDAYS',
        'GIRLBOY', 'HESHE', 'HIMHER', 'HISHER', 'LADYLORD', 'LEVEL',
        'MALEFEMALE', 'MANWOMAN', 'MONTH', 'MONTHNAME', 'DAY', 'PLAYER1-6',
        'PRO_BROTHERSISTER', 'PRO_CLASS', 'PRO_GIRLBOY', 'PRO_HESHE',
        'PRO_HIMHER', 'PRO_HISHER', 'PRO_LADYLORD', 'PRO_MALEFEMALE',
        'PRO_MANWOMAN', 'PRO_MASTERMISTRESS', 'PRO_RACE', 'PRO_SIRMAAM'
        'PRO_SONDAUGHTER', 'RACE', 'SIRMAAM', 'SONDAUGHTER', 'TM', 'YEAR',
        'SPELLLEVEL', 'WEAPONNAME', 'SPECIALABILITYNAME', 'ITEMCOST',
        'ITEMNAME', 'DURATION', 'HOUR' , 'PRO', 'PLAYER1', 'PLAYER2',
        'PLAYER3', 'PLAYER4', 'PLAYER5', 'PLAYER6', 'DAMAGER', 'DAMAGEE',
        'AMOUNT', 'TYPE', 'FIGHTERTYPE', 'MAGESCHOOL', 'RESISTED',
        'SERVERVERSION', 'CLIENTVERSION', 'MINIMUM', 'MAXIMUM', 'script',
        'CLASS', 'CurrentChapter', 'HP', 'EXPERIENCE', 'NEXTLEVEL',
        'number', 'DURATIONNOAND', 'DOTS1', 'DOTS2', 'DOTS3', 'DOTS4',
        'DOTS5', 'EXPERIENCEAMOUNT', 'TARGET', 'CREATURE', 'LEVELDIF',
        'losing', 'battle', 'RESOURCE', 'PRO_HEHER', 'AREA_NAME', '_',
        'MISSING_CONTENT', 'PERCENT', 'COMPLETE', 'TIME', 'REMAINING'}

special_pinyin = {'贾希拉': 'Gu3xi1la1', '爱蒙': 'Ai4meng2',
        '守牢魔像': 'Shou3lao2mo2xiang4', '阿塔夸': 'A1ta3kua1',
        '瑞雷夫': 'Rui1lei2fu1', '依力奇': 'Yi1li4qi2',
        '卡妮雅': 'Ka3ni1ya3', '伊雷米': 'Yi1lei3mi3',
        '乌蕾妮': 'Wu1lei3ni1', '清扫魔像': 'Qing1sao3mo2xiang4',
        '受折磨者': 'Shou4zhe2mo2zhe3', '攸旭摩': 'You1xu4mo2',
        '逃脱的复制体': 'Tao2tuo1de5fu4zhi4ti3', '佛南登': 'Fo2nan2deng1',
        '李尔': 'Li3er3', '贝丝女士': 'Bei4si1Nu:3shi4',
        '安姆士兵': 'An1mu3shi4bing1', '费尔加斯': 'Fei4er3jia1si1',
        '哈洛德': 'Ha1luo4de2', '哈洛德太太': 'Ha1luo4de2Tai4tai5',
        '欧法大人': 'Ou1fa3da4ren5', '欧法女士': 'Ou1fa3Nu:3shi4',
        '传令员': 'chuan2ling4yuan2', '莫论': 'Mo4lun4',
        '安姆保镖': 'An1mu3bao3biao1', '夸塔立斯': 'Kua1ta3li4si1',
        '吉蓝': 'Ji2lan2', '叫卖小贩': 'Jiao4mai4Xiao3fan4',
        '优丝女士': 'You1si1Nu:3shi4', '狄德丽': 'Di2de2li4',
        '利博德': 'Li4bo2de2', '盖瑞斯': 'Ge3rui4si1',
        '布瑞姆': 'Bu4rui1mu3', '塔洛斯牧师': 'Ta3luo4si1Mu4shi4',
        '哈瑞姗': 'Ha1rui4shan1', '巨灵': 'Ju4ling2', '艾黎': 'Ai4li2',
        '宠妓奴隶': 'Chong3ji4nu2li4', '奎里': 'Kui2li3',
        '马戏团表演着': 'Ma3xi4tuan2biao3yan3zhe3',
        '马戏团员工': 'Ma3xi4tuan2yuan2gong1'}

do_not_add_pinyin = {'<NO TEXT>'}

def main(lang, encoding):
    jieba.set_dictionary('materials/dicts/jieba_dict_large.txt')
    header, string_refs, string_reps = read_lang_file(lang, encoding)
    add_pinyin_to_data(string_reps, string_refs)
    print_lang_file_from_data_classes(header, string_refs, string_reps,
    'testa.txt')

def add_pinyin_to_data(string_reps, string_refs):
    i = 1 #dodge '<NO TEXT>'
    displacement_factor = 9 #<no text> = 9
    zh_dict = get_dictionary()
    while i < len(string_refs):
        str_with_pinyin = add_pinyin(string_reps[i].str_string, zh_dict)
        string_reps[i].update_string(str_with_pinyin)
        string_refs[i].update_info(len(str_with_pinyin.encode('utf_8')), displacement_factor)
        displacement_factor += len(str_with_pinyin.encode('utf_8'))
        i += 1

def add_pinyin(zh_string, zh_dict):
    pinyin = get_pinyin(zh_string, zh_dict)
    
    if zh_string in do_not_add_pinyin:
        return zh_string
    elif zh_string in special_pinyin:
        return zh_string + '\n' + special_pinyin[zh_string]
    
    zh_string += '\n'
    for item in pinyin:
        if item in do_not_parse:
            zh_string += item
        else:
            zh_string += ' ' + item

    return zh_string

def get_pinyin(zh_string, zh_dict):
    line = tuple(jieba.cut(zh_string, cut_all=False))
    pinyin = []
    for word in line:
        if word in zh_dict:
            pinyin.append(zh_dict[word]['pinyin'])
        else:
            if word in do_not_parse or ord(word[0]) < 255:
                pinyin.append(word)
            else: 
                for character in word:
                    if character in zh_dict:
                        pinyin.append(zh_dict[character]['pinyin'])
                    else:
                        pinyin.append(character)

    return pinyin

def get_dictionary():
    return cc_cedict_parser.parse_dict('materials/dicts/cedict_modified.txt')

if __name__ == '__main__':
    main('b2_zh', 'utf_8')
