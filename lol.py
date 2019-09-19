from discord.ext import commands

import json
import os
import requests

champions = json.loads(requests.get("http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json").text)['data']

class Lol(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def story(self, ctx, *name): #print the storyline from all champions starting with your input
        for champ in getChamps(name):
            data = getStory(champ)
            await ctx.send(data)


def getChampData(id): # get the specific data for a champ with the given id
    return json.loads(requests.get("http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion/" + id +".json").text)['data'][id]


def getStory(champion): # get the storyline from a specific champion
    data = getChampData(champion["id"])
    return data["name"] + ": " + data["title"] + "\n----------\n" + data["lore"]

def getChamps(nameparts): #select all fitting your input(nameparts)
    return  [champions[champ] for champ in champions if any([any([realName.casefold().startswith(name.casefold()) for realName in champions[champ]['name'].split(" ")]) for name in nameparts])]





def setup(bot): #needed to be a multifile discord bot
    bot.add_cog(Lol(bot))
