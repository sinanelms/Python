#çalıştırdığınız dizini düzenler

from __future__ import print_function

import os
import shutil
import sys

EXT_VIDEO_LIST = ['FLV', 'WMV', 'MOV', 'MP4', 'MPEG', '3GP', 'MKV', 'AVI']
EXT_IMAGE_LIST = ['JPG', 'JPEG', 'GIF', 'PNG', 'SVG']
EXT_DOCUMENT_LIST = ['DOC', 'DOCX', 'PPT', 'PPTX', 'PAGES', 'PDF', 'ODT', 'ODP', 'XLSX', 'XLS', 'ODS', 'TXT', 'IN', 'OUT', 'MD']
EXT_MUSIC_LIST = ['MP3', 'WAV', 'WMA', 'MKA', 'AAC', 'MID', 'RA', 'RAM', 'RM', 'OGG']
EXT_CODE_LIST = ['CPP', 'RB', 'PY', 'HTML', 'CSS', 'JS']
EXT_EXECUTABLE_LIST = ['LNK', 'DEB', 'EXE', 'SH', 'BUNDLE']
EXT_COMPRESSED_LIST = ['RAR', 'JAR', 'ZIP', 'TAR', 'MAR', 'ISO', 'LZ', '7ZIP', 'TGZ', 'GZ', 'BZ2']

try:
    destLocation = str(sys.argv[1])
except IndexError:
    destLocation = str(input('Dizin yolu girin:'))

def ChangeDirectory(dir):
    try:
        os.chdir(dir)
    except WindowsError:
        print('Hata! Dizin değiştirilemiyor')
        print('Geçerli bir dizin girin!')
        ChangeDirectory(str(input('Dizin girin:')))


ChangeDirectory(destLocation)


def Organize(dirs, name):
    try:
        os.mkdir(name)
        print("{} Klasör Oluşturuldu".format(name))
    except WindowsError:
        print('{} klasör var'.format(name))

    src = '{}\\{}'.format(destLocation, dirs)
    dest = '{}\{}'.format(destLocation, name)

    os.chdir(dest)
    shutil.move(src, '{}\\{}'.format(dest, dirs))

    print(os.getcwd())
    os.chdir(destLocation)


TYPES_LIST = ['Video', 'Images', 'Documents', 'Music', 'Codes', 'Executables', 'Compressed']
for dirs in os.listdir(os.getcwd()):
    if 1:
        for name, extensions_list in zip(TYPES_LIST, [EXT_VIDEO_LIST, EXT_IMAGE_LIST, EXT_DOCUMENT_LIST, EXT_MUSIC_LIST,
                                                      EXT_CODE_LIST, EXT_EXECUTABLE_LIST, EXT_COMPRESSED_LIST]):
            if dirs.split('.')[-1].upper() in extensions_list:
                Organize(dirs, name)
    else:
        if dirs not in TYPES_LIST:
            Organize(dirs, 'klasörler')

print('Belirttiğiniz dizinde Dosya ve Klasörü Düzenleme Tamamlandı')