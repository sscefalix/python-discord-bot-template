from disnake.ext import commands
from disnake import ApplicationCommandInteraction as Interaction, ButtonStyle
from disnake.ui import Button

from models.client import Client
from models.embed import Embed

class Info(commands.Cog):
    def __init__(self, client: Client) -> None:
        self.client = client

    @commands.slash_command(name="help")
    async def help(self, inter: Interaction):
        "Получить список всех команд бота."
        categories = {
            'Info': 'Информация'
        }

        embed = Embed()

        for chapter, name in categories.items():
            cmds = [f"`/{command.name}` — {command.description}" for command in self.client.slash_commands if command.cog_name == chapter]
            for c in self.client.slash_commands:
                print(c.cog_name, chapter)
            embed.add_field(
                name=name,
                value='\n'.join(cmds)
            )

        await inter.send(embed=embed)

    @commands.slash_command(name="server")
    async def server(self, inter: Interaction):
        "Получить информацию о сервере."

        embed = Embed(title=f'{inter.guild.name}')
        embed.set_thumbnail(url=inter.guild.icon)
        embed.add_field('Владелец', inter.guild.owner)
        embed.add_field('Айди', inter.guild.id)
        embed.add_field('Дата создания', f'<t:{int(inter.guild.created_at.timestamp())}:f>')

        await inter.send(embed=embed)

    @commands.slash_command(name="bot")
    async def bot(self, inter: Interaction):
        "Получить информацию о боте."

        embed = Embed(title=f'Информация о {self.client.user}')
        embed.add_field('Пинг', f'{round(self.client.latency*1000)} мс')
        embed.add_field('Количество серверов', self.client.guild_count)
        embed.add_field('Колиество пользователей', self.client.user_count)
        embed.add_field('Запущен', f'<t:{int(self.client.uptime)}:R>')
        if website := self.client.config.get('website'):
            components = [
                Button(style=ButtonStyle.url, url=f'{website}', label='Сайт')
            ]
            await inter.send(embed=embed, components=components)
        else: await inter.send(embed=embed)


def setup(client: Client):
    client.add_cog(Info(client=client))