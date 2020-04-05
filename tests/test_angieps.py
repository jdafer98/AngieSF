import sys
sys.path.append('/home/travis/build/jdafer98/AngieSF/angieps')


from angie_colors import AngieColors
from angie_task import AngieTask
from port_scanner import PortScanner


## AngieTask

def task_se_genera_con_datos_correctos():
    test_pass = False
    example_ip = "192.168.1.1"
    example_port = 80
    t = AngieTask(example_ip, example_port)

    if t.get_ip() == example_ip and t.get_port() == example_port:
        test_pass = True

    assert test_pass

def las_id_son_distintas_y_consecutivas():
    test_pass = False
    n_tasks = 5
    example_ip = "192.168.1.1"
    example_port = 80

    task_list = []
   
    for i in range(1,n_task+1):
        a = AngieTask(example_ip,example_port)
        task_list.append(a.get_id())

    test_pass = task_list == list(range(1,n_task+1))
    assert test_pass
