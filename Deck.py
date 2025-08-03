import random
class Deck:
    def __init__(self):
        self.cards = ['A♠️','2♠️','3♠️','4♠️','5♠️','6♠️','7♠️','8♠️','9♠️','10♠️','J♠️','Q♠️','K♠️',
                      'A♥️','2♥️','3♥️','4♥️','5♥️','6♥️','7♥️','8♥️','9♥️','10♥️','J♥️','Q♥️','K♥️',
                      'A♦️','2♦️','3♦️','4♦️','5♦️','6♦️','7♦️','8♦️','9♦️','10♦️','J♦️','Q♦️','K♦️',
                      'A♣️','2♣️','3♣️','4♣️','5♣️','6♣️','7♣️','8♣️','9♣️','10♣️','J♣️','Q♣️','K♣️']  *6
        self.shuffle() 
        
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None
    
    def reset(self):
        self.__init__()