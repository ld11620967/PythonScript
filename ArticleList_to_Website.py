#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

path=os.getcwd()
erase=False
for dirpaths, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('txt'):
            with open('Website.txt','w') as f_w:
                with open('ArticleList.txt','r') as f_r:
                    line_r= f_r.readlines()
                    for i in range(len(line_r)):
                        if '<div style="clear: both;"></div><div class="row">' in line_r[i-1]:
                            erase=True
                        if erase:
                            f_w.write(line_r[i])
                        if '<div style="margin-top: 20px;">' in line_r[i]:
                            erase=False
            with open('Website.txt','r') as f:
                line= f.readlines() 
                for i in range(len(line)): 
                    if '<a href="' in line[i]:
                        line[i]=line[i].replace('<a href="','http://www.apkbus.com/')   
                    if '" target="_blank">' in line[i]:
                        line[i]=line[i].replace('" target="_blank">','')               
                    
                    c = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    line[i] = c.sub('',line[i])
                    z = re.compile(r'<[^>]+>',re.S)
                    line[i] = z.sub('',line[i])      
            # open('Website.txt','w',encoding='utf-8').writelines(line)

            # with open('Website1.txt','w') as f_w:
            #     with open('Website.txt','r',encoding='utf-8') as f_r:
            #         line_r= f_r.readlines()
            #         for i in range(len(line_r)):
            #             if 'http://www.apkbus.com/' in line_r[i]:
            #                 line_r[i]=line_r[i]
            #             else:
            #                 line_r[i]=''   
            # open('Website1.txt','w',encoding='utf-8').writelines(line_r)

                    if 'http://www' in line[i]:
                        line[i]=line[i]
                    else:
                        line[i]=''   
            open('Website.txt','w',encoding='utf-8').writelines(line)
            
        else:
            pass