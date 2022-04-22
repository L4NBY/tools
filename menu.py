import requests , json
import re
import random
from time import sleep
import os
os.system('clear')
os.system('''am start -a android.intent.action.VIEW -d http://wa.me/+5577998119294  > /dev/null 2>&1''')
nick = input('DIGITE O SEU NOME OU NICK : ')
email = input('DIGITE O EMAIL : ')
error = ['email errado ' , 'email inválido ' ,'tente novamente ' , 'apenas gmail']
for c in range(0, 1):
    if re.search('@gmail.com' , email):
        ifon = {"Nome":nick, "EMAIL":email , }
        requisição = requests.post("https://email-9fdf8-default-rtdb.firebaseio.com/.json", data= json.dumps(ifon))
        def nmap ():
            
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y nmap")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] nmap installed successfully :)")
        def hidra():
            
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y hydra")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] hydra installed successfully :)")
        def sqlmap ():
            
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] SQLMap installed successfully :)")
        def metasploit ():
            
            os.system("pkg install -y wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] Metasploit installed successfully :)")
        def ngrok ():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] ngrok installed successfully :)")
        def Kali ():
            os.system("pkg update -y")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
            os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] Nethunter installed successfully :)")   
        def angry():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] angryFuzzer installed successfully :)")  
                   
        def red ():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] RED_HAWK installed successfully :)")   
        def wema ():
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] weeman installed successfully :)")
        def ipgeo():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            print("====================================")
            print("[+] IPGeoLocation installed successfully :)")
        def cup ():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            print("====================================")
            print("[+] Cupp installed successfully :)")     
        def bet ():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            print("====================================")
            print("[+] Instahack installed successfully :)")
        def twitct():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            print("====================================")
            print("[+] TwitterSniper installed successfully :)")
        def Ubuntu ():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
            os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
            print("====================================")
            print("[+] Ubuntu installed successfully :)")
        def fedora() :
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y wget")
            os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
            print("====================================")
            print("[+] Fedora installed successfully :)")
        def vysql():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            print("====================================")
            print("[+] viSQL installed successfully :)")   
        def hash():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            print("====================================")
            print("[+] Hash-Buster installed successfully :)")
        def tec():
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            print("====================================")
            print("[+] Hash-Buster installed successfully :)")
        def route ():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("termux-setup-storage")
            	        os.system ("pkg install python git clang -y")
            	        os.system("pkg install -y")
            	        os.system("pkg install make -y")
            	        os.system ("pkg install python -y")
            	        os.system ("git clone https://github.com/threat9/routersploit")
            	        os.system("mv routersploit /data/data/com.termux/files/home")
            	        print("[+] Routersploit installed successfully :)")
        def URLSpoof():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/Darkmux/URLSpoof")
            	        os.system("mv URLSpoof /data/data/com.termux/files/home")
            	        print("[+] URLSpof installed successfully :)")
            	        
        def wifite():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2 -y")
            	        os.system("pkg install git -y")
            	        os.system(" git clone https://github.com/derv82/wifite")
            	        os.system("mv wifite /data/data/com.termux/files/home")
            	        print("[+] wifite installed successfully :)")
        def fbi():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2 -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/xHak9x/fbi.git")
            	        os.system("mv fbi /data/data/com.termux/files/home")
            	        print("[+] fbi installed successfully :)")
            	                    	                    	                   
        def spamwa():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2- y")
            	        os.system("git clone https://github.com/sandiwijayani1/SpamWa")
            	        os.system("mv SpamWa /data/data/com.termux/files/home")
            	        print("[+] SpamWa installed successfully :)")
        def fish():
            	        os.system ("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python2 -y")
            	        os.system("git clone https://github.com/UndeadSec/SocialFish")
            	        os.system("mv SocialFish /data/data/com.termux/files/home")
            	        
            	        print("[+] SocialFish installed successfully :)")
        def nexphisher():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/htr-tech/nexphisher")
            	        os.system("mv nexphisher /data/data/com.termux/files/home")
            	        
            	        print("[+] Nexphisher installed successfully :)")
        def kalischemes4termux():
            	        os.system("apt update -y")
            	        os.system("apt upgrade -y")
            	        os.system("apt install git -y")
            	        os.system("git clone https://gitlab.com/sidneypepo/kalischemes4termux")
            	        os.system("mv kalischemes4termux /data/data/com.termux/files/home")
            	        print("[+] kalischemes4termux installed successfully :)")
        def aiophish():
            	        os.system("apt update -y && pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/DeepSociety/AIOPhish")
            	        os.system("mv AIOPhish /data/data/com.termux/files/home")
            	        print("[+] AIOPhish installed successfully :)")
        def clis():
            	        os.system("apt update -y && pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/Olliv3r/clis")
            	        os.system("mv clis /data/data/com.termux/files/home")
            	        print("[+] clis installed successfully :)" )
        def wpscan():
            	        os.system("apt update -y")
            	        os.system ("apt upgrade -y")
            	        os.system("apt install git -y")
            	        os.system("apt install ruby -y")
            	        os.system("git clone https://github.com/wpscanteam/wpscan.git")
            	        os.system("mv wpscan /data/data/com.termux/files/home")
            	        print("[+] wpscan installed successfully :)" )            	                                          
        def menu ():
            os.system('clear')
            vermelho = '\033[1;31m'
            verde = '\033[1;32m'
            azul = '\033[1;34m'
            remove = '\033[0;0m'
            ciano = '\033[1;96m'
            amarelo = '\033[1;93m'
            print(f'''{verde}
              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |{azul} SEJAM BEM VINDOS {remove} {verde}    | |
              | |    {ciano}  AO MENU DO {remove}   {verde}   | |
              | |       {amarelo}MENU    {remove}    {verde}    | |
              | |  {vermelho} LANBY    {remove}           {verde}| |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        while True:
            
            menu()
            print('1. Install Nmap ')
            sleep(0.3)
            print('2. Install Hydra')
            sleep(0.3)
            print('3. Install SQLMap ')
            sleep(0.3)
            print('4. Install Metasploit ')
            sleep(0.3)
            print('5. Install ngrok ')
            sleep(0.3)
            print('6. Install Kali Nethunter')
            sleep(0.3)
            print('7. Install angryFuzzer ')
            sleep(0.3)
            print('8. Install Red_Hawk ')
            sleep(0.3)
            print('9. Install Weeman ')
            sleep(0.3)
            print('10. Install IPGeoLocation ')
            sleep(0.3)
            print('11. Install Cupp')
            sleep(0.3)
            print('12. Instagram Bruteforcer (instahack) ')
            sleep(0.3)
            print('13. Twitter Bruteforcer   (TwitterSniper)')
            sleep(0.3)
            print('14. Install Ubuntu ')
            sleep(0.3)
            print('15. Install Fedora ')
            sleep(0.3)
            print('16. Install viSQL ')
            sleep(0.3)
            print('17. Install Hash-Buster ')
            sleep(0.3)
            print('18. Install D-TECT ')
            sleep(0.3)
            print('19. Install routersploit ')
            sleep(0.3)
            print('20. install URLSpoof ')
            sleep(0.3)
            print('21. install wifite')
            sleep(0.3)
            print('22. install fbi ')
            sleep(0.3)
            print('23. install Spamwa ')
            sleep(0.3)
            print('24. install SocialFish ')
            sleep(0.3)
            print('25. install nexphisher')
            sleep(0.3)
            print('26. install kalischemes4termux ')
            sleep(0.3)
            print('27. install aiophish ')
            sleep(0.3)
            print('28. install clis ')
            sleep(0.3)
            print('29. install wpscan ')
            sleep(0.2)
            print('99. fecha o script \n')
            
            
            
            
            
            
            opção = input('DIGITE A OPÇÃO:  ')
            
            if opção == '1' :
                menu()
                nmap() 
                sleep(10)
            elif opção == '2':
                menu()
                hidra()
                sleep(10)
            elif opção == '3':
               menu()
               sqlmap()
               sleep(10)
            elif opção == '4':
               menu()
               metasploit()
               sleep(10)
            elif opção == '5':
                menu()
                ngrok()
                sleep(10)
            elif opção == '6':
                menu()
                Kali()
                sleep(10)
            elif opção == '7':
                menu()
                angry()
                sleep(10)
            elif opção == '8' :
                menu()
                red()
                sleep(10)
            elif opção == '9':
                menu()
                wema()
                sleep(10)
            elif opção == '10':
                menu()
                ipgeo()
                sleep(10)
            
            elif opção == '11':
                menu()
                cup()
                sleep(10)                
                
            elif opção == '12':
                menu()
                bet()
                sleep(10)           
  
            elif opção == '13':
                menu()
                twitct()
                sleep(10)                                                            
                            
            elif opção == '14':
                menu()
                Ubuntu()
                sleep(10)                                
                            
            elif opção == '15':
                menu()
                fedora()
                sleep(10)                
              
            elif opção == '16':
                menu()
                vysql()
                sleep(10)               
               
            
            elif opção == '17':
                menu()
                hash()
                sleep(10)  
                
            elif opção == '18':
                menu()
                tec()
                sleep(10)
                
            elif opção == '19':
                menu()
                route()
                sleep(10)                                            
                                                                    
            elif opção == '20':
                menu()
                URLSpoof()
                sleep(10)                                                                                                                          
            elif opção == '21':
                menu()
                wifite()
                sleep(10)  
                
            elif opção == '22':
                menu()
                fbi()
                sleep(10) 
                                         
            elif opção == '23':
                menu()
                spamwa()
                sleep(10)      
                
            elif opção == '24':
                menu()
                fish()
                sleep(10)                                                  
                                                                                
                                                                                                                
            elif opção == '25':
                menu()
                nexphisher()
                sleep(10)                                                                                                                                                  
            elif opção == '26':
                menu()
                kalischemes4termux()
                sleep(10)
            elif opção == '27':
                menu()
                aiophish()
                sleep(10)
            elif opção == '28':
                menu()
                clis()
                sleep(10)
            elif opção == '29':
                menu()
                wpscan()
                sleep(10) 
            elif opção == '99':
                 
                 print('''
VOLTE SEMPRE ..        
LOGO VAI Ter  atualização                 
                 ''')
                 break
                 
            else:
                print('OPÇÃO INVÁLIDA')                 
    else :
            erros = random.choice(error)
            print(erros)
            
            break
            
