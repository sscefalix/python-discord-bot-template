from disnake.ext import commands
from disnake import ApplicationCommandInteraction as Interaction

from models.client import Client
from models.embed import Embed

class Info(commands.Cog):
    def __init__(self, client: Client) -> None:
        self.client = client

    @commands.slash_command(name="help")
    async def help(self, inter: Interaction):
        "Получить список всех команд бота."
        categories = {
            'info': 'Информация'
        }

        embed = Embed()

        for chapter, name in categories.items():
            cmds = [f"`{command.name}` — {command.description}" for command in self.client.slash_commands if command.cog_name == chapter]
            embed.add_field(
                name=name,
                value='\n'.join(cmds),
                inline=True
            )

        await inter.send(embed=embed)


def setup(client: Client):
    client.add_cog(Info(client=client))