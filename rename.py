import os

path = './'
file_list = os.listdir(path)
for i in file_list:
    if i == 'rename.py' or i == 'list.py':
        continue
    k = i[:len(i) - 4]
    k = k.replace('...', '_')
    k = k.replace('..', '_')
    k = k.replace('.', '_')
    if k[-1] == '_': k = k[:len(k) - 1]
    k = k + '.ogg'
    os.rename(i, k)
