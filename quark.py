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
    await message.send(f'Hi! <@{message.author.id}>')
    
@client.command()
async def invite(message):
    embed = discord.Embed(description = '[click here](https://discord.com/api/oauth2/authorize?client_id=795670723343286343&permissions=8&scope=bot)', color = 0x00ff00)
    embed.set_footer(text = 'made by Leptons#4142', icon_url = 'https://cdn.discordapp.com/attachments/781843712489685076/795690819130097664/539043631c7bdee39d16fe326897df6e.jpg')
    await message.send(embed = embed)
    
client.run('Nzk1NjcwNzIzMzQzMjg2MzQz.X_MwGw.lNxj4zQCGSbG7afmU3o4xcJUSug')
