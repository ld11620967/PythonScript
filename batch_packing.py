import os

file_name=[]
str_file='D:\plugin_merger\configs\OnlineGame'
for dirpaths, dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        if "." in filename:
            filename=filename.split(".")[0]
            file_name.append(filename)
for i in range(0,len(file_name)):           
	temp=file_name[i]
	command = "my_plugin_merge.py D:\\plugin_merger\\configs\\OnlineGame\\"+temp+".xml"
	os.system(command)