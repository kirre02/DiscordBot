import logging

import os
import discord

from discord.ext import commands

from dotenv import load_dotenv


# this creates the prefix that you put before the command for example "--ping"
Client = commands.Bot(command_prefix='--')


# this function makes the bot print out "logged on!" each time it boots
@Client.event
async def on_ready():
    print('Logged on!')

# These two are the commands
# the first command is a command that responds with pong when someone writes "--ping"


@Client.command()
async def ping(ctx):
    await ctx.send(' :ping_pong: Pong!!')

# a command that writes the name of the user that wrote the message and the message


@Client.command()
async def sh(ctx, message):
    await ctx.send(f'{ctx.author.name} shouted to {message}')

# this is a command that makes it possible to invite a user


@Client.command(name='invite', pass_context=True)
async def invite(ctx, *argument):
    # this will create an invite link
    inviteLink = await ctx.channel.create_invite(max_uses=1, Unique=True)
    # sending it to a user
    await ctx.author.send(inviteLink)

# this will log everything that happens to the bot
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

Handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
Handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(Handler)


@Client.event
async def on_guild_join(guild):
    print(guild.channels)
    print([i.type for i in guild.channels])
    text_channel = [
        channel for channel in guild.channels if channel.type is discord.ChannelType.text]

    print(text_channel)
    await text_channel[0].send("yo yo yo")

# to make sure that you have the correct token and start the bot
# and the keep_alive function above is connected to the flask server
# that is written in the keep_alive file and it was made to keep it alive
# as long as the flask server was active
# the load_dotenv function makes it able to read the .env file so that it can read the token from the .env file

load_dotenv()

Client.run(os.getenv("TOKEN"))
