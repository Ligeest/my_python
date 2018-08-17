from PIL import Image  
import shutil
import os 
import os.path 

def file_extension(path):
    return os.path.splitext(path)[1] 

def file_name(file_dir): 
    for files in os.walk(file_dir):  
         return(files) 

file_dir = 'C:\\Users\\17703\\Desktop\\下载\\'
imgs = file_name("C:\\Users\\17703\\Desktop\\下载")
imgs = imgs[2:]
img_list = []
for img in imgs[0]:
    if file_extension(file_dir+img) == '.jpg':
        img_info = Image.open(file_dir+img)  
        size = img_info.size
        length = max(size)
        width = min(size)
        if length == width:
            print(file_dir+img)
            img_list.append(file_dir+img)
            shutil.copy(file_dir+img,'E:\\tx\\')
for i in range(len(img_list)):
    os.remove(img_list[i])