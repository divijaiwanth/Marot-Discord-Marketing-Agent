import discord
from config import DISCORD_TOKEN
from core.orchestrator import handle_message

def create_bot() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} is online and operational!")

    @bot.event
    async def on_message(msg: discord.Message):
        # Don't respond to ourselves
        if msg.author == bot.user:
            return

        user_id = str(msg.author.id)
        user_message = msg.content
        
        # We can implement a typing indicator to make it feel more "alive"
        async with msg.channel.typing():
            response_text = await handle_message(user_id, user_message)

        # Discord has a 2000 character limit per message
        for part_num in range((len(response_text) // 2000) + 1):
            start = part_num * 2000
            end = start + 2000
            chunk = response_text[start:end]
            if chunk:
                await msg.channel.send(chunk)

    return bot

def run_discord_bot():
    if not DISCORD_TOKEN:
        print("Error: DISCORD_TOKEN not found in environment variables. Check your .env file.")
        return
        
    bot = create_bot()
    bot.run(DISCORD_TOKEN)
