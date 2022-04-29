from read_write_lang_file import *
import jieba
import pinyiniser as pyer
from materials.special_pinyin import special_pinyin

do_not_parse = {'CHARNAME', 'BROTHERSISTER', 'DAYANDMONTH',
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
        'losing', 'battle', 'RESOURCE', 'PRO_HEHER', 'AREA_NAME',
        'MISSING_CONTENT', 'PERCENT', 'COMPLETE', 'TIME', 'REMAINING'}

do_not_parse = do_not_parse.union(pyer.do_not_parse_set)

def main(lang, encoding):
    jieba.set_dictionary('materials/dicts/jieba_dict_large.txt')
    header, string_refs, string_reps = read_lang_file(lang, encoding)
    add_pinyin_to_data(string_reps, string_refs)
    write_lang_file_from_data_classes(header, string_refs, string_reps,
    'dialog.tlk')
    write_just_string_reps(string_reps, 'reference.txt')

def add_pinyin_to_data(string_reps, string_refs):
    i = 1 #dodge '<NO TEXT>'
    displacement_factor = 9 #<no text> = 9
    zh_dict = pyer.get_dictionary(True)
    while i < len(string_refs):
        str_with_pinyin = pyer.add_pinyin(string_reps[i].str_string, zh_dict,
                special_pinyin, do_not_parse).strip('\n')
        string_reps[i].update_string(str_with_pinyin)
        string_refs[i].update_info(bytes_len := len(str_with_pinyin.encode('utf_8')), displacement_factor)
        displacement_factor += bytes_len
        i += 1

def finalise_data(path):
    lines = read_lines(path)
    i = 0
    while i < len(lines):
        string_reps[i].update_string(str_with_pinyin.strip('\n'))
        string_refs[i].update_info(bytes_len := len(str_with_pinyin.encode('utf_8')), displacement_factor)
        displacement_factor += bytes_len
        i += 1
    write_lang_file_from_data_classes(header, string_refs, string_reps, 'dialog.tlk')

if __name__ == '__main__':
    main('b2_zh', 'utf_8')
