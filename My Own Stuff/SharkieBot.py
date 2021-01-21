import discord
import time
import random
from colorama import init, Fore, Back, Style

from discord.ext import commands

client = discord.Client()
TOKEN = 'REDACTED'
BOT_PREFIX = "_"
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print('Ready.')

#error proofing
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
       await ctx.send("Command not found. Use `_sharkhelp` for assistance")
    elif isinstance(error, commands.MissingAnyRole):
       await ctx.send("You do not have the permission to use this command.")

#Delete Messages
@commands.has_any_role("Owner", "Co-Owner", "Administrator", "admin", "bitchboy")
@bot.command()
async def clear(ctx, amount = 6):
    def check(m):
         return m.author == ctx.author and m.channel == ctx.channel
    cmnd_channel = bot.get_channel(ctx.channel.id)
    await cmnd_channel.purge(limit=amount)
    await cmnd_channel.send("Five messages cleared. Deleting this message in 5 seconds")
    time.sleep(5)
    await cmnd_channel.purge(limit=1)

#help menu
@commands.has_any_role("Owner", "Co-Owner", "Administrator", "admin", "bitchboy")
@bot.command()
async def sharkhelp(ctx):
    cmnd_channel = bot.get_channel(ctx.channel.id)
    help = discord.Embed(
        colour=discord.Colour.blue(),
        timestamp=ctx.message.created_at,
        title="Hello!!!",
        description="Hello there, currently the bot has a few commands you can use.\n\n`_newembed` - creates a custom embed which you can customize through chat. \n`_clear` - deletes the last 5 messages in a channel.\n`_sharksay` - makes the bot say a message in a channel."
    )

    # Author and Icon
    help.set_author(name="SharkBot", icon_url="https://image.myanimelist.net/ui/5LYzTBVoS196gvYvw3zjwHLO3GSBAcZcRtzfQVeb_MA")
    help.set_image(url="https://qph.fs.quoracdn.net/main-qimg-146b772c3c629a7a07d6d39dafd8ce57.webp")
    await cmnd_channel.send(embed=help)

