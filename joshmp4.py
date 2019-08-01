# Work with Python 3.6
import discord
import random

TOKEN = 'NjA2NDAyOTU3MTQ3MjQyNDk3.XUKjEw.EU0-veZ6UfoKceAoL7IdSm11FlE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith("so"):
        msg = 'GUYS I GOT THIS EPIC RUST RAID YESTERDAY WE HAD AKS AND ROCKET LAUNCHERS WE GOT SO MUCH C4'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!skin"):
        msg = "my favourite rust skin would probably be that one on that gun".format(message)
        await client.send_message(message.channel, msg)

    if "lol" in message.content:
        await client.send_message(message.channel, 'YOU JUST SAID LOL YOU FUCKING NERD LMAO')

    if message.content.startswith("bruh"):
        msg = "moment".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("ok buddy"):
        msg = "retard".format(message)
        await client.send_message(message.channel, msg)

    if "minecraft" in message.content:
        await client.send_message(message.channel, "dId SoMeBoDy SaY mInEcRaFt?")
    if "walter" in message.content:
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/603884430448263189/606407526388465664/walter.jpg")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
