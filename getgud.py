import os
import shutil

from_dir='./C/Downloads'
to_dir='./C/SchoolWork'

list_of_FILES=os.listdir(from_dir)
#print(list_of_FILES)

for file_name in list_of_FILES:
    name, extension=os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension=='':
        continue
    if extension in ['.txt','.doc','.docx',".pdf"]:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+'PYthon'
        path3 = to_dir+'/'+'PYthon' + '/' + file_name
        
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving')
            shutil.move(path1,path3)
thingy=os.listdir(to_dir)
print(thingy)

 