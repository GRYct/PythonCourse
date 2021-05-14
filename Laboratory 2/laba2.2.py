# поиск файлов дубликатов с помощью контроьных сумм

import os
import hashlib

path = r'C:\laba2.1\tex'
files = os.listdir(path)
filecount = []
for file in files:
    with open(path+'\\'+file, 'rb') as f:
        content = f.read()
        f.close()
        filecount.append(hashlib.md5(content).hexdigest())

for i in range(len(files) - 1):
    for j in range(i + 1, len(files)):
        if filecount[i] == filecount[j]:
            print(files[i], ' is ', files[j])