import discord
from discord.ext import commands

from bot.config import DISCORD_TOKEN
from bot.events import EventHandlers
from bot.logger import logger

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

handlers = EventHandlers(bot)

@bot.event
async def on_ready():
    await handlers.on_ready()

@bot.event
async def on_guild_join(guild):
    await handlers.on_guild_join(guild)

@bot.event
async def on_member_join(member):
    await handlers.on_member_join(member)

if __name__ == "__main__":
    logger.info("Starting bot...")
    bot.run(DISCORD_TOKEN)
