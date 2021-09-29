from dataclasses import dataclass, field, InitVar
import struct

@dataclass
class Header:
    """Class for storing header information"""
    b_version: bytes
    b_misc1: bytes
    b_num_of_strings: bytes
    b_string_start: bytes
    i_start_of_strings: int = field(init=False)
    i_num_of_strings: int = field(init=False)

    def __post_init__(self):
        self.i_start_of_strings = int.from_bytes(self.b_string_start,
                byteorder='little') 
        self.i_num_of_strings = int.from_bytes(self.b_num_of_strings,
                byteorder='little')

    def __str__(self):
        return self.b_version + self.b_misc1 + self.b_num_of_strings + \
            self.b_string_start

@dataclass
class StringRef:
    b_flag: bytes
    b_sound_res_ref: bytes
    b_off_set: bytes
    b_str_len: bytes
    i_position: int = field(init=False)
    i_str_len: int = field(init=False)
    i_start_of_strings_offset: InitVar[int]

    def __post_init__(self, i_start_of_strings_offset):
        self.i_position = (int.from_bytes(self.b_off_set,
            byteorder='little') + i_start_of_strings_offset)

        self.i_str_len = int.from_bytes(self.b_str_len,
            byteorder='little')

    def update_info(self, updated_str_len, new_displacement):
        self.i_str_len = updated_str_len
        self.i_position += new_displacement
        self.b_off_set = struct.pack('<I', new_displacement)
        self.b_str_len = struct.pack('<I', self.i_str_len)
    
    def __str__(self):
        return self.b_flag + self.b_sound_res_ref + self.b_off_set + \
            self.b_str_len

@dataclass
class StringRep:
    encoding: str
    str_string: str = field(init=False)
    b_string: InitVar[bytes]

    def __post_init__(self, b_string):
        self.str_string = b_string.decode(self.encoding)

    def update_string(self, updated_str):
        self.str_string = updated_str

    def __str__(self):
        return self.str_string.encode(self.encoding)
