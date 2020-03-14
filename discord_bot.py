import os

import discord.utils
import requests
from discord import DMChannel
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(msg: discord.Message):
    if msg.channel.id == 683302727912390770 or type(msg.channel) is DMChannel:
        if msg.content in ['!로그인', '!로긴']:
            res = requests.get(f'http://127.0.0.1:8000/set_token?discord_id={msg.author.id}')
            if res.status_code == 200:
                load = eval(res.content.decode('utf-8'))
                await msg.author.send(load['link'])
            elif res.status_code == 403:
                await msg.author.send('권한이 부여되지 않았습니다. 개발팀에게 문의해주시길 바랍니다.')
            elif res.status_code == 404:
                await msg.author.send('목록에 없는 유저입니다. 개발팀에게 문의해주시길 바랍니다.')


client.run(os.getenv('COVIDIC_BOT_TOKEN'))
