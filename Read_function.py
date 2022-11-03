import imaplib
import sys
import email
import argparse
import re
import os
from email.header import decode_header
from os import path



RE_EMAIL = re.compile('[^@]+@[^@]+\.[a-zA-Z]{2,}')

def email_type(value):
    if not RE_EMAIL.match(value):
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid email")
    return value

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', type= email_type)
    parser.add_argument('--password', type= str, help= 'Escriba su token/contraseña')
    args = parser.parse_args()
    sys.stdout.write(str(read_mail(args)))
  


def read_mail(args):
    mail = imaplib.IMAP4_SSL(host= 'imap.gmail.com', port= 993)
    mail.login(args.user, args.password)
    status, mensajes = mail.select("INBOX")
    x = 3
    mensajes = int(mensajes[0])
    for i in range(mensajes, mensajes - x, -1):
#     # Obtener el mensaje
        try:
            res, mensaje = mail.fetch(str(i), "(RFC822)")
        except:
            break
    for respuesta in mensaje:
        if isinstance(respuesta, tuple):
            # Obtener el contenido
            mensaje = email.message_from_bytes(respuesta[1])
            # decodificar el contenido
            subject = decode_header(mensaje["Subject"])[0][0]
            if isinstance(subject, bytes):
                # convertir a string
                subject = subject.decode()
            # si el correo es html
            if mensaje.is_multipart():
                # Recorrer las partes del correo
                for part in mensaje.walk():
                    # Extraer el contenido
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # el cuerpo del correo
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # Mostrar el cuerpo del correo
                        pass
                    elif "attachment" in content_disposition:
#                         # download attachment
                        nombre_archivo = part.get_filename()
                        if nombre_archivo:
                            if not os.path.isdir(subject):
                                # crear una carpeta para el mensaje
                                os.mkdir(subject)
                            ruta_archivo = os.path.join(subject, nombre_archivo)
                            # download attachment and save it
                            open(ruta_archivo, "wb").write(part.get_payload(decode=True))
            else:
                # contenido del mensaje
                content_type = mensaje.get_content_type()
                # cuerpo del mensaje
                body = mensaje.get_payload(decode=True).decode()
        
    mail.close()
    mail.logout()
if __name__ == '__main__':
    main()