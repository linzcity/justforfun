# -*- coding:utf-8 -*-
import requests
import json
import re

def main():
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(27853227) + '&lv=1&kv=1&tv=-1' # 某曲音乐：以rap god为例

    lyric = requests.get(lrc_url) # 请求url
    
    json_obj = lyric.text 

    j = json.loads(json_obj)

    lrc = j['lrc']['lyric']

    pat = re.compile(r'\[.*\]') # 正则表达式

    lrc = re.sub(pat, "", lrc) # 替换为空

    lrc = lrc.strip()

    doc = open('one_lrc.txt','a+',encoding='utf-8')

    print('%s\n'% lrc,file=doc)

    doc.close()

    print(lrc)

    '''
    # 去掉歌词附加信息，建议只用于中文歌，英文歌可能歌词本身包含':'
    lrc = lrc.replace('：',':')# 去掉附加信息：作曲、作词人介绍等，否则会出现较多的人名
    index = find_last(lrc,':')
    index = lrc.find('\n',index)
    if index == -1:
        index = 0
    print(lrc[index:])
    '''


def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position

if __name__ == '__main__':
    main()
