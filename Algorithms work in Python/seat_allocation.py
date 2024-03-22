from itu.algs4.sorting.max_pq import MaxPQ

class Party:
    def __init__(self,votes,partyid):
        self.votes = votes
        self.partyid = partyid
        self.seats = 0
        self.quotient = self.votes / (self.seats+1)

    def addseat(self):
        self.seats += 1
        self.quotient = self.votes / (self.seats+1)

    def __lt__(self, other):
        return self.quotient < other.quotient
    

n,m = [int(value) for value in input().strip().split(" ")]
quotients = MaxPQ()
parties = []
for i in range(n):
    party = Party(int(input()), i)
    parties.append(party)
    quotients.insert(party)

for _ in range(m):
    party = quotients.del_max()
    party.addseat()
    quotients.insert(party)

for party in parties:
    print(party.seats)