#comptf2bot.py
#a discord bot made by tf_lecter 
#youtube.com/tf_lecter, steamcommunity.com/profile/tf_lecter

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from steam import Steam
import json
import yaml

#fordebug
#import logging
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

load_dotenv()
discordTOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

steamTOKEN = os.getenv('STEAM_TOKEN')
steam = Steam(steamTOKEN)

#etf2lTOKEN = os.getenv('ETF2l_TOKEN') for both 6s and 9s. 

#Very basic command which prints message (and username) back to the user
@bot.command(name='greet', help='Greets the user')
async def greet(ctx):
    await ctx.send(f'Hello World, and {ctx.author}.')

#convert command for the bot
#takes steamurl, returns steamid64
#@bot.command(name='convert', help='Converts steamurl into steamid64')
#async def convertStmURL(ctx, url : str):

#    this doesnt work for some reason
#    query = steam.users.resolve_vanity_url(steam, url)

#    if query['success'] == 1 :
#        steamid64 = query['response']['steamid']
#        await ctx.send(f"{steamid64}")
#    else :
#        await ctx.send("Something went wrong in the conversion.")

#bot command which performs account lookup on steam
#takes steamid64 as arg
@bot.command(name='lookup', help='Pulls a steam profile info (.json)')
async def lookup(ctx, steamid : int):

    #get .json from api & convert .json to .yaml for human readable output
    userFinal = yaml.dump(steam.users.get_user_details(steamid))

    await ctx.send(f"```{userFinal}```")


#Main Use of the Bot
#Step 1: Supply Steamid64
#Step 2: Use Steamid64 to generate ETF2L Division Information
#Step 3: Convey this info to the user
#Step 4: Profit!!
@bot.command(name='div', help='Div-checks a player. Input in steamid64')
@commands.has_role('Founder')
async def div(ctx, steamid : int ):

    #temporary for debug, this is the SUCCESS-response.
    if steamid > 0:
        msg = f"Hello, {ctx.author}. The request seems to have worked (poggers)"
        await ctx.send(msg)

#event in case of asking for not-existing command
@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound):  
        await ctx.send("Error! This command does not exist.")

#Catches errors related to the !div command. Hopefully supplies specific error message.
@div.error
async def div_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Something went wrong with your request. Missing required argument.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Something went wrong with your request. Argument of wrong type.')
    elif isinstance(error, commands.MissingRole):
        await ctx.send('Something went wrong with your request. You might not have the rights needed for this request.')
    else :
        await ctx.send('Something went wrong with your request.')
        raise error

bot.run(discordTOKEN)# , log_handler = handler)#, root_logger=True)