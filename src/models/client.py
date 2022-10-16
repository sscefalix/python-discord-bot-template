from disnake.ext.commands import AutoShardedInteractionBot

class Client(AutoShardedInteractionBot):
    @property
    def guild_count(self) -> int:
        return len(self.guilds)

    @property
    def user_count(self) -> int:
        return len(self.guilds)