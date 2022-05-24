from sample_py.sample_py.arith import basic

def test_add():
    b = basic.Basic()
    assert b.add(1, 2) == 3

def test_subtract():
    b = basic.Basic()
    assert b.subtract(1, 2) == -1

