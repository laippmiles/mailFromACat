#!/usr/bin/python
# -*- coding: utf-8 -*-
from weather_test import getweather,temperatureRes


def loadImgSubAndCon(locale):
    from random import uniform
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'
    subjectlist = [
            '永恒',
            '不是猫，是老虎',
            '第二个硬币',
            '老朋友的田园生活',
            '闲暇午后',
            'Pinchos适合配一杯西班牙卡瓦',
            '能挑选到好餐厅是一种本领',
            '还知道用侧脸对着镜头',
            'Sangiovese',
            '天气不错',
            '一模一样',
            '海边',
            '另一种拓展生活的方式',
            '拍糊的版本',
            '山中何事',
            '一个硬币',
            '傻里傻气',
            '横冲直撞',
            '不是每次来沙漠都必须找骆驼',
            '长大的不只是胆子，还有体重',
            '幼稚',
            '灵感源于生活',
            '不知道跟谁学的',
            '纪念',
            'The Hunter',
            '这样的纪念品也不错',
            '下次试试这个',
            '完美的西红柿',
            '不速之客',
                ]
    subject_list_index = int(uniform(0, len(subjectlist)))
    subject = subjectlist[subject_list_index]
    try:
        print("开始获取天气",locale)
        temperature, weather = getweather(locale)
        print("temperature, weather ",temperature, weather)
        content = "今天最低"+ temperature.replace('℃', '').split('到')[0] + "度," + temperatureRes(temperature)
        #+ '天气,' + weather
    except Exception as e:
        print("addImage",e)
        content = ""

    return subject, content