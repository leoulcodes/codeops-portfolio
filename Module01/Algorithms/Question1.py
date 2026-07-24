# Question 1 
# Given an array of numbers, write a function that prints in the console another arraywhich contains all the even numbers in the original array, which also have even indexes only.
#       ○ Test 1: getOnlyEvens([1, 2, 3, 6, 4, 8]) prints [ 4]
#       ○ Test 2: getOnlyEvens([0, 1, 2, 3, 4]) prints [0, 2, 4]


def getonlyevens(nums):
    evensonly = []
    for i in range(len(nums)):
        if i % 2 ==0 and nums[i] % 2 == 0:
            evensonly.append(nums[i])

    print(evensonly)

getonlyevens([1,2,3,6,4,8])
getonlyevens([0, 1, 2, 3, 4])