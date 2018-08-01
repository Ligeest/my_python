from PIL import Image  
import shutil
import os 
import os.path 

def file_extension(path):
    return os.path.splitext(path)[1] 

def file_name(file_dir): 
    for files in os.walk(file_dir):  
         return(files) 

imgs = file_name("E:\\文件\\python\\imgs")
#print(imgs)
for img in imgs[2:]:
    print("")
for img1 in img:
    if file_extension(img1) == '.py':
        print(file_extension(img1))
    else:
        img_info = Image.open(img1)  
        size = img_info.size
        length = max(size)
        width = min(size)
        if length == width:
            shutil.copy('E:\\文件\\python\\imgs\\' + img1,'E:\\文件\\头像\\1')