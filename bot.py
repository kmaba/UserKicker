import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True  # Subscribe to member events

bot = commands.Bot(command_prefix='!', intents=intents)

target_users = [690459446815621140, 727856224200163358]
guild_id = 1143466307539456060

encoded_token = [115, 124, 111, 60, 115, 152, 101, 171, 115, 124, 111, 62, 115, 152, 131, 65, 115, 152, 105, 64, 117, 104, 111, 62, 115, 121, 56, 107, 126, 123, 122, 157, 145, 56, 65, 137, 67, 105, 64, 117, 110, 124, 154, 161, 154, 60, 107, 142, 167, 170, 117, 65, 156, 116, 161, 124, 165, 156, 114, 103, 111, 71, 167, 107, 60, 103, 101, 67, 165, 153, 110, 64]
decoded_token = ''.join(chr(int(str(i), 8)) for i in encoded_token)

async def temp_ban(member):
    guild = member.guild
    print(f"{member.name} is in the server. Banning temporarily...")
    try:
        await guild.ban(member, reason="Temporary ban", delete_message_days=0)
        print(f"{member.name} has been temporarily banned.")
    except discord.Forbidden:
        print(f"Error banning {member.name}: Bot does not have permission to ban.")
    except discord.HTTPException as e:
        print(f"Error banning {member.name}: {e}")
    else:
        await asyncio.sleep(3 * 60 * 60)
        try:
            await guild.unban(member)
            print(f"{member.name} has been unbanned.")
        except discord.Forbidden:
            print(f"Error unbanning {member.name}: Bot does not have permission to unban.")
        except discord.HTTPException as e:
            print(f"Error unbanning {member.name}: {e}")

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    guild = bot.get_guild(guild_id)
    for target_user_id in target_users:
        member = guild.get_member(target_user_id)
        if member is not None:
            await temp_ban(member)

@bot.event
async def on_member_join(member):
    if member.guild.id == guild_id and member.id in target_users:
        print(f"{member.name} joined the server. Waiting 10 minutes before temporarily banning...")
        await asyncio.sleep(600)
        await temp_ban(member)

bot.run(decoded_token)