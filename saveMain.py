#!/home/vedim/prg/Ptl/bin/myvenv python3

import os

import time

source = ['"/home/vedim/prg/Ptl"', '"/home/vedim/prg/DjoLss"'] #Возможно будут мешать двойные ковычки

target_dir = '/home/vedim/Документы'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

print('Проверка тайм', time.strftime('%Y%m%d%H%M%S'))

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print('Проверка строки',zip_command)

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')

