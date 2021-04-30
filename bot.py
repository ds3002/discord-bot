#!/usr/bin/env python3

# import ssl
import discord
from discord.ext import commands
import random
import requests
import os

bot = commands.Bot(command_prefix = '.', verify=False)

@bot.event
async def on_ready():
    print("This bot is ready to go!")

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
async def covid(ctx, state):
    if state:
        url = (f'https://api.covid19api.com/world/total')
        response = requests.get(url)
        cases = response.text['TotalConfirmed']
        deaths = response.text['TotalDeaths']
        recovered = response.text['TotalRecovered']
        await ctx.send(f'Current global COVID-19 statistics:\n  - Total cases: {cases}\n  - Confirmed deaths: {deaths}\n  - Confirmed recoveries: {recovered}')
    else:
        url = (f'https://api.covid19api.com/world/total')
        response = requests.get(url)
        cases = response.text['TotalConfirmed']
        deaths = response.text['TotalDeaths']
        recovered = response.text['TotalRecovered']
        await ctx.send(f'Current global COVID-19 statistics:\n  - Total cases: {cases}\n  - Confirmed deaths: {deaths}\n  - Confirmed recoveries: {recovered}')
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