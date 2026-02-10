import os
from dotenv import load_dotenv

# Load .env only if it exists (safe for Render)
load_dotenv()


def get_env(name: str, cast=str, required: bool = True):
    value = os.getenv(name)

    if value is None:
        if required:
            raise RuntimeError(f"Missing required environment variable: {name}")
        return None

    try:
        return cast(value)
    except Exception:
        raise RuntimeError(f"Invalid value for environment variable: {name}")


# Discord
DISCORD_TOKEN = get_env("DISCORD_TOKEN")

# Guild / Channels
CENTRAL_GUILD_ID = get_env("CENTRAL_GUILD_ID", int)
JOINS_CHANNEL_ID = get_env("JOINS_CHANNEL_ID", int)
SYSTEM_LOGS_CHANNEL_ID = get_env("SYSTEM_LOGS_CHANNEL_ID", int)
