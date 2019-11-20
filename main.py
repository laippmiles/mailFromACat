#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from sendEmailFromLzy import  mailFromLZY
from getSubAndCon import getSubAndCon
from random import uniform
from time import sleep

# 2019年11月2日22:08:12
def mail(hour,h):
    #subject, content = getSubAndCon(hour,h)
    fileName = 'file0.jpg'
    filePath = r'D:\桌面\mailFromAKing\file' + '\\'
    ballot = int(uniform(0, 101))
    print("ballot" ,ballot)
    if 0 <= ballot <= 20:
        mailFromLZY(hour,h, filePath, fileName, sendFile=False, addImg=True)
    else:
        mailFromLZY(hour,h, filePath, fileName, sendFile=False, addImg=False)

def main():
    '''h表示设定的小时，m为设定的分钟'''
    print('Begin')
    print ('test')
    h = [8, 14, 20]
    # h = [1,1,21]
    # 写现在的时间，调试用
    index = int(uniform(0, len(h)))
    mailtime = h[index]
    # 赋初值
    m = int(uniform(1, 59))
    # 取现在的时间，调试用
    # m = datetime.now().minute
    print('Init m：', m)
    # print(m)
    # 判断是否达到设定时间，例如0:00
    while True:
        while True:
            # 内部死循环是为了检测时间的
            now = datetime.now()
            if now.hour == 1 and now.minute == 13:
                # 此处更新今天的发信时间
                index = int(uniform(0, len(h)))
                mailtime = h[index]
                print('Update mailtime:', mailtime)
            if now.hour not in h:
                m = int(uniform(1, 59))
                # 只在非发信时段更新m值
            if now.hour == mailtime and now.minute == m:
                break
                # 到达设定时间，结束内循环
            print('Now Time：', now.hour, '：', now.minute, '：', now.second)
            print('Update m：', m, 'Today mail time :', mailtime)
            sleep(30)  # 检测周期是30秒
        # 到点发信
        print('Send mail.')
        mail(now.hour, h)
        sleep(60)
        # 等60秒，到下一分钟再开检测
main()
