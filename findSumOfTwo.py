# Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. 
# Return true if the sum exists and return false if it does not.

# 5 7 1 2 8 4 3
# Target Sum 10
# 7+3=10, 2+8=10
# Target Sum 19 No 2 values sum up to 19

def find_sum_of_two(array, val):
    """ Find out of if sum of any two value of array is equal to input 'val' """
    found_value = []
    for a in array:
        if val - a in found_value:
            return True
        found_value.append(a)
    return False
