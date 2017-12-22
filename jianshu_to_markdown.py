#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os;
import re

path=os.getcwd()
str_file=os.getcwd()
for dirpaths, dirnames, filenames in os.walk(str_file):
    for filename in filenames:
        if filename.endswith('txt'):
            # print filename
            with open(filename,'r')as f:
                line= f.readlines()



                for i in range(len(line)):

                    if '<h2>' in line[i]:
                        line[i]=line[i].replace('<h2>','##')
                    if '</h2>' in line[i]:
                        line[i]=line[i].replace('</h2>','')
                    if '<h3>' in line[i]:
                        line[i]=line[i].replace('<h3>','###')
                    if '</h3>' in line[i]:
                        line[i]=line[i].replace('</h3>','')
                    if '<h5>' in line[i]:
                        line[i]=line[i].replace('<h5>','####')
                    if '</h5>' in line[i]:
                        line[i]=line[i].replace('</h5>','')

                    if '<pre><code class="java">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="java">','```java')
                    if '<pre><code class="xml">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="xml">','```\n')
                    if '<pre><code class="groovy">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="groovy">','```')
                    if '<pre><code>' in line[i]:
                        line[i]=line[i].replace('<pre><code>','```')
                    if '</code></pre>' in line[i]:
                        line[i]=line[i].replace('</code></pre>','```')

                    if '<li>' in line[i]:
                        line[i]=line[i].replace('<li>','- ')
                    if '</li>' in line[i]:
                        line[i]=line[i].replace('</li>','')   
                    if '<p>' in line[i]:
                        line[i]=line[i].replace('<p>','')


                    a = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    line[i] = a.sub('',line[i])

                    # a = re.compile(r'<title[^>]+>(.*)</title[^>]+>',re.S)
                    # line[i] = a.sub('',line[i])
                    # b = re.compile(r'<a[^>]+>(.*)</a[^>]+>',re.S)
                    # line[i] = b.sub('',line[i])
                    # c = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    # line[i] = c.sub('',line[i])
                    # z = re.compile(r'<[^>]+>',re.S)
                    # d = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    # line[i] = d.sub('',line[i])
                    # e = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    # line[i] = e.sub('',line[i])



                    z = re.compile(r'<[^>]+>',re.S)
                    line[i] = z.sub('',line[i])
                    if len(line[i].strip()) == 0:
                        line[i]=line[i].strip()



                    if '&lt;' in line[i]:
                        line[i]=line[i].replace('&lt;','<')
                    if '&gt;' in line[i]:
                        line[i]=line[i].replace('&gt;','>')
                    if '  ' in line[i]:
                        line[i]=line[i].replace('  ','')        

                        
            open(filename,'w').writelines(line)
        else:
            pass