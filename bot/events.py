import discord
from bot.logger import logger
from bot.config import (
    JOINS_CHANNEL_ID,
    SYSTEM_LOGS_CHANNEL_ID,
    CENTRAL_GUILD_ID
)
from bot.utils import now


class EventHandlers:
    def __init__(self, bot: discord.Client):
        self.bot = bot

    # -----------------------------
    # Internal helpers
    # -----------------------------
    async def send_system_log(self, message: str):
        channel = self.bot.get_channel(SYSTEM_LOGS_CHANNEL_ID)

        if not channel:
            logger.error("SYSTEM_LOGS_CHANNEL_ID not found")
            return

        try:
            await channel.send(message)
        except Exception:
            logger.exception("Failed to send system log")

    async def send_join_log(self, message: str):
        channel = self.bot.get_channel(JOINS_CHANNEL_ID)

        if not channel:
            logger.error("JOINS_CHANNEL_ID not found")
            return

        try:
            await channel.send(message)
        except Exception:
            logger.exception("Failed to send join log")

    # -----------------------------
    # Discord events
    # -----------------------------
    async def on_ready(self):
        logger.info(f"Bot ready as {self.bot.user} (ID: {self.bot.user.id})")

        await self.send_system_log(
            f"🟢 **Bot Online**\n"
            f"User: {self.bot.user}\n"
            f"Time: {now()}"
        )

    async def on_guild_join(self, guild: discord.Guild):
        logger.info(
            f"Joined guild: {guild.name} "
            f"(ID: {guild.id}, Members: {guild.member_count})"
        )

        await self.send_system_log(
            f"📥 **Joined New Server**\n"
            f"Name: {guild.name}\n"
            f"ID: `{guild.id}`\n"
            f"Members: {guild.member_count}\n"
            f"Time: {now()}"
        )

    async def on_member_join(self, member: discord.Member):
        # Ignore bot accounts
        if member.bot:
            return

        # Ignore joins in central ops server
        if member.guild.id == CENTRAL_GUILD_ID:
            return

        logger.info(
            f"Member joined | "
            f"Server: {member.guild.name} ({member.guild.id}) | "
            f"User: {member} ({member.id})"
        )

        await self.send_join_log(
            f"👤 **Member Joined**\n"
            f"Server: {member.guild.name}\n"
            f"Server ID: `{member.guild.id}`\n"
            f"User: {member.name}#{member.discriminator}\n"
            f"User ID: `{member.id}`\n"
            f"Time: {now()}"
        )
