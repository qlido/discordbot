import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

bot = commands.Bot(command_prefix='!')
url = 'https://finance.naver.com/item/main.naver?code=005930'
# url = 'https://finance.naver.com/item/main.naver?code=000100'
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#chart_area > div.rate_info')
    print(title.getText().split('\n\n')[1].replace('포인트', '원'))
else:
    print(response.status_code)
col = 0xff0000


@bot.event
async def on_ready():
    global body
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#chart_area > div.rate_info')
        body = (title.getText().split('\n\n')[1].replace('포인트', '원'))
        print(body)
    else:
        print(response.status_code)
    if '플러스' in body:
        col = 0xff0000
    else:
        col = 0x0000ff


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sam(ctx):
    await ctx.send(title.getText().split('\n\n')[1].replace('포인트', '원'))


@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="오늘의 삼성 주식", description=title.getText().split('\n\n')[1].replace('포인트', '원'), color=col)
    await ctx.send(embed=embed)


bot.run('/*  */')
