import random
import time
from multiprocessing.dummy import Pool
import requests
from lxml import etree


#  从详情页中解析出视频的地址


# 求真实url
def get_relURL(url, ID):
    list2 = url.split('/')
    list3 = list2[-1].split('-')

    list3[0] = "cont-" + ID
    print(list2)
    print(list3)
    list2[-1] = '-'.join(list3)
    return '/'.join(list2)


# 视频下载，对链接发起请求获取视频的二进制数据，然后持久化存储
def get_video(dic):
    url = dic['url']
    filename = dic['name']
    print(filename, '正在下载..')
    file = requests.get(url=url, headers=headers).content
    with open(filename, 'wb') as f:
        f.write(file)
        print(filename, '下载完成')


headers = {}
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 "
    "Safari/537.36 "
]
headers['User-Agent'] = random.choice(user_agent_list)
# 原则:线程池处理的是阻塞且耗时的操作
# 对下述url发起请求，解析出视频详情页的url和视频的名称
page_url = "https://www.pearvideo.com/category_5"
page_text = requests.get(url=page_url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
# 视频详情页面ajax请求的url
get_url = "https://www.pearvideo.com/videoStatus.jsp"
videos = []
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div[@class="vervideo-bd"]/a/@href')[0]
    video_name = li.xpath('.//div[@class="vervideo-title"]/text()')[0] + '.mp4'
#     # 添加ajax请求需要的参数
    contId = li.xpath('./div[@class="vervideo-bd"]/a/@href')[0][6:]
    params = {
        "contId": contId,
        "mrd": random.random(),
    }
    # 给请求头信息添加Referer
    headers['Referer'] = detail_url
    # 获取视频详情页面ajax请求返回数据
    data = requests.get(url=get_url, headers=headers, params=params).json()
    #  从详情页中解析出假的视频url
    fal_video_url = data['videoInfo']['videos']['srcUrl']
    # 组合真实视频url
    rel_video_url = get_relURL(fal_video_url, contId)
    video_dict = {
        "name": video_name,
        "url": rel_video_url
    }
    videos.append(video_dict)
#
# # 使用线程池对数据进行请求(较为耗时的阻塞操作)
# pool = Pool(4)
# pool.map(get_video, videos)
# # 线程池关闭
# pool.close()
# # 主线程等待子线程结束之后结束
# pool.join()