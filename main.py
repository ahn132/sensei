import discord
import random
from db import *
from nodb import *

# initialize discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
        return

    # get random quote
    if message.content.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)
        return

    if message.content.startswith("$new"):
        cmd = message.content.split(" ", 2)[1]
        if cmd == "sad_word":
            print("test")
            print(message.content.split(" ", 2)[2])
            add_sad(message.content.split(" ", 2)[2])
        return

    # emotional response
    for word in message.content.split():
        response = respond(word)
        if response is not None:
            await message.channel.send(response)


bot.run("MTEwNTE2MDA3NTU1Mjc3MjIyNw.GABpu_.JPvp0odWvj20zqHxzKRnbdvhcJHsiClOO5OznU")
