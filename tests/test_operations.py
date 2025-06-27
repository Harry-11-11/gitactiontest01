from scr.math_operation import add,sub 


def test_add(): 
    assert add(2,4)==6 
    assert add(1,3)==4 


def test_sub(): 
    assert sub(5,3)==2 
    assert sub(8,4)==4 
    assert sub(-10,10)==0      