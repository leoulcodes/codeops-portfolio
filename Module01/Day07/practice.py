
# day07/practice.py

import time
from collections import deque
import random


# =====================================================
# 1. Name the Big-O
# =====================================================

# 1. List index lookup
# Big-O: O(1)
# Reason: Accessing a list element by index jumps directly
# to the memory location.

numbers = [10, 20, 30, 40]
print(numbers[2])


# 2. Single loop
# Big-O: O(n)
# Reason: The loop runs once for every item in the list.

for number in numbers:
    print(number)


# 3. Nested loop
# Big-O: O(n^2)
# Reason: For every item, we go through all items again.

for i in numbers:
    for j in numbers:
        print(i, j)


# 4. Dictionary lookup
# Big-O: O(1)
# Reason: Dictionary uses hashing, so lookup is constant time
# on average.

accounts = {"A001": "Abebe"}
print(accounts["A001"])


# 5. Binary search
# Big-O: O(log n)
# Reason: Each step cuts the search space in half.


# =====================================================
# 2. List vs Dict Lookup Timing
# =====================================================

print("\n--- List vs Dictionary Lookup ---")


# Create 100,000 fake account numbers

account_numbers = [
    f"ACC{i}"
    for i in range(100000)
]


account_dict = {
    number: True
    for number in account_numbers
}


target = "ACC99999"


# List search

start = time.time()

target in account_numbers

list_time = time.time() - start


# Dictionary search

start = time.time()

target in account_dict

dict_time = time.time() - start


print("List lookup time:", list_time)
print("Dictionary lookup time:", dict_time)



# =====================================================
# 3. Stack Implementation
# =====================================================

print("\n--- Stack ---")


class Stack:

    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.items:
            return None

        return self.items.pop()


    def peek(self):
        if not self.items:
            return None

        return self.items[-1]



names = [
    "Abebe",
    "Sara",
    "Miki",
    "Liya"
]


stack = Stack()


for name in names:
    stack.push(name)


reversed_names = []


while stack.items:
    reversed_names.append(stack.pop())


print(reversed_names)



# =====================================================
# 4. Queue using deque
# =====================================================

print("\n--- Bank Queue ---")


bank_queue = deque()


customers = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
    "Customer 4",
    "Customer 5"
]


# Enqueue

for customer in customers:
    bank_queue.append(customer)



# Serve customers

while bank_queue:
    customer = bank_queue.popleft()

    print(
        f"Serving {customer}"
    )



# =====================================================
# 5. Singly Linked List
# =====================================================

print("\n--- Linked List ---")


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None



    def push_front(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node



    def print_all(self):

        current = self.head

        while current:

            print(current.data)

            current = current.next



linked_list = LinkedList()


linked_list.push_front("Account C")
linked_list.push_front("Account B")
linked_list.push_front("Account A")


linked_list.print_all()