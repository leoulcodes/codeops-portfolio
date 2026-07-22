
# day09/registry.py

from collections import deque



# Reuse Account + AccountRegistry from Day08




# 1. Branch Tree (Hierarchy)


class Branch:

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.children = []   # sub-branches


    def add_account(self, account):
        self.accounts.append(account)


    def add_child(self, branch):
        self.children.append(branch)


    # -----------------------------------------
    # Recursive total balance
    # -----------------------------------------
    def total_balance(self):

        # Sum this branch accounts
        total = sum(acc.balance for acc in self.accounts)

        # Add children recursively
        for child in self.children:
            total += child.total_balance()

        return total


# =====================================================
# 2. Transfers Graph (BFS)
# =====================================================

class TransferGraph:

    def __init__(self):
        self.graph = {}   # adjacency list


    def add_edge(self, from_acc, to_acc):

        if from_acc not in self.graph:
            self.graph[from_acc] = []

        self.graph[from_acc].append(to_acc)


    # -----------------------------------------
    # BFS traversal
    # -----------------------------------------
    def bfs(self, start):

        visited = set()
        queue = deque([start])

        reachable = []

        while queue:

            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)
            reachable.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

        return reachable


# =====================================================
# Testing Everything Together
# =====================================================

if __name__ == "__main__":

    # -------------------------------
    # Create accounts
    # -------------------------------
    class Account:
        def __init__(self, owner, number, balance):
            self.owner = owner
            self.account_number = number
            self.balance = balance

    a1 = Account("Abebe", "CBE-1", 1000)
    a2 = Account("Sara", "CBE-2", 2000)
    a3 = Account("Miki", "CBE-3", 1500)
    a4 = Account("John", "CBE-4", 3000)


    # -------------------------------
    # Build Branch Tree
    # -------------------------------
    head = Branch("Head Office")

    region1 = Branch("Region 1")
    region2 = Branch("Region 2")

    branch1 = Branch("Branch 1")
    branch2 = Branch("Branch 2")

    # Structure:
    # Head
    # ├── Region1
    # │   └── Branch1
    # └── Region2
    #     └── Branch2

    head.add_child(region1)
    head.add_child(region2)

    region1.add_child(branch1)
    region2.add_child(branch2)


    # Assign accounts
    branch1.add_account(a1)
    branch1.add_account(a2)

    branch2.add_account(a3)
    branch2.add_account(a4)


    # -------------------------------
    # Recursive total
    # -------------------------------
    print("\n--- Bank Total Balance ---")
    print("Total:", head.total_balance())


    # -------------------------------
    # Build Transfer Graph
    # -------------------------------
    graph = TransferGraph()

    graph.add_edge("CBE-1", "CBE-2")
    graph.add_edge("CBE-1", "CBE-3")
    graph.add_edge("CBE-2", "CBE-4")
    graph.add_edge("CBE-3", "CBE-4")


    # -------------------------------
    # BFS Traversal
    # -------------------------------
    print("\n--- BFS from CBE-1 ---")

    reachable = graph.bfs("CBE-1")

    print("Reachable:", reachable)