from itu.algs4.fundamentals.uf import WeightedQuickUnionUF

def read_input():
    """
    Takes input()

    returns
        n,
        List of operations as tuple of op, s, t
    """

    n, m = input().strip().split(" ")
    operations = []
    for _ in range(int(m)):
        elements = input().strip().split(" ")
        operations.append(tuple(int(element) for element in elements))

    return int(n), operations

def get_index_of_element(family, element):
    for index, family_member in enumerate(family):
        if element in family_member:
            return index
    raise IndexError(f"Could not find {element}")

def do_op(family: WeightedQuickUnionUF, op, s, t):
    if op == 0:
        # Query operation
        print(int(family.connected(s, t)))
    elif op == 1:
        # Union operation
        family.union(s, t)
    elif op == 2:
        # Move operation
        # Save parent
        s_root = family.find(s)
        t_root = family.find(t)
        if s_root != t_root:
            old_parent = family._parent[s]
            family._parent[s] = t_root
            family._size[s_root] -= 1
            family._size[t_root] += 1

            # Since we are only moving one node we need to find any children and connect them to our parent.
            for index, parent in enumerate(family._parent):
                if parent != s:
                    continue

                if old_parent == s:
                    # If the item we move was the root we need to build a new root.
                    old_parent = index
                    family._size[old_parent] = family._size[s]

                family._parent[index] = old_parent

n, operations = read_input()

family = WeightedQuickUnionUF(n)
for op, s, t in operations:
    do_op(family, op, s, t)
