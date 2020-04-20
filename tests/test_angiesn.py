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
