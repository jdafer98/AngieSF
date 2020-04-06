import sys
sys.path.append('/home/travis/build/jdafer98/AngieSF/angieps')


from angie_colors import AngieColors
from angie_task import AngieTask
from port_scanner import PortScanner
from mole import Mole

## AngieTask

def test_task_se_genera_con_datos_correctos():
    test_pass = False
    example_ip = "192.168.1.1"
    example_port = 80
    t = AngieTask(example_port, example_ip)

    if t.get_ip() == example_ip and t.get_port() == example_port:
        test_pass = True

    assert test_pass

def test_las_id_son_distintas_y_consecutivas():
    test_pass = False
    n_tasks = 5
    example_ip = "192.168.1.1"
    example_port = 80

    task_list = []
   
    for i in range(1,n_tasks+1):
        a = AngieTask(example_ip,example_port)
        task_list.append(a.get_id())

    test_pass = task_list == list(range(1,n_tasks+1))
    assert test_pass

## AngieMole

def test_scan_port():
    ip = '127.0.0.1'
    port = 80

    test_pass = False
    r = Mole.scan_port(ip,port,False)

    if not r[1] and r[0] == port:
        test_pass = True

    assert test_pass

def test_ping():
    host = 'www.google.es'
    assert Mole.ping(host)
