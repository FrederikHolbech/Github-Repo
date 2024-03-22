def read_input():
    """
    Takes input()

    returns
        k,
        numbers as a list of integers
    """

    _ , k = input().strip().split(" ")

    numbers = input().strip().split(" ")
    numbers = [int(num) for num in numbers]
    return int(k), numbers

k, numbers = read_input()
i = [str(i) for i in numbers[k-1::k]]
print(" ".join(i))