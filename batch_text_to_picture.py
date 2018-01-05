# -*- coding: utf-8 -*-
 
import os
import re
from PIL import Image, ImageFont, ImageDraw

def rename():
	#path_temp='C:\\Users\\丽丽\\Desktop'
	#path=unicode(path_temp, "utf-8")#中文文件路径转码
	path=os.getcwd()#获取当前目录路径
	for dirpaths, dirnames, filenames in os.walk(path):
		for file in filenames:
			Olddir=os.path.join(dirpaths,file)#原来的文件路径
			filename=os.path.splitext(file)[0]#文件名

			# text = u"这是一段测试文本，test 123。"

			if '_' in filename:
				a=filename.replace(filename[0:filename.rfind('_', 1) + 1],'')	
       			 
				im = Image.new("RGB", (320, 180), (194, 30, 88))
				dr = ImageDraw.Draw(im)
				font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 20)
 				# dr.text((30, 60), text, font=font, fill="#000000")
				dr.text((30, 70), a, font=font, fill="#FFFFFF")
 
				# im.show()
				im.save(filename+".png")
rename()