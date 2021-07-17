'''Creates a 2-combination of len(args) tuples'''
def create_all_choose_two_combinations(*args):
    if len(args) < 2:
        print('At least two arguments are needed')
        exit

    i = 0
    list_of_tuples = []
    while i < len(args) - 1:
        j = i + 1
        while(j < len(args)):
            list_of_tuples.append((args[i], args[j]))
            list_of_tuples.append((args[j], args[i]))
            j += 1
        i += 1

    return list_of_tuples

'''takes in two file paths, and appends below's strings to ontop's'''
def splice_chunks(ontop, below):
    for key in ontop:
        if key in below:
            ontop[key]['dest'] = splice_strings(
                                    ontop[key]['dest'],
                                    below[key]['dest'])

    return ontop

def splice_strings(left_side, right_side):
    #string format = <Dest>plain-text here</Dest>
    if left_side == right_side:
        return left_side
    left_side = left_side.rstrip()
    right_side = right_side.lstrip()
    spliced = left_side[0:-7] + ' ' + right_side[6:]
    return spliced 

'''Returns a dictionary of chunks <string>.*</string> and the keys are the
edids'''
def chunk_file(file_path):
    chunks = {}
    with open(file_path) as f:
        j = 0
        key = ''
        save_edid = ''
        save_string = ''
        for line in f:
            if j < 9: #skip the first 9 lines
                j += 1
                continue
            if '<String' in line:
                save_string = line
            elif '<EDID>' in line:
                save_edid = line
            elif '<REC>' in line:
                key = save_edid.strip() + line.strip()
                if key in chunks:
                    print('non-unique key found')
                chunks[key] = {'string': save_string}
                chunks[key]['edid'] = save_edid
                chunks[key]['rec'] = line
            elif '<Source>' in line:
                chunks[key]['source'] = line
            elif '<Dest>' in line:
                chunks[key]['dest'] = line
            elif '</String>' in line:
                chunks[key]['/string'] = line

    return chunks 

'''Uses the ISO 639-1 language code e.g. de for german'''
def get_file_path(suffix):
    return 'FalloutNV_' + suffix + '.xml'

def save_file(file_path, chunks):
    header = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'\
             '<SSTXMLRessources>\r\n'\
             '  <Params>\r\n'\
             '    <Addon>FalloutNV.esm</Addon>\r\n'\
             '    <Source>en</Source>\r\n'\
             '    <Dest>en</Dest>\r\n'\
             '    <Version>2</Version>\r\n'\
             '  </Params>\r\n'\
             '  <Content>\r\n'
    footer = '  </Content>\r\n' '</SSTXMLRessources>'
    with open(file_path, 'w') as f:
        f.write('\ufeff') #utf8-bom
        f.write(header)
        for key in chunks:
            for key2 in chunks[key]:
                f.write(chunks[key][key2])
        f.write(footer)

def combine(lang_one, lang_two):
    lang_one_chunks = chunk_file(get_file_path(lang_one))
    lang_two_chunks = chunk_file(get_file_path(lang_two))

    final_chunks = splice_chunks(lang_one_chunks, lang_two_chunks)
    print(len(final_chunks))
    print(len(lang_one_chunks))
    save_file(get_file_path(lang_one + '_' + lang_two), final_chunks)

if __name__ == '__main__':
    #tuples = create_all_choose_two_combinations('de', 'en', 'it', 'fr', 'es')
    combine('en', 'de')
