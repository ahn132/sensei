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

    # $hello
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
        return

    # $inspire
    if message.content.startswith("$inspire"):
        inspo = get_inspo()
        await message.channel.send(inspo)
        return

    # $quote
    if message.content.startswith("$quote"):
        author = message.content.split("$quote ", 1)[1]
        quote = get_quote(author)
        if quote is not None:
            await message.channel.send(quote)
        else:
            await message.channel.send("Invalid author...try again")



    # $new
    if message.content.startswith("$new"):
        cmd = message.content.split(" ", 2)[1]
        arg = message.content.split(" ", 2)[2]
        if cmd == "sad_word":
            add_sad(arg)
        elif cmd == "angry_word":
            add_angry(arg)
        elif cmd == "encouraging_phrase":
            add_encourage(arg)
        elif cmd == "calming_phrase":
            add_calm(arg)
        elif cmd == "quote":
            add_quote(arg)
        return

    # emotional response
    for word in message.content.split():
        response = respond(word)
        if response is not None:
            await message.channel.send(response)

bot.run("MTEwNTE2MDA3NTU1Mjc3MjIyNw.GeYQzs.ZbxwuZHu7cK4BZuDZj0qfCdYrC5L3WJONa1lBg")
