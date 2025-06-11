from telethon import TelegramClient, events
import asyncio

api_id = 29866247
api_hash = 'dda8a20bae7b7a17de79aedcd2c056b1'
source_channel = 'https://t.me/+Ur52sNQaMl1cHTya'
target_bot = '@ExtraPeBot'

keywords = ['loot', 'big loot', 'brand loot', '90%']

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    text = event.raw_text.lower()
    if any(keyword in text for keyword in keywords):
        await client.send_message(target_bot, event.message)

print("Bot is running...")
client.start()
client.run_until_disconnected()
