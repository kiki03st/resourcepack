import os

path = './pixelmon_bgm/assets/minecraft/sounds/bgm/'
file_list = os.listdir(path)
print(file_list)
f = open('./sounds.json', 'w')
f.write('{\n')
for i in file_list:
    if i == 'list.py' or i == 'rename.py':
        continue
    k = i[:len(i) - 4]
    f.write('"bgm.' + k + '": {"sounds": ["bgm/' + k + '"]},\n')
f.write('}')
f.close
