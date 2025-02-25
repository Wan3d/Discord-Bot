import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import random
import asyncio

class MyClient(commands.Bot):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        try:
            guild = discord.Object(id=1090322790051229806)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} guilds')
        except Exception as e:
            print('Failed to sync commands: {e}')
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('I need help'):
            await message.channel.send(f'What do you need, {message.author}?')
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('Do not react')
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1090322790051229806)

@client.tree.command(name="hello", description="Just hello", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")
@client.tree.command(name="printer", description="I will print whatever you get me", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)
@client.tree.command(name="embed", description="beta", guild=GUILD_ID)
async def printEmbed(interaction: discord.Interaction):
    embed = discord.Embed(title="I am a title", url="https://discord.com/", description="I am the description", color=discord.Color.blue())
    embed.set_thumbnail(url="https://media.istockphoto.com/id/801485864/vector/flag-of-venezuela.jpg?s=612x612&w=is&k=20&c=TjGAJBN_dfqGlvjB1B2uEAZchUlnoIZPtjY82Sev534=")
    embed.add_field(name="Field 1", value ="File 1 Beta", inline=False) # If inline is true, it will alow multiple fields in the same line. Either way (false), the next field will be under the firset line
    embed.add_field(name="Field 2", value ="File 2 Beta")
    embed.set_footer(text="Footer text")
    embed.set_author(name=interaction.user.name, url="https://www.instagram.com/zullojeanpiero/")
    await interaction.response.send_message(embed=embed)
class View(discord.ui.View):
    @discord.ui.button(label="Start", style=discord.ButtonStyle.green)
    async def button_callback(self, interaction, button):
        button.disabled = True
        await interaction.response.edit_message(view=self) #Edits the message to make disappear the button 
        number = random.randint(1,1000)
        await interaction.followup.send(":white_check_mark: Random number generated :white_check_mark:")
        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel
        attempts = 15
        cont = 0
        for i in range(attempts):
            try:
                msg = await interaction.client.wait_for("message", timeout=15.0, check=check)
                guess = int(msg.content)
                cont += 1
                if (number == guess):
                    await interaction.followup.send(f"YOU HAVE GUESSED THE NUMBER IN {cont} ATTEMPTS :fire: :fire: CONGRATSSSS! :partying_face:")
                    return
                elif (number > guess):
                    await interaction.followup.send("Too low! :arrow_down:")
                elif (number < guess):
                    await interaction.followup.send("Too high! :arrow_up: ")
            except asyncio.TimeoutError:
                await interaction.followup.send(":clock: You took to long to guess. Game ended.")
                return
        await interaction.followup.send(f"You have reached the attempts limit :x: The number was {number} :sob:")
    @discord.ui.button(label="Info", style=discord.ButtonStyle.blurple)
    async def second_button_callback(self, interaction, button):
        button.disabled = True
        await interaction.response.edit_message(view=self) #Edits the message to make disappear the button 
        attempts = 15
        await interaction.followup.send(f":white_circle: A random number will be generated between the range of 1 and 1000. You have {attempts} attempts to guess it.\n:warning: Think fast, because you have only 15 seconds to type each answer.")
class viewHangman(discord.ui.View):
    @discord.ui.button(label="Start", style=discord.ButtonStyle.primary)
    async def first_button_callback(self, interaction, button):
        button.disabled = True
@client.tree.command(name="guess_the_number", description="Ready to play?", guild=GUILD_ID)
async def guessingButton(interaction):
    await interaction.response.send_message("Before starting, if you don't know how to play you should press the 'Info' button.\nWhenever you are ready, press the 'Start' button.", view=View())
@client.tree.command(name="hangman", description="Guess the random word", guild=GUILD_ID)
async def hangmanButton(interaction):
    await interaction.response.send_message("Test", view=viewHangman())

# from test import randomWordToGuess
# the idea is to get the random word that we generated after and start to work with it in this class
from config import TOKEN
client.run(TOKEN)



