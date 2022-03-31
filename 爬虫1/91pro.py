import requests
from lxml import etree
# url = 'https://0822.workgreat17.live/index.php'
#6092900-60929089


headers = {
'Referer': 'https://0822.workgreat17.live/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
for n in range(0,90):
    url = f'https://cdn77.91p49.com/m3u8/609290/609290{n}.ts'
    response = requests.get(url=url,headers = headers).content
    with open(f'609290{n}.ts','wb') as f:
        f.write(response)

# response = requests.get(url=url,headers = headers).text
# resp_xpa = etree.HTML(response)
# resp_xpa = resp_xpa.xpath('//*[@id="wrapper"]/div[1]/div[2]/div/div')
# for a_xpa in resp_xpa:
#     b_xpa = a_xpa.xpath('./div/div/a/@href')
#     for url in b_xpa:
#         print(url)
