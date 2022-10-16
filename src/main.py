from models.client import Client, load_config
from disnake import Intents


config: dict = load_config('config.yml')


client = Client(sync_commands_debug=True, owner_ids=[map(lambda i: int(i), config.get('owners'))], intents=Intents.all(), reload=True)
client.load_extensions('cogs')



client.run(config.get('token'))