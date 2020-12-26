import os
import requests
import time
banner = ("""


  __  __                 _______          _ 
 |  \/  |               |__   __|        | |
 | \  / | __ _ ___ ___     | | ___   ___ | |
 | |\/| |/ _` / __/ __|    | |/ _ \ / _ \| |
 | |  | | (_| \__ \__ \    | | (_) | (_) | |
 |_|  |_|\__,_|___/___/    |_|\___/ \___/|_|
                                            
                                            
""")
print(banner)
time.sleep(5)
anlasma = input("Hiç bir şekilde bunu illegal bir amaç için kullanmıcağına söz verebilir misin ?")
if anlasma == "e":
    print("\033[31m Sana güveniyorum genç dostum \033[0m")
    time.sleep(3)
    os.system("clear")
    temel = input("{1} Bilgi Toplama ve Açık Arama Araçları")
    if temel == "1":
        time.sleep(3)
        os.system("clear")
        info = input("{1}Nikto {2}Nmap {3}WhoIs {4}Uniscan")
        if info == "1":
            c = input("\033[31mHedef site\033[0m")
            os.system("nikto -h"+c)
            if info == "2":
                d = input("\033[33;4m Hedef ip:\033[0m")
                os.system("nmap -sS -sV"+2)
                if info == "3":
                    f = input("\033[31m hedef : example.com \033[0m")
                    os.system("whois"+f)
                    if info == "4":
                        p = input("\033[33;4m Hedef : example.com\033[0m")
                        os.system("uniscan -u"+p+"-qweds")
                              
