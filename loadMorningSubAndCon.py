#!/usr/bin/python
# -*- coding: utf-8 -*-
from weather_test import getweather,temperatureRes
def loadMorningSubAndCon(locale):
    from random import uniform
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'
    SSRlist = ['我对你好，不需要原因。',
               '没关系，我有耐心，等你慢慢开窍。',
               '我从未如此想要靠近一个人。',
               '想让我后悔的话，就不要在这种地方倒下。',
               '即使末日来临，我也会陪在你身边。',
               '天气并不是赖床以及迟到的理由。'
                ]
    SRlist = ['在眼中，万般风景不如你。',
              '我世界中唯一的变数就是你。',
              '不知为什么，面对你，我总能卸下心防。',
              '或许我已经等不及让你慢慢开窍了。',
              '我正好在外面，咳，带你出去吃早餐。',
              '连咖啡都煮不好的笨蛋，还能做什么……',
              '约好8点见，多一秒钟一分钟都不是8点！',
              '一个影视公司开会这么死气沉沉？',
              '心静自然凉。',
              '丧值爆表？某人拖延工作的理由又多了一条。',
              '笨蛋果然是笨蛋。'
              ]
    Rlist = ['每个人都有很多面，不像你只有儍的一面。',
             '你的身体，你不关心，可是我关心。',
             '这就是你给我的礼物？好吧，我勉强收下。',
             '不仅要占领你的心，还要占领你的胃。',
             '专心创作吧，应酬和交际，交给我就好。',
             '我有哪次没有出手帮你。',
             '以后遇到问题，该找我就不要傻扛着。',
             '某个笨蛋估计又要摔倒了吧。',
             '最近天气预报的准确率有所提高。',
             '你来说说，发呆的意义在哪里？',
             '谁告诉你，我只会做西餐？',
             '头回见到PPT里的备注写得比剧本还精彩的。',
             '某人眼皮打架的激烈程度比股价波动大多了。',
             '精准扼要的报告值得鼓励。',
             '判断一个人成熟与否的标准有很多，比如打伞的时候是否还会转雨伞。',
             '做事要沉得住气。',
             '不是非要看到成功，某人的进步也很值得关注。',
             '异国街头，循着酒香找到了一家很不错的店。',
             '打开表盖就看见一张傻笑的脸。',
             '八点开会，七点四十起床，某人的新纪录。',
             '突然从音响里放出了“让人印象深刻的是您的长寿秘诀……”，确实印象很深刻。',
             '冰山？正好给你降降温。',
             '今天会前节目是某人表演徒手解数据线十分钟。',
             '领带和围巾的区别不止是材质，还有打法。',
             '某人今天简直就是一颗行走的话梅糖。',
             '看来私下偷偷练过字。',
             '比起收藏，使用更能赋予物品灵魂。',
             '小时候估计没少因为多动症被叫过家长。',
             '从一个人的表情就可以轻而易举地猜出她的内心活动。',
             '胆子倒是变大了。',
             '做报告前在办公室外双手合十碎碎念是什么环节？',
             '你是把我当作备忘录了吗？',
             '嚷嚷李泽言也是为了减压？',
             '意志力的作用往往大于行动力。',
             '没有任何一件事可以简单地用正确或错误来定义。',
             '机会一旦错过了，就不会再次转回眼前。',
             '百米冲刺式的碰瓷，还是第一次见到。',
             '我替地板谢谢你的咖啡。',
             '看来某人一到deadline，脑子就会离家出走。',
             '共情是一项优点，不需要感到困扰。',
             '你是这样的人。',
             '全程思考到达之后说的第一句话，意义在哪里？',
             '没有绝对静止，但必然有绝对运动。',
             '有些小伎俩一眼就能看穿。',
             '有些人就是过了多少年都会被小吃摊缠住脚。',
             '"不可能到老婆婆的时候还会这样啦！"那到时候见证一下。',
             '今天倒是有好好遵守约定。',
             '公司停电并不是延迟工作的理由。'
            ]
    morningList = ['记得吃早饭。',
                   '早安，笨蛋。',
                   '早上好，别再赖床了。',
                ]
    ballot = int(uniform(0,101))
    try:
        temperature, weather = getweather(locale)
        ballot = int(uniform(0,101))
        if 0 <= ballot <= 10 :
            SSRindex = int(uniform(0,len(SSRlist)))
            subject = SSRlist[SSRindex]
        elif 11 <= ballot <= 30:
            SRindex = int(uniform(0,len(SRlist)))
            subject = SRlist[SRindex]
        else:
            Rindex = int(uniform(0,len(Rlist)))
            subject = Rlist[Rindex]
        subjectIndex = int(uniform(0, len(morningList)))
        content = morningList[subjectIndex] + "\n" + \
                      "今天最低"+ temperature.replace('℃','').split('到')[0] + "度," + temperatureRes(temperature) #+ '天气,' + weather
    except Exception as e:
        print(e)
        if 0 <= ballot <= 10 :
            SSRindex = int(uniform(0,len(SSRlist)))
            subject = SSRlist[SSRindex]
        elif 11 <= ballot <= 30:
            SRindex = int(uniform(0,len(SRlist)))
            subject = SRlist[SRindex]
        else:
            Rindex = int(uniform(0,len(Rlist)))
            subject = Rlist[Rindex]
        subjectIndex = int(uniform(0,len(morningList)))
        content = morningList[subjectIndex]
    return subject, content