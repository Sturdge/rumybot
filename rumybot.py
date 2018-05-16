import discord
from discord.ext.commands import Bot
from discord import Game
import random
import csv

prefix = "!"
client = Bot(command_prefix=prefix)

quotes = []
dates = []

async def readlist():
    with open('quotes.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            getquote = row[0]
            getdate = row[1]
            quotes.append(getquote)
            dates.append(getdate)

@client.command(name='quote', description='Retrieves a random Rumy quote.', aliases=['Quote'], pass_context=True)
async def quote(context):
    picked = random.randrange(0, len(quotes))
    msg = f"{quotes[picked]} - {dates[picked]}"
    await client.send_message(context.message.channel, msg)

@client.command(name='rumym8', description='Tells you who Rumy is', aliases=['Rumym8', 'rumy', 'Rumy'])
async def rumy():
    await client.say('Acts About 12, Garunteed To Piss You Off')

@client.event
async def on_message(message):
    if message.author != client.user:
        if 'rumy' in message.content.lower() and not message.content.startswith('!'):
            msg = "Don't BULLY me!!!!!!!"
            await client.send_message(message.channel, msg)
    await client.process_commands(message)


@client.event
async def on_ready():
    await readlist()
    await client.change_presence(game=Game(name="with himself"))
    print("Awaiting commands...")

client.run("NDQ0NjM4MzA3NDYxMjM0Njg5.Dd4gzg.GbSG3xybY673klpW_oaIXIr-usI")