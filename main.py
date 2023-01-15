import os
import time
import colorama
from mcstatus import JavaServer
from mcstatus import BedrockServer

prefix = f"{colorama.Fore.RED}[STATUS] {colorama.Fore.RESET}"
yellow = f"{colorama.Fore.YELLOW}"

os.system('')
print(f"""{colorama.Fore.LIGHTGREEN_EX}



░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░  ░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗  ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝  ╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗  ░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║  ██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░

""")
print(f"{colorama.Fore.RESET}Server Status 1.0 {colorama.Fore.GREEN}BETA{Fore.WHITE} Made By Mehran1022)

time.sleep(2)
print(f"{colorama.Fore.RESET}")
print("[1] Java Edition")
print("[2] Bedrock Edition")
print('')
type = input(prefix + "Please Select One Of The Versions: ")
if type == '1':
   ipj = str(input(prefix + "Please Type Target Domain/IP With Port: "))
   server = JavaServer.lookup(ipj)
   status = server.status()
   print(prefix + "Loading Services")
   time.sleep(2.5)
   print(prefix + f"Online Players: {status.players.online} | Max Players: {status.players.max} |Players Latency: {status.latency}")
  
if type == '2':
 ipb = str(input(prefix + "Please Type Target Domain/IP With Port: "))
 server = BedrockServer.lookup(ipb)
 status = server.status()
 print(prefix + "Loading Services")
 time.sleep(2.5)
 print(prefix + f"Online Players: {status.players.online} | Max Players: {status.players.max} | Players Latency: {status.latency}")