# -*- coding: utf-8 -*-
'''
Created on 2016年8月27日

@author: izumi
'''
import os
import sys
import codecs
class FileControl(object):
    def __init__(self,dirPath,suffix,oldcode,newcode):
        self.__dirPath=dirPath
        if suffix == '':
            self.suffixSet = set()
            self.sufIsEmtpy = True
        else:
            self.suffixSet = suffix.split(',')
            self.sufIsEmtpy = False
        #加上'.'
        i = 0
        while i < len(self.suffixSet):
            self.suffixSet[i] = '.' + self.suffixSet[i];
            i+=1
        self.__oldcode=oldcode
        self.__newcode=newcode
        self.__successfiles=[]
    def convert(self):
        self.filecontrol(self.__dirPath)
        print "转换成功文件数:",len(self.__successfiles)
        print self.suffixSet
        #列出成功的文件
        for file in self.__successfiles:
            print file
    def filecontrol(self,currentPath):
        #如果当前是目录
        if os.path.isdir(currentPath):
            #列出该目录下所有目录和文件
            self.__lists=os.listdir(currentPath)
            #查找出子目录、文件
            #sdirs = [subdir for subdir in self.__lists if os.path.isdir(os.path.join(currentPath,subdir))]
            for single in self.__lists:
                self.filecontrol(os.path.join(currentPath,single))
        else:
            self.codeConvert(currentPath)
                
    def codeConvert(self,currentFilePath):
        #提取文件后缀名
        filename,filenamesuf=os.path.splitext(currentFilePath)
        if self.sufIsEmtpy:
            self.suffixSet.add(filenamesuf)
        for suffix in self.suffixSet:
            #如果和传入的文件后缀名一样则进行转码
            if filenamesuf == suffix:
                try:
                    with codecs.open(currentFilePath,'r', self.__oldcode) as f:
                        text=f.read()
                    #先转换成unicode码
                    t_gbk=text.encode(self.__oldcode)
                    t_unicode=t_gbk.decode(self.__oldcode)
    #                     t_utf8=t_unicode.encode('utf-8')
                    with codecs.open(currentFilePath,'w',self.__newcode) as f:
                        f.write(t_unicode)
                        self.__successfiles.append(currentFilePath)
                except:
                    print "文件:'%s'不是'%s'编码" % (currentFilePath,self.__oldcode)
           
    
if __name__ == '__main__':
    path = raw_input('转换的目录(默认当前目录):').rstrip()
    #如果 path 为空，则默认当前目录
    if path == '':
        path = sys.path[0]
    fileSuffix = raw_input('文件类型，如txt(多种文件","隔开，默认全部文件):').rstrip()
    oldCode = raw_input('当前文件的编码格式(默认GBK):').rstrip()
    if oldCode == '':
        oldCode = 'gbk'
    newCode = raw_input('转换的编码格式(默认UTF-8):').rstrip()
    if newCode == '':
        newCode = 'utf-8'
    if oldCode != newCode:
#         filec=FileControl('/Users/Lan/Desktop/猫头鹰/1/2/hello.py','py','gbk','utf8')
        filec=FileControl(path,fileSuffix,oldCode,newCode)
        filec.convert()
    else:
        print "转换的编码不能和原来一样"
    