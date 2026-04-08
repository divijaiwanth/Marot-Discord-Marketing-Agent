import os
from dotenv import load_dotenv

# We need to load environment variables first before importing modules that might depend on them.
load_dotenv()

from interfaces.discord_bot import run_discord_bot

if __name__ == "__main__":
    print("Initializing DXJ Marketing Agent...")
    run_discord_bot()
