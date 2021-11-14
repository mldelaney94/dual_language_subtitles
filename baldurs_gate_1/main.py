from read_lang_file import *
import jieba
from materials.cc_cedict_materials import cc_cedict_parser_opt

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
        '守牢魔像': 'shou3lao2mo2xiang4', '阿塔夸': 'A1ta3kua1',
        '瑞雷夫': 'Rui1lei2fu1', '依力奇': 'Yi1li4qi2',
        '卡妮雅': 'Ka3ni1ya3', '伊雷米': 'Yi1lei3mi3',
        '乌蕾妮': 'Wu1lei3ni1', '清扫魔像': 'Qing1sao3mo2xiang4',
        '受折磨者': 'shou4zhe2mo2zhe3', '攸旭摩': 'You1xu4mo2',
        '逃脱的复制体': 'tao2tuo1de5fu4zhi4ti3', '佛南登': 'Fo2nan2deng1',
        '李尔': 'Li3er3', '贝丝女士': 'bei4si1nu:3shi4',
        '安姆士兵': 'an1mu3shi4bing1', '费尔加斯': 'Fei4er3jia1si1',
        '哈洛德': 'Ha1luo4de2', '哈洛德太太': 'Ha1luo4de2Tai4tai5',
        '欧法大人': 'Ou1fa3da4ren5', '欧法女士': 'Ou1fa3Nu:3shi4',
        '传令员': 'chuan2ling4yuan2', '莫论': 'Mo4lun4',
        '安姆保镖': 'An1mu3bao3biao1', '夸塔立斯': 'Kua1ta3li4si1',
        '吉蓝': 'Ji2lan2', '叫卖小贩': 'Jiao4mai4Xiao3fan4',
        '优丝女士': 'You1si1Nu:3shi4', '狄德丽': 'Di2de2li4',
        '利博德': 'Li4bo2de2', '盖瑞斯': 'Ge3rui4si1',
        '布瑞姆': 'Bu4rui1mu3', '塔洛斯牧师': 'Ta3luo4si1Mu4shi4',
        '哈瑞姗': 'Ha1rui4shan1', '巨灵': 'Ju4ling2', '艾黎': 'Ai4li2',
        '宠妓奴隶': 'chong3ji4nu2li4', '奎里': 'Kui2li3',
        '马戏团表演者': 'ma3xi4tuan2biao3yan3zhe3',
        '马戏团员工': 'ma3xi4tuan2yuan2gong1',
        '书店老板葛伦普': 'shu1dian4lao3ban3Ge2lun2pu3',
        '安姆守卫': 'an1mu3shou3wei4', '派崔西雅': 'Pai4cui1xi1ya3',
        '阿拉提欧·迪·邦尼托': 'A1la1ti2ou1·di2·bang1ni2tuo1',
        '兽人克星史迈鲁夫': 'shou4ren2ke4xing1shi3mai4lu3fu1',
        '曼卡·碎石者': 'man4ka3·sui4shi2zhe3', '波寄': 'Bo1ji1',
        '法师阿蒙': 'fa3shi1A1meng2', '拉葛': 'La1ge2',
        '女贵族': 'Nu:3gui4zu2', '拉瑟拉女士': 'La1se4la1nu:3shi4',
        '普格尼': 'Pu3ge2ni2', '克雷兰伯爵': 'Ke4lei2lan2bo2jue2',
        '艾莉西雅小姐': 'Ai4li4xi1ya3xiao3jie5', '莉贝卡': 'Li4bei4ka3',
        '丐童': 'Gai4tong2', '伊尔玛特女祭司': 'Yi1er3ma3te4nu:3ji4si1',
        '拉狄尔': 'La1di2er3', '恩格': 'En1ge2', '佩特': 'Pei4te4',
        '阿诺力尼斯': 'A1nuo4li4ni2si1',
        '矿石商人洁利雅': 'Kuang4shi2shang1ren2jie2li4ya3',
        '安姆百夫长': 'An1mu3bai3fu1chang2',
        '贝尔明·葛加斯': 'Bei4er3ming2·Ge2jia1si1',
        '盖兰·贝尔': 'Ge3lan2·Bei4er3',
        '蒙面法师执法者': 'Meng2mian4fa3shi1zhi2fa3zhe3',
        '半身人女性': 'ban4shen1ren2nv3xing4',
        '半身人男子': 'ban4shen1ren2nan2zi3', '威蓝': 'Wei1lan2',
        '无家的女人': 'Wu2jia1denv3ren2', '特索德': 'Te4suo3de2',
        '奴隶贩子守卫': 'Nu2li4fan4zi3shou3wui4',
        '凯莉·姚森': 'Kai3li4·yao2sen1', '塔特': 'Ta3te4',
        '科瓦尔': 'Ke1wa3er3', '布雷格': 'Bu4lei2ge2',
        '伊尔玛特牧师': 'Yi1er3ma3te4mu4shi1', '雷提南': 'Lei2ti2nan2',
        '酒馆顾客': 'Jui3guan3gu4ke4', '柏纳德': 'Bai3na4de2',
        '酒馆醉客': 'Jui3guan3zui4ke4', '加罗': 'Jia1luo2',
        '吉尔丹领主': 'Ji2er3dan1ling3zhu3',
        '昂格·希尔达克': 'Ang2ge2·Xi1er3da2ke4', '赫克塞特': 'He4ke4sai1te4',
        '提雅娜': 'Ti2ya3na4', '阿诺门': 'A1nuo4men2', '苏力': 'Su1li4',
        '寇根': 'Kou4gen1', '阿玛拉斯': 'A1ma3la1si1',
        '乔鲁夫': 'Qiao2lu3fu1'}

def main(lang, encoding):
    jieba.set_dictionary('materials/dicts/jieba_dict_large.txt')
    header, string_refs, string_reps = read_lang_file(lang, encoding)
    add_pinyin_to_data(string_reps, string_refs)
    print_lang_file_from_data_classes(header, string_refs, string_reps,
    'dialog.tlk')

def add_pinyin_to_data(string_reps, string_refs):
    i = 1 #dodge '<NO TEXT>'
    displacement_factor = 9 #<no text> = 9
    zh_dict = get_dictionary()
    while i < len(string_refs):
        str_with_pinyin = add_pinyin(string_reps[i].str_string, zh_dict)
        string_reps[i].update_string(str_with_pinyin)
        string_refs[i].update_info(bytes_len := len(str_with_pinyin.encode('utf_8')), displacement_factor)
        displacement_factor += bytes_len
        i += 1

def add_pinyin(zh_string, zh_dict):
    if zh_string in special_pinyin:
        return zh_string + '\n' + special_pinyin[zh_string]
    
    pinyin = get_pinyin(zh_string, zh_dict)
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
    return cc_cedict_parser_opt.parse_dict('materials/dicts/cedict_modified.txt')

if __name__ == '__main__':
    main('b2_zh', 'utf_8')
