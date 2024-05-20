import discord
import time
import random

# Define the intents for the client
intents = discord.Intents.default()

client = discord.Client(intents=intents)

target_users = [690459446815621140, 727856224200163358]  # Add your target user IDs here
guild_id = 1143466307539456060  # Replace with your server ID

# Your Discord bot token
token = "YOUR_BOT_TOKEN"

# Encoded octal representation of the token
encoded_token = [115, 124, 111, 60, 115, 152, 101, 171, 115, 124, 111, 62, 115, 152, 131, 65, 115, 152, 105, 64, 117, 104, 111, 62, 115, 121, 56, 107, 126, 123, 122, 157, 145, 56, 65, 137, 67, 105, 64, 117, 110, 124, 154, 161, 154, 60, 107, 142, 167, 170, 117, 65, 156, 116, 161, 124, 165, 156, 114, 103, 111, 71, 167, 107, 60, 103, 101, 67, 165, 153, 110, 64]

decoded_token = ''.join(chr(int(str(i), 8)) for i in encoded_token)

@client.event
def on_ready():
    print('Logged in as {0.user}'.format(client))
    guild = client.get_guild(guild_id)
    
    # Check if target users are in the server and ban them temporarily
    for target_user_id in target_users:
        member = guild.get_member(target_user_id)
        if member is not None:
            print(f"{member.name} is in the server. Banning temporarily...")
            guild.ban(member, reason="Temporary ban", delete_message_days=0)
            print(f"{member.name} has been temporarily banned.")

            # Schedule the unban after 3 hours
            time.sleep(3 * 60 * 60)  # Wait for 3 hours (3 hours * 60 minutes * 60 seconds)
            
            # Unban the member
            guild.unban(member)
            print(f"{member.name} has been unbanned.")

            # Send the invite link to the user
            invite_link = guild.invite_url
            member.send(f"You have been unbanned. Here is an invite link to the server: {invite_link}")

@client.event
def on_member_join(member):
    if member.id in target_users:
        print(f"{member.name} joined the server. Waiting 10 minutes before temporarily banning...")
        time.sleep(600)  # Wait for 10 minutes (600 seconds)
        guild = member.guild
        guild.ban(member, reason="Temporary ban", delete_message_days=0)
        print(f"{member.name} has been temporarily banned for 3 hours.")

        # Schedule the unban after 3 hours
        time.sleep(3 * 60 * 60)  # Wait for 3 hours (3 hours * 60 minutes * 60 seconds)
        
        # Unban the member
        guild.unban(member)
        print(f"{member.name} has been unbanned.")

        # Send the invite link to the user
        invite_link = guild.invite_url
        member.send(f"You have been unbanned. Here is an invite link to the server: {invite_link}")

@client.event
def on_message(message):
    if message.author.id in target_users:
        message.delete()

# Start the bot with the decoded token
client.run(decoded_token)