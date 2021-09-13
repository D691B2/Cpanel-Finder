#### LIBRARYS ####
import sys
import requests
import time
import os

############ Function Write By Time ############
def runtext(s):
        for words in s + '\n':
                sys.stdout.write(words)
                sys.stdout.flush()
                time.sleep(10. / 200)

############################### USING TOOL ###############################
os.system("color E")
runtext('''
Welcome Guys :)
By This Tool You Can found The admin control panel
Using is So Easy Just Put The Link of WebSite with Protocol (HTTP * HTTPS):
Example : https://google.com .
Starting ...
''')

########################### STARTING ###########################
os.system("color 9")
print('''
     _       _           _       _____ _           _           
    / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ 
   / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|
  / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |   
 /_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_|                                                                
''')
runtext ("""
                      ####################
                      ##  BY Derradj.I  ##
                      ####################
""")

time.sleep(3.14) # Wait 3.14 seconds #

File = open('Test.txt' , 'r') # we have in this file *txt* a list of Cpanels #

Web_Site = input ("Put the site here : ") # User Put The WebSite Here #

def Response_200():
        os.system("color A")
        print("FOUND >>>" , Web_Site , "/" , admin , "\n")
        time.sleep(1)

def Response_404():
        os.system("color 4")
        print("NOT FOUND >>>" , admin , "\n")

def Exit():
        os.system("cls")
        print ("** mayBe there are A problem ON the server or Your internet **")
        runtext ('Try Again ... ')
        runtext ('exit ... ')
        time.sleep (0.5)
        os.system("exit")

for admin in File:
    
    response = requests.get(Web_Site + "/" + admin)
    time.sleep(0.01)

    if response.status_code == 200:
        Response_200()

    elif response.status_code == 404:
        Response_404()

    else:
        Exit()

input('Press Enter to Close ... ')
    
