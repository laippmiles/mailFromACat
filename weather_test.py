#coding:utf-8
import urllib.parse
import urllib.request
from xml.dom.minidom import parseString
from random import uniform

def getweather(locale):
    url = "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName"
    values = {"theCityName":locale}
    print(locale)
    data = urllib.parse.urlencode(values).encode(encoding='UTF8')
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode("utf8")
    dom = parseString(the_page)
    string = dom.getElementsByTagName("string")


    for s in string:
        try:
            data = s.childNodes[0].data
            print(data)
        except IndexError as e:
            next

    temperature = string[5].childNodes[0].data.replace('/','到')
    weather = string[6].childNodes[0].data.split(' ')[1]
    print(temperature)#气温
    print(weather)#天气
    return temperature,weather

# getweather("广州")

def temperatureRes(temperature):

    temperatureList_cold =[
        "别穿太少，注意保暖", "出门不要忘了戴上围巾"
    ]

    temperatureList_normal =[
        "天气不错", "天气不错"
    ]

    temperatureList_hot =[
        "注意防晒", "不要贪凉"
    ]

    wencha = ''
    if int(temperature.replace('℃','').split('到')[1]) - int(temperature.replace('℃','').split('到')[0]) > 5:
        wencha = '，还有温差有点大，小心感冒'

    temperature = int(temperature.replace('℃','').split('到')[0])
    print(temperature)
    if temperature < 20:
        cold_index = int(uniform(0,len(temperatureList_cold)))
        return temperatureList_cold[cold_index] + wencha + '。'
    elif temperature >= 20 and temperature <= 26:
        normal_index = int(uniform(0,len(temperatureList_normal)))
        return temperatureList_normal[normal_index] + wencha + '。'
    elif temperature > 26:
        normal_index = int(uniform(0,len(temperatureList_normal)))
        return temperatureList_normal[normal_index] + wencha + '。'