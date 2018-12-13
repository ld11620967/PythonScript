#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os;
import re

path=os.getcwd()
erase=False
for dirpaths, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('txt'):
            with open('Markdown.txt','w') as f_w:
                with open('Original.txt','r') as f_r:
                    line_r= f_r.readlines()
                    for i in range(len(line_r)):
                        if '<div class="show-content-free">' in line_r[i-1]:
                            erase=True
                        if erase:
                            f_w.write(line_r[i])
                        if '<!-- 连载目录项 -->' in line_r[i]:
                            erase=False
            with open('Markdown.txt','r') as f:
                line= f.readlines() 
                for i in range(len(line)): 
                    if '<h1>' in line[i]:
                        line[i]=line[i].replace('<h1>','### ')   
                    if '</h1>' in line[i]:
                        line[i]=line[i].replace('</h1>','')               
                    if '<h2>' in line[i]:
                        line[i]=line[i].replace('<h2>','### ')
                    if '</h2>' in line[i]:
                        line[i]=line[i].replace('</h2>','')
                    if '<h3>' in line[i]:
                        line[i]=line[i].replace('<h3>','#### ')
                    if '</h3>' in line[i]:
                        line[i]=line[i].replace('</h3>','')
                    if '<h4>' in line[i]:
                        line[i]=line[i].replace('<h4>','#### ')
                    if '</h4>' in line[i]:
                        line[i]=line[i].replace('</h4>','')
                    if '<h5>' in line[i]:
                        line[i]=line[i].replace('<h5>','##### ')
                    if '</h5>' in line[i]:
                        line[i]=line[i].replace('</h5>','')
                    if '<h6>' in line[i]:
                        line[i]=line[i].replace('<h6>','##### ')
                    if '</h6>' in line[i]:
                        line[i]=line[i].replace('</h6>','')                        

                    if '<pre><code class="java">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="java">','```java\n')
                    if '<pre><code class="xml">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="xml">','```xml\n')
                    if '<pre><code class="groovy">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="groovy">','```\n')
                    if '<pre><code>' in line[i]:
                        line[i]=line[i].replace('<pre><code>','```\n')
                    if '</code></pre>' in line[i]:
                        line[i]=line[i].replace('</code></pre>','```\n')
                    if '<code>' in line[i]:
                        line[i]=line[i].replace('<code>','```')
                    if '</code>' in line[i]:
                        line[i]=line[i].replace('</code>','```')

                    if '<a href="' in line[i]:
                        line[i]=line[i].replace('<a href="','[')
                    if '<a href="https://link.jianshu.com?t=' in line[i]:
                        line[i]=line[i].replace('<a href="https://link.jianshu.com?t=','[')
                    if '" target="_blank"' in line[i]:
                        line[i]=line[i].replace('" target="_blank"',']')

                    if 'rel="nofollow">' in line[i]:
                        line[i]=line[i].replace('rel="nofollow">','(')
                    if '</a>' in line[i]:
                        line[i]=line[i].replace('</a>',')')

                    if '%2F' in line[i]:
                        line[i]=line[i].replace('%2F','/')                       
                    if '%3A' in line[i]:
                        line[i]=line[i].replace('%3A',':')

                    if '            <p>' in line[i]:
                        line[i]=line[i].replace('            <p>','')
                    # if '<ul>' in line[i]:
                    #     line[i+1]=line[i+1].replace('<li>',' - ')
                    if '<li><p>' in line[i]:
                        line[i]=line[i].replace('<li><p>','- ')
                    if '</p></li>' in line[i]:
                        line[i]=line[i].replace('</p></li>','')
                    if '<li>' in line[i]:
                        line[i]=line[i].replace('<li>','- ')
                    if '<strong>' in line[i]:
                        line[i]=line[i].replace('<strong>','**')
                    if '</strong>' in line[i]:
                        line[i]=line[i].replace('</strong>','**')
                    if '<blockquote>' in line[i]:
                        line[i+1]=line[i+1].replace('<p>','>')

                    if '<img' in line[i]:
                        a = re.compile(r'^<div(.*?)<img data-original-src="')
                        b = re.compile(r'" data-original-width(.*?)"></div>$')
                        line[i]=a.sub('![Picture](',line[i])
                        line[i]=b.sub(')',line[i])

                    if '<th>' in line[i]:
                        line[i]=line[i].replace('<th>','|')
                    # if '</th>' in line[i]:
                    #     line[i]=line[i].replace('</th>','')
                    # if '</thead>' in line[i]:
                    #     line[i]=line[i].replace('</thead>',':-:|:-:|:-:')

                    if '</thead>' in line[i]:
                        line[i]=line[i].replace('</thead>','| -------- | -------- |')    
                    if '<td>' in line[i]:
                        line[i]=line[i].replace('<td>','|')

                    if '</p>' in line[i]:
                        line[i]=line[i].replace('</p>','\r\n')

                    c = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    line[i] = c.sub('',line[i])
                    z = re.compile(r'<[^>]+>',re.S)
                    line[i] = z.sub('',line[i])         

                    if '&lt;' in line[i]:
                        line[i]=line[i].replace('&lt;','<')
                    if '&gt;' in line[i]:
                        line[i]=line[i].replace('&gt;','>')   
 
            open('Markdown.txt','w',encoding='utf-8').writelines(line)
        else:
            pass