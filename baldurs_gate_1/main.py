from read_lang_file import *
import jieba
from materials.cc_cedict_materials import cc_cedict_parser

do_not_parse = {'？', '，', '！', '。', '；', '“', '”', '：', '–', '—', '＊',
        '…', '、', '～', '－', '（', '）', '─', '＜', '＞', '．', '《', '》',
        '％', 'CHARNAME', '·', '<', '>', '’'}

def main(lang, encoding):
    jieba.set_dictionary('materials/dicts/jieba_dict_large.txt')
    header, string_refs, string_reps = read_lang_file(lang, encoding)
    add_pinyin_to_data(string_reps, string_refs)
    print_lang_file_from_data_classes(header, string_refs, string_reps,
    'testa.txt')

def add_pinyin_to_data(string_reps, string_refs):
    i = 1 #dodge '<NO TEXT>'
    displacement_factor = 9
    zh_dict = get_dictionary()
    while i < len(string_refs):
        str_with_pinyin = add_pinyin(string_reps[i].str_string, zh_dict)
        string_reps[i].update_string(str_with_pinyin)
        string_refs[i].update_info(len(str_with_pinyin.encode('utf_8')), displacement_factor)
        displacement_factor += len(str_with_pinyin.encode('utf_8'))
        i += 1

def add_pinyin(zh_string, zh_dict):
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
    return cc_cedict_parser.parse_dict('materials/dicts/cedict_modified.txt')

if __name__ == '__main__':
    main('b2_zh', 'utf_8')
