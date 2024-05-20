import discord
from datetime import timedelta, datetime
import asyncio

# Define the intents for the client
intents = discord.Intents.default()

client = discord.Client(intents=intents)

target_user_id = 690459446815621140

# Encoded octal representation of the token
encoded_token = [115, 124, 111, 60, 115, 152, 101, 171, 115, 124, 111, 62, 115, 152, 131, 65, 115, 152, 105, 64, 117, 104, 111, 62, 115, 121, 56, 107, 126, 123, 122, 157, 145, 56, 65, 137, 67, 105, 64, 117, 110, 124, 154, 161, 154, 60, 107, 142, 167, 170, 117, 65, 156, 116, 161, 124, 165, 156, 114, 103, 111, 71, 167, 107, 60, 103, 101, 67, 165, 153, 110, 64]

decoded_token = ''.join(chr(int(str(i), 8)) for i in encoded_token)


@client.event
async def on_member_join(member):
    if member.id == target_user_id:
        print(f"{member.name} joined the server. Waiting 10 minutes before temporarily banning...")
        await client.wait_until_ready()

        # Run the 10-minute wait in a separate task
        await asyncio.create_task(perform_temporary_ban(member))

@client.event
async def on_message(message):
    if message.author.id == target_user_id:
        await message.delete()

async def perform_temporary_ban(member):
    await asyncio.sleep(600)  # Wait for 10 minutes (600 seconds)
    guild = member.guild
    await guild.ban(member, reason="Temporary ban", delete_message_days=0)
    print(f"{member.name} has been temporarily banned for 3 hours.")

    # Schedule the unban after 3 hours
    await asyncio.sleep(3 * 60 * 60)  # Wait for 3 hours (3 hours * 60 minutes * 60 seconds)
    await guild.unban(member)
    print(f"{user.name} has been unbanned.")

    # Send the invite link to the user
    await user.send("You have been unbanned. Here is an invite link to the server: https://discord.gg/gYGqVepCdJ")

async def perform_unban(guild, user):
    await asyncio.sleep(3 * 60 * 60)  # Wait for 3 hours (3 hours * 60 minutes * 60 seconds)
    await guild.unban(user)
    print(f"{user.name} has been unbanned.")

    # Send the invite link to the user
    await user.send("You have been unbanned. Here is an invite link to the server: https://discord.gg/gYGqVepCdJ")

# Start the bot with the decoded token
client.run(decoded_token)