from missingArrayNumber import find_missing

def test_missingNumber1():
    assert 6 == find_missing([3, 7, 1, 2, 8, 4, 5], 8)

def test_missingNumber2():
    assert 5 == find_missing([3, 1, 2, 4], 5)