import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def nauka(ctx):
    tips = {
        "- Использовать многоразовые товары, такие как многоразовые пакеты, стаканчики и столовые приборы.",
        "- Переходить на цифровые форматы, чтобы избежать использования бумаги и пластиковых носителей информации.",
        "- Разделять отходы на перерабатываемые и неперерабатываемые материалы и утилизировать их соответствующим образом.",
        "- Покупать продукты с минимальным количеством упаковки и выбирать упаковки, которые можно переработать или разложить.",
        "- Участвовать в акциях по очистке окружающей среды и сознательно выбирать места для отдыха, чтобы не загрязнять природу.",
        "- Использовать энергосберегающие лампы, бытовую технику и электронику, а также максимально использовать естественное освещение."
    }
    used_tips = []
    while True:
        tip = random.choice(tips.values())
        if tip not in used_tips:
            used_tips.append(tip)
            message = f"{tip}\n"
            await ctx.send(message)

bot.run("MTE1Mjk2MDkxMzc3MTYwMjAwMQ.GcINRb.kSNEQDpcDu9g5Q-5DgjPO_nqLzfV5lNwlEOqM0")