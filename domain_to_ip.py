import socket
import pyfiglet #banner package
from termcolor import colored

banner = colored(pyfiglet.figlet_format("DOMAIN TO IP"), 'green')

domain_name = input('enter domain : ')

ip = socket.gethostbyname(domain_name)

print(ip)