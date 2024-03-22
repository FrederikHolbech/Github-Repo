n = int(input())
line = input() 
numbers = [num for num in line.split()]
tal = []
for bror in numbers:
    tal.append(int(bror))
print(sum(tal))