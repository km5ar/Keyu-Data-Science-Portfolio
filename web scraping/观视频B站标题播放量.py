# KEYU CHEN


 #导入模块
import json
import requests

# headers = {
#       'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
#     }

 
# for loops to get every single pages
for i in range(1,46):
    #模拟浏览器
    headers = {
      'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    #包含待爬取信息的url
#####################################################################################################################################
    url = 'https://api.bilibili.com/x/space/arc/search?mid=54992199&ps=30&tid=0&pn=' + str(i) + '&keyword=&order=pubdate&jsonp=jsonp'
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
        list = ['av: '+str(item['aid']),' 视频标题: '+item['title'],' 播放量: '+str(item['play']),' 评论条数: '+str(item['video_review'])]
        #转化为字符串格式
        result = ''.join(list)
        #写进文件里
        with open('观视频B站所有视频标题播放量标题.txt','a+',encoding="utf-8") as f:
            f.write(result+'\n')
