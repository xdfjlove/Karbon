import discord
import random
import os 
from discord.ext import commands
sirk = ["Saudi Aramco 2017 ile 2019 yılları arasında 59.26",
"Chevron 43.35",
"Gazprom 43.23",
"ExxonMobil 41.90",
"National Iranian Oil Co 35.66",
"BP 34.02",
"Royal Dutch Shell 31.95",
"Coal India 23.12",
"Pemex 22.65"
"Petroleos de Venezuela 15.75",
"PetroChina 15.63",
"Peabody Energy 15.39",
"ConocoPhillips 15.23",
"Abu Dhabi National Oil Co 13.84",
"Kuwait Petroleum Corp 13.48",
"Iraq National Oil Co 12.60",
"Total SA 12.35",
"Sonatrach 12.30",
"BHP Billiton 9.80",
"Petrobras 8.68"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
#Bot hazırlık
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def Merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, dünyada en çok karbon salınımı yapan şirketleri hiç merak ettiniz mi')
@bot.command()
async def bunlar_ne(ctx):
    await ctx.send(random.choice(sirk))

bot.run(Token buraya gelecek)