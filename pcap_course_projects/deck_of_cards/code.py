import random 

suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


class Deck:
    
    def __init__(self):
        cards = []
        for x in suits:
            for y in values:
                cards.append(Card(y, x))
        self.cards = cards

    def new_deck(self):
        cards = []
        for x in suits:
            for y in values:
                cards.append(Card(y, x))
        self.cards = cards
        return self.cards

    def shuffle(self):
            random.shuffle(self.cards)
        
    def deal(self):
        if self.cards != []:
            card = self.cards[-1]
            self.cards.remove(card)
            return card.present()
        else:
            return None
    
    def count_remaining(self):
            return len(self.cards)
            
    def get_remaining(self):
            return [card.present() for card in self.cards]


class Card:
    
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value 
    
    def present(self):
        # return self.value, 'of', self.suit
        return f'{self.value} of {self.suit}'
   
# ace = Card('ace', 'spades')
# ace.present()
def game():
    while True:
        choice = input('Shuffle, deal, get remaining, count remaining, new deck: ')

        if choice == 's':
            deck.shuffle()
        elif choice == 'l':
            print('Bye!')
            break
        elif choice == 'd':
             count = input('How many?')
             for i in range(int(count)):
                  print(deck.deal())
        elif choice == 'g':
             print(deck.get_remaining())
        elif choice == 'c':
             print(deck.count_remaining())
        elif choice == 'n':
             deck.new_deck()
        else:
            print('Please enter a correct value')

deck = Deck()

     
game()

# for i in range(48):
#print(deck.deal())
# # deck.shuffle()
# #deck.get_remaining()
# print(deck.count_remaining())

#print(deck.cards)

