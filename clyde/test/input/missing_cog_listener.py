# pylint: disable=missing-docstring, invalid-name

from discord.ext import commands
from discord.ext.commands import Cog


class A(commands.Cog):
    async def on_message(self, _message):  # [missing-cog-listener]
        pass


class B(Cog):
    async def on_message(self, _message):  # [missing-cog-listener]
        pass


class C(Cog):
    @commands.Cog.listener()
    async def on_message(self, _message):
        pass


class D(Cog):
    @Cog.listener()
    async def on_message(self, _message):
        pass
