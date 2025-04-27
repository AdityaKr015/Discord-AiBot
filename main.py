import discord
from discord.ext import commands
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-002")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

user_histories = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Process commands only if they start with '!'
    if message.content.startswith('!'):
        await bot.process_commands(message)

@bot.command(name="ask")
async def ask(ctx, *, question):
    async with ctx.typing():
        user_id = str(ctx.author.id)

        history = user_histories.get(user_id, [])

        history.append(f"User: {question}")

        if len(history) > 5:
            history = history[-5:]

        prompt = "\n".join(history)

        try:
            response = model.generate_content(prompt)
            reply = response.text

            if len(reply) > 1900:
                reply = reply[:1900] + "..."

            await ctx.send(reply)

            history.append(f"Bot: {reply}")

            user_histories[user_id] = history

        except Exception as e:
            await ctx.send("Sorry, something went wrong.")
            print(f"Error: {e}")

bot.run(DISCORD_TOKEN)
