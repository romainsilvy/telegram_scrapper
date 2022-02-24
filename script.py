import configparser
from http.client import SWITCHING_PROTOCOLS
import string
import os
from telethon import TelegramClient

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
phone = config['Telegram']['phone']
username = config['Telegram']['username']

#start a new telegram client 
client = TelegramClient('session_id', api_id, api_hash)
channelName = input("enter channel id(if the invitation link is t.me/abc, enter abc):")
os.mkdir(channelName)
type = input("enter type of file (photo, video or both):")
startNumber = input("start from message : ")
startNumber = int(startNumber)

async def main():
    count = 0
    print("start downloading...")
    async for message in client.iter_messages(channelName):
        print("message number : ", count)
        if count >= startNumber:
            if (message.photo and type == "photo"):
                path = await client.download_media(message.photo, channelName)
            elif (message.video and type == "video") :
                path = await client.download_media(message.video, channelName)
            elif ((message.video or message.photo) and type == "both") :
                path = await client.download_media(message.media, channelName)
            print('File saved')  # printed after download is done
        count = count + 1
    print("you downloaded : ", count, type)

with client:
    client.loop.run_until_complete(main())

