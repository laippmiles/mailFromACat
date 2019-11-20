#!/usr/bin/python
# -*- coding: utf-8 -*-
from sendEmailFromLzy import  mailFromLZY
from getSubAndCon import getSubAndCon
#写文件名要用的
subject, content = getSubAndCon(5)
fileName = 'file0.jpg'
filePath = r'D:\桌面\mailFromAKing\file' + '\\'
mailFromLZY(subject, content, filePath, fileName, sendFile=False)
