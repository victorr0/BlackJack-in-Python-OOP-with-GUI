#!/usr/bin/python3

# File name: Texts.py
# Contains the Scorebox class for displaying scores and functions for other text in the GUI
# Assignment by Victor from the book by Zelle, chapter 10
# Date: 17-12-2016

from graphics import *

class Scorebox(Text):
    """Creates a 'scorebox' with a unchancing 'label' (text) and changing value"""
    def __init__(self, win, center,text,value):
        x = center.getX()
        y = center.getY()

        self.text = Text(Point(x-15,y), text)
        self.text.setSize(12)
        self.text.draw(win)

        self.value = self.text.clone()
        self.value.move(30,0)
        self.value.setText(value)
        self.value.draw(win)

    def updateText(self,new_value):
        """Allows the value of the Scorebox to be changed"""
        if self.value.getText() == new_value:
            pass
        else:
            self.value.setText(new_value)
            # Visual feedback when the value changes for the user
            for i in range(2):
                time.sleep(0.1)

                if i % 2 == 0:
                    self.value.setStyle('bold')
                else:
                    self.value.setStyle('normal')

def FlashyText(win,center,text,timing):
    """Creates a flashy text to the user"""
    winner = Text(center,text)
    winner.setFace("arial")
    winner.setFill("black")
    winner.setSize(30)
    for i in range(1,6):
        time.sleep(timing)
        if i % 2 == 0:
            winner.draw(win)
        else:
            winner.undraw()
