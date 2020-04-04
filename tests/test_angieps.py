import sys
sys.path.append("../angieps/ejemplo")
import ejemplo


def test_se_crean_todos_los_campos():
    
    test_pass = ejemplo.ejemplo()
    assert test_pass
