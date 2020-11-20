import discord
import random
import time
import asyncio

TOKEN = "( I removed it from this so u cant rape my bot :^) )"

client = discord.Client()

Coinflip = (
    "Heads",
    "Tails",
)

responses = (
    "No.",
    "Yes.",
    "My sources say no.",
    "It seems likely.",

)


@client.event
async def on_message(message):
    if message.author == client.users:
        return

    if message.content.startswith("+Test"):
        await message.channel.send("Im online.")

        if message.content.startswith("+Say"):
            mes = message.content.split()
            output = " "
            for word in mes[1:]:
                output += word
                output += " "
                await message.channel.send(output)
                await message.delete()

    if message.content.startswith("+8ball"):
        await message.channel.send(random.choice(responses))

    if message.content.startswith("+Coinflip"):
        await message.channel.send(random.choice(Coinflip))

    if message.content.startswith("+Help"):
        embed = discord.Embed(title="__Commands__", color=0x00ff00)
        embed.add_field(name="+Help", value="Shows this message")
        embed.add_field(name="+Coinflip", value="Flips a coin")
        embed.add_field(name="+8ball", value="Tells u the answer to ur question (for example am i good at videogames?)")
        await message.channel.send(content=None, embed=embed)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Vp trying to code"))

    print("Im ready and online !")


client.run(TOKEN)
