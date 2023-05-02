import sys, os, shutil as sh, logging as lg
lg.basicConfig(stream=sys.stdout, level=lg.INFO)
file_list = os.listdir('dcim')
file_list_new,files_left,file_set = list(),set(),set()
percent = 0
counter=0

for i in file_list:
    x = i[:-4]
    file_list_new.append(x)
    file_set.add(x)
    files_left.add(x)
def animation(counter,file_list_new):
    global percent
    if (100 * counter) / len(file_list_new) > percent:
        print('O',end='')
        percent += 2.5
os.mkdir('dcim\\.raw')
os.mkdir('dcim\\.jpg')
os.mkdir('dcim\\.alone_files')
counter = 0
lg.info('!work in progress - please wait!')
print('|' + 38 * '-' + '|')
for i in file_set:
    x = 0
    for j in file_list_new:
        if j == i:
           x+=1
        if x == 2 and j==i:
            files_left.remove(i)
            sh.copyfile('dcim\\' + i + '.RW2', 'dcim\\.raw\\' + i + '.RW2')
            counter += 1
            lg.debug(f'{counter}/{len(file_list_new)}')
            animation(counter,file_list_new)
            sh.copyfile('dcim\\' + i + '.JPG', 'dcim\\.jpg\\' + i + '.JPG')
            counter += 1
            lg.debug(f'{counter}/{len(file_list_new)}')
            animation(counter,file_list_new)
raw_and_jpg = counter
for i in files_left:
    sh.copyfile('dcim\\' + i + '.RW2', 'dcim\\.alone_files\\' + i + '.RW2')
    counter += 1
    lg.debug(f'{counter}/{len(file_list_new)}')
    animation(counter, file_list_new)
print('\n' + '|' + 38 * '-' + '|')
lg.info(f'RAW:  {raw_and_jpg}')
lg.info(f'JPG:  {raw_and_jpg}')
lg.info(f'LEFT: {len(file_list_new) - raw_and_jpg}')