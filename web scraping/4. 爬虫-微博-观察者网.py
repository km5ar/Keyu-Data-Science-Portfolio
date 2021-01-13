
# 目标
# 转发评论点赞播放



import json
import requests


weibo = requests.get('https://weibo.com/newoutlook?refer_flag=1005055013_&is_all=1', auth=('user', 'pass'))
weibo  # 200, good 



requests.get('https://weibo.com/u/7314384474/home?topnav=1&wvr=6', auth=('user', 'pass'))



