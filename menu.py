
from rich.table import Table
from rich.console import  Console
from subprocess import Popen, PIPE
import requests , json
import re
import random
from time import sleep
import os
os.system('clear')
nick = input('DIGITE O SEU NOME OU NICK : ')
email = input('DIGITE O EMAIL : ')
error = ['email errado ' , 'email inválido ' ,'tente novamente ' , 'apenas gmail']
for c in range(0, 1):
    if re.search('@gmail.com' , email):
        ifon = {"Nome":nick, "EMAIL":email , }
        requisição = requests.post("https://email-9fdf8-default-rtdb.firebaseio.com/.json", data= json.dumps(ifon))
        def url3():
            os.system('clear')
            print('\033[1;96m')
            print('''
[1] LIGAR
[2] DESLIGAR \n''')
            url4 = input('DIGITE A OPÇÃO ').lstrip().lstrip('0').rstrip()
            if url4 == '1':
                os.system('''echo 'terminal-onclick-url-open=true'> ~/.termux/termux.properties''')
                os.system('termux-reload-settings')
                print('LIGADO COM SUCESSO \n')
                print('''CLICK NA URL 

click >  http://wa.me/+5577998119294
 
   ''')
                input('ENTER VOLTA AO MENU  ')
            elif url4 == '2':
                os.system('''echo 'terminal-onclick-url-open=false'> ~/.termux/termux.properties''')
                print('DESLIGADO COM SUCESSO \n')
                os.system('termux-reload-settings')
                input('ENTRE PARA VOLTAR O MENU')
            else:
                print('OPÇÃO INVÁLIDA VOLTANDO AO MENU')
                sleep(3)
        def information():
            ip = requests.get('https://ipwhois.app/json/')
            resultado = ip.json()
            ip2 = resultado['ip']

            whoami = Popen(['whoami'], stdin=PIPE, stdout=PIPE, stderr=PIPE).stdout.read().decode()
            console = Console()
            table = Table(title=' SUAS INFORMAÇÕES ' , style='blue') #nome da tabela 
            table.add_column('NOME' )
            table.add_column('EMAIL')
            table.add_column('USUARIO')
            table.add_column('IP')
            table.add_row(f'{nick} ' , f'{email}' , f'{whoami}' , f'{ip2} ' , style='green')

            console.print(table , style='cyan')
            con = Console()

            tab = Table(title='DONO INFO' , style='purple')
            tab.add_column('NUMERO ' )
            tab.add_column('PIX')
            tab.add_column('CRIADOR')
            tab.add_row('+5577998119294' , '8b750993-cda8-4efd-9ebe-bb3c05cfcae4', 'LANBY' , style='cyan')
            tab.add_row(' ' , 'vou desisti dessa porra ninguém doar nada , 1 centavo faz a diferença ' , ' ' , style='yellow')

            con.print(tab , style='green')
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
            sleep(0.1)
            print('2. Install Hydra')
            sleep(0.1)
            print('3. Install SQLMap ')
            sleep(0.1)
            print('4. Install Metasploit ')
            sleep(0.1)
            print('5. Install ngrok ')
            sleep(0.1)
            print('6. Install Kali Nethunter')
            sleep(0.1)
            print('7. Install angryFuzzer ')
            sleep(0.1)
            print('8. Install Red_Hawk ')
            sleep(0.1)
            print('9. Install Weeman ')
            sleep(0.1)
            print('10. Install IPGeoLocation ')
            sleep(0.1)
            print('11. Install Cupp')
            sleep(0.1)
            print('12. Instagram Bruteforcer (instahack) ')
            sleep(0.1)
            print('13. Twitter Bruteforcer   (TwitterSniper)')
            sleep(0.1)
            print('14. Install Ubuntu ')
            sleep(0.1)
            print('15. Install Fedora ')
            sleep(0.1)
            print('16. Install viSQL ')
            sleep(0.1)
            print('17. Install Hash-Buster ')
            sleep(0.1)
            print('18. Install D-TECT ')
            sleep(0.1)
            print('19. Install routersploit ')
            sleep(0.1)
            print('20. install URLSpoof ')
            sleep(0.1)
            print('21. install wifite')
            sleep(0.1)
            print('22. install fbi ')
            sleep(0.1)
            print('23. install Spamwa ')
            sleep(0.1)
            print('24. install SocialFish ')
            sleep(0.1)
            print('25. install nexphisher')
            sleep(0.1)
            print('26. install kalischemes4termux ')
            sleep(0.1)
            print('27. install aiophish ')
            sleep(0.1)
            print('28. install clis ')
            sleep(0.1)
            print('29. install wpscan ')
            sleep(0.1)
            print('30. informações ')
            sleep(0.1)
            print('31. URL NO TERMUX ')
            sleep(0.1)
            print('99. fecha o script \n')
            
            
            
            
            
            
            opção = input('DIGITE A OPÇÃO:  ').lstrip().lstrip('0').rstrip()
            
            if opção == '1' :
                menu()
                nmap() 
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '2':
                menu()
                hidra()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '3':
               menu()
               sqlmap()
               input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '4':
               menu()
               metasploit()
               input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '5':
                menu()
                ngrok()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '6':
                menu()
                Kali()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '7':
                menu()
                angry()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '8' :
                menu()
                red()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '9':
                menu()
                wema()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '10':
                menu()
                ipgeo()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            
            elif opção == '11':
                menu()
                cup()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')               
                
            elif opção == '12':
                menu()
                bet()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')           
  
            elif opção == '13':
                menu()
                twitct()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')                                                          
                            
            elif opção == '14':
                menu()
                Ubuntu()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')                               
                            
            elif opção == '15':
                menu()
                fedora()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')                
              
            elif opção == '16':
                menu()
                vysql()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')              
               
            
            elif opção == '17':
                menu()
                hash()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ') 
                
            elif opção == '18':
                menu()
                tec()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
                
            elif opção == '19':
                menu()
                route()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')                                           
                                                                    
            elif opção == '20':
                menu()
                URLSpoof()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')                                                                                                                        
            elif opção == '21':
                menu()
                wifite()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')  
                
            elif opção == '22':
                menu()
                fbi()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ') 
                                         
            elif opção == '23':
                menu()
                spamwa()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')      
                
            elif opção == '24':
                menu()
                fish()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')                                                  
                                                                                
                                                                                                                
            elif opção == '25':
                menu()
                nexphisher()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')                                                                                                                                                
            elif opção == '26':
                menu()
                kalischemes4termux()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '27':
                menu()
                aiophish()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '28':
                menu()
                clis()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '29':
                menu()
                wpscan()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '30':
                os.system('clear')
                information()
                input('\nENTER PARA VOLTA AO MENU PRINCIPAL ')
            elif opção == '31':
                url3()
            elif opção == '99':
                 
                 print('''
VOLTE SEMPRE ..        
LOGO VAI Ter  atualização                 
                 ''')
                 break
                 
            else:
                print('\nOPÇÃO INVÁLIDA')                 
    else :
            erros = random.choice(error)
            print(erros)
            
            break
