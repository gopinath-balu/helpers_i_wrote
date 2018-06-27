'''to traverse through all folders, sub folders and do manipulation. '''

import os
import shutil

rootdir = '/home/gopi34/Desktop/FDDB/originalPics/'
destdir = '/home/gopi34/Desktop/FDDB/trainpics/'
for subdir, dirs, files in sorted(os.walk(rootdir)):
    for file in files:
        #print(subdir)
        print(os.path.join(subdir, file))
        #shutil.move(os.path.join(subdir, file), destdir+str('_'.join(os.path.join(subdir, file).split('/')[6:])))
        #print('_'.join(os.path.join(subdir, file).split('/')[6:]))
