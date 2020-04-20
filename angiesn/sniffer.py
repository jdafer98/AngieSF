from scapy.all import *
import os
import keyboard
import threading

class Sniffer:

    def __init__(self):
        self.selected_iface = None
        self.total_rows = []
        self.signal = False
        self.count = 0

    def detect_ifaces(self):
        return os.listdir('/sys/class/net')

    def select_iface(self,i):
        self.selected_iface = i

    def inter(self,x):
        print("PACKET #{}: \n".format(self.count) + x.summary())
        self.count = self.count + 1

    def sniff_pcks(self,n,f):
        self.count = 0
        res = sniff(iface=self.selected_iface,filter=f,prn=lambda x: self.inter(x),stop_filter=lambda x: keyboard.is_pressed('ctrl'))
        return res

    def begin_sniff(self,f):
        print("Sniff empezado. Manten pulsado <ctrl izq> para terminar...\n\n\n")
        if self.selected_iface != None:

            self.total_rows = self.sniff_pcks(1,f=f)

            
            otro_paquete = False
            posibles_respuestas = ["s","S","n","N"]


            si_no = input("¿Quieres analizar un paquete? (s/n)")

            while si_no not in posibles_respuestas:
                si_no = input("Introduce un valor válido (s/n)")
            
            otro_paquete = (si_no == "s" or si_no == "S")

            while otro_paquete:

                paquete_correcto = False
                while not paquete_correcto:
                    try:
                        paquete = int(input("¿Que paquete?  "))      
                    except ValueError:
                        print("Introduce un valor válido.")
                        continue
                    else:
                        paquete_correcto = True

                self.total_rows[paquete].show()

                si_no = input("¿Quieres analizar un paquete? (s/n)")

                while si_no not in posibles_respuestas:
                    si_no = input("Introduce un valor válido (s/n)")
            
                otro_paquete = (si_no == "s" or si_no == "S") 
           

            si_no_pcap = input("¿Quieres guardar la captura en un archivo pcap? (s/n)")

            while si_no not in posibles_respuestas:
                si_no_pcap = input("Introduce un valor válido (s/n)")
            
            pcap = (si_no_pcap == "s" or si_no_pcap == "S") 

            nombre = "angiesn_out.pcap"
                
            if pcap:
                nombre_prov = input("nombre del archivo (por defecto 'angiesn_out.pcap'): ")
                if nombre_prov != '':
                    nombre = nombre_prov
                wrpcap(nombre,self.total_rows)


