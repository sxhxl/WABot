import pyautogui
import time
import subprocess
import pywhatkit

class bcolors:
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    WHITE = '\033[37m'
    CYAN = '\033[36m'
    MAG = '\033[35m'
    BLUE = '\033[34m'
    BOLD = '\033[1m'
    DEF = '\033[0m'

def banner1():
    print(bcolors.RED + """\r\n$$\      $$\ $$\                  $$\                $$$$$$\                              $$$$$$$\             $$\     
$$ | $\  $$ |$$ |                 $$ |              $$  __$$\                             $$  __$$\            $$ |    
$$ |$$$\ $$ |$$$$$$$\   $$$$$$\ $$$$$$\    $$$$$$$\ $$ /  $$ | $$$$$$\   $$$$$$\          $$ |  $$ | $$$$$$\ $$$$$$\   
$$ $$ $$\$$ |$$  __$$\  \____$$\\_$$  _|  $$  _____|$$$$$$$$ |$$  __$$\ $$  __$$\ $$$$$$\ $$$$$$$\ |$$  __$$\\_$$  _|  
$$$$  _$$$$ |$$ |  $$ | $$$$$$$ | $$ |    \$$$$$$\  $$  __$$ |$$ /  $$ |$$ /  $$ |\______|$$  __$$\ $$ /  $$ | $$ |    
$$$  / \$$$ |$$ |  $$ |$$  __$$ | $$ |$$\  \____$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |        $$ |  $$ |$$ |  $$ | $$ |$$\ 
$$  /   \$$ |$$ |  $$ |\$$$$$$$ | \$$$$  |$$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$$  |        $$$$$$$  |\$$$$$$  | \$$$$  |
\__/     \__|\__|  \__| \_______|  \____/ \_______/ \__|  \__|$$  ____/ $$  ____/         \_______/  \______/   \____/ 
                                                              $$ |      $$ |                                           
                                                              $$ |      $$ |                                           
                                                              \__|      \__|                                           """)
    print(bcolors.RED + "\r\n+[+[+[ SXHXL TOOLS ]+]+]+")

def banner2():
    print(bcolors.BOLD + "\r\n Run the script and head over to the chat-box!!!")
    print(bcolors.BOLD + "\r\n Come back to the console and press ctrl+c to stop the bot. ")

def clear():
    subprocess.call("clear", shell=True)

def menu():
    opt = input(bcolors.CYAN+'''\r\n1. Spam using a text file
2. Spam using you custom message
3. Exit'''+bcolors.BOLD+'''
Select an option : ''')
    if opt == '1':
        clear()
        banner2()
        path = input(bcolors.GREEN + "\r\nEnter the path to text file : ")
        delay = int(input(bcolors.GREEN + "\r\nEnter a delay (in seconds) : "))
        file = open(path, 'r')
        while True:
            for words in file:
                time.sleep(delay)
                pyautogui.typewrite(words)
                pyautogui.press('enter')
    elif opt == '2':
        clear()
        banner2()
        msg = input(bcolors.GREEN + "\r\nEnter the message you want to send : ")
        delay = int(input(bcolors.GREEN + "\r\nEnter a delay (in seconds) : "))
        while True:
            time.sleep(delay)
            pyautogui.typewrite(msg)
            pyautogui.press('enter')
    elif opt == '3':
        clear()
        banner1()
        print(bcolors.MAG + 'Thank you for using the script.')
        exit()

if __name__ == '__main__':
    banner1()
    menu()
