from data_classes import Header
from data_classes import StringRef
from data_classes import StringRep

def read_lang_file(lang: str, encoding: str):
    with open(lang + '/dialog.tlk', 'rb') as f:
        header = read_header(f)

        i = 0
        stringrefs = []
        while i < header.i_num_of_strings:
            stringrefs.append(read_stringref(f))
            i+=1

        i = 0
        stringreps = []
        while i < len(stringrefs):
            stringreps.append(read_stringrep(f, stringrefs[i].i_str_len,
                encoding))
            i+=1

        return header, stringrefs, stringreps

def read_header(f):
    version_info = f.read(8)
    misc1 = f.read(2)
    num_of_strings = f.read(4)
    start_of_strings = f.read(4)

    return Header(version_info, misc1, num_of_strings, start_of_strings)
    
def read_stringref(f):
    flag = f.read(2)
    sound_res_ref = f.read(16)
    offset = f.read(4)
    length = f.read(4)

    return StringRef(flag, sound_res_ref, offset, length)

def read_stringrep(f, str_len, encoding):
    b_string = f.read(str_len)
    return StringRep(encoding, b_string)

def print_lang_file_from_data_classes(header, string_refs, string_reps,
        file_path):
    with open(file_path, 'wb') as f:
        f.write(header.__str__())
        for ref in string_refs:
            f.write(ref.__str__())
        for rep in string_reps:
            f.write(rep.__str__())

if __name__ == '__main__':
    #takes in two-letter ISO codes
    # see https://docs.python.org/3/library/codecs.html#standard-encodings
    # for encodings
    read_lang_file('zh', 'utf_8')
