from disnake import Embed
from typing import Any

class Embed(Embed):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.set_default_colour(0xffffff)
        return super().__call__(*args, **kwds)