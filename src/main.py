import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+yum'):
        await message.channel.send('https://ibb.co/J3hVwdV')

    if message.content.startswith('+drunky'):
        await message.channel.send('https://dogemuchwow.com/wp-content/uploads/2019/03/orang-man-attak.jpg')

    if message.content.startswith('+voices'):
        await message.channel.send('https://c.tenor.com/qf36AOwq4eEAAAAd/cat-cursed.gif')

client.run('OTE4NTcyOTE4NzkzOTg2MDcx.YbJNsg.VAv0mGFhLSRG-UufjBmRIFSr7') ADD "b8" TO THE END IF YOU WILL USE THIS CODE YOURSELF