# Embed
@commands.has_any_role("Owner", "Co-Owner", "Administrator", "admin", "bitchboy")
@bot.command()
async def newembed(ctx):
    cmnd_channel = bot.get_channel(ctx.channel.id)
    def check(m):
         return m.author == ctx.author and m.channel == ctx.channel



    #Colors
    await cmnd_channel.send("What would you like the color to be? Your options are the following;\nRed, Blue, Green, Purple, Orange, Teal, Gold." )
    embed_color = await bot.wait_for('message', check=check, timeout=400)
    embed_color = embed_color.content.lower()
    while (embed_color != "red" and embed_color != "blue" and embed_color != "green" and embed_color != "purple" and embed_color != "orange" and embed_color != "teal" and embed_color != "gold"):
           await cmnd_channel.send("Color unavailable, please chose one of are the following;\nRed, Blue, Green, Purple, Orange, Teal, Gold.")
           embed_color = await bot.wait_for('message', check=check, timeout=400)
    if (embed_color == "red"):
        embed_color = discord.Colour.red()
    elif (embed_color == "blue"):
        embed_color = discord.Colour.blue()
    elif (embed_color == "green"):
        embed_color = discord.Colour.green()
    elif (embed_color == "purple"):
        embed_color = discord.Colour.purple()
    elif (embed_color == "orange"):
        embed_color = discord.Colour.orange()
    elif (embed_color == "teal"):
        embed_color = discord.Colour.teal()
    elif (embed_color == "gold"):
        embed_color = discord.Colour.gold()

    #title
    await cmnd_channel.send("What would you like the title to be?")
    embed_title = await bot.wait_for('message', check=check, timeout=400)

    #description
    await cmnd_channel.send("What would you like the description to be?")
    embed_description = await bot.wait_for('message', check=check, timeout=400)

    #author
    await cmnd_channel.send("Who would you like to be the author?")
    embed_author = await bot.wait_for('message', check=check, timeout=400)

    #Icon
    await cmnd_channel.send("Would you like the default icon? (Y/N)")
    embed_iconchoice = await bot.wait_for('message', check=check, timeout=400)
    embed_iconchoice = embed_iconchoice.content.upper()
    while (embed_iconchoice != "N" and embed_iconchoice != "Y"):
           await cmnd_channel.send("Invalid answer. Would you like the default icon?(Y/N)")
           embed_iconchoice = await bot.wait_for('message', check=check, timeout=400)
           embed_iconchoice = embed_iconchoice.content.upper()

    if (embed_iconchoice == "Y"):
        embed_icon = "https://cdn.discordapp.com/emojis/593028185759809536.png?v=1"
        d_icon = "true"

    elif (embed_iconchoice == "N"):
          await cmnd_channel.send("What would you like the icon to be? (URL)")
          embed_icon = await bot.wait_for('message', check=check, timeout=400)
          d_icon = "false"

    #thumbnail
    await cmnd_channel.send("Would you like the default thumbnail? (Y/N)")
    embed_thumbnailchoice = await bot.wait_for('message', check=check, timeout=400)
    embed_thumbnailchoice = embed_thumbnailchoice.content.upper()
    while (embed_thumbnailchoice != "N" and embed_thumbnailchoice != "Y"):
           await cmnd_channel.send("Invalid answer. Would you like the default thumbnail?(Y/N)")
           embed_thumbnailchoice = await bot.wait_for('message', check=check, timeout=400)
           embed_thumbnailchoice = embed_thumbnailchoice.content.upper()

    if (embed_thumbnailchoice == "Y"):
        embed_thumbnail = "https://i.imgur.com/xJyIgAQ.png"
        d_thumbnail = "true"

    elif (embed_thumbnailchoice == "N"):
          await cmnd_channel.send("What would you like the thumbnail to be? (URL)")
          embed_thumbnail = await bot.wait_for('message', check=check, timeout=400)
          d_thumbnail = "false"

    #Main image
    await cmnd_channel.send("What would you like the image to be? (URL)")
    embed_image = await bot.wait_for('message', check=check, timeout=400)
    d_image = "false"
    if (embed_image.content == "test"):
        embed_image = "https://images-ext-2.discordapp.net/external/F94KlbsTNpGzF6zVvHBa9EI_9yuzm9bsva-SFKq_rRE/%3Fcb%3D20160409201542/https/vignette1.wikia.nocookie.net/gtawiki/images/b/b4/Vacca-GTAV-front.png/revision/latest?width=994&height=560"
        d_image = "true"

    #Additional Fields
    await cmnd_channel.send("Would you like to add an aditional field below the description?(Y/N)")
    embed_fieldchoice = await bot.wait_for('message', check=check, timeout=400)
    embed_fieldchoice = embed_fieldchoice.content.upper()
    while (embed_fieldchoice != "N" and embed_fieldchoice != "Y"):
           await cmnd_channel.send("Invalid answer. Would you like to add an aditional field below the description?(Y/N)")
           embed_fieldchoice = await bot.wait_for('message', check=check, timeout=400)
           embed_fieldchoice = embed_fieldchoice.content.upper()

    if (embed_fieldchoice == "Y"):
        await cmnd_channel.send("How many additional fields would you like? (1/2/3)")
        embed_field_number = await bot.wait_for('message', check=check, timeout=400)
        print(embed_field_number.content)
        while (embed_field_number.content != "1" and embed_field_number.content != "2" and embed_field_number.content != "3"):
               await cmnd_channel.send("Invalid answer. How many additional fields would you like? (1/2/3)")
               embed_field_number = await bot.wait_for('message', check=check, timeout=400)

    embed = discord.Embed(
        colour = embed_color,
        timestamp = ctx.message.created_at,
        title = embed_title.content,
        description = embed_description.content
    )

    #Author and Icon
    if (d_icon == "true"):
        embed.set_author(name=embed_author.content, icon_url=embed_icon)
    elif(d_icon == "false"):
        embed.set_author(name=embed_author.content, icon_url=embed_icon.content)

    # Thumbnail
    if (d_thumbnail == "true"):
        embed.set_thumbnail(url=embed_thumbnail)
    elif (d_thumbnail == "false"):
        embed.set_thumbnail(url=embed_thumbnail.content)

    #Main Image
    if (d_image == "true"):
        embed.set_image(url=embed_image)
    else:
        embed.set_image(url = embed_image.content)



    #Field
    if (embed_fieldchoice == "Y"):
        if (embed_field_number.content == "1"):
            #1st field
            await cmnd_channel.send("What would you like the title of the 1st field to be?")
            embed_field_title = await bot.wait_for('message', check=check, timeout=400)

            await cmnd_channel.send("What would you like the description of the 1st field to be?")
            embed_field_description = await bot.wait_for('message', check=check, timeout=400)
            embed.add_field(name = embed_field_title.content, value = embed_field_description.content, inline = True)

        elif (embed_field_number.content == "2"):
              #1st field
              await cmnd_channel.send("What would you like the title of the 1st field to be?")
              embed_field1_title = await bot.wait_for('message', check=check, timeout=400)

              await cmnd_channel.send("What would you like the description of the 1st field to be?")
              embed_field1_description = await bot.wait_for('message', check=check, timeout=400)

              #2nd field
              await cmnd_channel.send("What would you like the title of the 2nd field to be?")
              embed_field2_title = await bot.wait_for('message', check=check, timeout=400)

              await cmnd_channel.send("What would you like the description of the 2nd field to be?")
              embed_field2_description = await bot.wait_for('message', check=check, timeout=400)

              embed.add_field(name = embed_field1_title.content, value = embed_field1_description.content, inline = True)
              embed.add_field(name = embed_field2_title.content, value = embed_field2_description.content, inline = True)

        elif (embed_field_number.content == "3"):
              #1st field
              await cmnd_channel.send("What would you like the title of the 1st field to be?")
              embed_field1_title = await bot.wait_for('message', check=check, timeout=400)

              await cmnd_channel.send("What would you like the description of the 1st field to be?")
              embed_field1_description = await bot.wait_for('message', check=check, timeout=400)

              #2nd field
              await cmnd_channel.send("What would you like the title of the 2nd field to be?")
              embed_field2_title = await bot.wait_for('message', check=check, timeout=400)

              await cmnd_channel.send("What would you like the description of the 2nd field to be?")
              embed_field2_description = await bot.wait_for('message', check=check, timeout=400)

              await cmnd_channel.send("What would you like the title of the 3nd field to be?")
              embed_field3_title = await bot.wait_for('message', check=check, timeout=400)

              await cmnd_channel.send("What would you like the description of the 3nd field to be?")
              embed_field3_description = await bot.wait_for('message', check=check, timeout=400)

              embed.add_field(name = embed_field1_title.content, value = embed_field1_description.content, inline = True)
              embed.add_field(name = embed_field2_title.content, value = embed_field2_description.content, inline = True)
              embed.add_field(name = embed_field3_title.content, value = embed_field3_description.content, inline = True)

    elif (embed_fieldchoice == "N"):
          pass

    await ctx.send('What channel would you like to send this embed to?')
    wanted_channel = await bot.wait_for('message', check=check, timeout=400)
    wanted_channel = bot.get_channel(wanted_channel.raw_channel_mentions[0])
    await wanted_channel.send(embed = embed)
    await cmnd_channel.send("Embed sent.")

