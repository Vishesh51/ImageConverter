import os

dir_name = "Images\\"
test = os.listdir(dir_name)

"""for item in test:
	dir1=os.listdir(dir_name+item)"""
for item1 in dir1:
	if item1.endswith(".pgm"):
		os.remove(os.path.join(dir_name, item))
