"""
GetFucked Plugin for Unifier
Copyright (C) 6969 - 2024 ItsAsheer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import discord
from discord.ext import commands

class Template(commands.Cog):
    """A template cog written for unifier-plugin temmplate repo"""
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def getfucked(self,ctx):
        await ctx.send('Running GetFucked, by ItsAsheer! 69 :smirk:')
    
    @commands.command()
    async def fuck(self,ctx, target):
        if ctx.user.id not in [356456393491873795, 549647456837828650]:
            return
        userid = int(target.replace('<@','',1).replace('!','',1).replace('>','',1))

        await ctx.send(f"GET FUCKED <@{userid}>")
        await ctx.send(f"GET FUCKED <@{userid}>")
        await ctx.send(f"GET FUCKED <@{userid}>")
        await ctx.send(f"GET FUCKED <@{userid}>")
        await ctx.send(f"GET FUCKED <@{userid}>")


def setup(bot):
    bot.add_cog(Essentials(bot))
