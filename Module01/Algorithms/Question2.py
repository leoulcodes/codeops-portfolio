# Question 2
# ● Create a function that takes a two-digit number as an parameter and prints "Ok" inthe console if the given string is greater than its reversed digit version. If not, the function will print "Not ok"
#      ○ Test 1: reverseCompare(72) prints "ok" because 72 > 27
#      ○ reverseCompare(23) prints "Not ok", because 23 is not greater than 32

def reverseCompare(num):

    # Get digits
    normal = num // 10
    reversed = num % 10

    
    reversed_num = reversed * 10 + normal

    
    if num > reversed_num:
        print("Ok")
    else:
        print("Not ok")

reverseCompare(23)