
import discord
import time
import random
import os
import datetime

#importing...
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
prefix = "$"
client = commands.Bot(command_prefix=prefix, intents=intents)

reputation = 0
bio = 1
money = 2
AR = 3
main = 4
element = 5
weapon = 6
region = 7
platform = 8
genshinstatus = 9
server = 10
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        #to see if the bot is functional
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(prefix+"help"))
    

    async def on_message(self, message):
        now = datetime.datetime.now()
        
        
        

        iza = client.get_user(216230858783326209)
        
        

        msg = str.lower(message.content)
        if(message.guild.id == 922901280245026876):
            if("$" in msg):
                
                try:
                    w = open(msg[len(prefix)+11:30]+".txt", "a")
                except:
                    w = open(msg[len(prefix)+10:29]+".txt", "a")
                
                w.close()
                try:
                    r =  open(msg[len(prefix)+11:30]+".txt", "r")
                except:
                    r =  open(msg[len(prefix)+10:29]+".txt", "r")
                data = r.readlines()
                
                r.close()
                
                if(len(data) < 1):
                    data.append("0\n")

                
                while(len(data)< 12):
                    if(len(data)==2):
                        data.append("5\n")
                    elif(len(data)==11):
                        data.append(str(int(now.strftime('%d')))+"\n")
                        
                    else:
                        data.append("Unknown\n")
                cake =int(now.strftime('%d'))
                bake =str(int(data[2][0:2]) +(cake-int(data[11][0:2])))
                data[2] = bake+"\n"
                data[11] = str(int(now.strftime('%d')))+"\n"
                
                    

    
                    
                try:
                    w = open(msg[len(prefix)+11:30]+".txt", "w+")
                except:
                    w = open(msg[len(prefix)+10:29]+".txt", "w+")
                    
                
                w.writelines(data)
                w.close()
                
            
            if(msg.startswith(prefix)):
                
                
                w = open(str(message.author.id)+".txt", "a")
                
                w.close()
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                
                r.close()
                
                if(len(data) < 1):
                    data.append("0\n")

                
                while(len(data)< 12):
                    if(len(data)==2):
                        data.append("5\n")
                    elif(len(data)==11):
                        data.append(str(int(now.strftime('%d')))+"\n")
                        
                    else:
                        data.append("Unknown\n")
                cake =int(now.strftime('%d'))
                bake =str(int(data[2][0:2]) +(cake-int(data[11][0:2])))
                data[2] = bake+"\n"
                data[11] = str(int(now.strftime('%d')))+"\n"
                
                    

    
                    
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                
            
    
            if(msg == prefix+"profile" and len(msg)<10):
                
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Reputation", value="`"+data[0]+"`", inline=False)
                embedVar.add_field(name="Reputation to give", value="`"+data[2]+"`", inline=False)
                embedVar.add_field(name="Bio", value="`"+data[1]+"`", inline=False)
                
                embedVar.add_field(name="Adventure rank", value="`"+data[3]+"`", inline=False)
                
                embedVar.add_field(name="Main", value="`"+data[4]+"`", inline=False)
                embedVar.add_field(name="Favorite Element", value="`"+data[5]+"`", inline=False)
                embedVar.add_field(name="Favorite Weapon", value="`"+data[6]+"`", inline=False)
                embedVar.add_field(name="Favorite Region", value="`"+data[7]+"`", inline=False)
                embedVar.add_field(name="Platform(s)", value="`"+data[8]+"`", inline=False)
                embedVar.add_field(name="Genshin UID", value="`"+data[9]+"`", inline=False)
                embedVar.add_field(name="Genshin Server(s)", value="`"+data[10]+"`", inline=False)
                

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"profile")):
                try:
                    
                    r =  open(str(msg[len(prefix)+11:30])+".txt", "r")
                except:
                    r =  open(str(msg[len(prefix)+10:29])+".txt", "r")
                data = r.readlines()
                r.close()
                didu=0
                try:

                    uzr = await client.fetch_user(int(msg[len(prefix)+11:30]))
                    didu=1
                except:
                    uzr = await client.fetch_user(int(msg[len(prefix)+10:29]))
                    didu = 2
                if(didu==0):
                    embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                    embedVar.set_thumbnail(url=message.author.avatar_url)
                    embedVar.add_field(name="**try putting space once between the command and the user or contact the bot creator**", value="`eg $profile @iza`", inline=False)
                    await message.channel.send(embed=embedVar)
                    
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=uzr.avatar_url)
                
                embedVar.add_field(name="Reputation", value="`"+data[0]+"`", inline=False)
                embedVar.add_field(name="Reputation to give", value="`"+data[2]+"`", inline=False)
                embedVar.add_field(name="Bio", value="`"+data[1]+"`", inline=False)
                
                embedVar.add_field(name="Adventure rank", value="`"+data[3]+"`", inline=False)
                
                embedVar.add_field(name="Main", value="`"+data[4]+"`", inline=False)
                embedVar.add_field(name="Favorite Element", value="`"+data[5]+"`", inline=False)
                embedVar.add_field(name="Favorite Weapon", value="`"+data[6]+"`", inline=False)
                embedVar.add_field(name="Favorite Region", value="`"+data[7]+"`", inline=False)
                embedVar.add_field(name="Platform(s)", value="`"+data[8]+"`", inline=False)
                embedVar.add_field(name="Genshin UID", value="`"+data[9]+"`", inline=False)
                embedVar.add_field(name="Genshin Server(s)", value="`"+data[10]+"`", inline=False)
                await message.channel.send(embed=embedVar)
                

                
            elif(msg.startswith(prefix+"setbio")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[1] =msg[(len(prefix)+7):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setadventurerank")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[3] =msg[(len(prefix)+17):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setmain")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[4] =msg[(len(prefix)+8):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setelement")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[5] =msg[(len(prefix)+11):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setweapon")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[6] =msg[(len(prefix)+10):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setregion")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[7] =msg[(len(prefix)+10):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setuid")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[9] =msg[(len(prefix)+7):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setserver")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[10] =msg[(len(prefix)+10):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"setplatform")):
                r =  open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                
                data[8] =msg[(len(prefix)+12):]+"\n"
                print(data)
                w = open(str(message.author.id)+".txt", "w+")
                
                w.writelines(data)
                w.close()
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="Set!", value="**it has been set!**", inline=False)

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"giverep")):
                if(len(msg)>=30 ):
                    
                   
                    try:
                        print(str(msg[len(prefix)+11:30]))
                        
                        r = open(msg[len(prefix)+11:30]+".txt", "r")
                        a =str(msg[len(prefix)+11:30])

                    except:
                        r = open(msg[len(prefix)+10:29]+".txt", "r")
                        a = str(msg[len(prefix)+10:29])
                        
                    data = r.readlines()
                    r.close()
                    
                        
                    k = open(str(message.author.id)+".txt", "r")
                    pata = k.readlines()
                    k.close()
                    if(a==str(message.author.id)):
                        
                                                                    
                        embedVar = discord.Embed(title="giverep requested by "+ message.author.name, description="", color=0x00ff00)
                        embedVar.set_thumbnail(url=message.author.avatar_url)
                        embedVar.add_field(name="**you can't give reputation points to yourself >:(**", value="`you just can't ;)`", inline=False)
                    
                        await message.channel.send(embed=embedVar)     
                
                    elif(int(pata[2])>0):
                        data[0] = str(int(data[0])+1)+"\n"
                        pata[2] =  str(int(pata[2])-1)+"\n"
                        embedVar = discord.Embed(title="giverep requested by "+ message.author.name, description="", color=0x00ff00)
                        embedVar.set_thumbnail(url=message.author.avatar_url)
                        embedVar.add_field(name="**reputation point given successfully!**", value="`that's nice of you!`", inline=False)
                    
                        await message.channel.send(embed=embedVar)
                    else:
                        embedVar = discord.Embed(title="giverep requested by "+ message.author.name, description="", color=0x00ff00)
                        embedVar.set_thumbnail(url=message.author.avatar_url)
                        embedVar.add_field(name="**You don't have enough points to give reputation. it increases everyday**", value="`just wait for a day :)`", inline=False)
                    
                        await message.channel.send(embed=embedVar)
                    
                    

                    
                    try:
                        f = open(msg[len(prefix)+11:30]+".txt", "w+")
                    except:
                        f = open(msg[len(prefix)+10:29]+".txt", "w+")
                    f.writelines(data)
                    f.close()
                    f = open(str(message.author.id)+".txt", "w+")
                    f.writelines(pata)
                    f.close()
                else:
                    embedVar = discord.Embed(title="giverep requested by "+ message.author.name, description="", color=0x00ff00)
                    embedVar.set_thumbnail(url=message.author.avatar_url)
                    embedVar.add_field(name="**You have to tag the person you want to give rep to with one space after the command**", value="`eg $giverep @iza`", inline=False)
                    
                    await message.channel.send(embed=embedVar)
                    
                
                
                
                
                
                
                
                
                
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
            
            embedVar = discord.Embed(title=" Commands requested by "+ message.author.name, description="", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            embedVar.add_field(name="**Fun**", value="`selfdestruct` `roll`", inline=False)
            embedVar.add_field(name="**Profile interactions**", value="`profile` `giverep` `setbio` `setregion` `setmain` `setweapon` `setplatform` `setuid` `setelement` `setadventurerank` `setserver`", inline = False)
            await message.channel.send(embed=embedVar)

        elif (msg == prefix+"roll"):
            
            embedVar = discord.Embed(title="roll requested by "+ message.author.name, description="**roll**:game_die: **"+ str(random.randint(1,100))+"**", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            

            await message.channel.send(embed=embedVar)
        





        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()

client.run('MzQwMDU0NjEwOTg5NDE2NDYw.WXmqiQ.ykVNnAFI9x7bAZ22FMF7V_FNGMo')
