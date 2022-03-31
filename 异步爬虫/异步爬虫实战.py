import asyncio,aiohttp



#detail_url = f'https://spa5.scrape.center/api/book/{bookid}/'

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

semaphore = asyncio.Semaphore(5)
async def list_books(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url,headers = header) as resp:
                resp = await resp.json()
                for books_list in resp['results']:
                    return books_list['id'],books_list['name']
tasks1 = []
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for i in range(0,10):
        list_url = f'https://spa5.scrape.center/api/book/?limit=18&offset={i*18}'
        tasks1.append(asyncio.ensure_future(list_books(list_url)))
    loop.run_until_complete(asyncio.wait(tasks1))
    for i in tasks1:
        print(i.result())







