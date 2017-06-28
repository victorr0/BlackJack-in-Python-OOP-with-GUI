#!/usr/bin/python3

# File name: GamePlay.py
# Class and methods for playing the game of blackjack
# Assignment by Victor from the book by Zelle, chapter 10
# Date: 17-12-2016

from graphics import *
import time
import random
from Deck import*
from Button import*
from Texts import*

class Game():
    def __init__(self,win):
        # Set variables for the game
        score = winnings = 0
        money = 1000
        center = Point(250,100)

        # Draw the money, score and winnings in the window
        bank_view = Scorebox(win, Point(115,20),"    $",money)
        score_view = Scorebox(win, Point(210,20),"Score:",score)
        winnings_view = Scorebox(win, Point(310,20),"You won:",winnings)

        # Draw the buttons needed in the game
        deal_Button = Button(win, Point(50,40), 75, 25,15,"Deal", True)
        draw_Button = Button(win, Point(50,65),75,25,15,"Draw", False)
        pass_Button = Button(win, Point(50,90),75,25,15,"Pass", False)
        again_Button = Button(win, Point(50,115), 75, 25,15,"Again", False)
        quit_Button = Button(win, Point(50,140), 75, 25,15,"Quit", True)
        newdeck_Button = Button(win, Point(112,33), 50, 12,10,"New deck", False)
        buttons = [deal_Button,draw_Button,pass_Button,again_Button,quit_Button,newdeck_Button]

        # Create a deck and shuffle it 3 times
        deck = Deck()
        for i in range(3):
            deck.Shuffle()

        p = win.getMouse()
        totalCards = 0

        while not quit_Button.clicked(p):
            p = win.getMouse()
            # User can click the deal button to start playing
            if deal_Button.clicked(p):
                totalCards += 2 # Keeps counting through the rounds
                cardCount = 1 # Resets each round, needed for relative placement of cards dealt if the user draws.
                dealtCards = [] # Resets each round, stores the cards for the current round, needed for undrawing at the end of the round.
                gameUpdates('stillplaying',score,winnings,money,score_view,winnings_view,bank_view,False)
                buttonUpdates('stillplaying',buttons)

                # Deals 2 cards from the deck
                for i in range(2):
                    location = Point(125+25*i,90) # Place each card 25*i further on the x-axis
                    kaart,score,dealtCards = dealCard(win,deck,dealtCards,score,location)
                    score,winnings,money = gameUpdates('stillplaying',score,winnings,money,score_view,winnings_view,bank_view,False)

            # User can choose to draw another card
            elif draw_Button.clicked(p):
                totalCards += 1
                cardCount += 1
                location = Point(125+25*cardCount,90) # Place each card 25*cardcount (ammount of cards on the table) further on the x-acis
                kaart,score,dealtCards = dealCard(win,deck,dealtCards,score,location)
                score,winnings,money = gameUpdates('stillplaying',score,winnings,money,score_view,winnings_view,bank_view,False)

                # If the cardvalue is over 21, the game is over
                if Bust(score) is True:
                    score,winnings,money = gameUpdates('gameover',score,winnings,money,score_view,winnings_view,bank_view,True)
                    FlashyText(win,center,"Bust",0.15)
                    buttonUpdates('gameover',buttons)

                # If the cardvalue is exactly 21, the user has blackjack and wins
                elif BlackJack(score) is True:
                    score,winnings,money = gameUpdates('gameover',score,winnings,money,score_view,winnings_view,bank_view,True)
                    FlashyText(win,center,"BLACKJACK!",0.15)
                    buttonUpdates('gameover',buttons)

            # User can pass and take winnings
            elif pass_Button.clicked(p):
                score,winnings,money = gameUpdates('gameover',score,winnings,money,score_view,winnings_view,bank_view,True)
                buttonUpdates('gameover',buttons)

            # Checks if there are enough cards left in the deck for a game, if not, game is aborted and a new deck is needed
            if totalCards > 50:
                # Inform user
                FlashyText(win,center,"No more cards in deck",0.5)
                # Payout winnings or losses 
                score,winnings,money = gameUpdates('gameover',score,winnings,money,score_view,winnings_view,bank_view,True)
                buttonUpdates('outofcards',buttons)
                totalCards = 0

            # User can create a new deck and keep playing
            elif newdeck_Button.clicked(p):
                clearfromTable(dealtCards)
                deck = Deck()
                deck.Shuffle()
                score,winnings,money = gameUpdates('newgame',score,winnings,money,score_view,winnings_view,bank_view,True)
                buttonUpdates("newgame", buttons)

            # After a bust, pass or blackjack, the user can play again
            elif again_Button.clicked(p):
                # Undraw cards of previous round
                clearfromTable(dealtCards)
                score,winnings,money = gameUpdates('newgame',score,winnings,money,score_view,winnings_view,bank_view,True)
                buttonUpdates("newgame", buttons)

        # Window closes if the quit_Button is clicked
        win.close()

def gameUpdates(result,score,winnings,money,score_view,winnings_view,bank_view,s):
    """Updates all Scoreboxes with their new values according to the result of the game"""
    if result == 'stillplaying':
        winnings,money = winsScheme(score,money,winnings,False) # No payout yet
        
    elif result == 'gameover':
        winnings,money = winsScheme(score,money,winnings,True) # Money payed or payed out

    elif result == 'newgame': # Resets the score and winnings so a new round can be played
        score = 0
        winnings = 0

    score_view.updateText(score)
    winnings_view.updateText(winnings)
    bank_view.updateText(money)
    return score,winnings,money

    
def dealCard(win,deck,dealtcards,score,location):
    """Deals a card, draws it and adds it to the dealtCards list, then returns the card, score (value) and the list of total cards"""
    value = deck.Deal()
    card = Card(win,value,location)
    dealtcards.append(card)
    score += card.getValue()
    return card,score,dealtcards

def clearfromTable(dealtCards):
    """Clears all the cards on the table"""
    for i in dealtCards:
        i.Undraw()

def winsScheme(score,money,winnings,s):
    """Checks the payout for the current score, adds it to the bank if s = True (at the end of a round)"""
    if score < 18:
        pass
    elif score == 21:
        winnings = 10
    elif score == 20:
        winnings = 5
    elif score == 19:
        winnings = 3
    elif score == 18:
        winnings = 1
    elif score > 21:
        winnings = -3
    if s is False:
        return winnings,money
    else:
        money = money + winnings
        return winnings,money

def BlackJack(score):
    """Returns True if the score is exaclty 21"""
    if score == 21:
        return True
    else:
        return False

def Bust(score):
    """Returns True if the score is over 21"""
    if score > 21:
        return True
    else:
        return False
