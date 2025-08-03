import re

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getValue(self):
        val = 0
        ace_count = 0
        for c in self.cards:
            rank = re.match(r'\d+|[JQKA]', c).group()
            if rank in 'JQK':
                val += 10
            elif rank == 'A':   
                val += 11
                ace_count += 1
            else:
                val += int(rank)
        while val > 21 and ace_count > 0:
                val -= 10
                ace_count -= 1
        return val
    
    def has_usable_ace(self):
        val = 0
        ace_count = 0
        for c in self.cards:
            rank = re.match(r'\d+|[JQKA]', c).group()
            if rank in 'JQK':
                val += 10
            elif rank == 'A':
                val += 11
                ace_count += 1
            else:
                val += int(rank)
        while val > 21 and ace_count > 0:
            val -= 10
            ace_count -= 1
        return ace_count > 0
    
    def reset(self):
        self.cards = []

    