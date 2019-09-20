from discord.ext import commands

import json
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

    @commands.command()
    async def h2p(self, ctx, *name): #get tips for all champions starting with your input
        for champ in getChamps(name):
            data = getTips(champ)
            await ctx.send(data)

    @commands.command()
    async def counter(self, ctx, *name): #get countertips for all champions starting with your input
        for champ in getChamps(name):
            data = getCountertips(champ)
            await ctx.send(data)

    @commands.command()
    async def passive(self, ctx, *name): #get passive information for all champions starting with your input
        for champ in getChamps(name):
            data = getPassive(champ)
            await ctx.send(data)

    @commands.command()
    async def abilities(self, ctx, *name): #get main information about the abilitys of champions
        for champ in getChamps(name):
            data = getAbilitys(champ)
            for ability in data:
                await ctx.send(ability)



def getChampData(id): # get the specific data for a champ with the given id
    return json.loads(requests.get("http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion/" + id +".json").text)['data'][id]


def getStory(champion): # get the storyline from a specific champion
    data = getChampData(champion["id"])
    return data["name"] + ": " + data["title"] + "\n----------\n" + data["lore"]

def getChamps(nameparts): #select all fitting your input(nameparts)
    return  [champions[champ] for champ in champions if any([any([realName.casefold().startswith(name.casefold()) for realName in champions[champ]['name'].split(" ")]) for name in nameparts])]

def getTips(champion):
    data = getChampData(champion["id"])
    return data["name"] + "\n----------\n" + ("no tips available" if data["allytips"] == [] else "*" + '\n*'.join(data["allytips"]))

def getCountertips(champion):
    data = getChampData(champion["id"])
    return data["name"] + "\n----------\n" + ("no tips available" if data["enemytips"] == [] else "*"+ '\n*'.join(data["enemytips"]))

def getAbilitys(champion):
    data = getChampData(champion["id"])
    return [ability["name"] + "\n----------\n" + ability["description"] for ability in data["spells"]]

def getPassive(champion):
    data = getChampData(champion["id"])
    return data["passive"]["name"] + "\n----------\n" + data["passive"]["description"]

def setup(bot): #needed to be a multifile discord bot
    bot.add_cog(Lol(bot))
