import requests
import json
import asyncio
import os, sys
from datetime import datetime
from time import gmtime, strftime
from colorama import init, Fore, Back, Style
from discord.ext import commands
from discord.ext.commands import Bot
os.system('cls')
print(f'''
{Fore.RED}
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ████████╗██╗███╗░░░███╗███████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██║████╗░████║██╔════╝
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ░░░██║░░░██║██╔████╔██║█████╗░░
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ░░░██║░░░██║██║░╚═╝░██║███████╗
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝{Fore.RESET}
''')
print(f"""
			{Fore.LIGHTCYAN_EX}Discord: lyt1x#6666{Fore.RESET}
""")

Bot = commands.Bot(command_prefix='>', self_bot=True)
Bot.remove_command('help')

with open('token.txt','r') as f:
    token = f.readline()

@Bot.event
async def on_ready():
    print('')
    print('[=========================================================================================]')
    print('')
    print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Successfully logged in account [{Fore.LIGHTMAGENTA_EX}{Bot.user}{Fore.RESET}]')
    print('')
    print('[=========================================================================================]')
    print('')
    a = input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] Start the script? [+ / -] ')
    print('')
    if a == '+':
        while True:
            await asyncio.sleep(3) #time between updating
            months = ['January','February','March','April','May','June','July','August','September','October','November','December']
            now = datetime.now()
            second = now.second
            minute = now.minute
            hour = now.hour
            if now.second < 10:
                second = f'0{now.second}'
            if now.minute < 10:
                minute = f'0{now.minute}'
            if now.hour < 10:
                hour = f'0{now.hour}'
            text = f'{now.day} {months[now.month - 1]} {now.year}, {hour}:{minute}:{second}, timezone: GMT {strftime("%z", gmtime()).replace("0","")}'
            status_data = json.dumps(
                {
                    "custom_status":
                        {
                            "text": text
                        }
                }
            )
            sys.stdout.write("\r" + f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {text}')
            sys.stdout.flush()
            r = requests.patch("https://discordapp.com/api/v6/users/@me/settings",headers={"Authorization": token, "Content-Type": "application/json"}, data=status_data)
    else:
        print(f'[{Fore.RED}-{Fore.RESET}] Exiting...')
        await asyncio.sleep(3)
        os._exit(0)

Bot.run(token,bot=False)