import time 
from colorama import init
from termcolor import colored
import os
import webbrowser as wbb

init()

print(colored("=== ESScript 3.0 [beta] ===\n", "magenta"))
print(colored("[1]", "red"), colored("Help", "green"))
print(colored("[2]", "red"), colored("Registration", "green"))
print(colored("[3]", "red"), colored("Docs\n", "green"))
print(colored("===", "magenta"), colored("    by Code Idea   ", "cyan"), colored("===\n", "magenta"))

command_1 = ["1"]
command_2 = ["2"]
command_3 = ["3"]
command_cls = ["cls"]
command_clear = ["clear"]
sm = [":start matrix", ":sm"]
em = [":end matrix", ":em"]

while True:
    commands = input(colored("$: ", "cyan"))

    if commands in command_1:
        print(colored("For creating matrix:\n\n1):start matrix:\n2):your text for playing\n3):end matrix\n", "green"))
        print(colored("For creating new matrix:\n\n:start matrix\n\nOld file will be deleted!", "green"))

    elif commands in command_2:
        id = input(colored("Api id: ", "cyan"))
        hash = input(colored("Api hash: ", "cyan"))
        with open("data.py", 'w') as f:
            f.write(f"api_id = {id}\napi_hash = '{hash}'")
        print(colored("Success! your datas saved!", "green"))

    elif commands in command_3:
        try:
            wbb.open("https://code-idea.netlify.app/esscript/ess.html")
        except:
            print(colored("https://code-idea.netlify.app/esscript/ess.html", "cyan"))

    elif commands in command_clear:
        os.system("clear")
        print(colored("=== ESScript 2.0 [beta] ===\n", "magenta"))
        print(colored("[1]", "red"), colored("Help", "green"))
        print(colored("[2]", "red"), colored("Registration", "green"))
        print(colored("[3]", "red"), colored("Docs\n", "green"))
        print(colored("===", "magenta"), colored("    by Code Idea   ", "cyan"), colored("===\n", "magenta"))

    elif commands in command_cls:
        os.system("cls")
        print(colored("=== ESScript 2.0 [beta] ===\n", "magenta"))
        print(colored("[1]", "red"), colored("Help", "green"))
        print(colored("[2]", "red"), colored("Registration", "green"))
        print(colored("[3]", "red"), colored("Docs\n", "green"))
        print(colored("===", "magenta"), colored("    by Code Idea   ", "cyan"), colored("===\n", "magenta"))

    # userbot 

    # starting
    elif commands in sm:
        with open("bot.py", 'w') as f:
            f.write(f"import time\nfrom telethon import TelegramClient, events, sync\nfrom data import api_id, api_hash\n")
        with open('bot.py', 'a') as f:
            f.write(f"client = TelegramClient('anon', api_id, api_hash)\n\n")
        with open("bot.py", "a") as f:
            f.write(f"@client.on(events.NewMessage)\nasync def my_event_handler(event):\n")
        with open("bot.py", "a") as f:
            f.write(f'   if event.raw_text in event.raw_text:\n')
        print(colored("$: :...", "green"))

    # editing 

    elif commands.startswith(": "):
        with open("bot.py", "a") as f:
            f.write(f'    await event.edit("{commands[1:]}")\n')
    
    # end matrix

    elif commands in em:
        with open("bot.py", "a") as f:
            f.write(f'    time.sleep(1)\n')
        with open("bot.py", "a") as f:
            f.write(f'    await event.edit(event.raw_text)\n')
        with open('bot.py', "a") as f:
            f.write("client.start()\nclient.run_until_disconnected()")

        print(colored(":$ > Success!", "green"))

    else:
        print(colored(f"::Console:: Error! i don't know sytax '{commands}'", "red"))


    
