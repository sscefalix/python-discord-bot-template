from disnake.ext import commands

from models.client import Client

class Events(commands.Cog):
    def __init__(self, client: Client) -> None:
        self.client = client

    @commands.Cog.listener('on_ready')
    async def connected(self):
        print(f'{self.client.user} Успешно запущен!')

def setup(client: Client):
    client.add_cog(Events(client=client))