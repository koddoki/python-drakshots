import discord
import os
from dotenv import load_dotenv
from db import insert_shot_log, get_shot_count

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$shot'):
        partes = message.content.split(" ", 1)
        insert_shot_log(partes[1])

        shot_count = get_shot_count()

        await message.channel.send(f'Já foram {shot_count} shots!')


client.run(os.getenv('TOKEN'))
