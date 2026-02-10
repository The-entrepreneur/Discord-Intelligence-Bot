# Discord Intelligence Bot

## Overview

The **Discord Intelligence Bot** is a centralized, observability‑first Discord bot designed to monitor and collect structured intelligence signals across multiple Discord servers and report them into a single, controlled Discord server (the **Central Guild**).

This is **not a conversational bot**. It is infrastructure.

The bot focuses on **telemetry, logging, and lifecycle events**, providing a clean foundation for future analytics, reporting, and automation layers.

---

## Core Goals

* Join multiple Discord servers (invited or via normal join links where permitted)
* Observe key server and member lifecycle events
* Centralize all reporting into one Discord server
* Keep logs persistent, auditable, and organized
* Remain lightweight, compliant, and extensible

---

## What the Bot Currently Does

### Implemented Features

* Connects to Discord using `discord.py`
* Validates runtime configuration on startup
* Logs bot startup and health
* Logs when the bot joins new servers
* Logs when non‑bot users join servers
* Sends all intelligence data to a dedicated Central Guild

### Centralized Reporting Structure

All output is sent to a single Discord server split into two channels:

* **System Logs Channel**

  * Bot startup events
  * Server join events
  * System‑level messages

* **Joins Feed Channel**

  * Member join events
  * Server context
  * Timestamps

No direct messages are used. All data remains persistent and reviewable.

---

## Project Structure

```
bot/
├── main.py          # Bot initialization, validation, event wiring
├── config.py        # Environment‑based configuration
├── events.py        # Discord event handling & reporting
├── logger.py        # Centralized logging setup
├── utils.py         # Helper utilities (timestamps, etc.)
.env                 # Secrets & IDs (not committed)
```

---

## File Responsibilities

### `main.py`

* Initializes the Discord bot
* Configures required intents
* Validates Central Guild and channels
* Delegates all event logic to handlers
* Starts the bot process

No business logic lives here.

---

### `events.py`

* Handles Discord lifecycle events
* Formats structured intelligence messages
* Routes messages to correct reporting channels

Implemented events:

* `on_ready`
* `on_guild_join`
* `on_member_join`

---

### `config.py`

Loads configuration strictly from environment variables:

* `DISCORD_TOKEN`
* `CENTRAL_GUILD_ID`
* `JOINS_CHANNEL_ID`
* `SYSTEM_LOGS_CHANNEL_ID`

This keeps the project deployment‑safe and CI/CD friendly.

---

### `logger.py`

* Provides unified logging
* Timestamped output
* Works in local and hosted (Render) environments

---

## Environment Configuration

Create a `.env` file with the following values:

```env
DISCORD_TOKEN=your_bot_token
CENTRAL_GUILD_ID=1234567890
JOINS_CHANNEL_ID=1234567890
SYSTEM_LOGS_CHANNEL_ID=1234567890
```

Never commit `.env` to version control.

---

## Design Principles

* **Intelligence‑first**: No commands or chat logic yet
* **Centralized visibility**: One source of truth for logs
* **Fail loudly**: Misconfiguration is surfaced immediately
* **Lenient compliance**: Supports different server join methods
* **Extensible**: Designed to layer OAuth2, APIs, and analytics later

---

## What Is Intentionally Not Implemented Yet

These are planned extensions, not missing features:

* OAuth2 authorization flows
* REST / webhook API layer
* `aiohttp` server
* Database persistence
* Per‑server aggregation
* Commands or UI interactions

The current phase focuses strictly on a solid, correct foundation.

---

## Deployment

The bot is designed to deploy cleanly on platforms like **Render**.

Typical flow:

1. Push code to GitHub
2. Set environment variables in Render dashboard
3. Deploy as a background worker
4. Bot connects and begins reporting automatically

---

## Current State Summary

* Bot connects reliably
* Central Guild receives all intelligence
* System and join events are logged cleanly
* Architecture is modular and scalable
* Ready for OAuth2, APIs, and analytics layers

---

## Future Roadmap (High Level)

1. OAuth2 authorization & server discovery
2. REST / ingestion endpoints
3. Persistence and historical analysis
4. Aggregation and advanced intelligence

---

## Philosophy

This project is built as **Discord infrastructure**, not a toy bot.

The foundation prioritizes correctness, clarity, and observability — ensuring future features can be added without refactoring or architectural debt.
