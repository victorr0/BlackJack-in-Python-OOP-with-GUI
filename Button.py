#!/usr/bin/python3

# File name: Button.py
# Contains the Button class and function for button behaviour
# Assignment by Victor from the book by Zelle, chapter 10
# Date: 17-12-2016

import sys
from graphics import *

class Button:
    """Draws a button"""
    def __init__(self, win, center, width, height, size,text,s):
        w = width / 2.0
        h = height / 2.0
        x = center.getX()
        y = center.getY()
        self.x_max = x+w
        self.x_min = x-w
        self.y_max = y+h
        self.y_min = y-h
        p1 = Point(self.x_min, self.y_min)
        p2 = Point(self.x_max, self.y_max)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('green4')
        self.rect.draw(win)
        self.text = Text(center, text)
        self.text.setSize(size)
        self.text.draw(win)
        if s is True:
            self.activate()
        else:
            self.deactivate()
        
    def clicked(self, p):
        return (self.active and
                self.x_min <= p.getX() <= self.x_max and
                self.y_min <= p.getY() <= self.y_max)

    def activate(self):
        self.text.setFill('black')
        self.rect.setWidth(1)
        self.active = True
 
    def deactivate(self):
        self.text.setFill('darkgreen')
        self.rect.setWidth(1)
        self.active = False

def buttonUpdates(status,buttons):
    """Activates or deactivates buttons based on the status of the game"""
    if status == 'gameover':
        buttons[0].deactivate()
        buttons[1].deactivate()
        buttons[2].deactivate()
        buttons[3].activate()
        buttons[4].activate()
    elif status == 'stillplaying':
        buttons[0].deactivate()
        buttons[1].activate()
        buttons[2].activate()
    elif status == 'newgame':
        buttons[0].activate()
        buttons[1].deactivate()
        buttons[2].deactivate()
        buttons[3].deactivate()
        buttons[5].deactivate()
    elif status == 'outofcards':
        buttons[0].deactivate()
        buttons[1].deactivate()
        buttons[2].deactivate()
        buttons[3].deactivate()
        buttons[4].activate()
        buttons[5].activate()

