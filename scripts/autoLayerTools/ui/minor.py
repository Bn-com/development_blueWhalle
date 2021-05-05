#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = minor
__author__ = Ben 
__mtime__ = 2021/5/4 : 20:56
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""
import re,os,sys
import subprocess

mayapy = r"D:\Alias\Maya2019\bin\mayapy.exe"
code_path = r"F:\development\DevOnGithub\scripts\MayaStandaloneTools\scripts\invoke\autoLayer.py"

andir = r"E:\work\MAYAPROJS\MAYA19_FAQ\autolayer\scenes\batchTst"
outdir = r"E:\work\MAYAPROJS\MAYA19_FAQ\autolayer\scenes\batchTst\out20210505"

maya = subprocess.Popen([mayapy,code_path,andir,outdir],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = maya.communicate()
print out
exitcode = maya.returncode
if str(exitcode) != '0':
    print(err)
    print('error happend')
else:
    print('done')