import discord
from discord.ext import commands
from time import sleep
client = commands.Bot(command_prefix = '>')
from random import randint
from discord.utils import get

def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel


 

shop1 = {}
shop2 = {}
shop3 = {}
shop4 = {}

@client.command()
async def addToShop1(ctx, arg1, arg2,):
    shop1[arg1] = arg2
    await ctx.send(arg1 +"Added to shop1")
  
@client.command()
async def search(ctx, arg):
    if arg in shop1:
        await ctx.send("found" +  arg  + "shop1")

@client.command()
async def deleteInShop1(ctx, arg):
    del shop1[arg]
    await ctx.send(arg + "verwijderd uit shop1")


@client.command()
async def  changeInShop1(ctx, arg1, arg2, arg3):
    del shop1[arg1]
    shop1[arg2] = arg3
    await ctx.send(arg1 + "vervangen met" + arg2 + ":" + arg3)
    

@client.command()
async def openShop1(ctx):
    embed = discord.Embed(title="shop1", Description="Shop1", color = discord.Color.orange())
    for Key in shop1:
        embed.add_field(name=Key,value=shop1[Key],inline=True)
    await ctx.send(embed=embed)





@client.command()
async def addToShop2(ctx, arg1, arg2,):
    shop2[arg1] = arg2
    await ctx.send(arg1 +"Added to shop2")

@client.command()
async def deleteInShop2(ctx, arg):
    del shop2[arg]
    await ctx.send(arg + "verwijderd uit shop2")


@client.command()
async def  changeInShop2(ctx, arg1, arg2, arg3):
    del shop2[arg1]
    shop2[arg2] = arg3
    await ctx.send(arg1 + "vervangen met" + arg2 + ":" + arg3)
    

@client.command()
async def openShop2(ctx):
    embed = discord.Embed(title="shop2", Description="Shop2", color = discord.Color.orange())
    for Key in shop2:
        embed.add_field(name=Key,value=shop2[Key],inline=True)
    await ctx.send(embed=embed)



@client.command()
async def addToShop3(ctx, arg1, arg2,):
    shop3[arg1] = arg2
    await ctx.send(arg1 +"Added to shop3")

@client.command()
async def deleteInShop3(ctx, arg):
    del shop3[arg]
    await ctx.send(arg + "verwijderd uit shop3")


@client.command()
async def  changeInShop3(ctx, arg1, arg2, arg3):
    del shop3[arg1]
    shop3[arg2] = arg3
    await ctx.send(arg1 + "vervangen met" + arg2 + ":" + arg3)
    

@client.command()
async def openShop3(ctx):
    embed = discord.Embed(title="shop3", Description="Shop3", color = discord.Color.orange())
    for Key in shop3:
        embed.add_field(name=Key,value=shop1[Key],inline=True)
    await ctx.send(embed=embed)








#the bot token
client.run('ODA4NjAyOTY1NTgwNzA5OTAw.YCI8Mg.Tn2XL63tJX41dX1d-GdNPcb-u94')
