import requests
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command

# Replace with your own API keys
TELEGRAM_BOT_TOKEN = "7673034498:AAFqDjXmv-Ktg4rdHHhtuiu5c875SWATBzI"
MW_API_KEY = "bc80556b-d6fc-4b34-a76c-8951f4e84364"

# Initialize Bot & Dispatcher
bot = Bot(
    token="YOUR_TELEGRAM_BOT_TOKEN",
    default=DefaultBotProperties(parse_mode="Markdown")  # Use this instead
)
dp = Dispatcher()

# Logging
logging.basicConfig(level=logging.INFO)

# Function to get word definition from Merriam-Webster API
async def get_definition(word):
    # url = f"https://dictionaryapi.com/api/v3/references/learners/json/{word}?key={MW_API_KEY}"
    url = f"https://dictionaryapi.com/api/v3/references/learners/json/{word}?key=bc80556b-d6fc-4b34-a76c-8951f4e84364"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], dict) and "shortdef" in data[0]:
                return f"📖 *Definition of {word}:*\n" + "\n".join(f"- {d}" for d in data[0]["shortdef"])
            else:
                return "❌ No definitions found. Try another word."
        else:
            return "❌ Word not found. Try again."
    else:
        return f"⚠️ API Error: {response.status_code}"

# Command handler for /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("👋 Hello! Send me any word, and I'll fetch its definition.")

# Message handler for word definitions
@dp.message()
async def word_handler(message: Message):
    word = message.text.strip()
    definition = await get_definition(word)
    await message.answer(definition)

# Main function to run the bot
async def main():
    print("🤖 Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
