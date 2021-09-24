import struct

def get_file_path(lang_code):
    return lang_code + '/dialog.tlk'

def main(lang_code):
    with (open('zh/dialog.tlk', 'rb') as a,
    open('it/dialog.tlk', 'rb') as b,
    open('ru/dialog.tlk', 'rb') as c,
    open('en/dialog.tlk', 'rb') as d,
    open('ja/dialog.tlk', 'rb') as e,
    open('fr/dialog.tlk', 'rb') as f,
    open('es/dialog.tlk', 'rb') as g,
    open('ko/dialog.tlk', 'rb') as h,
    open('hu/dialog.tlk', 'rb') as i,
    open('tr/dialog.tlk', 'rb') as j,
    open('pl/dialog.tlk', 'rb') as k,
    open('pt/dialog.tlk', 'rb') as l,
    open('cs/dialog.tlk', 'rb') as m,
    open('de/dialog.tlk', 'rb') as n,
    open('uk/dialog.tlk', 'rb') as o):
        d.seek(int.from_bytes(b'\xCC\x32\x35\x00', 'little') + 884018)
        print(d.read(int.from_bytes(b'\x28\x00', 'little')))

def big_to_little(byte_string):
    return byte_string[::-1]


def read_all_files():
    z = 0
    return z
        #while z < 30:
#           bytea = a.read(4)
#           byteb = b.read(4)
#           bytec = c.read(4)
#           bytee = e.read(4)
#           bytef = f.read(4)
#           byteg = g.read(4)
#           byteh = h.read(4)
#           bytei = i.read(4)
#           bytej = j.read(4)
#           bytek = k.read(4)
#           bytel = l.read(4)
#           bytem = m.read(4)
#           byten = n.read(4)
#           byteo = o.read(4)
#           if byteo != byten:
#               print('found')
#               print(z)
#               print(z*4)
#               print('ZH: ')
#               print(bytea)
#               print('IT: ')
#               print(byteb)
#               print('RU: ')
#               print(bytec)
#               print('EN: ')
#               print(byted)
#               print('JP: ')
#               print(bytee)
#               print('FR: ')
#               print(bytef)
#               print('ES: ')
#               print(byteg)
#               print('KR: ')
#               print(byteh)
#               print('HU: ')
#               print(bytei)
#               print('TR: ')
#               print(bytej)
#               print('PL: ')
#               print(bytek)
#               print('BR: ')
#               print(bytel)
#               print('CZ: ')
#               print(bytem)
#               print('DE: ')
#               print(byten)
#               print('UA: ')
#               print(byteo)
     #       z += 1


if __name__ == '__main__':
    main(get_file_path('en'))
