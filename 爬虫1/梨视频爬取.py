import requests
import re
from multiprocessing.dummy import Pool

url = 'https://www.pearvideo.com/category_8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Referer': 'https://www.pearvideo.com/'
}

def get_relURL(url,id):
    list1 = url.split('/')
    list2 = list1[-1].split('-')
    list2[0] = 'cont-'+ id
    list1[-1] = '-'.join(list2)
    return '/'.join(list1)



response = requests.get(url,headers = headers)
reptext = response.text
# print(type(reptext))
#print(response.status_code)
titlelist = re.findall('<div class="vervideo-title">(.+)</div>',reptext)
idlist = re.findall('<a href="video_(.+)" class="vervideo-lilink actplay">',reptext)
dictitle = zip(titlelist,idlist)
# print(dictitle)
# print(dict[dictitle])
url_1 = 'https://www.pearvideo.com/video_'
dic_video = []
for i,j in dictitle:
    url_2 = url_1 + j
    headers['Referer'] = url_2
    url_3 = f'https://www.pearvideo.com/videoStatus.jsp?contId={j}&mrd=0.8036022119327422'
    data = requests.get(url_3,headers = headers).json()
    res_url = data['videoInfo']['videos']['srcUrl']
    video_url = get_relURL(res_url,j)
    video = {
        'name':i,
        'url':video_url
    }
    dic_video.append(video)
print(dic_video)



