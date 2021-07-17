import os

def combine_languages(fl, sl):
    if fl == '' or sl == '':
        print('Please specify what PO files you would like to combine')
        exit

    file_pairs = zip_list(get_files(fl), get_files(sl))

    for pair in file_pairs:
        first_language_file_chunks = chunk_file(pair[0])
        second_language_file_chunks = chunk_file(pair[1])
        final = stitch_chunks(first_language_file_chunks, second_language_file_chunks)
        with open(pair[0].split('/')[1], 'w+') as f:
            f.write(final)

def chunk_file(file_path):
    chunks = {}
    chunk_counter = 0
    with open(file_path, 'rb') as f:
        chunk = []
        for line in f:
            line = line.decode('cp1252')
            if line == '\r\n': #blank line in these files
                chunks[chunk_counter] = chunk
                chunk_counter += 1
                chunk = []
            else:
                chunk.append(line)
    
    return chunks

def stitch_chunks(top_chunks, bottom_chunks):
    if (len(top_chunks.keys()) != len(bottom_chunks.keys())):
        print('Error: this file does not have enough keys')
        exit

    final = top_chunks[0][0] + '\r\n'
    for chunk_counter in range(1, len(top_chunks.keys())):
        top_chunks[chunk_counter][1] = top_chunks[chunk_counter][1][0:-3]
        top = ''.join(top_chunks[chunk_counter])
        bottom = bottom_chunks[chunk_counter][1].split(':', maxsplit=1)
        top += bottom[1]
        top += '\r\n'
        final += top

    return final

def remove_newlines_and_quotes_from_end_of_string(input):
    return str.rstrip(input, '"\\n\\r')

'''Returns a list of files in a directory sorted with case insensitive sorting'''
def get_files(dir):
    return sorted([file.path for file in os.scandir(dir)], key=str.casefold)

'''Uses a list comprehension to return a list of tuples for two
equal length lists'''
def zip_list(list1, list2):
    if (len(list1) != len(list2)):
        print('ERROR: Lists are different lengths')
        print(list1)
        print(list2)
        exit
    return [(list1[i], list2[i]) for i in range(len(list1))]

if __name__ == '__main__':
    combine_languages('subs_en/', 'subs_de/')
