import requests, threading, os
from colorama import Fore

os.system(f'title [server leaver]')
os.system(f'mode 80,20')

print(f'                                 {Fore.CYAN}server leaver \n\n')

print(f'                                   {Fore.YELLOW}@uo2 {Fore.LIGHTMAGENTA_EX} \n')

def leave(guild_id, token):
   rq = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers={"Authorization": token})
   if rq.status_code == 204 or 200:
     print(f"left {guild_id}")
def get_all_guilds(token) -> list():
   servers = []
   rq = requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"Authorization": token})
   for guild in rq.json():
    servers.append(guild["id"])
   return servers
def start():
   token = input(f"Token: ")
   guilds = get_all_guilds(token)
   for guild in guilds:
       threading.Thread(target=leave, args=(guild, token,)).start()
start()
