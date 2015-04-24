import random

suits = ('c','s','h','d')
ranks = ('2','3','4','5','6','7','8','9','10','j','q','k','a')

suits_dict = {'c':'Clubs','s':'Spades','h':'Hearts','d':'Diamonds'}

ranks_dict = {'2' : 'Two', '3' : 'Three', '4' : 'Four', '5' : 'Five', '6' : 'Six', '7' : 'Seven', '8' : 'Eight', '9' : 'Nine', '10' : 'Ten', 'j' : 'Jack', 'q' : 'Queen', 'k' : 'King', 'a' : 'Ace'}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = self.value()
    # def __str__(self):
    #     "Optional to fill out"
    #     pass
    # def __repr__(self):
    #     "optional to fill out"
    #     pass
    # def __radd__(self,other):
    #     pass
    def value(self):
        if self.rank in ['2','3','4','5','6','7','8','9','10']:
            return int(self.rank)
        elif self.rank in ['j','q','k']:
            return 10
        # elif self.rank == 'a':
        #     return 11

class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in suits for r in ranks]
    def shuffle(self):
        random.shuffle(self.cards)
    def one(self):
        "get one card"  
        return self.cards.pop()

class Player:
    def __init__(self):
        self.name = raw_input('Please enter player name: ')
        self.holding = []

    def __str__(self):
        return self.rank + self.suit

    # def __lt__(self,other):
    #     pass
    
    def get(self,card):
        "adds a card to the users hand"
        self.holding.append(card)

    def choose(self, deck):
        "choose new card"
        print "%s's current hand value is: %s" % (self.name, self.hand_value())        
        new_card = deck.one()
        print '%s drew a %s of %s' % (self.name, ranks_dict[new_card.rank], suits_dict[new_card.suit])
        self.get(new_card)
        print "%s's hand value is now: %s" % (self.name, self.hand_value())

    def hand_value(self):
        "calculate the number value of the users hand"
        holding_value = 0
        aces = False

        for i in self.holding:
            if 'a' not in i.rank:
                holding_value += i.value
            elif 'a' in i.rank:                
                aces = True
        if aces:
            for i in self.holding:
                if i.rank == 'a' and holding_value < 11:
                    holding_value += 11
                elif i.rank == 'a' and holding_value >= 11:
                    holding_value += 1
        return holding_value
    
    def bust(self):
        return self.hand_value() > 21

    def won(self):
        "do they have 21"
        return self.hand_value() == 21

class Dealer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = 'Dealer'

    # def __str__(self):
    #     "optional"
    #     pass
        
class Game:
    def __init__(self):
        #Game setup, adds players and a dealer, creates and shuffles a deck
        self.n_players = int(raw_input('How many players? '))
        self.players = []
        for i in range(0, self.n_players):
            self.players.append(Player())
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.shuffle()
    
    def print_table(self):
        #helper method to print out all the players hands
        for i in self.players:
            for j in i.holding:
                print '%s holds the %s of %s.' % (i.name, ranks_dict[j.rank], suits_dict[j.suit])
        print "Dealer's showing the %s of %s." % (ranks_dict[self.dealer.holding[0].rank], suits_dict[self.dealer.holding[0].suit])
    
    def initial_deal(self):
        #inital deal to all players, including dealer
        for i in self.players:
            i.get(self.deck.one())
            i.get(self.deck.one())
            print "%s's hand value is %s." % (i.name, i.hand_value())
        self.dealer.get(self.deck.one())
        self.dealer.get(self.deck.one())
        print "Dealer's showing the %s of %s." % (ranks_dict[self.dealer.holding[0].rank], suits_dict[self.dealer.holding[0].suit])

    def ask_player_loop(self, player):
        #ui loop to ask player hit or stay
        ui = 'h'
        while ui != 's':
            ui = raw_input(player.name + ': h)it or s)tay  - or c)heck hands? ')
            if ui == 'c':
                self.print_table()
            if ui == 'h':
                player.choose(self.deck)
                if player.bust():
                    print "Busted!"
                    ui = 's'
                if player.won():
                    ui = 's'

    def check_results(self, player):
            if player.hand_value() > self.dealer.hand_value():
                print "%s has %s, Dealer has %s. %s wins! :-)" % (player.name, player.hand_value(), self.dealer.hand_value(), player.name)
            elif player.hand_value() < self.dealer.hand_value():
                print "%s has %s, Dealer has %s. %s loses! :'( " % (player.name, player.hand_value(), self.dealer.hand_value(), player.name)
            elif player.hand_value() == self.dealer.hand_value():
                print "Push! :-| "

    def play(self):
        "top level, manages the game"
        self.initial_deal()

        self.print_table()
        
        #Check for blackjack
        for player in self.players:
            if player.won():
                print "Winner winner chicken dinner! %s WINS!" % player.name
        
        if self.dealer.won():
               return "Dealer Blackjack! Everyone loses!"

        for player in self.players:
            if not player.won():
                self.ask_player_loop(player)

        while self.dealer.hand_value() < 17:
            self.dealer.choose(self.deck)
            print "Dealer has %s." % self.dealer.hand_value()

        for player in self.players:
            if not player.bust()
            self.check_results(player)
        
        if raw_input("Play again? y/n: ") == 'y':
            g = Game()
            g.play()


g = Game()
g.play()