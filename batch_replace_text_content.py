#!/usr/bin/env python
# coding=utf-8

import os;

path=os.getcwd()
for dirpaths, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('txt'):
            with open(filename,'r')as f:
                line= f.readlines()
                for i in range(len(line)):
                    if 'http://' in line[i]:
                        line[i]=line[i].replace(line[i][-6:],'12-26\n')
            open(filename,'w').writelines(line)
        else:
            pass
