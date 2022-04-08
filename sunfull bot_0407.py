import discord
import asyncio
import random
import emoji

 
client = discord.Client()
 
@client.event
async def on_ready(): 
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("회사생활"))
 
@client.event
async def on_message(message): 
    content = message.content 
    guild = message.guild 
    author = message.author 
    channel = message.channel
    category = channel.category
    channels = message.guild.text_channels
    topic = message.channel.topic

    if topic is not None and '동아리생성 실험' in topic:
        if content.startswith("!동아리-"):
            removeblank = message.content.replace(" ","")
            clubname = "🏫" + removeblank[5:] + "🏫"
            alreadyexist = False
            overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), author: discord.PermissionOverwrite(read_messages=True)}
            for ch in channels :
                if ch.name == clubname :
                    await message.channel.send('해당 학교 동아리가 존재합니다. 해당 동아리에 가입시켜드리겠습니다.', reference=message)
                    await ch.set_permissions(author, overwrite = discord.PermissionOverwrite(read_messages=True), reason=None)
                    await ch.send(f'{author.mention}님, 동아리에 가입하신 것을 환영합니다!')
                    alreadyexist = True
            if alreadyexist == False :
                clubchannel = await guild.create_text_channel(clubname, overwrites=overwrites, category = category)
                await message.add_reaction('✅')
                await clubchannel.send(f'{author.mention}님, 동아리가 생성되었습니다! 친구들을 초대해보세요😀')
                alreadyexist = True


client.run('OTU5MDA4MDM3NjAxOTY4MTY5.YkVn1Q.VGasbiMmSHlSbdymioCFnIBhUOo')
