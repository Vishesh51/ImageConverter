from PIL import Image
import os,sys
from pathlib import Path
import shutil


path='Images\\'
dirs=os.listdir(path);

#print dirs

"""
for item in dirs:
	dir1=os.listdir(path+item)
	#print dir1"""
	
for item in dirs:
	#print path+item+'\\'+item1
	if os.path.isfile(path+item):
		im=Image.open(path+item)
		f, e = os.path.splitext(path+item)
		im.convert('RGB').save(f+".jpg","JPEG")
			#shutil.move(os.path.join(path, f+e), os.path.join(path, f+".jpg"))

