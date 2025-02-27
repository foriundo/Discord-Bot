import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  
  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith("$Who sucks?"):
      await message.channel.send('Jordan!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM0NDc2MTQ3NjU5ODIwMjM5OQ.GWZ4SE.BpotyNwL5Lyt_spW3eS4PmrYlf54wiyKJW2Yv8') # Replace with your own token.



