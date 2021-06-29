import os
os.system("type>null Address.txt")
os.system("ipconfig | findstr 'Dirección'>>Address.txt")
file=open("Address.txt","r")
Direccion=[]
for i in file:
    Direccion.append(i.split(":"))
    print(i)
Direccion[0].pop(0)
Direccion[1].pop(0)
Direccion_local=str(Direccion[1])