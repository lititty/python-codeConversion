# -*- coding: utf-8 -*-
'''
Created on 2016年8月28日

@author: Lan
'''
import codecs

o=codecs.open(u'/Users/Lan/Desktop/猫头鹰/1/2/hello.py','w','gbk')
o.write(u'中文')
o.close()

# i=codecs.open(u'/Users/Lan/Desktop/猫头鹰/1/2/hello2.py','r','utf8')
# str=i.read()
# i.close()
# print str