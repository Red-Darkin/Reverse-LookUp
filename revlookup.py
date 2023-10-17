import socket
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def reverse_lookup(ip):
    try:
        host = socket.gethostbyaddr(ip)
        return host[0]
    except socket.herror:
        return Fore.RED + "Domain Not Found" + Style.RESET_ALL

def main():
    if len(sys.argv) != 2:
        print("Usage: python revlookup.py filename.txt")
        sys.exit(1)

    filename = sys.argv[1]
    ips = []

    try:
        with open(filename, 'r') as file:
            ips = file.read().splitlines()
    except FileNotFoundError:
        print(f"File {F'{filename}' not Found.")
        sys.exit(1)

    for ip in ips:
        domain = reverse_lookup(ip)
        print(f"Dirección IP: {ip} - Dominio: {Fore.GREEN}{domain}")

if __name__ == "__main__":
    main()
