#!/usr/bin/python
# -*- coding: utf-8 -*-
from weather_test import getweather,temperatureRes
def loadNightSubAndCon(locale):
    from random import uniform
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'
    SSRlist = ['我对你好，不需要原因。',
               '没关系，我有耐心，等你慢慢开窍。',
               '我从未如此想要靠近一个人。',
               '想让我后悔的话，就不要在这种地方倒下。',
               '即使末日来临，我也会陪在你身边。',
               '今天营业。',
               '晚上布丁买一送十。'
                ]
    SRlist = ['帮别人完成工作，熬到深夜， 你傻吗？',
              '我想......一直和你在一起。',
              '雨要到后半夜才停，坐我的车回去吧。',
              '我疲惫的一面只在你面前展现。',
              '晤......谢谢你能理解我。',
              '喜欢吃红酒炖梨的，大概也就只有上了年纪的人和笨蛋了。',
              '随便找了部电影看。',
              '赠人玫瑰，手有余香。'
             ]
    Rlist = ['时间静止只为与你相遇。',
             '汽水容易失眠，喝一杯牛奶吧。',
             '如果睡不着，允许你找我闲聊。',
             '对我来说，能看到你的笑容就好。',
             '无论什么要求，我都会满足你。',
             '在我面前，还是实话实说比较好。',
             '我可以给你带各地的纪念品。',
             '我没有意见，这次你做得很好。',
             '伟大的音乐能带你超越思想，品尝静心的滋味。',
             '堵车的时候听上一首巴赫的《Air on the G string》，能有效缓解焦虑情绪。',
             '怎样回礼比较合适？',
             '无意中看到某人的早期作品，倒也有趣。',
             '有个幼稚的人在身边，每天都是六一儿童节。',
             '某人自己说要看恐怖电影，然后全程捂耳闭眼。',
             '在慈善晚会上哭得惊天动地的人，我还是第一次见。',
             '某人的身体里大概装了两种灵魂，弹钢琴时一种，吃饭时一种。',
             '什么时候才能改掉吃饭前拍照的习惯。',
             '看到某人今天夜宵订单的长度，决定把报告的截止期提前一天。',
             '“过去、现在、未来的区别只是一种持久顽固的幻觉。”',
             '傻人有傻福。',
             '雨滴落在头上是一件值得大喊大叫的事？',
             '确实已经很久没有安静欣赏雨后城市的心情了。',
             '……给我老实呆着。',
             '梅子酒煎牛排？',
             '有人吵着要玫瑰，结果被刺扎了手。',
             '稀奇古怪的糖果然很难吃。',
             '删几张照片就能解决的事，为什么能纠结一个晚上。',
             '某人还有时间研究什么玩具，看来最近很闲。',
             '如果瑜伽球是毛线团做的，某人现在已经动弹不得了。',
             '水平不够的话，就老实用模具。',
             '再给你削个苹果，以示嘉奖？',
             '很难想象一个超市推车都控制不好的笨蛋是怎么学会开车的。',
             '果然在衣橱的西装口袋里又找到了其他东西。',
             '为什么帽子上要有兔子耳朵。',
             '艺术应当取悦生活，而不是被永久封存。',
             '气势很足，但没什么实际内容的占卜。',
             '想要收获惊喜的滋味，必须认真体会食物的气质。',
             '难得安静下来。',
             '希望某人能按时赴约一次。',
             '我对你唯一的希望，就是不要又在奇怪的地方迷路。',
             '喜欢就留住，没有人会为了你的克制发荣誉证书。',
             '不要害怕犯错，但成熟的人知道如何从错误中获得进步。',
             '旋律动听的原因在于音符之间的比例之美。',
             '太依靠夜晚的指示灯，反而会更分不清方向。',
             '微调了一下手冲咖啡的成分。',
             '有人接机还迟到。',
             '一开始就亮出底牌是什么战术？'
            ]
    nightList = ['少吃点夜宵。',
                 '晚安，笨蛋。',
                 '不要熬夜了。',
                ]
    ballot = int(uniform(0,101))
    try:
        temperature, weather = getweather(locale)
        ballot = int(uniform(0,101))
        if ballot >= 0 and ballot <= 10 :
            SSRindex = int(uniform(0,len(SSRlist)))
            subject = SSRlist[SSRindex]

        elif ballot >= 11 and ballot <= 30:
            SRindex = int(uniform(0,len(SRlist)))
            subject = SRlist[SRindex]
        else:
            Rindex = int(uniform(0,len(Rlist)))
            subject = Rlist[Rindex]

        subjectIndex = int(uniform(0, len(nightList)))
        content = nightList[subjectIndex] + "\n" + \
                      "今天最低"+ temperature.replace('℃','').split('到')[0] + "度," + temperatureRes(temperature) #+ '天气,' + weather
    except Exception as e:
        print(e)
        ballot = int(uniform(0,101))
        if 0 <= ballot <= 20 :
            SSRindex = int(uniform(0,len(SSRlist)))
            subject = SSRlist[SSRindex]
        elif 21 <= ballot <= 50:
            SRindex = int(uniform(0,len(SRlist)))
            subject = SRlist[SRindex]
        else:
            Rindex = int(uniform(0,len(Rlist)))
            subject = Rlist[Rindex]
        subjectIndex = int(uniform(0,len(nightList)))
        content = nightList[subjectIndex]

    return subject, content