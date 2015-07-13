# -*- coding: utf-8 -*-
from hanziconv import HanziConv

with open('newcj.cin.txt', 'r') as f:
    lines = f.readlines()

new_lines = []

n = 0
for line in lines:
    if line[0] in "#%":
        new_lines.append(line)
        continue
    try:
        cmd, value = line.strip(' ').decode('utf-8').split(u' ', 1)
    except ValueError as e:
        # '\t' 鍵盤對應部份
        new_lines.append(line)
        continue

    newv = HanziConv.toTraditional(value)
    if newv != value:
        # print value ,
        # print ' -> ',
        # print newv
        n += 1
    elif len(value.strip()) > 1:
        print value.strip()
        pass
    else:
        newl = line.strip().split(' ')[0].decode('utf-8') + ' ' + newv
        new_lines.append(newl.encode('utf-8'))

print len(lines)
print n    



with open('newcj.cin-new.txt', 'w') as f:
    f.writelines(new_lines)
