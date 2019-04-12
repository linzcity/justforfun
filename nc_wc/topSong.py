# -*- coding:utf-8 -*-
import requests
import json
import re
from bs4 import BeautifulSoup
import time

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

singer_url = 'https://music.163.com/artist?id=3684' # id为歌手的id，可以通过浏览器浏览网易云歌手页获取，这里比较蠢要靠手工获取

# 设置header，cookie很重要，需通过抓包工具获取（推荐fiddler）
header = {
"Connection":"keep-alive",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Cookie":""
}

web_data = requests.get(singer_url,headers=header,verify=False)

soup = BeautifulSoup(web_data.text, 'lxml')

singer_name = soup.select("#artist-name")

r = soup.find('ul', {'class': 'f-hide'}).find_all('a')

r = (list(r))

# 获取歌手热门的50首音乐id
music_id=[]
for each in r:
    song_name = each.text  # print(each.text)
    song_id = each.attrs["href"]
    music_id.append(song_id[9:])

print(music_id) 

doc = open('lrc.txt','a+',encoding='utf-8') # 后续需要手动调用generate.py

for id in music_id:
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(id) + '&lv=1&kv=1&tv=-1' #
    lyric = requests.get(lrc_url) # 请求url
    json_obj = lyric.text
    try:
        j = json.loads(json_obj)
        lrc = j['lrc']['lyric']
        pat = re.compile(r'\[.*\]') # 正则表达式
        lrc = re.sub(pat, "", lrc) # 替换为空
        lrc = lrc.strip() 
    except KeyError as e2:
        lrc = ''
        pass
    print('%s\n\n\n'% lrc,file=doc)
    print(id + '下载完成\n')
    time.sleep(0.2) # 避免一下子请求太多，设置一下休眠（虽然好像没什么必要，但小心为上）

doc.close()


