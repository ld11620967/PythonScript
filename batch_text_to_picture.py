# -*- coding: utf-8 -*-
 
import os
from PIL import Image, ImageFont, ImageDraw

def rename():
	#path_temp='C:\\Users\\丽丽\\Desktop'
	#path=unicode(path_temp, "utf-8")#中文文件路径转码
	path=os.getcwd()#获取当前目录路径
	for dirpaths, dirnames, filenames in os.walk(path):
		for file in filenames:
			Olddir=os.path.join(dirpaths,file)#原来的文件路径
			filename=os.path.splitext(file)[0]#文件名
			print(filename)	

			# text = u"这是一段测试文本，test 123。"
			im = Image.new("RGB", (320, 180), (0, 255, 255))
			dr = ImageDraw.Draw(im)
			font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 20)
 			# dr.text((30, 60), text, font=font, fill="#000000")
			dr.text((30, 60), filename, font=font, fill="#000000")
 
			# im.show()
			im.save(filename+".png")
rename()