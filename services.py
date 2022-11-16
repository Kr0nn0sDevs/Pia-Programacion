import subprocess

def service(command,services):
    if command == "Start-Service":
        #command=command
        ps="powershell -Command "+ command +" "+ services
        rsp=subprocess.check_output(ps)
        service_s="is Running"
    else:    
        #command=command#Example: Get-Command
        ps="powershell -Command "+ command + " " + services
        rsp=subprocess.check_output(ps)
        service_s="is Stopped"
"""
if __name__ == "__main__":
    command=str(input("Ingrese su comando: "))
    services=str(input("Ingrese el servicio: "))
    
service(command,services)
"""