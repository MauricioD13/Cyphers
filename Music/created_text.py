import os

names = ['Daft Punk - Da Funk','Lil Nas X - Industry Baby','Arcangel - Hace mucho tiempo']

bad_names = ['daft_punk%-da_funk',"lil_nas_x-industry%baby(lyrics)", 'arcangel-hace_mucho_tiempo(oficial)']
work_dir = os.getcwd()
print(work_dir)
try:
    os.mkdir('names')
except:
    pass
try:
    os.mkdir('bad_names')
except:
    pass
os.chdir('names')

for name in names:
    name = name + '.txt'
    command = 'touch '+ name
    f = open(name,'w')
    f.close()

os.chdir(work_dir)
print(os.getcwd())
os.chdir('bad_names')

for name in bad_names:
    name = name + '.txt'
    f = open(name,'w')
    f.close()
