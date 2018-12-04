'''
Created on Dec 4, 2018

@author: carter buerk
'''

from tkinter import *
import tkinter.messagebox
import os.path


    
    
class Tracker(Frame):
    #Variables
    localWins = 0    
    localGames = 0
 
    def __init__(self):
        #Set up the window and widgets
        Frame.__init__(self)
        self.master.title("Game Tracker")
        self.grid()
        
        self._fileLabel = Label(self, text = "Series Length")
        self._fileLabel.grid(row = 0, column = 0)
        
        self._seriesVar = StringVar()
        self._seriesLengthEntry = Entry(self, textvariable = self._seriesVar)
        self._seriesLengthEntry.grid(row = 0, column = 1)
        
        #Command buttons
        self._winBtn = Button(self, text = "Win", command = self._winCounter)
        self._winBtn.grid(row = 1, column = 0)
        
        self._lossBtn = Button(self, text = "Loss", command = self._gameCounter)
        self._lossBtn.grid(row = 1, column = 1)
        
        
    def _winCounter(self):
        localWins += 1
        return localWins
    def _gameCounter(self):
        localGames += 1
        return localGames
        
def main():
    Tracker().mainloop()
    
main()        
x = input()
