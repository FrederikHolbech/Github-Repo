n = int(input())
words = [input().strip() for _ in range(n)]
hvert_andet_ord = [bror for i, bror in enumerate(words) if i % 2 == 0]
for resultat in hvert_andet_ord:
    print(resultat)