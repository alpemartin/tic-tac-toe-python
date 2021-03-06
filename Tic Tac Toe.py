from Tkinter import *
from tkk import Entry, Button

class Tile(Label):
    def__init__:(self,parent):
        Label.__init__(self,aprent,font = ("",30), width = 2, justify = 'center', relief = 'raised',bg = 'white')
         self.checkWin = checkWin
        self.bind('<Button-1>',self.markX)
        self.bind('<Button-2>',self.markO)
        self.marked = ""
       

        def markX(self,event):
        if not self.marked:
        self.config(text = 'X')
        self.marked = 'X'
        self.checkWin()

        def markO(self,event):
        if not self.marked:
        self.config(text = 'O')
        self.marked = 'O'
        self.checkWin()


class Main():
    def __init__(self,parent):
        self.parent = parent

self.player1 = StringVar()
self.player2 = StringVar()
self.winner = Stringvar()


self.createWidgets()

def createWidgets(self):
self.mainFrame = Frame(self.parent)
Label(self.MainFrame, text="Tic Tac Toe", font =("",50)).pack()
frame1 = Frame(self.mainFrame)
Label(frame1,text='Player1 (X, Button-1)').grid(padx =5, pady = 5)
Entry(frame1,textvariable = self.pla)
Label(frame1,text='Player2 (O, Button-2)').grid(padx =5, pady = 5)
frame1.pack()
Button(self.mainFrame,text ='Start', command = self.start).pack()
self.mainFrame.pack(padx = 10, pady = 10)
self.gameFrame = Frame(self.parent)
self.winFrame = Frame(self.parent)
Label(self.winFrame,textvariable = self.wiiner,font = ('',50)).pack()
Button(self.winFrame,text = 'Play Again?',command = self.start).pack()

def start(self):
    player1 = self.player1.get()
    player2 = self.player2.get()
    self.tiles=[]
    self.winFrame.pack_forget()

    if player1 and player2 and player1 != player2:
        self.mainFrame.forget()
        for i in range(3):
            for j in range(3):
            tile = Tile(self.gameFrame, checkWin)
            tile.grid(row = i, column = j))
            self.tiles.append(tile)
self.gameFrame.pack()

def checkWin(self):
    for x,y,z in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]: #possible arrangements for win
        if self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'X':
            self.showWin(self.player1.get())
         if self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'O':
            self.showWin(self.player2.get())   

def showWin(self,player):
    self.gameFrame.pack:forget()
    self.winFrame.pack(pady = 10, padx = 10)
    self.winner.set(player+' Won!')


if __name__='__main':
root = Tk()
Main(root)
root.mainloop()