#coding=utf-8  

import os;
import time;

def rename():
	path='D:\\temp';
	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	for files in filelist:#遍历所有文件
		Olddir=os.path.join(path,files);#原来的文件路径
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue;
		filename=os.path.splitext(files)[0]#文件名
		filetype=os.path.splitext(files)[1]#文件扩展名
		if filename.find('---')>0:#如果文件名中含有---
			Dir_temp=os.path.join(path,filename.split('---')[0]);
			Newdir=os.path.join(path,Dir_temp+str('---')+time.strftime("%Y.%m.%d",time.localtime())+filetype);#新的文件路径
			# 取---前面的字符，若需要取后面的字符则使用filename.split('---')[1]
			os.rename(Olddir,Newdir);#重命名

rename();