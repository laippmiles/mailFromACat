#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.utils import formataddr
from time import sleep
from getTo import getTo
from getSubAndCon import getSubAndCon

def sendEmailFromLzy(mailTime,h, filePath= r'D:\桌面\mailFromAKing\file' + '\\', fileName= 'file0.jpg',sendFile = False,addImg = False):
    import smtplib
    import os
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    #from email import encoders


    user = '邮箱名'
    pwd = '邮箱授权码'
    smtpHost = 'smtp.qq.com'
    s = smtplib.SMTP_SSL(smtpHost,465)
    s.login(user, pwd)

    toList = getTo()
    for to in toList.keys():
        msg = email.mime.multipart.MIMEMultipart()
        print(toList[to])
        subject, content,addImgAfter = getSubAndCon(mailTime, h, toList[to],addImg)
        msg['From'] = formataddr(["李泽言", user])
        msg['Subject'] = subject
        msg['to'] = to

        mail_msg = '''
        <p>\n\t ''' + content + '''</p>''' + '''
        <p><img src="cid:image1"></p>
        '''

        msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        if sendFile == True:
            # ------------------------------------------------------------
            annexPath = filePath + fileName
            part = MIMEApplication(open(annexPath, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=fileName)
            msg.attach(part)
        # -----------------------------------------------------------
        if addImgAfter == True:
            try:
                # 指定图片为当前目录
                img_name = subject
                # 树莓派用路径
                img_path = r'/home/pi/Desktop/mailFromAKing/file/img/' + img_name + '.jpg'
                # 电脑调试用路径
                # img_path = r'K:\代码\mailFromACat\file\img' + '\\' + img_name + '.jpg'
                # img_path = r"K:\代码\mailFromACat\file\img\Pinchos适合配一杯西班牙卡瓦.jpg"
                msgImage = MIMEImage(open(img_path, 'rb').read(), _subtype='octet-stream')
                # 定义图片 ID，在 HTML 文本中引用
                msgImage.add_header('Content-ID', '<image1>')
                msg.attach(msgImage)
            except Exception as e:
                print("正文添加图片出错", e)
        s.sendmail(user, to, msg.as_string())
        print('发送成功')
        sleep(5)
        #每隔20秒发一次信
    s.close()


def mailFromLZY(hour,h, filePath, fileName, sendFile = False, addImg = False):
    #try:
    sendEmailFromLzy(hour,h, filePath, fileName,sendFile,addImg)
    #except Exception as err:
        #print(err)