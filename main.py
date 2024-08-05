import os
import google.generativeai as genai
import discord

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

content = " "

def response_generate():
    content = input("your turn: ")
    response = chat.send_message(content)
    print(response.text)

DISCORD_KEY = os.environ["DISCORD_BOT_API_KEY"]

client = discord.Client()
@client.event
async def on_message(message):
        await message.channel.send(response_generate())
client.run(DISCORD_KEY)