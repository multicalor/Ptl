import os

import time

source = ['"/home/vedim/prg/Ptl"', '"/home/vedim/prg/DjoLss"'] 

target_dir = '/home/vedim/Документы'

bkf = time.strftime('%Y%m%d') # страка с действительной датой и годом для названия папки в которой хохраняются бэк апы

today = target_dir + os.sep + bkf

now = time.strftime('%H%M%S')

comment = input('Введите комментарий --> ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace('', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
print('Коталог с именем' + today + ' успешно создан') 



print('Проверка тайм', now)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print('Проверка строки',zip_command)

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')