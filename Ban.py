import discord
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix=',', intents = intents)

client = commands.Bot(
    command_prefix='x',
    case_insensitive=True
)


@client.event
async def on_ready():
    print("Don't be shy, just say xban to ban all users you got it!!")
    
@client.command()
async def ban(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            if member != ctx.author:
                await member.ban()
            else:
                continue
        except discord.Forbidden:
            continue

client.run("ENTER-YOUR-TOKEN-HERE")
