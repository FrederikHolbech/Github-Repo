def read_input():
    """
    Takes input()

    returns
        n,
        lectures as a list of integers
    """

    n = input().strip()

    lectures = input().strip()
    lectures = [int(lecture) for lecture in lectures]
    return int(n), lectures

n, lectures = read_input()

awake_counter = 0
for index,machine in enumerate(lectures):
    if 1 in lectures[max(index-2,0):index+1]:
        awake_counter += 1
print(awake_counter)