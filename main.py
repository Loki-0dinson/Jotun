import asyncio
import logging

from discord import Client as DiscordClient, Game
from discord.ext import commands

from core.settings import TOKEN, DEBUG, LOG_LEVEL, LOG_FORMAT, LOG_DATE_FORMAT
from core.utils import loginfo, logwarn, logcritical
from db import DB as db

if DEBUG:
    from icecream import ic

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, style='{')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_prefix(bot, message):
    prefixes = ['$']

    # # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '$'

    # If we are in a guild, we allow for the user to mention us or use any of
    # the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix='$')
initial_extensions = ['cogs.greetings']


@bot.event
async def on_ready():
    logger.info('Logged in as: NAME {bot.user.name}, ID {bot.user.id}')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you
    # could remove type and url.
    await bot.change_presence(activity=Game(name='Cogs Example'))


@bot.event
async def on_message_delete(message):
    """Called when a message is deleted. If the message is not found in the
    internal message cache, then this event will not be called. Messages might
    not be in cache if the message is too old or the client is participating in
    high traffic guilds.

    If this occurs increase the Client.max_messages attribute or use the
    `on_raw_message_delete()` event instead.

    This requires Intents.messages to be enabled.
    """
    pass



if __name__ == '__main__':
    logger.info('Loading cogs')
    for extension in initial_extensions:
        bot.load_extension(extension)
    
    logger.info('Running bot')
    bot.run(TOKEN)
