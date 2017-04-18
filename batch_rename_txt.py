#coding=utf-8  

import os;

def rename():
	path=os.getcwd()
	for dirpaths, dirnames, filenames in os.walk(path):
		for file in filenames:
			Olddir=os.path.join(dirpaths,file)
			filename=os.path.splitext(file)[0]
			filetype=os.path.splitext(file)[1]
			with open("name.txt",'r')as f:
				line= f.readlines()
				for i in range(len(line)):
					if filename in line[i]: 
						print Olddir 
						Dir_temp=os.path.join(dirpaths,line[i].strip('\n'))
						print Dir_temp
						Newdir=os.path.join(dirpaths,Dir_temp+filetype)
						print Newdir
						os.rename(Olddir,Newdir)
rename()