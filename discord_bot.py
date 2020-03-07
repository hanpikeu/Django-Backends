import os

import discord.utils

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(msg: discord.Message):
    if msg.channel.id == 683302727912390770:
        if msg.content in ['!로그인', '!로긴']:
            print(msg.author)
            await msg.author.send("이 글이 보이시면 말 해주세요.")


client.run(os.getenv('BOT_TOKEN'))
