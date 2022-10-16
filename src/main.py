from models.client import Client
from yaml import safe_load

def load_config(filename: str) -> dict:
    with open(f'{filename}', 'r', encoding="utf-8") as f:
        return safe_load(f)

config: dict = load_config('config.yml')


client = Client(sync_commands_debug=True, owner_ids=map(lambda i: int(i), config.get('owners')))
client.load_extensions('cogs')



client.run(config.get('token'))