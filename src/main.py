import discord
import os

from movie_picker import MoviePicker
from joke_teller import JokeTeller
from bot_logger import BotLogger

cmd_rsp_dict = dict()
client = discord.Client()
bot_logger = BotLogger()

@client.event
async def on_ready():
  bot_logger.info("SuperBot is logged in as {0.user}.".format(client))
  init_commands_responses_dictionary()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("superbot"):
    if message.content not in cmd_rsp_dict.keys():
      response = "I don't know this command, sorry!"
    elif message.content in cmd_rsp_dict.keys():
      response = cmd_rsp_dict.get(message.content)
      if message.content == "superbot":
        run_bot()

      if message.content == "superbot pick movie":
        movie_picker = MoviePicker()
        movie_data = movie_picker.pick_movie()
        response += "\n" + movie_data

      elif message.content == "superbot tell joke":
        joke_teller = JokeTeller()
        joke = joke_teller.tell_joke()
        response += joke
        
      elif message.content == "superbot bye":
        await message.channel.send(response)
        try:
          await client.logout()
        finally:
          bot_logger.info("SuperBot logged out.")
          return

    await message.channel.send(response)

def init_commands_responses_dictionary():
  global cmd_rsp_dict
  with open("config/commands.config", "r") as communication_protocol:
    for line in communication_protocol:
      cmd_rsp_pair = line.rstrip().split(",")
      cmd_rsp_dict.update({cmd_rsp_pair[0]:cmd_rsp_pair[1]})

def run_bot():
  client.run(os.getenv("BOT_TOKEN"))

if __name__ == '__main__':
  run_bot()
