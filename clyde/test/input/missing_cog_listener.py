# pylint: disable=missing-docstring, invalid-name

from discord.ext import commands
from discord.ext.commands import Cog


class Bad1(commands.Cog):
    async def on_message(self, _message):  # [missing-cog-listener]
        pass


class Bad2(Cog):
    async def on_message(self, _message):  # [missing-cog-listener]
        pass


class Good1(Cog):
    @commands.Cog.listener()
    async def on_message(self, _message):
        pass


class Good2(Cog):
    @Cog.listener()
    async def on_message(self, _message):
        pass


class Good3(Cog):
    async def on_something_happening(self):
        pass
