import json
import os
import pinyiniser as pyer

def main(path):
    zh_dict = pyer.get_dictionary(True)
    with os.scandir(path) as d:
        for file in d:
            contents = read_file(file.path)
            add_pinyin(dict(contents), zh_dict)
            write_file(file.path, contents)

def read_file(path):
    with open(path, 'r') as f:
        return json.load(f)

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(json.dumps(content, ensure_ascii=False, indent=2))

def add_pinyin(dict_object, zh_dict):
    for item in dict_object['strings']:
        item['Value'] = pyer.add_pinyin(item['Value'], zh_dict)

if __name__ == "__main__":
    main('./lang_files')
