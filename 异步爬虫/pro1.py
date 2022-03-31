import requests
import time
from multiprocessing import Pool

url_list=['百度','搜狐','虎牙','斗鱼','腾讯']

def geturl(str):
    print('正在爬取',str)
    time.sleep(2)
    print(str,'爬取完成')

pool = Pool(5)
pool.map(geturl,url_list)
print(6666)