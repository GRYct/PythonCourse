
# 7 вариант найти все смайлы подстроки вида :)

import re


path = open('text2.4.txt', 'r')
lines = path.readlines()
pattern = r'(\:+\)+)'


count = 0
for line in lines:
    count+=1
    smile = re.findall(pattern, line)
    if smile:
        for newSmile in smile:
            print('Строка {0}, позиция {1} : найдено {2}'.format(count, line.index(newSmile), smile))