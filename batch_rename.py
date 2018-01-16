#coding=utf-8  

import os;
import time;

def rename():
	#path_temp='C:\\Users\\丽丽\\Desktop'
	#path=unicode(path_temp, "utf-8")#中文文件路径转码
	path=os.getcwd()#获取当前目录路径
	for dirpaths, dirnames, filenames in os.walk(path):
		for file in filenames:
			Olddir=os.path.join(dirpaths,file)#原来的文件路径
			filename=os.path.splitext(file)[0]#文件名
			filetype=os.path.splitext(file)[1]#文件扩展名
			# if file.find('需要被替换的')>0:#如果文件名中含有...
			# 	Dir_temp=filename.replace('需要被替换的','替换的')
			# 	Newdir=os.path.join(dirpaths,Dir_temp+'.avi')#新的文件路径
			if file.find('----')>0:#如果文件名中含有---
				Dir_temp=os.path.join(dirpaths,filename.split('----')[0])
				Newdir=os.path.join(dirpaths,Dir_temp+str('----')+time.strftime("%Y.%m.%d",time.localtime())+filetype)#新的文件路径
				os.rename(Olddir,Newdir)#重命名
rename()