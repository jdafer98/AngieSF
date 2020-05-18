import sys
sys.path.append('/home/travis/build/jdafer98/AngieSF/angierp')

from repeater import Repeater

def test_se_detectan_interfaces():
    test_pass = False
    r = Repeater()
    e = "abc"

    r.set_endl(e)

    test_pass = e == r.ENDL
    assert test_pass

def test_read_from_file():
    name = '/home/travis/build/jdafer98/AngieSF/angierp/ehttp'

    r = Repeater()
    q = r.read_from_file(name)

    assert q.find('HTTP') != -1

def test_send_http():
    name = '/home/travis/build/jdafer98/AngieSF/angierp/ehttp'

    test_pass = False
    r = Repeater()
    q = r.read_from_file(name)

    qq = r.send_http(q,'info.cern.ch',80)

    assert qq.find('200') != -1

def test_send_https():
    name = '/home/travis/build/jdafer98/AngieSF/angierp/ehttps'

    test_pass = False
    r = Repeater()
    q = r.read_from_file(name)

    qq = r.send_https(q,'www.youtube.com',443)

    assert qq.find('200') != -1

