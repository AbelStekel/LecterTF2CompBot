#comptf2bot.py
#a discord bot made by tf_lecter 
#youtube.com/tf_lecter, steamcommunity.com/profile/tf_lecter

import json
import re
import requests

from steam import Steam
#from steam.utils.web import make_requests_session

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
discordTOKEN = os.getenv('DISCORD_TOKEN')
#steamTOKEN = os.getenv('STEAM_TOKEN')
#etf2lTOKEN = os.getenv('ETF2l_TOKEN')

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
@bot.command(name='div', help='Divs a player for both 6s and 9s. Needs url as argument')
@commands.has_role('Founder')
async def div(ctx, url:str):

    #recent6sDiv =
    #highest6sDiv = 
    #recent9sDiv = 
    #highest9sDiv = 

    #response = ("Most Recent (6s): {recent6sDiv}, Highest Div (6s): {highest6sDiv}. Most Recent (9s): {recent9sDiv}, Highest Div (9s): {highest9sDiv}.")
    #ctx.send("Hello {ctx.author}, Your request regarding {userName}: {response}")

    #temporary for debug
    if url :
        #steam64 = steam64_from_url(url)
        msg = f"Hello, {ctx.author}." #You asked about {steam64}."
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
        await ctx.send('Something went wrong with your request. You might not have the rights needed for this reques.')
    else :
        await ctx.send('Something went wrong with your request.')
        raise error


#function to turn supplied url into steamid64
#steamid64 may then be used with other APIs
#def steam64_from_url(url, http_timeout=30):
    """
    Takes a Steam Community url and returns steam64 or None

    .. warning::
        Each call makes a http request to ``steamcommunity.com``

    .. note::
        For a reliable resolving of vanity urls use ``ISteamUser.ResolveVanityURL`` web api

    :param url: steam community url
    :type url: :class:`str`
    :param http_timeout: how long to wait on http request before turning ``None``
    :type http_timeout: :class:`int`
    :return: steam64, or ``None`` if ``steamcommunity.com`` is down
    :rtype: :class:`int` or :class:`None`

    Example URLs::

        https://steamcommunity.com/gid/[g:1:4]
        https://steamcommunity.com/gid/103582791429521412
        https://steamcommunity.com/groups/Valve
        https://steamcommunity.com/profiles/[U:1:12]
        https://steamcommunity.com/profiles/76561197960265740
        https://steamcommunity.com/id/johnc
        https://steamcommunity.com/user/cv-dgb/
    """

#    match = re.match(r'^(?P<clean_url>https?://steamcommunity.com/'
#                     r'(?P<type>profiles|id|gid|groups|user)/(?P<value>.*?))(?:/(?:.*)?)?$', url)

#    if not match:
#        return None

#    web = make_requests_session()

#    try:
#        # user profiles
#        if match.group('type') in ('id', 'profiles', 'user'):
#            text = web.get(match.group('clean_url'), timeout=http_timeout).text
#            data_match = re.search("g_rgProfileData = (?P<json>{.*?});[ \t\r]*\n", text)

#            if data_match:
#                data = json.loads(data_match.group('json'))
#                return int(data['steamid'])
#        # group profiles
#        else:
#            text = web.get(match.group('clean_url'), timeout=http_timeout).text
#            data_match = re.search("OpenGroupChat\( *'(?P<steamid>\d+)'", text)

#            if data_match:
#                return int(data_match.group('steamid'))
#    except requests.exceptions.RequestException:
#        return None


bot.run(discordTOKEN)