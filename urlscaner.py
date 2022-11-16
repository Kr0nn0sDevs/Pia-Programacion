import json
import xlsxwriter as xls
import requests
import re
import pyautogui, os, time

def validar(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if re.match(regex, url):
        urls=url
        return urls
    else:
        urls="http://"+url
        return urls

def analisis(api,urls):
    #Api a URLScan
    headers = {'API-Key': api ,'Content-Type':'application/json'}
    #headers['API-Key']=args.api
    data = {"url": urls, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    r=response.json()
    #rs=str(response)
    return r
    
def report(r):
    report=xls.Workbook('report.xlsx')
    #Establecimiento del tamaño de las celdas
    worksheet=report.add_worksheet()
    worksheet.set_column('A:A', 30)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 40)
    worksheet.set_column('D:D', 40)
    #Cabecera
    #worksheet.write('A1','Codigo de Respuesta')
    worksheet.write('A1','URL')
    worksheet.write('B1','Envio')
    worksheet.write('C1','UUID')
    worksheet.write('D1','Visibilidad')
    #Informacion del Reporte
    #worksheet.write('A2',rs)
    worksheet.write('A2',r['url'])
    worksheet.write('B2',r['message'])
    worksheet.write('C2',r['uuid'])
    worksheet.write('D2',r['visibility'])
    report.close()
    
def auto_open():
    simp_path = 'report.xlsx'
    abs_path = os.path.abspath(simp_path)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite(abs_path)
    time.sleep(1)
    pyautogui.press('enter')
"""    
if __name__ == '__main__':
    api=str(input("Ingrese su api key: "))
    url=str(input("Ingrese la url a escanear: "))

urls=validar(url)
r=analisis(api,urls)
report(r)
auto_open()
"""