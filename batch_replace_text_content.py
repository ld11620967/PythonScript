#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os;

path=os.getcwd()
str_file=os.getcwd()
for dirpaths, dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        if filename.endswith('xml'):
            print filename
            with open(filename,'r')as f:
                line= f.readlines()
                for i in range(len(line)):
                    if 'daluandou' in line[i]:
                        line[i]=line[i].replace('daluandou','yingxionglianmeng')
            open(filename,'w').writelines(line)
        else:
            pass








