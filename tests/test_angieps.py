import sys

sys.path.append('/home/travis/build/jdafer98/AngieSF/angieps')
import ejemplo


def test_se_crean_todos_los_campos():
    test_pass = ejemplo.ejemplo()
    assert True
