
import discord
import time
import random
import os
import datetime
import random
import asyncio
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
def timetillnextday(dt=None):
    # type: (datetime.datetime) -> datetime.timedelta
    """
    Get timedelta until end of day on the datetime passed, or current time.
    """
    if dt is None:
        dt = datetime.datetime.now()
    tomorrow = dt + datetime.timedelta(days=1)
    return ((str(datetime.datetime.combine(tomorrow, datetime.time.min) - dt)[::-1])[7:])[::-1]
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        #to see if the bot is functional
        await client.change_presence(status=discord.Status.online, activity=discord.Game(prefix+"help"))
    

    async def on_message(self, message):
        now = datetime.datetime.now()
        iza = client.get_user(216230858783326209)
        
        

        msg = str.lower(message.content)
        if(message.author.id == 340054610989416460):
            return
        if(message.guild.id == 922901280245026876):
            
            if((msg.startswith(prefix+"giverep") or msg.startswith(prefix+"profile")) and msg.startswith(prefix)):
                if(len(msg)>20):
                    try:
                        m = int(msg[len(prefix)+11:30])
                    except:
                        try:
                            m = int(msg[len(prefix)+10:29])
                        except:
                            
                            embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                            embedVar.set_thumbnail(url=message.author.avatar_url)
                            embedVar.add_field(name="**try putting space once between the command and the user or contact the bot creator**", value="`eg $profile @iza`", inline=False)
                            await message.channel.send(embed=embedVar)
                            return
                
                try:
                    m = int(msg[len(prefix)+11:30])
                    
                    w = open(msg[len(prefix)+11:30]+".txt", "a")
                    
                except:
                    
                    
                    w = open(msg[len(prefix)+10:29]+".txt", "a")
                
                w.close()
                try:
                    m = int(msg[len(prefix)+11:30])
                    
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
                print(data[2])
                bake =str(int(data[2]) +(cake-int(data[11])))

                
                data[2] = bake+"\n"
                data[11] = str(int(now.strftime('%d')))+"\n"
                
                    

    
                    
                try:
                    m = int(msg[len(prefix)+11:30])
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
                bake =str(int(data[2]) +(cake-int(data[11])))
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
                embedVar.add_field(name="Next reputation point to give in", value="`"+timetillnextday()+"`", inline=False)
                

                await message.channel.send(embed=embedVar)
            elif(msg.startswith(prefix+"profile")):
                try:
                    print(int(msg[len(prefix)+11:30]))
                    
                    r =  open(str(msg[len(prefix)+11:30])+".txt", "r")
                    m = int(msg[len(prefix)+11:30])
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
                embedVar.add_field(name="Next reputation point to give in", value="`"+timetillnextday()+"`", inline=False)
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
                        print(int(msg[len(prefix)+11:30]))
                        
                        r = open(msg[len(prefix)+11:30]+".txt", "r")
                        a =str(msg[len(prefix)+11:30])

                    except:
                        r = open(msg[len(prefix)+10:29]+".txt", "r")
                        a = str(msg[len(prefix)+10:29])
                        print(a+"here")
                        
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
                        print(pata[2])
                        print(data[0])
                        try:
                            m =int(pata[2])
                            m =int(data[0])
                        except:
                            print("something went wrong")
                            return
                        
                        data[0] = str(int(data[0])+1)+"\n"
                        pata[2] =  str(int(pata[2])-1)+"\n"
                        embedVar = discord.Embed(title="giverep requested by "+ message.author.name, description="", color=0x00ff00)
                        embedVar.set_thumbnail(url=message.author.avatar_url)
                        embedVar.add_field(name="**reputation point given successfully!**", value="`that's nice of you! They now have "+ data[0]+ "reps!`", inline=False)
                    
                        await message.channel.send(embed=embedVar)
                    else:
                        embedVar = discord.Embed(title="giverep requested by "+ message.author.name, description="", color=0x00ff00)
                        embedVar.set_thumbnail(url=message.author.avatar_url)
                        embedVar.add_field(name="**You don't have enough points to give reputation. it increases everyday**", value="`just wait for a day :)`", inline=False)
                    
                        await message.channel.send(embed=embedVar)
                    
                    

                    
                    try:
                        print(int(msg[len(prefix)+11:30]))
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
            elif(msg == prefix+"promote"):
                r = open(str(message.author.id)+".txt", "r")
                data = r.readlines()
                r.close()
                if(int(data[0])>=100):
                    await message.author.add_roles(discord.utils.get(message.guild.roles, name="Acknowledged human"))
                    embedVar = discord.Embed(title="promotion requested by "+ message.author.name, description="", color=0x00ff00)
                    embedVar.set_thumbnail(url=message.author.avatar_url)
                    embedVar.add_field(name="**congrats!**", value="**You are now an acknowledged human!**", inline=False)
                    await message.channel.send(embed=embedVar)
                elif(discord.utils.get(message.guild.roles, name="Acknowledged human")in message.author.roles):
                    embedVar = discord.Embed(title="promotion requested by "+ message.author.name, description="", color=0x00ff00)
                    embedVar.set_thumbnail(url=message.author.avatar_url)
                    embedVar.add_field(name=":joy:", value="**You are already an acknowledged human!**", inline=False)
                    await message.channel.send(embed=embedVar)
                    
                
                else:
                    embedVar = discord.Embed(title="promotion requested by "+ message.author.name, description="", color=0x00ff00)
                    embedVar.set_thumbnail(url=message.author.avatar_url)
                    embedVar.add_field(name="**hmm**", value="**You are " +str(100-int(data[0]))+" points away from being an acknowledged human!**", inline=False)
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
        elif (msg.startswith(prefix+"rps")):
            args = msg[len(prefix)+4:]
            m = ["rock", "paper", "scissors"]
            m = random.choice(m)
            
            if(m==args):
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**I chose "+ args+"**!", value="I guess it's a tie :person_shrugging:", inline=False)

                await message.channel.send(embed=embedVar)
            elif(m == "rock" and args == "scissors"):
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**I chose "+ m +"**!", value="I smashed your **scissors** to pieces with my **rock** >:)", inline=False)

                await message.channel.send(embed=embedVar)
            elif(m=="rock" and args == "paper"):
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**I chose "+ m +"**!", value="You covered my **rock** with your **paper** and trapped it? interesting >:)", inline=False)

                await message.channel.send(embed=embedVar)
            elif(m=="scissors" and args == "paper"):
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**I chose "+ m +"**!", value="I cut your **paper** into tiny pieces with my **scissors** >:)", inline=False)

                await message.channel.send(embed=embedVar)
            elif(m=="scissors" and args == "rock"):
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**I chose "+ m +"**!", value="you smashed my **scissors** with your **rock**? Didn't expect u to choose that!", inline=False)

                await message.channel.send(embed=embedVar)
            elif(m=="paper" and args == "rock"):
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**I chose "+ m +"**!", value="I covered your **rock** with my **paper** now it's useless!", inline=False)

                await message.channel.send(embed=embedVar)
            elif(m=="paper" and args == "scissors"):
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**I chose "+ m +"**!", value="How dare you cut my **paper** into tiny pieces with your **scissors**! >:(", inline=False)

                await message.channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.add_field(name="**Hmm**!", value="I only understand **rock**, **paper**, and **scissors**. Eg $rps paper", inline=False)

                await message.channel.send(embed=embedVar)
                
                
                
 
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
            embedVar.add_field(name="**Fun**", value="`selfdestruct` `roll` `fight` `rps(rock paper scissors)`", inline=False)
            embedVar.add_field(name="**Profile interactions**", value="`profile` `promote` `giverep` `setbio` `setregion` `setmain` `setweapon` `setplatform` `setuid` `setelement` `setadventurerank` `setserver`", inline = False)
            await message.channel.send(embed=embedVar)

        elif (msg == prefix+"roll"):
            
            embedVar = discord.Embed(title="roll requested by "+ message.author.name, description="**roll**:game_die: **"+ str(random.randint(1,100))+"**", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            

            await message.channel.send(embed=embedVar)
        elif(msg.startswith(prefix+"fight")):
            try:
                m = int(msg[len(prefix)+9:28])
            except:
                try:
                    m = int(msg[len(prefix)+8:27])
                except:
                    embedVar = discord.Embed(title="requested by "+ message.author.name, description="", color=0x00ff00)
                    embedVar.set_thumbnail(url=message.author.avatar_url)
                    embedVar.add_field(name="Hmm", value="**make sure you leave a space between the command and the mention e.g $fight @iza**", inline=False)

                    await message.channel.send(embed=embedVar)
                    
            hp1 =100
            hp2 = 100
            opponent = await client.fetch_user(m)
            you = message.author
            if(opponent == you):
                embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                embedVar.add_field(name=f"OUCH!", value=f"**You killed yourself :joy:**", inline=False)
           
                await message.channel.send(embed=embedVar)
                return
                
            embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
            embedVar.add_field(name=f"attack or heal? {opponent.name}'s turn", value=f"**{you.name}'s health: `{hp1}` \n{opponent.name}'s health: `{hp2}` **", inline=False)
           
            await message.channel.send(embed=embedVar)
            try:
                m = await client.wait_for('message', check=lambda message: message.author.id == opponent.id and (message.content == "attack" or message.content == "heal" or message.content == "Attack" or message.content == "Heal"), timeout = 60)
                m = str.lower(m.content)
            except asyncio.TimeoutError:
                embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                embedVar.add_field(name=f"hmm", value=f"**Battle terminated. opponent took too long**", inline=False)
           
                await message.channel.send(embed=embedVar)
                return;
            while(True):


                if(m == "attack"):
                    cake = random.randint(5,30)
                    hp1 = hp1 - cake

                    if(not hp1<=0):
                        embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                        embedVar.add_field(name=f"OUCH!", value=f"**{opponent.name} dealt `{cake}` damage!!!**", inline=False)
                        embedVar.add_field(name=f"attack or heal? {you.name}'s turn", value=f"**{you.name}'s health: `{hp1}` \n{opponent.name}'s health: `{hp2}` **", inline=False)
                        await message.channel.send(embed=embedVar)
                    else:
                        embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                        embedVar.add_field(name=f"OUCH!", value=f"**{opponent.name} dealt `{cake}` damage!!!**", inline=False)
                        embedVar.add_field(name=f"{opponent.name} won the battle!", value=f"**{you.name}'s health: `{hp1}` \n{opponent.name}'s health: `{hp2}` **", inline=False)
                        await message.channel.send(embed=embedVar)
                        return
                    
                    
           
                    
                elif(m=="heal"):
                    
                    cake = random.randint(5,20)
                    hp2 = hp2 + cake
                    if(hp2>100):
                        hp2 = 100
                    embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                    embedVar.add_field(name=f"Interesting!", value=f"**{opponent.name} healed `{cake}` health!**", inline=False)
                    embedVar.add_field(name=f"attack or heal? {you.name}'s turn", value=f"**{you.name}'s health `{hp1}` \n{opponent.name}'s health: `{hp2}` **", inline=False)
                    await message.channel.send(embed=embedVar)
                try:
                    m = await client.wait_for('message', check=lambda message: message.author.id == you.id and (message.content == "attack" or message.content == "heal" or message.content == "Attack" or message.content == "Heal"), timeout = 60)
                    m = str.lower(m.content)
                except asyncio.TimeoutError:
                    embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                    embedVar.add_field(name=f"hmm", value=f"**Battle terminated. opponent took too long**", inline=False)
           
                    await message.channel.send(embed=embedVar)
                    return
                if(m == "attack"):
                    cake = random.randint(5,30)
                    hp2 = hp2 - cake
                    if(not hp2<=0):
                        embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                        embedVar.add_field(name=f"OUCH!", value=f"**{you.name} dealt `{cake}` damage!!!**", inline=False)
                        embedVar.add_field(name=f"attack or heal? {opponent.name}'s turn", value=f"**{you.name}'s health: `{hp1}` \n{opponent.name}'s health: `{hp2}` **", inline=False)
                        await message.channel.send(embed=embedVar)
                    else:
                        embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                        embedVar.add_field(name=f"OUCH!", value=f"**{you.name} dealt `{cake}` damage!!!**", inline=False)
                        embedVar.add_field(name=f"{you.name} won the battle!", value=f"**{you.name}'s health: `{hp1}` \n{opponent.name}'s health: `{hp2}` **", inline=False)
                        await message.channel.send(embed=embedVar)
                        return
                    
           
                    
                elif(m=="heal"):
                    cake = random.randint(5,20)
                    hp1 = hp1 + cake
                    if (hp1> 100):
                        hp1 = 100
                    embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                    embedVar.add_field(name=f"Interesting!", value=f"**{you.name} healed `{cake}` health!**", inline=False)
                    embedVar.add_field(name=f"attack or heal? {opponent.name}'s turn", value=f"**{you.name}'s health `{hp1}` \n{opponent.name}'s health: `{hp2}` **", inline=False)
                    await message.channel.send(embed=embedVar)
                try:
                    m = await client.wait_for('message', check=lambda message: message.author.id == opponent.id and (message.content == "attack" or message.content == "heal" or message.content == "Attack" or message.content == "Heal"), timeout = 60)
                    m = str.lower(m.content)
                except asyncio.TimeoutError:
                    embedVar = discord.Embed(title="BATTLE!!!", description="", color=0x00ff00)
            
                    embedVar.add_field(name=f"hmm", value=f"**Battle terminated. opponent took too long**", inline=False)
           
                    await message.channel.send(embed=embedVar)
                    return
                
                
                
                    
                    
                    
                
                    
            

                
                    
                
            
                
                
            
        





        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()

client.run("Your bot's token")
