import time
import random
import os
import signal
from datetime import datetime
logfile = open('log.txt', 'r+')
definitions = open('definitionsHtml.txt', 'r')
rights = open('rights.txt', 'r')
loglines = logfile.readlines()
global deflines
deflines = definitions.readlines()


rlines = rights.readlines()
rline1 = rlines[0]
rline2 = rlines[1]
rline3 = rlines[2]
noRun = random.randrange(1, 100)
if noRun == 50:
    print()
    print("The program just don't like you right now. It no want to run :P")
    print()
    os.kill(os.getpid(), signal.SIGTERM)


def Start():
    logfile.write('Session started at: ' + datetime.now().ctime() + '\n\n')
    print(logfile.readlines())
    print()
    print("This tool was made to help programmers, like myself,")
    print("with HTML tags. It takes your input, say you typed")
    print("<div>, it would give you an accurate description of")
    print("that tag and a list of its uses.")
    print()
    print("Guest users please login as 'Guest'")
    print()
    print("(Remember, type BASE tags -<p>- ONLY)")
    print()

    while True:
        Username = input("Username: ")
        if Username == 'Guest':
            Username = 'Guest'
            logfile.write('User: Guest' + '\n\n')
            print()
            print('CHECKING..')
            time.sleep(2)
            print('''
  Welcome, Guest!
''')
            Block()
            break
        elif Username == '/admin061503':
            Username = "Admin Chase"
            logfile.write('User: Admin Chase' + '\n\n')
            Pass = input("Password: ")
            if Pass == '*************':
                Username = 'Admin Chase'
                logfile.write('logged in!' + '\n\n')
                print()
                print('CHECKING..')
                time.sleep(2)
                print('''
  Welcome, Admin Chase!
''')
                Block()
                break
            else:
                print()
                print("The Input is Incorrect")
                print()
                logfile.write('Wrong Password has been inputed.' + '\n\n')
        else:
            print()
            print('CHECKING..')
            time.sleep(2)
            print('''
Incorrect Username
''')


def Block():
    Input = input("TAG: ")
    if Input == 'exit':
        answerexit = input("Are you sure? ")
        if answerexit == 'yes':
            logfile.write('session ended at: ' + datetime.now().ctime() + '\n')
            logfile.close()
            print()
            print("SHUTTING DOWN..")
            print()
            time.sleep(2)
            os.kill(os.getpid(), signal.SIGTERM)
        elif answerexit == 'no':
            print()
            print("SHUTDOWN ABORTED..")
            print()
            Block()
    elif Input == 'restart':
            print()
            print("RESTARTING..")
            print()
            time.sleep(1.5)
            Start()
    elif Input == '':
        print()
        print("Please enter a tag or command.")
        print()
        Block()
    elif Input == 'credits':
        print()
        print(rline1)
        print(rline2)
        print(rline3)
        print()
        Block()
    elif Input == '<!DOCTYPE html>':
        print()
        print(deflines[0])
        time.sleep(1)
        Block()
    elif Input == '<p>':
        print()
        print(deflines[1], deflines[2], deflines[3], deflines[4], deflines[5])
        print(deflines[6], deflines[7], deflines[8])
        print()
        time.sleep(1)
        Block()
    elif Input == '<h>':
        print()
        print(deflines[9], deflines[10], deflines[11], deflines[12])
        print(deflines[13], deflines[14], deflines[15], deflines[16])
        print()
        time.sleep(1)
        Block()
    elif Input == '<a>':
        print()
        print(deflines[17], deflines[18], deflines[19], deflines[20])
        print(deflines[21], deflines[22], deflines[23], deflines[24])
        print(deflines[25])
        print()
        time.sleep(1)
        Block()
    elif Input == '<div>':
        print(deflines[26], deflines[27], deflines[28], deflines[29])
        print(deflines[30], deflines[31], deflines[32], deflines[33])
        print(deflines[34])
        time.sleep(1)
        Block()
    elif Input == '<link>':
        print(deflines[35], deflines[36], deflines[37])
        time.sleep(1)
        Block()
    elif Input == '<br>':
        print(deflines[38], deflines[39], deflines[40], deflines[41])
        time.sleep(1)
        Block()
    elif Input == '<button>':
        print(deflines[42], deflines[43], deflines[44])
        time.sleep(1)
        Block()
    elif Input == '<iframe>':
        print(deflines[45], deflines[46])
        time.sleep(1)
        Block()
    else:
        print()
        print('''The tag or command you entered is Not Recognized or is not yet
supported by this tool.''')
        print()
        Block()
Start()
