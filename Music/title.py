import os


os.chdir('Downloads/Prueba')
files = os.listdir()
#print(files)
#print(os.getcwd())
new_names = []
for file in files:
    new_file = ''
    file = file.split('-')
    new_file = file[0]
    for idx, splited in enumerate(file):
        if idx == len(file)-1:
            break
        if idx != 0:
            new_file = new_file + '-' + splited
        
        
        
    print(new_file)
    new_names.append(new_file+'.mp3')

for idx, file in enumerate(new_names):
    print(new_names)
    os.rename(files[idx], new_names[idx])