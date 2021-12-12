import os 


def last_stage(name):
    name = name.split('-')
    new_name = name[0]
    new_name = new_name + ' - ' + name[1]
    new_name = new_name + '.mp3'
    return new_name

def obtain_lists(dir_paths):
    names = []
    files_dir = []

    files_dir.append(os.listdir(dir_paths))
    #Normalize text to compare wih lev distance
    new_files_dir = []
    ignore_char = '%$#"!/()?!°[]{}_'
    ignore_words = ['oficial','official','audio','lyrics','video']
    for list_files in files_dir:
        new_names = []
        for name in list_files:
            
            for item in ignore_char:
                name = name.replace(item,' ')
            for item in ignore_words:
                name = name.replace(item,'')    
            names.append(name)

        for name in names:
            new_names.append(last_stage(name))
        new_files_dir.append(new_names)   
    return new_files_dir, files_dir

def normalize(paths):
    names = []
    new_lists, files_dir = obtain_lists(paths)

    os.chdir(paths)
    print(os.getcwd())
    print(new_lists)
    for idx, new_name in enumerate(new_lists[0]):
        print(f"src: {files_dir[0][idx]}, dst: {new_lists[0][idx]}")
        os.replace(files_dir[0][idx], new_lists[0][idx])


