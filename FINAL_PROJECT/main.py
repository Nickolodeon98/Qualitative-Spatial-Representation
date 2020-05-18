import numpy as np
import matplotlib.pyplot as plt
import collections
from pyswip import Prolog
from pynput.keyboard import Key, Listener
import random
import vision
import interface

# global num
num = 0
bRegion = []
relationList = ['dc', 'ec', 'po', 'tpp', 'itpp', 'ntpp', 'intpp', 'eq']
colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'magenta']
color = []

class baseRegion:
    def __init__(self, region, color):
        self.base = region
        self.color = color

def setNum(option):
    global num
    num = num + 1
    if option <= 0:
        num = option


def addRegion(option):
    global bRegion
    bRegion.append(option)
    if option == 0:
        bRegion = []


def addColor(option):
    global color
    color.append(option)
    if option == 0:
        color = []

def removeColor(option):
    global colorList
    colorList.remove(option)


def on_press(key):
    #print('{0} pressed'.format(
    #key))
    check_key(key)

def on_release(key):
    #print('{0} release'.format(
    # key))
    if key == Key.space:
        # Stop listener
        return False


def check_key(key):
    if key == Key.space:
        setNum(1)
        # print('YES')

def compute(x, y):
    return 2 * abs(x - y)

Coord = collections.namedtuple('Coord', ['x', 'y'])

class Region:
    def __init__(self, name, xCoord, yCoord, width, height):
        self.name = name
        self.x = xCoord
        self.y = yCoord
        self.w = width
        self.h = height
        self.a = Coord(self.x - (self.w/2), self.y + (self.h/2))
        self.b = Coord(self.x + (self.w/2), self.y + (self.h/2))
        self.c = Coord(self.x + (self.w/2), self.y - (self.h/2))
        self.d = Coord(self.x - (self.w/2), self.y - (self.h/2))

def close():
    plt.close()

class relations:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.A = region

    def relation(self, nextRegion):
        prolog = Prolog()

        if self.name not in relationList:
            print("Command not found!")
            setNum(-1)
            return None
        else:
            prolog.consult(self.name + ".pl")
            l = list(prolog.query(f'{self.name}({self.region.w}, {self.region.h}, Bw, Bh, {self.region.x}, {self.region.y}, Bx, By), label([Bw, Bh, Bx, By])'))

            self.Bw = []
            self.Bh = []
            self.Bx = []
            self.By = []

            for item in l:
                self.Bw.append(item["Bw"])
                self.Bh.append(item["Bh"])
                self.Bx.append(item["Bx"])
                self.By.append(item["By"])

            ppRelationList = ['tpp', 'itpp', 'ntpp', 'intpp']

            if self.name in ppRelationList:
                length = len(self.Bw)
                index = []
                for i in range(0, length):
                    B = Region('Test', self.Bx[i], self.By[i], self.Bw[i], self.Bh[i])

                    if bool(list(prolog.query(f'check{self.name}({self.region.w}, {self.region.h}, {B.w}, {B.h}, {self.region.x}, {self.region.y}, {B.x}, {B.y})'))):
                        continue
                    else:
                        index.append(i)

                index.sort(reverse=True)

                for i in index:
                    del self.Bx[i]
                    del self.By[i]
                    del self.Bw[i]
                    del self.Bh[i]

            sublabel = self.region.name
            label = chr(ord(sublabel)+1)
            try:
                if nextRegion != None:
                    B = Region(nextRegion, self.Bx[num], self.By[num], self.Bw[num], self.Bh[num])
                else:
                    B = Region(label, self.Bx[num], self.By[num], self.Bw[num], self.Bh[num])
            except IndexError as error:
                print(f'Error occurred! Unable to visualise! ({error})')
                setNum(-1)
                return None
        return B

    def display(self, base_region, next):
            if num != -1:
                print(f'{self.name} is one of the relation.')

            statement = ' '

            while(1):
                # print(num)
                reader = input(f'***************************************************\nEnter 1 to visualise this relation {statement}\nEnter 2 to try a different relation\n'
                               f'Enter 3 to add one more region in this relation\nEnter 4 to go back to the previous menu\n'
                               f'Enter 5 to terminate the program\n***************************************************\n>>> ')
                while (reader not in ['1', '2', '3', '4', '5']):
                    print('Wrong Input! Try Again!')
                    reader = input('>>> ')
                if reader == '1':
                    if num == -1:
                        print('**************************\nImpossible to visualise!\n**************************')
                        continue
                    statement = 'further'
                    print('Press Space bar to close the window and see more options: ')
                    sublabel = self.region.name
                    label = chr(ord(sublabel) + 1)
                    try:
                        if next != None:
                            B = Region(next, self.Bx[num], self.By[num], self.Bw[num], self.Bh[num])
                        else:
                            B = Region(label, self.Bx[num], self.By[num], self.Bw[num], self.Bh[num])
                    except IndexError as error:
                        print(f'Error occured! {error}')
                        break
                    if len(base_region) != 0:
                        for item in base_region:
                            if item.base != self.region:
                                vision.plot(item.base, item.color)
                    vision.plot(self.region, 'brown')
                    vision.plot(B, 'gray')
                    # plot(B, 'green')
                    vision.draw()
                    with Listener(
                            on_press=on_press,
                            on_release=on_release) as listener:
                        listener.join()
                    close()
                    # close()
                    if num == len(self.Bx):
                        print('*********************************************************\nAll the possible visualisations for this relation is displayed!\n*********************************************************')
                        addRegion(0)
                        setNum(-99)
                        break
                elif reader == '2':
                    addRegion(0)
                    setNum(-99)
                    break
                elif reader == '3':
                    print('The region has been successfully added!')
                    break
                elif reader == '4':
                    setNum(-99)
                    break
                elif reader == '5':
                    vision.save()
                    setNum(0)
                    print('Bye')
                    exit()


