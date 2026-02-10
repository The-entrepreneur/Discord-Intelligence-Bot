import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CENTRAL_GUILD_ID = int(os.getenv("CENTRAL_GUILD_ID", 0)) if os.getenv("CENTRAL_GUILD_ID") else None
JOINS_CHANNEL_ID = int(os.getenv("JOINS_CHANNEL_ID", 0)) if os.getenv("JOINS_CHANNEL_ID") else None
SYSTEM_LOGS_CHANNEL_ID = int(os.getenv("SYSTEM_LOGS_CHANNEL_ID", 0)) if os.getenv("SYSTEM_LOGS_CHANNEL_ID") else None
