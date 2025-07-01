import asyncio
from telethon import TelegramClient, events

# Get your API ID and HASH from https://my.telegram.org
api_id = 123456      # Replace with your API ID
api_hash = 'your_api_hash'  # Replace with your API hash

# You can name the session file anything
client = TelegramClient('anon', api_id, api_hash)

spamming = False  # Global flag to track spamming

@client.on(events.NewMessage(pattern='/start'))
async def start_spam(event):
    global spamming
    spamming = True
    await event.respond("Started spamming 'yo' every 2 seconds!")

    while spamming:
        await client.send_message(event.chat_id, "yo")
        await asyncio.sleep(2)

@client.on(events.NewMessage(pattern='/stop'))
async def stop_spam(event):
    global spamming
    spamming = False
    await event.respond("Stopped spamming.")

async def main():
    print("Bot is running...")
    await client.run_until_disconnected()

client.start()
client.loop.run_until_complete(main())

