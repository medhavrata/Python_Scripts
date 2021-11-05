# Find the missing number in the array

# You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. 
# The input array is not sorted.

# array = [3, 7, 1, 2, 8, 4, 5]
# n = 8 missing number = 6

# I think runtime compexity is O(n); need to confirm once

def find_missing(array, number):
    #array.sort()
    test_list = []
    for num in range(1, number + 1):
        test_list.append(num)

    for value in test_list:
        if value not in array:
            return value


            

