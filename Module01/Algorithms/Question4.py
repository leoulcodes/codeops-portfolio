#  A Meera array is defined to be an array containing only numbers as its elements and forall n values in the array, the value n*2 is not in the array. So [3, 5, -2] is a Meera array because 3*2, 5*2 or 2*2 are not in the array. But [8, 3, 4] is not a Meera array because 2*4=8 and both 4 and 8 are elements found in the array. Write a function that takes an array of numbered elements and prints “I am a Meera array” in the console if its array does NOT contain n and also n*2 as value. Otherwise, the function prints “I am NOT a Meera array”
#       ○ Test 1: checkMeera([10, 4, 0, 5]) outputs “I am NOT a Meera array” because 5 * 2 is 10
#       ○ Test 2: checkMeera([7, 4, 9]) outputs “I am a Meera array”
#       ○ Test 1: checkMeera([1, -6, 4, -3]) outputs “I am NOT a Meera array” because -3 *2 is -6 

def checkMeera(arr):
    list = set(arr)
    for i in list:
        if i !=0 and i*2 in list:
            print("Not a Meera array")
            return
    print("Meera array")

# checkMeera([10,5,9])
checkMeera([1, -6, 4, -3]) 

# def checkMeera(arr):
#     # Convert to a set for O(1) lookups
#     num_set = set(arr)
    
#     # Iterate through the array to check the Meera condition
#     for n in arr:
#         # Avoid matching 0 with itself (0 * 2 = 0) unless there are multiple zeros, 
#         # but standard Meera array definitions look for distinct n and 2n pairs.
#         if n != 0 and (n * 2) in num_set:
#             print("I am NOT a Meera array")
#             return
            
#     print("I am a Meera array")

# # --- Test Cases ---
# checkMeera([10, 4, 0, 5])      # Output: I am NOT a Meera array (5 * 2 = 10)
# checkMeera([7, 4, 9])          # Output: I am a Meera array
# checkMeera([1, -6, 4, -3])     # Output: I am NOT a Meera array (-3 * 2 = -6)