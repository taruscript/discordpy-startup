from discord.ext import commands
import os
import traceback
import connection_DB
import send_format




bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
table = connection_DB.table

def check_arg_format(arg):
    arg_count = len(arg.split())
    if arg_count != 3:     
        raise TypeError("引数のフォーマットが正しくありません")

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def mtg(ctx, *, arg):
    check_arg_format(arg)
    team, start_date, end_date = arg.split()
    table.insert({"team": team, "start_date": start_date, "end_date": end_date})
    await ctx.send(send_format.insert_msg.format(team, start_date, end_date))


@bot.command()
async def remind(ctx):
    for row in table.find():
        await ctx.send(send_format.remind_msg.format(row["team"], row["start_date"], row["end_date"]))

bot.run(token)
