from findSumOfTwo import find_sum_of_two

def test_findSumOfTwo_1():
    """ This is the test function to check the sum of two number and match with the input number """
    assert True == find_sum_of_two([5,7,1,2,8,4,3], 10)

def test_findSumOfTwo_2():
    """ This is the test function to check the sum of two number and match with the input number """
    assert False == find_sum_of_two([5,7,1,2,8,4,3], 19)