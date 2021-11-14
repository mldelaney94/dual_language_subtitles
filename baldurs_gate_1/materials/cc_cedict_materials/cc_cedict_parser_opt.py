"""Only gets pinyin"""
import sys

#define functions

#builds a dictionary with a simp character as the key
#the key accesses a dictionary of attributes - pinyin, and english definition
#dictionary[key]['pinyin'] accesses a list
#dictionary[key]['english'] also accesses a list
def parse_lines(lines):
    dictionary = {}
    for line in lines:
        parts = get_parts_of_line(line)
        add_entry(parts, dictionary)
    
    return dictionary

def get_parts_of_line(line):
    parts = {}
    line = line.rstrip('/')
    line = line.split('/')
    
    pinyin_hanzi = line[0].split('[')
    hanzi = pinyin_hanzi[0]
    hanzi = hanzi.split(' ')
    parts['simp_hanzi'] = hanzi[1]
    
    pinyin = pinyin_hanzi[1]
    pinyin = pinyin.rstrip(' ]')
    parts['pinyin'] = pinyin
    
    return parts
    
#no return deliberately
def add_entry(parts, dictionary):
    key = parts['simp_hanzi']

    pinyin = parts['pinyin']

    if key not in dictionary:
        dictionary[key] = {'pinyin': pinyin}

def parse_dict(path):
    #make each line into a dictionary
    with open(path, 'r') as f:
        text = f.read()
        lines = text.split('\n')
        dictionary = parse_lines(lines)

    return dictionary

if __name__ == "__main__":
    parsed_dict = parse_dict('../dicts/cedict_modified.txt')
    print(parsed_dict)
