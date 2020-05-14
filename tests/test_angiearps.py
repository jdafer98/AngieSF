import sys
sys.path.append('/home/travis/build/jdafer98/AngieSF/angiearpf')

from spoofer import Spoofer


def test_set_router_ip():
    test_pass = False
    sp = Spoofer()
    s = "127.0.0.1"

    sp.set_router_ip(s)

    test_pass = sp.router_mac == s

    assert test_pass

def test_set_target_ip():
    test_pass = False
    sp = Spoofer()
    s = "127.0.0.1"

    sp.set_target_ip(s)

    test_pass = sp.target_mac == s

    assert test_pass

def test_spoof():
    test_pass = False
    sp = Spoofer()
    s = "127.0.0.1"

    sp.set_router_ip(s)
    sp.set_target_ip(s)
    sp.spoof()

    assert True

def test_req_mac():
    sp = Spoofer()
    s = "127.0.0.1"
    
    sp.request_mac(s)

    assert True


