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
        for line in f:
            if '<String' in line:
                chunk = init_chunk(line)
                chunk = hashmapify_chunk(chunk, f)
                key = chunk['edid'].strip() + chunk['rec'].strip()
                chunks[key] = chunk
    return chunks 

def hashmapify_chunk(chunk, f):
    current_key = ''
    for line in f:
        if '<EDID>' in line:
            current_key = 'edid'
        elif '<REC>' in line:
            current_key = 'rec'
        elif '<Source>' in line:
            current_key = 'source'
        elif '<Dest>' in line:
            current_key = 'dest'
        elif '</String>' in line:
            chunk['final'] = line
            return chunk
        chunk[current_key] += line

    return 'error'

def init_chunk(line):
    chunk = {}
    chunk['string'] = line
    chunk['edid'] = ''
    chunk['rec'] = ''
    chunk['source'] = ''
    chunk['dest'] = ''
    chunk['final'] = ''
    return chunk

def create_file_header():
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'\
            '<SSTXMLRessources>\n'\
            '  <Params>\n'\
            '    <Addon>FalloutNV_de.esm</Addon>\n'\
            '    <Source>de</Source>\n'\
            '    <Dest>de</Dest>\n'\
            '    <Version>2</Version>\n'\
            '  </Params>\n'\
            '  <Content>\n'

def create_file_footer():
    return '  </Content>\n'\
            '</SSTXMLRessources>'

'''Uses the ISO 639-1 language code e.g. de for german'''
def get_file_path(suffix):
    return 'FalloutNV_' + suffix + '.xml'

def save_file(file_path, chunks):
    header = create_file_header()
    footer = create_file_footer()
    with open(file_path, 'w') as f:
        f.write(header)
        for key in chunks:
            for field in chunks[key]:
                f.write(chunks[key][field])
        f.write(footer)

def combine(lang_one, lang_two):
    lang_one_chunks = chunk_file(get_file_path(lang_one))
    lang_two_chunks = chunk_file(get_file_path(lang_two))

    final_chunks = splice_chunks(lang_one_chunks, lang_two_chunks)

    save_file(get_file_path(lang_one + '_' + lang_two), final_chunks)

if __name__ == '__main__':
    #tuples = create_all_choose_two_combinations('de', 'en', 'it', 'fr', 'es')
    combine('en', 'de')
