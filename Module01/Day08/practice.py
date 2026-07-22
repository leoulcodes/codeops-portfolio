
# day08/practice.py

import random



# 1. Recursive Functions


print("\n--- Recursive Sum & Countdown ---")

def total(nums):
    # Base case
    if not nums:
        return 0

    # Recursive case
    return nums[0] + total(nums[1:])


def count_down(n):
    if n <= 0:
        return

    print(n)
    count_down(n - 1)


nums = [1, 2, 3, 4, 5]

print("Sum:", total(nums))
count_down(5)




# 2. Binary Search (O(log n))


print("\n--- Binary Search ---")

def binary_search(items, target):

    left = 0
    right = len(items) - 1

    while left <= right:

        mid = (left + right) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


balances = [100, 200, 300, 400, 500]

print("Index of 300:", binary_search(balances, 300))
print("Index of 999:", binary_search(balances, 999))




# 3. Merge Sort (O(n log n))


print("\n--- Merge Sort ---")

def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


random_list = [
    random.randint(1, 100)
    for _ in range(10)
]

sorted_list = merge_sort(random_list)

print("Original:", random_list)
print("Merge Sorted:", sorted_list)
print("Python Sorted:", sorted(random_list))




# 4. Sort with Key


print("\n--- Sort with Key ---")

accounts = [
    ("Abebe", 500),
    ("Sara", 1500),
    ("Miki", 800),
]

# Sort by balance descending
sorted_accounts = sorted(
    accounts,
    key=lambda x: x[1],
    reverse=True
)

print(sorted_accounts)




# 5. Two Pointers (O(n))


print("\n--- Two Pointers ---")

def has_pair(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return False


nums = [1, 2, 3, 4, 6, 8]

print("Has pair (10):", has_pair(nums, 10))
print("Has pair (15):", has_pair(nums, 15))