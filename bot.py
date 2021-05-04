#!/usr/bin/env python3

# import ssl
import discord
from discord.ext import commands
import random
import requests
import json
import os

bot = commands.Bot(command_prefix = '.', verify=False)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def status():
    url = 'https://api.github.com/repos/ds3002/discord-bot/commits/main'
    response = requests.get(url)
    payload = response.text
    commit = payload['sha']
    await ctx.send(f'DS3002 Bot - Running commit `{commit}`')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined')

@bot.command(aliases=['pong'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def info(ctx):
    await ctx.send('My available commands are:\n\n`.ping` - A simple ping\n`.8ball` - play a game')

@bot.command()
async def clear(ctx, amount=5):
    if amount == 0:
        await ctx.send('Nothing to purge')
    else:
        await ctx.channel.purge(limit=amount)

@bot.command()
async def covid(ctx):
    url = (f'https://api.covid19api.com/world/total')
    response = requests.get(url)
    r = json.loads(response.text)
    cases = r['TotalConfirmed']
    deaths = r['TotalDeaths']
    recovered = r['TotalRecovered']
    await ctx.send(f'Current global COVID-19 statistics:\n  - Total cases: `{cases}`\n  - Confirmed deaths: `{deaths}`\n  - Confirmed recoveries: `{recovered}`\n\nData provided by https://api.covid19api.com/')
    # await ctx.send('You passed {} and {}'.format(arg1, arg2))

@bot.command(aliases=['8ball','eightball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes – definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)