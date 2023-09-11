#comptf2bot.py
#a discord bot made by tf_lecter 
#youtube.com/tf_lecter, steamcommunity.com/profile/tf_lecter

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#Very basic command which prints message (and username) back to the user
@bot.command(name='greet', help='Greets the user')
async def greet(ctx):
    await ctx.send(f'Hello World, and {ctx.author}.')

#Main Use of the Bot
#Step 1: Supply Steamid64 (could go one more and supply url -> convert into steamid64)
#Step 2: Use Steamid64 to generate ETF2L Division Information
#Step 3: Convey this info to the user
#Step 4: Profit!!

@bot.command(name='div', help='Divs a player for both 6s and 9s. Needs steamid64 as argument')
@commands.has_role('Founder')
async def div(ctx, userid:int):

    #recent6sDiv =
    #highest6sDiv = 
    #recent9sDiv = 
    #highest9sDiv = 

    #response = ("Most Recent (6s): {recent6sDiv}, Highest Div (6s): {highest6sDiv}. Most Recent (9s): {recent9sDiv}, Highest Div (9s): {highest9sDiv}.")
    #ctx.send("Hello {ctx.author}, Your request regarding {userName}: {response}")

    #temporary for debug
    if userid :
        msg = f"Hello, {ctx.author}"
        await ctx.send(msg)


#Catches errors. Hopefully supplies specific error message.
@div.error
async def div_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Something went wrong with your request. Try supplying a userid.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Something went wrong with your request. Try supplying an integer.')
    elif isinstance(error, commands.has_role('Founder')):
        await ctx.send('Something went wrong with your request. Are you allowed to run this command?')
    else :
        await ctx.send('Something went wrong with your request.')
        raise error

bot.run(TOKEN)