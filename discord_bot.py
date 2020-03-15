import asyncio
import os
import threading
import time
import discord.utils
import requests
from bs4 import BeautifulSoup
from discord import DMChannel
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


class HotPostCrawler:
    run = False

    staged_link = []

    def __init__(self):
        self.trd = None
        self.stage()
        self.channel = None

    @staticmethod
    def load():
        res = requests.get('https://gall.dcinside.com/mgallery/board/lists?id=dngks&exception_mode=recommend',
                           headers={'User-Agent': 'PostmanRuntime/7.22.0'})
        soup = BeautifulSoup(res.content, features='html.parser')
        data = []
        for html in soup.find_all('td', attrs={'class': 'gall_tit'}):
            link_node = html.find('a', attrs={'class': 'reply_numbox'})
            if link_node is not None:
                pair = {'title': html.text,
                        'link': link_node['href'].replace('&amp;', '&').replace('&t=cv', '')}
                data.append(pair)
        return data

    def start(self):
        self.run = True
        self.trd = threading.Thread(target=self.update, args=[])
        self.trd.setDaemon(True)
        self.trd.start()
        print('Start Crawling')

    def stop(self):
        self.run = False
        self.trd.join()
        print('Stop Crawling')

    def stage(self):
        for pair in HotPostCrawler.load():
            self.staged_link.append(pair['link'])

    def update(self):
        while self.run:
            for pair in HotPostCrawler.load():
                if not (pair['link'] in self.staged_link):
                    try:
                        asyncio.run_coroutine_threadsafe(self.channel.send(f'>>> {pair["title"]}\n {pair["link"]}'))
                        print(f'>>> {pair["title"]}\n {pair["link"]}')
                        self.staged_link.append(pair['link'])
                    except Exception as e:
                        print(e)

            time.sleep(5)


hot_post_crawler = HotPostCrawler()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    hot_post_crawler.channel = client.get_channel(682788528983506953)
    hot_post_crawler.start()


@client.event
async def on_message(msg: discord.Message):
    if msg.channel.id == 683302727912390770 or type(msg.channel) is DMChannel:
        if msg.content in ['!로그인', '!로긴']:
            res = requests.get(f'http://127.0.0.1:8000/set_token?discord_id={msg.author.id}')
            if res.status_code == 200:
                load = eval(res.content.decode('utf-8'))
                await msg.channel.send(load['link'])
            elif res.status_code == 403:
                await msg.channel.send('권한이 부여되지 않았습니다. 개발팀에게 문의해주시길 바랍니다.')
            elif res.status_code == 404:
                await msg.channel.send('목록에 없는 유저입니다. 개발팀에게 문의해주시길 바랍니다.')
        elif msg.author.id == 348066198983933954:
            if msg.content == '!념글크롤':
                await msg.author.send('>>> 6초 단위로 념글의 상태변화를 알려주는 명령어 입니다.\n!념글크롤 스테이지\n!념글크롤 시작\n!념글크롤 정지\n!념글크롤 상태')
            elif msg.content == '!념글크롤 스테이지':
                try:
                    hot_post_crawler.stage()
                    await msg.channel.send('성공적으로 스테이지했습니다.')
                except Exception as e:
                    text = '스테이지중 에러 발생 ' + str(e)
                    await msg.channel.send(text)
            elif msg.content == '!념글크롤 시작':
                if hot_post_crawler.run:
                    await msg.channel.send('이미 동작하고 있습니다.')
                else:
                    try:
                        hot_post_crawler.start()
                        await msg.channel.send('성공적으로 시작했습니다.')
                    except Exception as e:
                        text = '시작중 에러 발생 ' + str(e)
                        await msg.channel.send(text)
            elif msg.content == '!념글크롤 정지':
                if hot_post_crawler.run:
                    try:
                        hot_post_crawler.stop()
                        await msg.channel.send('성공적으로 정지 했습니다.')
                    except Exception as e:
                        text = '정지중 에러 발생 ' + str(e)
                        await msg.channel.send(text)
                else:
                    await msg.channel.send('이미 정지 되었습니다.')
            elif msg.content == '!념글크롤 상태':
                text = '념글 크롤은 '
                if hot_post_crawler.run:
                    text += '동작중'
                else:
                    text += '정지중'
                await msg.channel.send(text + '입니다.')


client.run(os.getenv('COVIDIC_BOT_TOKEN'))
''' 
To-Do
Add Notik Discord bot
'''
