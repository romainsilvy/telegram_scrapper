# telegram scrapper

This telegram bot is a simple helpfull tool which allows you to download pictures and videos from a Telegram channel.


# how to use this bot ?
Setup your pc using the following commands :
```
sudo apt update && apt upgrade

sudo apt install python3 python3-pip ipython3

pip install telethon 
```
Then, you just have to retrieve your telegram credentials : 
- visit https://my.telegram.org/
- login with phone number 
- go to the api developpement tools section 

Now you can enter the api id and api hash in the config.ini file 

When this is done, you can run the bot with 
```
python3 script.py
```
You will have to enter : 
- telegram channel id 
- media type 
- first message number 

and maybe 
- phone number starting with country code 
- 2fa security code received 


