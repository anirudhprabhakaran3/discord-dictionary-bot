import discord
import os
from dotenv import load_dotenv

from dictionary import definition, help, synonym, pronunciation, etymology, lexicalcategory, phrases

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$dict'):
        message_parts = message.content.split(' ')
        try:
            message_parts[1]
        except:
            await message.channel.send(help())
            return
        if message_parts[1][0] != '-':
            word = message_parts[1]
            response_text = definition(word)
        else:
            if message_parts[1] == '-syn':
                response_text = synonym(message_parts[2])
            elif message_parts[1] == '-pron':
                response_text = pronunciation(message_parts[2])
            elif message_parts[1] == '-etym':
                response_text = etymology(message_parts[2])
            elif message_parts[1] == '-lex':
                response_text = lexicalcategory(message_parts[2])
            elif message_parts[1] == '-phr':
                response_text = phrases(message_parts[2])
            else:
                response_text = help()
        await message.channel.send(response_text)

client.run(os.getenv('TOKEN'))
