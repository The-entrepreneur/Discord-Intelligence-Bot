import discord
from discord.ext import commands

from bot.config import (
    DISCORD_TOKEN,
    CENTRAL_GUILD_ID,
    JOINS_CHANNEL_ID,
    SYSTEM_LOGS_CHANNEL_ID
)
from bot.events import EventHandlers
from bot.logger import logger


# ---- Intents ----
intents = discord.Intents.default()
intents.guilds = True
intents.members = True


# ---- Bot Instance ----
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

handlers = EventHandlers(bot)


# ---- Events ----
@bot.event
async def on_ready():
    logger.info("Bot connected to Discord")

    # Validate central guild
    central_guild = bot.get_guild(CENTRAL_GUILD_ID)
    if not central_guild:
        logger.error(
            f"Bot is NOT in the central guild (ID: {CENTRAL_GUILD_ID})"
        )
    else:
        logger.info(
            f"Central guild detected: {central_guild.name} ({central_guild.id})"
        )

    # Validate channels
    for channel_id, name in [
        (JOINS_CHANNEL_ID, "JOINS_CHANNEL_ID"),
        (SYSTEM_LOGS_CHANNEL_ID, "SYSTEM_LOGS_CHANNEL_ID"),
    ]:
        channel = bot.get_channel(channel_id)
        if not channel:
            logger.error(f"Channel not found or inaccessible: {name} ({channel_id})")
        else:
            logger.info(f"Channel OK: #{channel.name} ({channel.id})")

    # Delegate to handler
    await handlers.on_ready()


@bot.event
async def on_guild_join(guild):
    await handlers.on_guild_join(guild)


@bot.event
async def on_member_join(member):
    await handlers.on_member_join(member)


# ---- Entrypoint ----
if __name__ == "__main__":
    logger.info("Starting Discord bot...")
    bot.run(DISCORD_TOKEN)
