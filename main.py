import discord
from discord.ext import commands
import random
import asyncio
import time
import nacl
from ffmpeg import *
from text_def import *

client = commands.Bot(command_prefix = '!jx ')

@client.event
async def on_member_join(member):
    channel = client.get_channel(1035525122418806818)
    await channel.send(f'`鞠躬 Welcome to China :{member.mention} ! 鞠躬`')
    await channel.send(f'`鞠躬  Its a land of freedom and control!  鞠躬`')
    await channel.send(f'`鞠躬       Try to enjoy your stay !       鞠躬`')

@client.command()
async def play(ctx):
    user = ctx.message.author
    voice_channel = user.voice.channel
    if voice_channel:
        await ctx.send('`向球鞠躬，約翰西娜`')
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(random.choice(sounds_get())), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
        await vc.disconnect()
    else:
        await ctx.send('`User is not in a voice channel.`')



@client.event
async def on_ready():
    print('John Xina is watching you!')
    print('一一一一一一一一一一一一一一一一一')

@client.command()
async def china_bad(ctx):
    await ctx.send('和日城贊 Aww, hell no 灣少飌乂')
    await ctx.send('ㅤ')
    await ctx.send('ㅤ')
    png_str = ["pictures/m30points.jpg","pictures/m69420points.jpg","pictures/mduzo.jpg"]
    with open(random.choice(png_str), "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@client.command()
async def china_good(ctx):
    await ctx.send('崇牢儗㞖 China Nr.#1 這兞和及')
    await ctx.send('ㅤ')
    await ctx.send('ㅤ')
    tab_str = ["pictures/p15points.jpg","pictures/p2770000points.jpg"]
    with open(random.choice(tab_str), "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@client.command()
async def tell_me(ctx):
    first_part = random.choice(first_get())
    second_part = random.choice(second_get())
    header = ''
    for i in range(((len(first_part) + len(second_part) + 6) // 4)-7):
        header += 'ㅤ'
    await ctx.send(header + '告訴我狗 Fact: 屎厄運渉')
    await ctx.send('ㅤ')
    await ctx.send('ㅤ')
    await ctx.send('𨧀 ' + first_part + ' ' + second_part + ' ! 州')

@client.command()
async def wok(ctx):
    await ctx.send('崇牢儗㞖 Wok: 這兞和及')
    await ctx.send('ㅤ')
    await ctx.send('ㅤ')
    with open('gif/wok-the-wock.gif', "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

client.run('MTA2ODI2OTA0MDc2MzY3NDYyNA.GYcZw5.CVq99EUtrjkQP_-rFyk3dHJSH0X15jxlBLRqLA')
