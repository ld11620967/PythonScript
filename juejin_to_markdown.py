#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

path = os.getcwd()
erase = False
for dirpaths, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('txt'):
            with open('Markdown.txt', 'w') as f_w:
                with open('Original.txt', 'r') as f_r:
                    line_r = f_r.readlines()
                    for i in range(len(line_r)):
                        if 'class="article-title"' in line_r[i-2]:
                            erase = True
                        if erase:
                            f_w.write(line_r[i-1])
                        if '关注下面的标签，发现更多相似文章' in line_r[i]:
                            erase = False
            with open('Markdown.txt', 'r') as f:
                line = f.readlines()
                for i in range(len(line)):
                    # if '            ' in line[i]:
                    #     line[i]=line[i].replace('            ','')
                    # if '<h1>' in line[i]:
                    #     line[i]=line[i].replace('<h1>','## ')
                    # if '</h1>' in line[i]:
                    #     line[i]=line[i].replace('</h1>','')
                    # if '<h2>' in line[i]:
                    #     line[i]=line[i].replace('<h2>','## ')
                    # if '</h2>' in line[i]:
                    #     line[i]=line[i].replace('</h2>','')
                    # if '<h3>' in line[i]:
                    #     line[i]=line[i].replace('<h3>','### ')
                    # if '</h3>' in line[i]:
                    #     line[i]=line[i].replace('</h3>','')
                    # if '<h4>' in line[i]:
                    #     line[i]=line[i].replace('<h4>','### ')
                    # if '</h4>' in line[i]:
                    #     line[i]=line[i].replace('</h4>','')
                    # if '<h5>' in line[i]:
                    #     line[i]=line[i].replace('<h5>','#### ')
                    # if '</h5>' in line[i]:
                    #     line[i]=line[i].replace('</h5>','')
                    # if '<h6>' in line[i]:
                    #     line[i]=line[i].replace('<h6>','#### ')
                    # if '</h6>' in line[i]:
                    #     line[i]=line[i].replace('</h6>','')

                    if '<pre><code class="hljs java copyable" lang="java">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="hljs java copyable" lang="java">','```java\n')
                    if '<pre><code class="hljs xml copyable" lang="xml">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="hljs xml copyable" lang="xml">','```xml\n')
                    if '<pre><code class="hljs groovy copyable" lang="groovy">' in line[i]:
                        line[i]=line[i].replace('<pre><code class="hljs groovy copyable" lang="groovy">','```\n')
                    # if '<pre><code>' in line[i]:
                    #     line[i]=line[i].replace('<pre><code>','```\n')
                    # if '</code></pre>' in line[i]:
                    #     line[i]=line[i].replace('</code></pre>','```\n')
                    # if '<code>' in line[i]:
                    #     line[i]=line[i].replace('<code>','```')
                    # if '</code>' in line[i]:
                    #     line[i]=line[i].replace('</code>','```')



                    # java                      
                    if '<span class="hljs-function">' in line[i]:
                        line[i]=line[i].replace('<span class="hljs-function">','')
                        line[i]=line[i].replace('</span> ','')
                    if '<span class="hljs-keyword">' in line[i]:
                        line[i]=line[i].replace('<span class="hljs-keyword">','')
                        line[i]=line[i].replace('</span> ','')
                    if '<span class="hljs-keyword">' in line[i]:
                        line[i]=line[i].replace('<span class="hljs-keyword">','')
                        line[i]=line[i].replace('</span> ','')
                    if '<span class="hljs-params">' in line[i]:
                        line[i]=line[i].replace('<span class="hljs-params">','')
                        line[i]=line[i].replace('</span> ','')

                    # xml
                    if '<span class="hljs-attr">' in line[i]:
                        line[i]=line[i].replace('<span class="hljs-attr">','')
                        line[i]=line[i].replace('</span> ','') 
                    # groovy
                    if '<span class="hljs-comment">' in line[i]:
                        line[i]=line[i].replace('<span class="hljs-comment">','')
                        line[i]=line[i].replace('</span> ','') 

                    if '<a target="_blank" href="https://link.juejin.im/?target=https%3A%2F%2F' in line[i]:
                        line[i]=line[i].replace('<a target="_blank" href="https://link.juejin.im/?target=https%3A%2F%2F','(https://')
                        line[i]=line[i].replace('%2F','/')
                        line[i]=line[i].replace('%40','@')
                        line[i]=line[i].replace(' rel="nofollow',')')
                        line[i]=line[i].replace(' noopener noreferrer">','[')
                        line[i]=line[i].replace('</a>',']')
                    if 'rel="nofollow">' in line[i]:
                        line[i]=line[i].replace('rel="nofollow">','[')
                    if '</a>' in line[i]:
                        line[i]=line[i].replace('</a>',']')

                    if '<li><p>' in line[i]:
                        line[i]=line[i].replace('<li><p>','- ')
                    if '</p></li>' in line[i]:
                        line[i]=line[i].replace('</p></li>','')
                    if '<li>' in line[i]:
                        line[i]=line[i].replace('<li>','- ')
                    if '<strong>' in line[i]:
                        line[i]=line[i].replace('<strong>','**')
                        line[i]=line[i].replace('</strong>','**')
                    if '<em>' in line[i]:
                        line[i]=line[i].replace('<em>','*')
                        line[i]=line[i].replace('</em>','*')
                    if '<blockquote>' in line[i]:
                        line[i+1]=line[i+1].replace('<p>','>')



                    if '</p>' in line[i]:
                        line[i]=line[i].replace('</p>','\r\n')
                    if '<p>' in line[i]:
                        line[i]=line[i].replace('<p>','')

                    if '<figure><img' in line[i]:
                        line[i]=line[i].replace('<figure><img class="lazyload inited loaded" data-src="','![Picture](')
                        line[i]=line[i].replace('" data-',')')
                        a = re.compile(r'(width=")[^>]+>(.*)</[^>]+(figure>)',re.S)
                        line[i] = a.sub('',line[i])

                    # if '<img' in line[i]:
                    #     a = re.compile(r'^<div(.*?)<img data-original-src="')
                    #     b = re.compile(r'" data-original-width(.*?)"></div>$')
                    #     line[i]=a.sub('![Picture](',line[i])
                    #     line[i]=b.sub(')',line[i])

                    # if '<th>' in line[i]:
                    #     line[i]=line[i].replace('<th>','|')
                    # if '</thead>' in line[i]:
                    #     line[i]=line[i].replace('</thead>','| -------- | -------- |')
                    # if '<td>' in line[i]:
                    #     line[i]=line[i].replace('<td>','|')

                    if ')[' in line[i]:
                        r1=re.findall("^.*?(?=\()",line[i],re.IGNORECASE)
                        r2=re.findall("\(.*?\)",line[i],re.IGNORECASE)
                        r3=re.findall("\[.*?\]",line[i],re.IGNORECASE)
                        r4=re.findall("(?<=\]).*?$",line[i],re.IGNORECASE)
                        line[i]="".join(r1+r3+r2+r4)



                    if "<table>" in line[i]:
                        continue
                    if "</table>" in line[i]:
                        continue
                    if "<thead>" in line[i]:
                        continue
                    if "</thead>" in line[i]:
                        continue
                    if "<tr>" in line[i]:
                        continue
                    if "</tr>" in line[i]:
                        continue
                    if "<th>" in line[i]:
                        continue
                    if "</th>" in line[i]:
                        continue
                    if "<td>" in line[i]:
                        continue
                    if "</td>" in line[i]:
                        continue
                    if "<tbody>" in line[i]:
                        continue
                    if "</tbody>" in line[i]:
                        continue

                    c = re.compile(r'<[^>]+>(.*)</[^>]+>',re.S)
                    line[i] = c.sub('',line[i])
                    z = re.compile(r'<[^>]+>',re.S)
                    line[i] = z.sub('',line[i])

                    if '&lt;' in line[i]:
                        line[i]=line[i].replace('&lt;','<')
                    if '&gt;' in line[i]:
                        line[i]=line[i].replace('&gt;','>')

            open('Markdown.txt', 'w', encoding='utf-8').writelines(line)
        else:
            pass
