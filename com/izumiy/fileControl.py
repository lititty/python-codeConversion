# -*- coding: utf-8 -*-
'''
Created on 2016年8月27日

@author: izumi
'''
import os
import codecs
class FileControl(object):
    def __init__(self,dirPath,suffix,oldcode,newcode):
        self.__dirPath=dirPath
        #检查后缀名有没有加点
        if "." == suffix:
            self.__suffix=suffix
        else:
            self.__suffix='.'+suffix
        self.__oldcode=oldcode
        self.__newcode=newcode
        self.__successfiles=[]
    def convert(self):
        self.filecontrol(self.__dirPath)
        print "转换成功文件数:",len(self.__successfiles)
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
        #如果和传入的文件后缀名一样则进行转码
        if filenamesuf == self.__suffix:
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
    path = raw_input('请输入要转换的目录:')
    fileSuffix = raw_input('请输入要转换的文件类型即后缀，如 .txt :')
    oldCode = raw_input('请输入当前文件的编码格式:')
    newCode = raw_input('请输入要转换的编码格式:')
    if oldCode != newCode:
#         filec=FileControl('/Users/Lan/Desktop/猫头鹰/1/2/hello.py','py','gbk','utf8')
        filec=FileControl(path,fileSuffix,oldCode,newCode)
        filec.convert()
    else:
        print "转换的编码不能和原来一样"
    