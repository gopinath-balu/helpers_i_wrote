'''read a text file and check if a particular line with specific starting sequence '''

unique_files = []
with open('/home/gopi34/Desktop/FDDB/FDDB-folds/FDDB-annotations.txt') as file:
    annotations = file.readlines()
    for line in annotations:
        if line.startswith(('2002/', '2003/')):
            # change directory structure convention to file naming convention
            file_name = '_'.join(line.split('/')).rstrip()+'.jpg'
            # append unique files to the list
            unique_files.append(file_name)
