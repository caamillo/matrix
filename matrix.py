from colorama import Fore,Style
from threading import Thread
import string
import random
import colorama
import time
import os
import random

colorama.init(autoreset=True)

class Matrix:
    def __init__(self,sy,rf,mit,mat,miof,maof):
        self.sizeX = self.getScreen()
        self.sizeY=sy
        self.rf=rf
        self.minT=mit
        self.maxT=mat
        self.minOf=miof
        self.maxOf=maof

        self.tiles=[]
        self.offset=0
        self.lt=-1
        self.totL=0

        self.started = False

        self.characters=string.ascii_letters+string.digits+string.punctuation

        self.screenChanged = False

        self.onScreenChangeThread = Thread(target=self.onScreenChange)
        self.onScreenChangeThread.start()

    def Setup(self):
        os.system("echo off")
        os.system("cls")
        self.createMatrix()
        self.printMatrix()

    def createMatrix(self):
        for i in range(self.sizeX):
            self.tiles.append([])
            for j in range(self.sizeY):
                #print(j,offset,lt)
                if(self.totL<self.sizeY):
                    offset=random.randrange(self.minOf,self.maxOf+1)
                    lt=random.randrange(self.minT,self.maxT+1)
                    self.totL+=lt+offset
                    #print('lt:',lt,' offset:',offset)
                    self.tiles[i].append(str(offset))
                    self.tiles[i].append(lt)
                    #print(tiles[i])
                else:
                    self.totL=0
                    break

    def printMatrix(self):
        cc=[0 for i in range(self.sizeX)]
        ypos=0
        self.started = True
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                if(int(self.tiles[j][cc[j]])<=0):
                    cc[j]+=1
                if(j%2==0):
                    if(type(self.tiles[j][cc[j]])==str):
                        self.tiles[j][cc[j]]=str(int(self.tiles[j][cc[j]])-1)
                        print(' ',end='')
                    else:
                        self.tiles[j][cc[j]]=int(self.tiles[j][cc[j]])-1
                        print(Fore.GREEN+random.choice(self.characters),end='')
                else:
                    print(' ',end='')
            print(" ")
            time.sleep(self.rf)
            if self.screenChanged:
                self.screenChanged = False
                self.started = False
                self.Setup()
    def getScreen(self):
        return os.get_terminal_size()[0]-1
    def onScreenChange(self):
        screen = self.sizeX
        while True:
            screenNew = self.getScreen()
            if screenNew != screen and self.started:
                print('Changed')
                self.screenChanged = True
                self.sizeX = screenNew
                screen = screenNew
            time.sleep(0.5)
