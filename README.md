# BlackJack in-Python ##
### OOP with GUI ###
Blackjack game in Python using Zelle's graphics.py. Based on the exercise in chapter 10 from his book 'Introduction to Python Programming'. Some variables have Dutch names, but that shouldn't change the thrill of the game. This game is the result of the following assignment requirements:
>Basis: Zelle, chapter 10, assignment 11, also assignment 12.
>Extends the "card" class of command 11 created using a method draw (self, win, center) that shows the map in a graphical window.
>Use this more extensive class to pull two cards randomly from a stick (of the 52 cards, so we play in contrast to the casino but with one deck at a time) and show these cards on the screen, with the total Blackjack value.
### Winning conditions ###
>Then the user can always choose "pass" or "draw" (make two buttons for this). If you fit you can earn dollars:
><ul>
><li>21: 10 dollars</li>
><li>20: 5 dollars</li>
><li>19: 3 dollars</li>
><li>18: 2 dollars</li>
><ul>
>If the total Blackjack value exceeds 21, you lose 3 dollars and start a new game.
>On the screen, always see what the total score in dollars so far is.
>Also, provide a "quit" button that lets you stop.


![Alt text](/blackjack_gui.jpg?raw=true "Example of the game")

## Requirements ##
All the classes for the objects needed are in the repository, including the dependancy for the GUI Zelle's graphics.py, wich is a wrapper around Tkinter.
<ul>
<li>Python 3.+</li>
</ul>

## Playing the game ##
Clone this repository
<code> git clone https://github.com/victorr0/BlackJack-in-Python-OOP-with-GUI.git </code>

Start the game with the command: 
<code> python3 BlackJack.py </code>

