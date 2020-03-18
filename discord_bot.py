import asyncio
import os
import traceback

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
        self.new_post_log_channel = None
        self.error_log_channel = None

    async def report_error(self, e):
        error = traceback.format_exc()
        error = error.replace(os.path.dirname(os.path.realpath(__file__)), ".") + '\n' + str(e)
        await self.error_log_channel.send(f'>>> {error}')

    async def load(self):
        while True:
            try:
                res = requests.get('https://gall.dcinside.com/mgallery/board/lists?id=dngks&exception_mode=recommend',
                                   headers={'User-Agent': 'PostmanRuntime/7.22.0'})
                soup = BeautifulSoup(res.content, features='html.parser')
                data = []
                for html in soup.find_all('td', attrs={'class': 'gall_tit'}):
                    link_node = html.find('a')
                    if link_node is not None:
                        pair = {'link': 'https://gall.dcinside.com/' + link_node['href'].replace('&amp;', '&')}
                        data.append(pair)
                return data
            except Exception as e:
                await self.report_error(e)
                await asyncio.sleep(10)

    async def start(self):
        self.run = True
        await self.error_log_channel.send('Start Crawling')

    async def stop(self):
        self.run = False
        await self.error_log_channel.send('Stop Crawling')

    async def stage(self):
        data = await self.load()
        self.error_log_channel.send('Stage Crawling')
        for pair in data:
            self.staged_link.append(pair['link'])

    async def update(self):
        self.error_log_channel.send('Update Crawling')
        data = await self.load()
        for pair in data:
            if not (pair['link'] in self.staged_link):
                try:
                    await self.new_post_log_channel.send(f'>>> {pair["link"]}')
                    print(f'>>> {pair["link"]}')
                    self.staged_link.append(pair['link'])
                except Exception as e:
                    await self.report_error(e)

        await asyncio.sleep(10)


hot_post_crawler = HotPostCrawler()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    hot_post_crawler.new_post_log_channel = client.get_channel(688934573668827171)
    hot_post_crawler.error_log_channel = client.get_channel(689662041753255959)
    await hot_post_crawler.start()
    await hot_post_crawler.stage()
    client.loop.create_task(hot_post_crawler_loop())


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
                    await hot_post_crawler.stage()
                    await msg.channel.send('성공적으로 스테이지했습니다.')
                except Exception as e:
                    text = '스테이지중 에러 발생 ' + str(e)
                    await msg.channel.send(text)
                    await hot_post_crawler.report_error(e)
            elif msg.content == '!념글크롤 시작':
                if hot_post_crawler.run:
                    await msg.channel.send('이미 동작하고 있습니다.')
                else:
                    try:
                        await hot_post_crawler.start()
                        await msg.channel.send('성공적으로 시작했습니다.')
                    except Exception as e:
                        text = '시작중 에러 발생 ' + str(e)
                        await msg.channel.send(text)
                        await hot_post_crawler.report_error(e)
            elif msg.content == '!념글크롤 정지':
                if hot_post_crawler.run:
                    try:
                        await hot_post_crawler.stop()
                        await msg.channel.send('성공적으로 정지 했습니다.')
                    except Exception as e:
                        text = '정지중 에러 발생 ' + str(e)
                        await msg.channel.send(text)
                        await hot_post_crawler.report_error(e)
                else:
                    await msg.channel.send('이미 정지 되었습니다.')
            elif msg.content == '!념글크롤 상태':
                text = '념글 크롤은 '
                if hot_post_crawler.run:
                    text += '동작중'
                else:
                    text += '정지중'
                await msg.channel.send(text + '입니다.')


async def hot_post_crawler_loop():
    while not client.is_closed():
        if hot_post_crawler.run:
            await hot_post_crawler.update()


client.run(os.getenv('COVIDIC_BOT_TOKEN'))
