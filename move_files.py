'''to move files from all sub directories to one global root folder. '''

import glob
import shutil

root_dir = '/home/gopi34/Videos/originalPics/'
destination = '/home/gopi34/Videos/fddb/'
for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    if filename.split('/')[-1] not in [file.split('/')[-1] for file in glob.glob(destination+'*.jpg')]:
        shutil.move(filename, destination)