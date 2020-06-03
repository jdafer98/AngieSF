import sys
sys.path.append('/home/travis/build/jdafer98/AngieSF/angiecr')

from crawler import Crawler

def test_custom_set_path():
    cr = Crawler()
    example = "abc"

    cr.set_custom_set_path(example)
    
    assert cr.custom_set_path == example

def test_custom_dict_path():
    cr = Crawler()
    example = "abc"

    cr.set_custom_dict_path(example)
    
    assert cr.custom_dict_path == example

def test_isFixed():
    cr = Crawler()
    example = "abc"

    cr.set_isFixed(example)
    
    assert cr.isFixed == example

def test_set_url():
    cr = Crawler()
    example = "abc"

    cr.set_url(example)
    
    assert cr.url == example

def test_set_nthreads():
    cr = Crawler()
    example = 5

    cr.set_nthreads(example)
    
    assert cr.nthreads == example

def test_size():
    cr = Crawler()
    example = 5

    cr.set_size(example)
    
    assert cr.size == example

def test_select_sets():
    cr = Crawler()
    example = 5

    cr.select_sets(True)
    
    assert cr.minus_selected == True

def test_read_custom_set():
    assert True



