@tasks.loop(seconds=40)  # How often the bot should change status, mine is set on every 40 seconds
async def changepresence():
    global x

    game = iter(
        [
            "Status 1",
            "Status 2",
            "Status 3",
            "Status 4",
            "Status 5?",
            "Status 6",
        ]
    )  # Every line above ^^ is one new status the bot can have
    for x in range(random.randint(1, 6)):  # Here you write the total of different status you have for the bot, I have 6 and that's why I have number 6 there. This makes it a 16.666% chance to change status every 40 second
        x = next(game)
    await bot.change_presence(activity=discord.Game(name=x))
