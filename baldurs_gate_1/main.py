from data_classes import Header
from data_classes import StringRef

def main(lang):
    header, stringrefs = read_all_strings(lang)

def read_all_strings(lang):
    with open(lang + '/dialog.tlk', 'rb') as f:
        header = read_header(f)
        stringrefs = []
        i = 0
        while i < header.i_num_of_strings:
            stringrefs.append(read_stringref(f, header.i_start_of_strings))
            i+=1

        return header, stringrefs

def read_header(f):
    version_info = f.read(8)
    misc1 = f.read(2)
    num_of_strings = f.read(4)
    start_of_strings = f.read(4)

    return Header(version_info, misc1, num_of_strings, start_of_strings)
    
def read_stringref(f, int_offset):
    flag = f.read(2)
    sound_res_ref = f.read(16)
    offset = f.read(4)
    length = f.read(4)

    return StringRef(flag, sound_res_ref, offset, length, int_offset)



if __name__ == '__main__':
    #takes in two-letter ISO codes
    main('en')
