import discord
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
  print('Bot Is Ready')
  
@client.command()
async def hello(message):
    await message.send('Hi! <@{message.author.id}>')
    
client.run('Nzk1NjcwNzIzMzQzMjg2MzQz.X_MwGw.lNxj4zQCGSbG7afmU3o4xcJUSug')
