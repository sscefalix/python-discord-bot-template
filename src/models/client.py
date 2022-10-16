from time import time
from disnake.ext.commands import AutoShardedInteractionBot
from typing import Any
from yaml import safe_load

def load_config(filename: str) -> dict:
    with open(f'{filename}', 'r', encoding="utf-8") as f:
        return safe_load(f)

class Client(AutoShardedInteractionBot):
    @property
    def guild_count(self) -> int:
        return len(self.guilds)

    @property
    def user_count(self) -> int:
        return len(self.guilds)

    @property
    def config(self) -> dict:
        return load_config('config.yml')

    def run(self, *args: Any, **kwargs: Any) -> None:
        self.uptime = time()
        return super().run(*args, **kwargs)