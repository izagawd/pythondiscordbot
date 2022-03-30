
import discord
import time
import random



from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
prefix = "$"
client = commands.Bot(command_prefix=prefix, intents=intents)


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        #to see if the bot is functional
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(prefix+"help"))
    
    async def on_message(self, message):
        

        iza = client.get_user(216230858783326209)
        
        

        msg = str.lower(message.content)
        if (message.channel.id == 931242116473057322):
            chan = client.get_channel(922901280752554007)
            await chan.send(message.content)
        if (msg == prefix+"selfdestruct"):
            await message.channel.send("self destructing in 3..")
            time.sleep(1)
            await message.channel.send("2..")
            time.sleep(1)
            await message.channel.send("1..")
            time.sleep(1)
            await message.channel.send("BOOM!")
            #message.channel.send sends the message in the channel in which the command was inputed
        elif (msg.startswith(prefix+"iza")):

            embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            embedVar.add_field(name="Sent!", value="**Izagawd has received your message!**", inline=False)

            await message.channel.send(embed=embedVar)
            chan = client.get_channel(926128808543797379)
            await chan.send("<@!216230858783326209> " +message.content[len(prefix)+4:] + " **sent by** <@!" + str(message.author.id)+">")

            
        elif (msg == prefix+"help"):
            
            embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            embedVar.add_field(name="Voila! My commands!", value="**" + prefix +"selfdestruct** -basically self destruct, \n **" + prefix +"roll** -gives a random number \n **" + prefix + "iza** -allows you to send a message to izagawd", inline=False)

            await message.channel.send(embed=embedVar)

        elif (msg == prefix+"roll"):
            
            embedVar = discord.Embed(title="requested by "+ message.author.name, description="**roll**:game_die: **"+ str(random.randint(1,100))+"**", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            

            await message.channel.send(embed=embedVar)





        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()

client.run('MzQwMDU0NjEwOTg5NDE2NDYw.WXmqiQ.DtUyfGFMgHm8iqTct7gEFOKmksY')