# Recursive function that solves the problem of recurring addition of more regions
def recursion(base, regionRep, region, relation, nextRegion):
    try:
        regionRep.display(base, nextRegion)
        if num == -99:
            setNum(0)
            return
        else:
            while(1):
                if len(base) == 0:
                    cRegion = input(f'Where do you want to add a new region to?\n**********************************\n1. {region.name}\n2. {region.name}\n**********************************\n>>> ')
                else:
                    print(f'Where do you want to add a new region to?\n**********************************')
                    count = 0
                    for item in base:
                        print(f'{count+1}. {item.base.name}')
                        count = count + 1
                    cRegion = input(f'{len(base)+1}. {region.name}\n**********************************\n>>> ')
                if cRegion == str(len(base)+1):
                    extraRegion = region
                elif len(base) != 0:
                    for i in range(0, len(base)):
                        if cRegion == str(i+1):
                            extraRegion = base[i].base
                else:
                    print('Wrong input!')

                newRelation = input('***************************************************\nWhat relation would you like a new region to have?\n***************************************************\n>>> ')

                if newRelation == 'exit':
                    exit()

                if nextRegion != None:
                    extraRegion_str = chr(ord(nextRegion) + 1)
                elif extraRegion != region:
                    extraRegion_str = chr(ord(extraRegion.name)+2)
                else:
                    extraRegion_str = chr(ord(extraRegion.name)+1)
                newRegion = relations(newRelation, extraRegion)
                C = newRegion.relation(extraRegion_str)
                if num == -1:
                    setNum(0)
                    continue
                if len(colorList) != 0:
                    color = random.choice(colorList)
                    thisRegion = baseRegion(region, color)
                    removeColor(color)
                    addRegion(thisRegion)
                else:
                    print('No more colors left!')
                    break
                recursion(bRegion, newRegion, C, newRelation, extraRegion_str)
                break
    except AttributeError as error:
        print(f'Error occured! {error}')


def main():
    while(1):
        choice = input('WELCOME! This is a spatial representation program.\n**************************************************'
              '\nEnter 1 to start using the program\n'
              'Enter 2 to load the previous representation\n'
              'Enter 3 to terminate the program\n**************************************************'
              '\n>>> ')

        if choice == '1':
            a = interface.interface
            a.show(a)
            while(1):
                setNum(0)
                user_input = input('What relation do you want to visualise?(Enter 0 to go to home menu)\n>>> ')
                if user_input == '0':
                    addRegion(0)
                    interface.interface.show(a)
                    continue
                elif user_input == 'exit':
                    print('Bye')
                    break
                if user_input not in relationList:
                    print('Wrong input!')
                    break

                A = Region('A',int(interface.interface.x),int(interface.interface.y),int(interface.interface.width),int(interface.interface.height))
                region_B = relations(user_input, A)
                B = region_B.relation(None)
                if len(colorList) != 0:
                    color = random.choice(colorList)
                    thisRegion = baseRegion(A, color)
                    removeColor(color)
                    addRegion(thisRegion)
                else:
                    print('No more color!')
                    break

                recursion(bRegion, region_B, B, user_input, None)
        elif choice == '2':
            print('Loading the file...')
            continue
        elif choice == '3':
            print('Bye')
            break
        else:
            print('Wrong input!')


if __name__ == '__main__':
    main()