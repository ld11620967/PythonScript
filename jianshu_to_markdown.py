#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os;
import re

path=os.getcwd()
erase=False
for dirpaths, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('txt'):
            with open('Markdown.txt','w') as f_w:
                with open('Jianshu.txt','r') as f_r:
                    line_r= f_r.readlines()
                    for i in range(len(line_r)):
                        if '<div data-note-content class="show-content">' in line_r[i-1]:
                            erase=True
                        if erase:
                            f_w.write(line_r[i])
                        if '<!--  -->' in line_r[i]:
                            erase=False
            with open('Markdown.txt','r') as f:
                line= f.readlines() 
                for i in range(len(line)): 
                    if '<h1>' in line[i]:
                        line[i]=line[i].replace('<h1>','##')   
                    if '</h1>' in line[i]:
                        line[i]=line[i].replace('</h1>','')               
                    if '<h2>' in line[i]:
                        line[i]=line[i].replace('<h2>','###')
                    if '</h2>' in line[i]:
                        line[i]=line[i].replace('</h2>','')
                    if '<h3>' in line[i]:
                        line[i]=line[i].replace('<h3>','####')
                    if '</h3>' in line[i]:
                        line[i]=line[i].replace('</h3>','')
                    if '<h4>' in line[i]:
                        line[i]=line[i].replace('<h4>','#####')
                    if '</h4>' in line[i]:
                        line[i]=line[i].replace('</h4>','')
                    if '<h5>' in line[i]:
                        line[i]=line[i].replace('<h5>','######')
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
                    if '<strong>' in line[i]:
                        line[i]=line[i].replace('<strong>','**')
                    if '</strong>' in line[i]:
                        line[i]=line[i].replace('</strong>','**')
                    if '<blockquote>' in line[i]:
                        line[i]=line[i].replace('<blockquote>','>')     
                    if '<img' in line[i]:
                        a = re.compile(r'^<div(.*?)<img data-original-src="')
                        b = re.compile(r'" data-original-width(.*?)"></div>$')
                        line[i]=a.sub('![ͼƬ??](',line[i])
                        line[i]=b.sub(')',line[i])

                    if '</p>' in line[i]:
                        line[i]=line[i].replace('</p>','\r\n')


                    c = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    line[i] = c.sub('',line[i])
                    z = re.compile(r'<[^>]+>',re.S)
                    line[i] = z.sub('',line[i])         
                    # if len(line[i].strip()) == 0:
                    #     line[i]=line[i].strip()

                    if '&lt;' in line[i]:
                        line[i]=line[i].replace('&lt;','<')
                    if '&gt;' in line[i]:
                        line[i]=line[i].replace('&gt;','>')
                    if '??' in line[i]:
                        line[i]=line[i].replace('??','')        
 
            open('Markdown.txt','w',encoding='utf-8').writelines(line)
        else:
            pass