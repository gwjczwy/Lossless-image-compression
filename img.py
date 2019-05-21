import os
from PIL import Image
import threading,time

def imgToProgressive(path):
    if not path.split('.')[-1:][0] in ['png','jpg','jpeg']:  #if path isn't a image file,return
        return
    if os.path.isdir(path):
        return
##########transform img to progressive
    img = Image.open(path)
    destination = path.split('.')[:-1][0]+'_destination.'+path.split('.')[-1:][0]
    try:
        print(path.split('\\')[-1:][0],'开始转换图片')
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True) #转换就是直接另存为
        print(path.split('\\')[-1:][0],'转换完毕')
    except IOError:
        PIL.ImageFile.MAXBLOCK = img.size[0] * img.size[1]
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True)
        print(path.split('\\')[-1:][0],'转换完毕')
    print('开始重命名文件')
    os.remove(path)
    os.rename(destination,path)

for d,_,fl in os.walk(os.getcwd()):    #遍历目录下所有文件
    for f in fl:
        try:
            imgToProgressive(d+'\\'+f)
        except:
            pass