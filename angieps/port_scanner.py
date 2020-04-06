import socket
from datetime import datetime
import ipaddress
from angie_task import AngieTask
from mole import Mole
import time
from angie_colors import AngieColors 
from datetime import datetime
from queue import Queue

class PortScanner:

    def __init__(self,host,ini_port,end_port,dn=False):
        self.task_queue = Queue()
        self.results = []
        self.host = host
        self.ini_port = ini_port
        self.end_port = end_port
        self.nmoles = 5
        self.dn = dn
        self.verbose = False
        self.sweep_mode = False

    def init_queue(self):

        default_value = [False,0]
        qq = self.lookup()
        if not self.sweep_mode:

            for i in range(self.ini_port, self.end_port+1):
                t = AngieTask(i,qq)
                self.task_queue.put(t)
                self.results.append(default_value)
        else:
            ipmask = self.parse_ipmask(qq)
            ipbase = ipmask[0]
            mask = ipmask[1]
                         
            my_ipbase = ipaddress.ip_address(ipbase)

            for i in range(0,2**(32-mask)):
                t = AngieTask(0,str(my_ipbase+i))
                self.task_queue.put(t)
                self.results.append(default_value)
                

    def set_verbose(self,v):
        self.verbose = v

    def set_sweep_mode(self,mm):
        self.sweep_mode = mm

    def fmole(q,results,v,sm): 

        if not sm:
            while not q.empty():
                t = q.get()
                res = Mole.scan_port(t.get_ip(),t.get_port(),v)
                results[t.get_id()] = res
                q.task_done()
        else:
            while not q.empty():
                t = q.get()
                if v:
                    print(t.get_ip())

                res = Mole.ping(t.get_ip())
                results[t.get_id()] = [t.get_ip(),res]
                q.task_done()



    def parse_ipmask(self,ipmask):
        
        split = ipmask.split('/')
        octets = split[0].split('.')
        mask = int(split[1])
        position = 0  

        if mask <= 32 and mask >= 24:
            co = int(octets[3])
            position = 3

        elif mask >= 16:
            co = int(octets[2])
            octets[3] = '0'
            position = 2

        elif mask >= 8:
            co = int(octets[1])
            octets[3] = octets[2] = '0'
            position = 1

        elif mask >= 0:
            co = int(octets[0])
            octets[3] = octets[2] = octets[1] = '0'
            position = 0

        else:
             co = 0

        mask_ones = mask % 8

        mask_final_octet = 0
        for i in range(0,mask_ones):
            mask_final_octet = mask_final_octet + i*2

        mask_final_octet = 256 - mask_final_octet

        octet_result = co & mask_final_octet
        octets[position] = octet_result
        final_ip = str(octets[0]) + '.' + str(octets[1]) + '.' + str(octets[2]) + '.' + str(octets[3])

        return [final_ip, mask]
        

        

    def make_report(self):
        report = []

        for r in self.results:
            if r[1]:
                report.append(r[0])

        return report

    def launch_moles(self):
        for i in range(self.nmoles):
            m = Mole(PortScanner.fmole,(self.task_queue,self.results,self.verbose,self.sweep_mode))
            m.daemon = True
            m.set_verbose(self.verbose)
            m.start()

        self.task_queue.join()

        

    def set_nmoles(self,n):
        self.nmoles = n

    def lookup(self):
        if self.dn:
            ip = socket.gethostbyname(self.host)
        else:
            ip = self.host
       
        return ip

    def begin_scan(self):

        self.init_queue()
        t1 = datetime.now()
        self.launch_moles()
        t2 = datetime.now()
        
        total_time = (t2-t1).total_seconds()
        rep = self.make_report()

        print(AngieColors.DEFAULT + AngieColors.UNDERLINE + "SCAN FINISHED SUCCESSFULLY. TOTAL TIME:" + AngieColors.ENDC + AngieColors.OKBLUE +" "+ "{0:.7f}".format((total_time)) + "s" + AngieColors.DEFAULT)

        print(AngieColors.OKGREEN + "OPEN PORTS: " + str(rep) )

    def begin_sweep(self):
        self.set_sweep_mode(True)

        self.init_queue()
        t1 = datetime.now()
        self.launch_moles()
        t2 = datetime.now()
        
        total_time = (t2-t1).total_seconds()
        rep = self.make_report()

        self.set_sweep_mode(False)

        print(AngieColors.DEFAULT + AngieColors.UNDERLINE + "SWEEP FINISHED SUCCESSFULLY. TOTAL TIME:" + AngieColors.ENDC + AngieColors.OKBLUE +" "+ "{0:.7f}".format((total_time)) + "s" + AngieColors.DEFAULT)

        print(AngieColors.OKGREEN + "HOSTS UP: " + str(rep) )
