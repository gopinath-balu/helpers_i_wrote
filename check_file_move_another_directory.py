'''to check a file exists in another directory and move to new destination folder '''

import glob, os, shutil

def get_unique_files(file_path, strtswith_tuple):
    unique_files = []
    with open(file_path) as file:
        annotations = file.readlines()
        for line in annotations:
            if line.startswith(strtswith_tuple):
                # change directory structure convention to file naming convention
                file_name = '_'.join(line.split('/')).rstrip()+'.jpg'
                # append unique files to the list
                unique_files.append(file_name)
    return unique_files

def get_all_files(file_path):
    return [file_ for file_ in glob.glob(file_path+'*')]


def get_same_files(files, unique_files, destination):
    count = 0
    for file in files:
        check_file = file.split('/')[-1]
        if (check_file in unique_files):
            #print(file)
            shutil.copy(file, destination)
            count += 1
    print(count)

unique_faces = get_unique_files('/home/gopi34/Desktop/FDDB/FDDB-folds/FDDB-annotations.txt', ('2002/', '2003/'))
all_files = get_all_files('/home/gopi34/Desktop/FDDB/originalPics_preprocessed/')       
get_same_files(all_files, unique_faces, '/home/gopi34/Desktop/FDDB/train_images/')
