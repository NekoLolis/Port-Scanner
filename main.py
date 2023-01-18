import socket, threading, concurrent.futures, colorama, os
from colorama import Fore
colorama.init()

print_lock = threading.Lock()

host = input(f"{Fore.LIGHTMAGENTA_EX}Host To Scan >{Fore.RESET} ")

def scan(host, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((host, port))
        scanner.close()
        with print_lock:
            print(f"{Fore.LIGHTMAGENTA_EX}[{port}] Is{Fore.GREEN} Open {Fore.RESET}")

    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(65535):
        executor.submit(scan, host, port+1)

print(f"{Fore.LIGHTMAGENTA_EX}Done Scanning Ports On {host} <3")
os.system("pause >nul")
