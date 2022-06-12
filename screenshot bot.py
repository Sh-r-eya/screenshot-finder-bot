import discord
from discord.ext import commands
import sqlite3

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):

    db= sqlite3.connect('main.sqlite')
    cursor=db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS
    content text,
    link text
    ''')
    if message.author==bot.user:
        return
    
    elif message.attachments !=[]: #to check if the message has an image attachment
   
        name = message.content

        url= 'https://discord.com/channels/'+str(message.guild.id)+'/'+str(message.channel.id)+'/'+str(message.id)

        
        if name=='':
            await message.channel.send('unnamed, save failed!')
            return
            try:
                sql='insert into main values ('+'"'+str(name)+'"'+','+'"'+str(url)+'"'+');'
                
                cursor.execute(sql)
                await message.channel.send('save completed!')
            except:
                await message.channel.send('error! save failed!')

    elif message.content.find('botsearch ') == 0:
        if len(message.content)>10:
            nm=str(message.content)[10::]
        
        sql = "SELECT * FROM main WHERE content = "+nm
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            await message.channel.send(x)

bot.run('ADD YOUR TOKEN HERE')