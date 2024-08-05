import os
import google.generativeai as genai
import discord

genai.configure(api_key=os.environ["GEN_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

content = " "

def response_generate(content):
    response = chat.send_message(content)
    return response.text

DISCORD_KEY = os.environ(os.environ["DIS_KEY"])

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == 1270035200100925510 and message.content.startswith("ask"):
        await message.channel.send(response_generate(message.content))
client.run(DISCORD_KEY)