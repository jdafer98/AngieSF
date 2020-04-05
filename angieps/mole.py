import os
import threading
import socket
from datetime import datetime

class Mole(threading.Thread):

    """ Clase que define el comportamiento de una hebra que realiza una tarea de escaneo a un puerto especificado 
    
        @param (Integer) port: Puerto objetivo
        @param (string) host: Ip o nombre de dominio del host objetivo.
        @param (boolean) dn: Verdadero si el argumento host es un nombre de dominio. Falso en caso contrario
    
    
    """

    def __init__(self, f,a): 
        super().__init__(target=f,args=a)
        self.verbose = False
    
    def set_verbose(self,v):
        self.verbose = v


    def scan_port(ip,port,v):    

        exit_value = False
        if v:
            print(AngieColors.DEFAULT)   


        if ip != None:

            

            if v:
                print(AngieColors.DEFAULT)
                print("trying " + str(ip) + ":" + str(port) + "..." )

            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                t1 = datetime.now()

                result = sock.connect_ex((ip, port))
                t2 = datetime.now()

                if result == 0:
                    
                    if v:
                        print(AngieColors.OKGREEN)
                        click.echo("port " + str(port) + " is OPEN on host " + str(ip))

                    exit_value = True            
                    sock.close()
                else:
                    
                    if v:
                        print(AngieColors.FAIL)
                        click.echo("port " + str(port) + " is CLOSED on host " + str(ip))
                    exit_value = False


            except socket.timeout as e:
                pass

        else:
            print("debe especificarse una dirección ip del host (--ip). Para más información utilice --help")
        
        return [port, exit_value]

    def ping(host):
        """ Petición ICMP al host especificado como parámetro """
        response = os.system("ping -c 1 " + host + " > /dev/null")
        return response == 0

