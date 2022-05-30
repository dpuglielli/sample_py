"""_summary_
"""
from sample_py.arith import basic


def test_add():
    """_summary_"""
    basic_math = basic.Basic()
    assert basic_math.add(1, 2) == 3


def test_subtract():
    """_summary_"""
    basic_math = basic.Basic()
    assert basic_math.subtract(1, 2) == -1
