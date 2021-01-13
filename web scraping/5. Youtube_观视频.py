#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:39:34 2020

@author: cory
"""

import pandas as pd
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import chromedriver_binary
import string
pd.options.display.float_format = '{:.0f}'.format


is_link = f'https://finance.yahoo.com/quote/AAPL/financials?p=AAPL'
response = requests.get(is_link)

html = response.content

soup = BeautifulSoup(html,'lxml')



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


is_link = 'https://finance.yahoo.com/quote/AAPL/financials?p=AAPL'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(is_link)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'lxml')

close_price = [entry.text for entry in soup.find_all('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]






is_link = 'https://www.youtube.com/c/GuanVideo%E8%A7%82%E8%A7%86%E9%A2%91%E5%B7%A5%E4%BD%9C%E5%AE%A4/videos'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(is_link)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'lxml')

soup.findAll('a')


is_link = 'https://www.youtube.com/watch?v=XNCWRtPDCYE'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(is_link)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'lxml')

soup.find_all('div', id = "columns")

















try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# -*- coding: UTF-8 -*-
#import urllib2
import time
import urllib
import json
import datetime
import requests
import sys
import xlsxwriter
from importlib import reload
reload(sys)
#sys.setdefaultencoding("utf-8")
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
channel = "Samsung"#频道名
channel_id = 'UCWwgaK7x0_FR1goeSRazfsQ'#频道ID
 
 
 
class YoukuCrawler:
    def __init__(self):
        self.video_ids = []
        self.maxResults = 50#每次返回的结果数
        self.app_key = 'AIzaSyA2ZuiytIbIsRc2UpmaZOP18_VvHd9sKKM'
        self.channel_api = 'https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list?part=snippet,contentDetails&publishedAfter=2016-11-01T00:00:00Z&publishedBefore=2017-12-31T00:00:00Z&id='+ channel_id + '&key=' + self.app_key
        # self.info_api = 'https://www.googleapis.com/youtube/v3/videos?maxResults=50&part=snippet,statistics' + '&key=' + self.app_key
        self.info_api = 'https://www.googleapis.com/youtube/v3/videos'
        now = time.mktime(datetime.date.today().timetuple())
 
 
    def get_all_video_in_channel(self, channel_id):
 
 
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
 
        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&publishedAfter=2016-11-01T00:00:00Z&publishedBefore=2017-12-31T00:00:00Z&order=date&maxResults=25'.format(self.app_key, channel_id)
        url = first_url
 
        while True:
            print(url)
 
            request = urllib2.Request(url=url)
            response = urllib2.urlopen(request)
            page = response.read()
            result = json.loads(page, encoding="utf-8")
            for i in result['items']:
                try:
                    self.video_ids.append(i['id']['videoId'])#获取作品ID
                except:
                    pass
 
            try:
 
                next_page_token = result['nextPageToken']#获取下一页作品
                url = first_url + '&pageToken={}'.format(next_page_token)
 
            except:
                print("no nextPageToken")
                break
 
    def main(self):
        self.get_all_video_in_channel(channel_id)
        return self.get_videos_info()
 
 
    def get_videos_info(self):#获取作品信息
        url = self.info_api
        query = ''
        count = 0
        f = open(channel_id + '.txt', 'w')
        print(len(self.video_ids))
        for i in self.video_ids:
            try:
                count += 1
                query = i
                results = requests.get(url,
                                       params={'id': query, 'maxResults': self.maxResults, 'part': 'snippet,statistics',
                                               'key': self.app_key})
                page = results.content
                videos = json.loads(page, encoding="utf-8")['items']
                for video in videos:
 
                    try:
                        like_count = int(video['statistics']['likeCount'])
                    except KeyError:
                        like_count = 0
                    try:
                        dislike_count = int(video['statistics']['dislikeCount'])
                    except KeyError:
                        dislike_count = 0
 
                    temp = time.mktime(time.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%S.000Z"))
 
                    dateArray = datetime.datetime.utcfromtimestamp(int(temp))
                    otherStyleTime = dateArray.strftime("%Y-%m-%d")
                    print(otherStyleTime,count)
                    if (otherStyleTime>='2016-11-01' and otherStyleTime<="2017-12-31"):
                        print(video['snippet']['title'], otherStyleTime, like_count, int(video['statistics']['viewCount']))
                        f.write("%s\t%s\t%s\t%s\n" % (video['snippet']['title'], otherStyleTime, str(like_count), video['statistics']['viewCount']))
 
                    if otherStyleTime <= '2016-10-01':
                        return 1
 
            except Exception as e:
                print (e, count)
 
        return 1
 
if __name__ == "__main__":
    c = YoukuCrawler()
    c.main()
