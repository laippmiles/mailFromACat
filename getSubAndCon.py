#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import uniform
from loadNormalSubAndCon import loadNormalSubAndCon
from loadMorningSubAndCon import loadMorningSubAndCon
from loadAfternoonSubAndCon import loadAfternoonSubAndCon
from loadNightSubAndCon import loadNightSubAndCon
from addImgMail import loadImgSubAndCon

def normal_get_sub_and_con(mailTime,h,locale):
    if mailTime == h[0]:
        # 第一个时段
        subject, content = loadMorningSubAndCon(locale)
        # subject, content = loadAfternoonSubAndCon(locale)
        # subject, content = loadNightSubAndCon(locale)
        return subject, content
    elif mailTime == h[1]:
        # 第二个时段
        subject, content = loadAfternoonSubAndCon(locale)
        return subject, content
    elif mailTime == h[2]:
        # 第三个时段
        subject, content = loadNightSubAndCon(locale)
        return subject, content

def getSubAndCon(mailTime,h,locale,addImg = False):
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'
    if addImg:
        try:
            subject, content = loadImgSubAndCon(locale)
            return subject, content, addImg
        except Exception as e:
            addImg = False
            print('loadImgSubAndCon', e)
            subject, content = normal_get_sub_and_con(mailTime, h, locale)
            return subject, content, addImg
    else:
        subject, content = normal_get_sub_and_con(mailTime, h, locale)
        return subject, content, addImg
