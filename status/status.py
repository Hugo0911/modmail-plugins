import discord
from discord.ext import commands, tasks

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.statuses = ['Playing with Python', 'Learning new tricks', 'Helping out in servers']
        self.status_task.start()

    def cog_unload(self):
        self.status_task.cancel()

    @tasks.loop(minutes=1)
    async def status_task(self):
        for status in self.statuses:
            await self.bot.change_presence(activity=discord.Game(name=status))
            await asyncio.sleep(60)

    @commands.command(name='startstatus', help='Start updating the bot\'s status every minute')
    async def start_status(self, ctx):
        self.status_task.start()
        await ctx.send('Status updates have started')

    @commands.command(name='stopstatus', help='Stop updating the bot\'s status')
    async def stop_status(self, ctx):
        self.status_task.stop()
        await ctx.send('Status updates have stopped')

def setup(bot):
    bot.add_cog(StatusCog(bot))
