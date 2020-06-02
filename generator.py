#created by Ph3nX-Z : https://github.com/Ph3nX-Z
ip_re=""
import time
def read(): #read file (first line)
     read=open(name, "r") 
     data=read.read()
     read.close()
     return data

choice=int(input("The attacker ip is in a file (1) or you want to put it manually (2) ? :"))
if choice==1:
    name=input("Name of the file (with extension):")
    temp=read()
else:
    temp=input("Attacker Ip :")


for numero in temp:
    cryptlist=["$","#","*","-","@","%","?","!","+"]
    if numero != "." :
        numero=cryptlist[int(numero)-1]
        ip_re+=numero
    else:
        ip_re+=numero

        
if choice!=1:
    print("your crypted ip is : ",ip_re)
    time.sleep(7)
    
else:
    write_temp=open("ip.txt","w")
    write_temp.write(ip_re)
    write_temp.close()
