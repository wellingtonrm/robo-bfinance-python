import os
import os
from termcolor import colored, cprint

from src.processos.color import bcolors

os.system("cls")

class Console():

    def log(self, param, color):
        print(color + "*******************INICIO************************")
        print(color, param)
        print(color + "*******************FIM************************")

