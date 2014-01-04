# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables

in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#global variable for games
deck = None
player = None
dealer = None


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.cardtype = card_images
            self.cardsize = CARD_SIZE
            self.cardcenter = CARD_CENTER
        else:
            self.suit = None
            self.rank = None
            self.cardtype = card_images
            self.cardsize = CARD_SIZE
            self.cardcenter = CARD_CENTER
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    def change_card_type(self):
        if (self.cardtype == card_images):
            self.cardtype = card_back
            self.cardsize = CARD_BACK_SIZE
            self.cardcenter = CARD_BACK_CENTER
        else:
            self.cardtype = card_images
            self.cardsize = CARD_SIZE
            self.cardcenter = CARD_CENTER
            
    def get_card_type(self):
        return self.cardtype

    def draw(self, canvas, pos):
        if (self.cardtype == card_images):
            card_loc = (self.cardcenter[0] + self.cardsize[0] * RANKS.index(self.rank), 
                    self.cardcenter[1] + self.cardsize[1] * SUITS.index(self.suit))
        else:
            card_loc = CARD_BACK_CENTER
        
        canvas.draw_image(self.cardtype, card_loc, self.cardsize, [pos[0] + self.cardcenter[0], pos[1] + self.cardcenter[1]], self.cardsize)

# define hand class
class Hand:
    def __init__(self):
        self.cardList = []
        

    def __str__(self):
        if len(self.cardList) == 0:
            return "Hand Contains"
        else:
            cards = ""
            for card in self.cardList:
                cards += " "+str(card)
            return "Hand Contains " + cards

    def add_card(self, card):
        self.cardList.append(card);
        pass	# add a card object to a hand

    def get_value(self):
        count = 0
        numberofaces = "False"
        for card in self.cardList:
            if card.rank == 'A':
                numberofaces = "True"
                count += 1
            else:
                count += VALUES[card.rank]
        if numberofaces == "True":
            if count + 10 <= 21:
                return count + 10
            else:
                return count
        else:
            return count
   
    def draw(self, canvas, pos):
            # draw a hand on the canvas, use the draw method for cards
         for card in self.cardList:
                pos[0] += 100
                card.draw(canvas,pos)

        
# define deck class 
class Deck:
    def __init__(self):
        self.cardList = []
        for suit in SUITS:
            for rank in RANKS:
                self.cardList.append(Card(suit, rank))
 

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cardList)

    def deal_card(self):
        removeitem = random.randrange(0, len(self.cardList))
        c = self.cardList.pop(removeitem)
        return c	
        # deal a card object from the deck
    
    def __str__(self):
        result = "Deck contains "
        for card in self.cardList:
            result += str(card) + " "
        return result  


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, score
    if ( in_play == True and player.get_value() > 0):
        score -= 1
        outcome = "Player lost the round! Deal again?"
        in_play = False
        return
        
    in_play = True
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    c = deck.deal_card()
    #print "Player is dealt with card "+ str(c)
    player.add_card(c)
    c = deck.deal_card()
    if (in_play == True):
        c.change_card_type()
    dealer.add_card(c)
    #print "Dealer is dealt with card "+ str(c)
    outcome = "Hit or Stand ?"
    
def hit():
    # replace with your code below
    global in_play, outcome, dealer, score, player
    handValue = player.get_value()
    # if the hand is in play, hit the player
    if in_play == False:
        outcome = "Might we remind you that you are already busted ?"
        #print "Might we remind you that you are already busted ?"
        return
    if handValue <= 21:
        c = deck.deal_card()
        player.add_card(c)
        #print "Player is dealt with Card "+ str(c)
 
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = "Player is busted. Dealer wins! New Deal??"
        score -= 1
        #print "You are busted. Dealer wins!"
        setinplayfalse()
        
def stand():
    # replace with your code below
    global dealer, deck, player, outcome, score
    if in_play == False:
        outcome = "Might we remind you that you are already busted ?"
        #print "Might we remind you that you are already busted ?"
        return
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while( dealer.get_value() < 17):
            c = deck.deal_card()
            dealer.add_card(c)
            #print "Dealer is dealt with Card "+ str(c)
            if dealer.get_value() > 21:
                outcome = "Dealer busted! Player wins! New Deal??"
                score += 1
                #print "Dealer busted! Player wins"
                setinplayfalse()
                return
    # assign a message to outcome, update in_play and score
    if player.get_value() > dealer.get_value():
        outcome = "Player wins! New Deal??"
        score += 1
        #print "Player wins!"
    else:
        outcome = "Dealer wins! New Deal??"
        score -= 1
        #print "Dealer wins!"
    setinplayfalse()
            
def setinplayfalse():
    global dealer, in_play
    in_play = False
    for card in dealer.cardList:
        if card.get_card_type() == card_back:
            card.change_card_type()
    
# draw handler    
def draw(canvas):
    canvas.draw_text('BlackJack', (250, 30), 40, 'Red')
    canvas.draw_text('May the odds be in your favor', (200,60), 20, 'Blue')
    canvas.draw_text('Player', (0,100), 20, 'White')
    canvas.draw_text('Dealer', (0,300), 20, 'White')
    canvas.draw_text(outcome, (0,500), 20, 'White')
    canvas.draw_text("Score: "+str(score), (0,550), 20, 'White')
    playerPos = [0, 100]
    dealerPos = [0, 300]
    player.draw(canvas, playerPos)
    dealer.draw(canvas, dealerPos)
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling

deal()
frame.start()


# remember to review the gradic rubric