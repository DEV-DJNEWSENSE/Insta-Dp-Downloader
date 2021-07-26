import instaloader
import os
bot = instaloader.Instaloader()
username = input("Enter The UserName: ")
print(bot.download_profile(username,profile_pic_only=True))