#Registrarse en URLScan.io
import requests
import json
import argparse
import xlsxwriter as xls
import pyautogui, subprocess, time
import os
import logging
import socket
from bs4 import BeautifulSoup 

parser = argparse.ArgumentParser()
parser.add_argument('--api', required = True, help = "Api Key")
parser.add_argument('--url', required = True, help = "URL")
parser.add_argument('--ip', required = True, help = "Ip")
parser.add_argument('--port', required = True, help = "Port to Scan")
parser.add_argument('--process', required = True, help = "Start or Stop Service")
parser.add_argument('--service', required = True, help = "Service to action")
args = parser.parse_args()

#PowerShell
if args.process == "Start-Service":
    command=args.process
    ps="powershell -Command "+ args.process +" "+ args.service
    rsp=subprocess.check_output(ps)
    service_s="is Running"
else:    
    command=args.process#Example: Get-Command
    ps="powershell -Command "+ command + " " + args.service
    rsp=subprocess.check_output(ps)
    service_s="is Stopped"

#PortScan
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t_IP = socket.gethostbyname(args.ip)

def port_scan(port):
    try:
        s.connect((t_IP, port))
        return True
    except:
        return False

if port_scan(args.port):
    port_r='Port ' + args.port + ' is open'
else:
    port_r='Port ' + args.port + ' is close'

#Web Scraping for all links
with open('data.txt', 'w') as f:
    URL = "http://"+args.url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        f.write(a_href["href"] + "\n")

#Api a URLScan
headers = {'API-Key': args.api ,'Content-Type':'application/json'}
#headers['API-Key']=args.api
data = {"url": args.url, "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
r=response.json()
rs=str(response)
report=xls.Workbook('report.xlsx')
#Establecimiento del tamaño de las celdas
worksheet=report.add_worksheet()
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 35)
worksheet.set_column('D:D', 40)
worksheet.set_column('E:E', 20)
worksheet.set_column('F:F', 30)
#Cabecera
worksheet.write('A1','Codigo de Respuesta')
worksheet.write('B1','URL')
worksheet.write('C1','Envio')
worksheet.write('D1','UUID')
worksheet.write('E1','Visibilidad')
worksheet.write('F1','Puerto')
worksheet.write('A4','Service')
worksheet.write('B4','Status')
#Informacion del Reporte
worksheet.write('A2',rs)
worksheet.write('B2',r['url'])
worksheet.write('C2',r['message'])
worksheet.write('D2',r['uuid'])
worksheet.write('E2',r['visibility'])
worksheet.write('F2',port_r)
worksheet.write('A5',args.service)
worksheet.write('B5',service_s)
report.close()

simp_path = 'report.xlsx'
abs_path = os.path.abspath(simp_path)
pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite(abs_path)
time.sleep(1)
pyautogui.press('enter')

time.sleep(4)
simp_pathx = 'data.txt'
abs_pathx = os.path.abspath(simp_pathx)
pyautogui.press("win")
time.sleep(1)
pyautogui.typewrite(abs_pathx)
time.sleep(1)
pyautogui.press('enter')

time.sleep(4)
im = pyautogui.screenshot()
im.save(r'ss.png')
simp_paths = 'ss.png'
abs_paths = os.path.abspath(simp_paths)
time.sleep(2)
pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite(abs_paths)
time.sleep(1)
pyautogui.press('enter')
