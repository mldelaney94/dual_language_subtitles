def read_bytes_file(path):
    with open(path, "rb") as f:
        for line in f:
            for i in range(0, len(line), 8):
                print(line[i:i+8])
            break


def split_into_octets(bytes_string):
    octets = {}

if __name__ == '__main__':
    read_bytes_file('en-us')
