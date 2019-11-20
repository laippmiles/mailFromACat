#!/usr/bin/python
# -*- coding: utf-8 -*-
from weather_test import getweather,temperatureRes
def loadAfternoonSubAndCon(locale):
    from random import uniform
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'
    SSRlist = ['我对你好，不需要原因。',
               '没关系，我有耐心，等你慢慢开窍。',
               '我从未如此想要靠近一个人。',
               '想让我后悔的话，就不要在这种地方倒下。',
               '即使末日来临，我也会陪在你身边。',
               '香水品位还可以。'
               ]
    SRlist = ['不要再自作聪明，撮合我和其他人了。',
              '我也很开心，因为你这么开心。',
              '你究竟什么时候才能明白呢？',
              '打算就这么走了吗？跟我共舞一曲如何。',
              '这家超市食物种类太少，有种想买下来重新改造的冲动。',
              '不仅理解能力有问题，连反应力都有问题。',
              '自说自话带我去那个奇怪的地方，自己还睡着了。',
              '世界上应该只会有一个笨蛋，端着碗西红柿鸡蛋汤说“cheers”。',
              '少了领带夹感觉不太对。',
              '手写明信片已经寄了。',
              '有厨房观众的结果就是做菜多用一倍的原材料。'
              '给一个笨蛋的回礼。',
              '去房间放行李都能迷路的人，我第一次见到。',
              '笨蛋果然有够迟钝。'
              ]
    Rlist = ['你是我亲自培养的，怎能允许他人否定。',
             '懒惰只能造成失败，打起精神来吧！',
             '我会赔偿你，被我毀掉的一半假期。',
             '这是我给你下达的命令，不许不遵从。',
             '录完节目后，完整出现在我面前。',
             '你不必羡慕，只要努力，你也会有。',
             '刚才说话太严厉了吗？抱歉。',
             '下次不准再不接我电话。',
             '生气生得莫名其妙。',
             '路遇两只不太乖的野猫。',
             '谢谢某人的保温瓶，用起来不错。',
             '收到一张头版LP。不是什么名曲，只是对我来说有纪念意义。',
             '这次家常菜的味道依然有待提高。其实……姑且算是有进步。',
             '水族馆里真的有跟不动的企鹅较劲的笨蛋。',
             '猎豹的等待，是为了一击必中。',
             '在漂流瓶里塞硬币，笨蛋的行为真让人难以预测。',
             '我在1分钟内扑出156个球，获得最强门将称号，快来挑战我！海量红包和门票等你拿！',
             '解释一下什么叫逆生长。',
             '见识到一个魔方的新“拼”法，把色块拆开，再按照颜色组装好。',
             '没有必要那么认真地去对待每一个细节。……我没说不好。眼光还行，选得不错。',
             'brunch只是生活习惯不规律的借口。',
             '有时候，保持适当的饥饿感，才能保持敏锐度。',
             '雨滴落在头上是一件值得大喊大叫的事？',
             '世间不可分享之物：心情和。',
             '每个录制现场都能有这样的水准，我会考虑多来几次。怎么，是我说的不够具体还是笑的不够甜？',
             '开心不需要用咧开上下所有牙齿的方式表现出来。',
             '心急不仅吃不到热豆腐，还会把汤喝到袖子上。',
             '有风险的支出才叫投资。',
             '工作中没有无限次的试错机会。',
             '根据某人工作时的打字速度，就知道根本是在“带薪聊天”。',
             '给空碗拍照留念的意义在哪？',
             '只有小孩才喜欢把期待留到最后。',
             '说好只拍一张照片，结果对着猫拍了一下午。',
             '肚子饿的速度总能赶超策划案完成的进度。',
             '不浪费是对食物最大的尊重。',
             '你那句“李泽言保佑”我隔着门都能听见。',
             '自我控制应该是种本能。',
             '摘草莓的目的就是把自己吃到消化不良吗？',
             '因为一个稀奇古怪的点子，又在厨房折腾了一下午。',
             '你发的那条被拍糊的照片，我有不糊的版本。',
             '减法比加法更难。',
             '为什么扔垃圾也要看APP？',
             '有人未免入戏太深。'
            ]
    afternoonList = ['下午好。',
                     '午安，笨蛋。',
                     '午安。',
                   ]
    ballot = int(uniform(0,101))
    try:
        temperature, weather = getweather(locale)
        ballot = int(uniform(0,101))
        if ballot >= 0 and ballot <= 10 :
            SSRindex = int(uniform(0,len(SSRlist)))
            subject = SSRlist[SSRindex]

        elif ballot >=11 and ballot <= 30:
            SRindex = int(uniform(0,len(SRlist)))
            subject = SRlist[SRindex]
        else:
            Rindex = int(uniform(0,len(Rlist)))
            subject = Rlist[Rindex]

        subjectIndex = int(uniform(0, len(afternoonList)))
        content = afternoonList[subjectIndex] + "\n" + \
                      "今天最低"+ temperature.replace('℃','').split('到')[0] + "度," + temperatureRes(temperature) #+ '天气,' + weather
    except Exception as e:
        print(e)
        if 0 <= ballot <= 20 :
            SSRindex = int(uniform(0,len(SSRlist)))
            subject = SSRlist[SSRindex]
        elif 21 <= ballot <= 50:
            SRindex = int(uniform(0,len(SRlist)))
            subject = SRlist[SRindex]
        else:
            Rindex = int(uniform(0,len(Rlist)))
            subject = Rlist[Rindex]
        subjectIndex = int(uniform(0,len(afternoonList)))
        content = afternoonList[subjectIndex]
    return subject, content