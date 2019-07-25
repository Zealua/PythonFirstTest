import urllib.request
import re

#fp = urllib.request.urlopen("https://demo.jobboardmount.com/career/26580/Structural-Engineer-Full-Time-Illinois-Il-Aledo")
fp = open('text.txt', 'r')
myText = fp.read()
ref2 = re.findall(r'<td\s.+"f\svac_item_ref.+<td>[^<]+</td>',myText)
title2 = re.findall(r'<h1\sclass="page-title">.+\s-',myText)
title1 = re.sub(r'<h1\s.+">\s+',r'',title2[0])
title = re.sub(r'\s+-',r'',title1)
ref1=re.sub(r'<td\s.+<td>\s+',r'',ref2[0])
ref=re.sub(r'\s+</td>',r'',ref1)
fp.close()
print("Job ref: "+ref)
print("Job title: "+title)