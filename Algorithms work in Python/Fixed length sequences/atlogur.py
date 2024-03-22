def read_input():
    """
    Takes input()

    returns
        n,
        health as a list of integers,
        strength as a list of integers
    """

    n = int(input().strip())
    health = [0] * n
    strength = [0] * n
    for i in range(n):
        health[i],strength[i] = [int(number) for number in input().strip().split()]
    return n, health, strength

n,health,strength = read_input()

challenger = 0
for i in range(1,n):
    while health[i]>0 and health[challenger]>0:
        health[i] -= strength[challenger]
        if health[i] > 0:
            health[challenger] -= strength[i]
    if health[i] > 0:
        challenger = i
print(challenger+1)
