import sys
sys.path.append('/home/travis/build/jdafer98/AngieSF/angiesn')

from sniffer import Sniffer

## AngieTask

def test_se_detectan_interfaces():
    test_pass = False
    sn = Sniffer()
    res = []

    res = sn.detect_ifaces()
    
    if res:
        test_pass = True

    assert test_pass


def test_seleccion_interfaz():
    test_pass = False
    sn = Sniffer()
    if_example = 'example'

    sn.select_iface(if_example)
    test_pass = (sn.selected_iface == if_example)
    assert test_pass
