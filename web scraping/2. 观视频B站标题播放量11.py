# KEYU CHEN


 #导入模块
import json
import requests
import pandas as pd # load pandas as pd
import numpy as np # load numpy
import re # re = "regular expression" which can be used to search
# headers = {
#       'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
#     }


# https://api.bilibili.com/x/space/arc/search?mid=54992199&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp
 
# for loops to get every single pages
for i in range(1,46):
    #模拟浏览器
    headers = {
      'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    #包含待爬取信息的url
#####################################################################################################################################
# 如何找到这个链接, 1) b 站主页 2)投稿专区 3） inspection 4）file name: search？
# 观视频          url = 'https://api.bilibili.com/x/space/arc/search?mid=54992199&ps=30&tid=0&pn=' + str(i) + '&keyword=&order=pubdate&jsonp=jsonp'
# 观察者网     
    url = 'https://api.bilibili.com/x/space/arc/search?mid=10330740&ps=30&tid=0&pn=' + str(i) + '&keyword=&order=pubdate&jsonp=jsonp'
# 科技袁人   url = 'https://api.bilibili.com/x/space/arc/search?mid=419501714&ps=30&tid=0&pn=' + str(i) + '&keyword=&order=pubdate&jsonp=jsonp'

#####################################################################################################################################

    # json not html
    #访问url
    r = requests.get(url,headers)
    #将爬取道德json格式的数据转化为字典
    text = json.loads(r.text)
    #取出嵌套字典里我们想要的部分
    #这里的字典嵌套在控制台里其实看的很清楚，我在上面的截图里圈了出来
    res = text['data']['list']['vlist']
    for item in res:
        #以列表的形式取出对我们有用的数据
#        list = ['av: '+str(item['aid']),' 视频标题: '+item['title'],' 播放量: '+str(item['play']),' 评论条数: '+str(item['video_review'])]
#        list = [' 发布时间: ' + str(item['created']) + ' 视频标题: '+item['title'],' 播放量: '+str(item['play']),' 评论条数: '+str(item['video_review'])]
        list = [' 发布时间: ' + str(datetime.datetime.fromtimestamp(item['created']).strftime(format)) + ' 视频标题: '+item['title'],' 播放量: '+str(item['play']),' 评论条数: '+str(item['video_review'])]
        #转化为字符串格式
        result = ''.join(list)
        #写进文件里
#####################################################################################################################################
        with open('4观察者网B站所有视频标题播放量标题total.txt','a+',encoding="utf-8") as f:
#####################################################################################################################################
            f.write(result+'\n')




import datetime
import pandas as pd  


str(datetime.datetime.fromtimestamp(item['created']).strftime(format))


# text = pd.Series(open('观视频B站所有视频标题播放量标题total.txt', encoding='utf8').read().splitlines()).str.split("::")
#text = pd.Series(open('观视频B站所有视频标题播放量标题total.txt', encoding='utf8').read().splitlines()).str.split(":")
text1 = pd.Series(open('观察者网B站所有视频标题播放量标题total.txt', encoding='utf8').read().splitlines()).str[7:]

text2 = text1.str.split(":")
text3 = text2.str[0].str.split(" ")
# text3.str[0]
# text3.str[1]
text4= text3.str[0]
# text2.str[1]
# text2.str[2]
textDF = pd.DataFrame()

textDF['栏目'] = text4
textDF['播放量'] = text2.str[1].str[:-4]
textDF['评论条数'] = text2.str[2]

textDF


text4.reset_index(drop=True)

text5 = list(text4)
text42 = text4.str.split("】")


import time
time.gmtime(1597582662)



# text5.to_csv(filename, index=False)