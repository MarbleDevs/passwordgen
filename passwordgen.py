import secrets
import time
import string
import sys
startmenu ='''
                                                                                 .o8                                   
                                                                                "888                                   
oo.ooooo.   .oooo.    .oooo.o  .oooo.o oooo oooo    ooo  .ooooo.  oooo d8b  .oooo888   .oooooooo  .ooooo.  ooo. .oo.   
 888' `88b `P  )88b  d88(  "8 d88(  "8  `88. `88.  .8'  d88' `88b `888""8P d88' `888  888' `88b  d88' `88b `888P"Y88b  
 888   888  .oP"888  `"Y88b.  `"Y88b.    `88..]88..8'   888   888  888     888   888  888   888  888ooo888  888   888  
 888   888 d8(  888  o.  )88b o.  )88b    `888'`888'    888   888  888     888   888  `88bod8P'  888    .o  888   888  
 888bod8P' `Y888""8o 8""888P' 8""888P'     `8'  `8'     `Y8bod8P' d888b    `Y8bod88P" `8oooooo.  `Y8bod8P' o888o o888o 
 888                                                                                  d"     YD                        
o888o                                                                                 "Y88888P'                        
                                                                                                                       
'''
def start():
    global number
    print(startmenu)
    time.sleep(3)
    print("Put in a 0 if you want to generate infinitely")
    time.sleep(2)
    number = int(input("How much passwords do you need?"))

def gen():
        global password
        global characters
        characters = string.ascii_letters + string.digits + string.punctuation
        
        with open('passwords.txt', 'w') as a:
            for _ in range(number):
                password = ''.join(secrets.choice(characters) for _ in range(21))
                print(f"{password}\n",file=a)

def gen_infinitely():
    characters = string.ascii_letters + string.digits + string.punctuation
    with open('passwords.txt', 'w') as a:
        while True:
            password = ''.join(secrets.choice(characters) for _ in range(21))
            print(f"{password}\n",file=a)
start()
gen()
if number == 0:
    while True:
        gen_infinitely()
else:
    print("Finished please consider giving a ☆ to the repo")
    sys.exit

            