import discord
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot('.')

@tasks.loop(seconds=30)
async def switch_presence():
    # list of all activities to switch between
    activities = [
        discord.Activity(type=discord.ActivityType.listening, name='First activity'),
        discord.Activity(type=discord.ActivityType.listening, name='Another activity')
    ]
    curr_activity = bot.activity
    # default to the first activity if not set or invalid
    if curr_activity not in activities:
        await bot.change_presence(activity=activities[0])
        return
    # use modulo to start from the beginning once the list is exhausted
    next_activity_index = (activities.index(curr_activity) + 1) % len(activities)
    await bot.change_presence(activity=activities[next_activity_index])

@bot.event
async def on_ready():
    switch_presence.start()
