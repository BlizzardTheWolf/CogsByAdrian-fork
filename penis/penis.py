import discord
import random
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify


class Penis(commands.Cog):
    """Penis related commands."""

    @commands.command()
    async def penis(self, ctx, *users: discord.Member):
        """Detects user's penis length

        This is 100% accurate.
        Enter multiple users for an accurate comparison!"""
        if not users:
            await ctx.send_help()
            return

        dongs = {}
        msg = ""
        state = random.getstate()

        for user in users:
            random.seed(str(user.id))

            if ctx.bot.user.id == user.id:
                length = "8" + "=" * 30 + "D"  # Default size for the bot
            elif user.id == 931911910985715762:
                length = "8" + "=" * 60 + "D"  # Adjusted size for the specific user
            else:
                length = "8" + "=" * random.randint(0, 30) + "D"  # Random size for other users

            dongs[user] = length

        random.setstate(state)
        dongs = sorted(dongs.items(), key=lambda x: x[1])

        for user, dong in dongs:
            msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)

        for page in pagify(msg):
            await ctx.send(page)