#sharksay
@commands.has_any_role("Owner", "Co-Owner", "Administrator", "admin", "bitchboy")
@bot.command()
async def sharksay(ctx):
    cmnd_channel = bot.get_channel(ctx.channel.id)
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    await cmnd_channel.send('What would you like the bot to say?')
    wanted_message = await bot.wait_for('message', check=check, timeout=120)
    await cmnd_channel.send("What channel would you like to send this to?")
    wanted_channel = await bot.wait_for('message', check=check, timeout=120)
    wanted_channel = bot.get_channel(wanted_channel.raw_channel_mentions[0])
    await wanted_channel.send(wanted_message.content)
    await cmnd_channel.send("Message sent.")

#morsecode
@commands.has_any_role("Owner", "Co-Owner", "Administrator", "admin", "bitchboy")
@bot.command()
async def morse(ctx):
    def check(m):
         return m.author == ctx.author and m.channel == ctx.channel
    cmnd_channel = bot.get_channel(ctx.channel.id)
    await cmnd_channel.send("Enter a phrase to translate.")
    phrase = await bot.wait_for('message', check=check, timeout=60)
    phrase = phrase.content.upper()
    morse_phrase = ""
    counter = 0
    while (counter < len(phrase)):
        if (phrase[counter] == "A"):
            morse_phrase += ".- "
        elif (phrase[counter] == "B"):
            morse_phrase += "-... "
        elif (phrase[counter] == "C"):
            morse_phrase += "-.-. "
        elif (phrase[counter] == "D"):
            morse_phrase += "-.. "
        elif (phrase[counter] == "E"):
            morse_phrase += ". "
        elif (phrase[counter] == "F"):
            morse_phrase += "..-. "
        elif (phrase[counter] == "G"):
            morse_phrase += "--. "
        elif (phrase[counter] == "H"):
            morse_phrase += ".... "
        elif (phrase[counter] == "I"):
            morse_phrase += ".. "
        elif (phrase[counter] == "J"):
            morse_phrase += ".--- "
        elif (phrase[counter] == "K"):
            morse_phrase += "-.- "
        elif (phrase[counter] == "L"):
            morse_phrase += ".-.. "
        elif (phrase[counter] == "M"):
            morse_phrase += "-- "
        elif (phrase[counter] == "N"):
            morse_phrase += "-. "
        elif (phrase[counter] == "O"):
            morse_phrase += "--- "
        elif (phrase[counter] == "P"):
            morse_phrase += ".--. "
        elif (phrase[counter] == "Q"):
            morse_phrase += "--.- "
        elif (phrase[counter] == "R"):
            morse_phrase += ".-. "
        elif (phrase[counter] == "S"):
            morse_phrase += "... "
        elif (phrase[counter] == "T"):
            morse_phrase += "- "
        elif (phrase[counter] == "U"):
            morse_phrase += "..- "
        elif (phrase[counter] == "V"):
            morse_phrase += "...- "
        elif (phrase[counter] == "W"):
            morse_phrase += ".-- "
        elif (phrase[counter] == "X"):
            morse_phrase += "-..- "
        elif (phrase[counter] == "Y"):
            morse_phrase += "-.-- "
        elif (phrase[counter] == "Z"):
            morse_phrase += "--.. "
        elif (phrase[counter] == "1"):
            morse_phrase += ".---- "
        elif (phrase[counter] == "2"):
            morse_phrase += "..--- "
        elif (phrase[counter] == "3"):
            morse_phrase += "...-- "
        elif (phrase[counter] == "4"):
            morse_phrase += "....- "
        elif (phrase[counter] == "5"):
            morse_phrase += "..... "
        elif (phrase[counter] == "6"):
            morse_phrase += "-.... "
        elif (phrase[counter] == "7"):
            morse_phrase += "--... "
        elif (phrase[counter] == "8"):
            morse_phrase += "---.. "
        elif (phrase[counter] == "9"):
            morse_phrase += "----. "
        elif (phrase[counter] == "0"):
            morse_phrase += "----- "
        elif (phrase[counter] == " "):
            morse_phrase += " "
        counter += 1
    await cmnd_channel.send(morse_phrase)

bot.run(TOKEN)
