#!/bin/bash
source .venv/bin/activate
python3 discord_bot.py &
echo $! > discord_bot.pid