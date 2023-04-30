import os

path = './pixelmon_bgm/assets/minecraft/sounds/bgm/'
file_list = os.listdir(path)
for i in file_list:
    k = i
    k = k.replace('(', '')
    k = k.replace(')', '')
    os.rename(path + i, path + k)
