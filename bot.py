from discord.ext import commands
import praw
import requests
import json
with open("stuff.json", 'r') as r:
    secrets = json.load(r)

prefix = "!"
bot = commands.Bot(command_prefix=prefix)
reddit = praw.Reddit(client_id=secrets['client_id'],
                     client_secret=secrets['client_secret'],
                     user_agent=secrets['user_agent'])
					 

@bot.event
async def on_ready():
    print("Logged in")
	
	
@bot.command()
async def ping(ctx):
    
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
	
@bot.command()
async def meme(ctx):
    
    post = reddit.subreddit('dankmemes').random()
    await ctx.send(post.url)

@bot.command()
async def urban(ctx, word):
    api = "http://api.urbandictionary.com/v0/define"
    resp = requests.get(api, params=[("term", word)]).json()
    if len(resp["list"]) == 0:
        await ctx.send("Word not found")
    await ctx.send(resp['list'][0]['definition'])
bot.run(secrets['token'])