'''
File name: BlockBust.py
Author: Max Donnelly
Version: 1.1.13
'''

from tkinter import *
from PIL import Image, ImageTk
import random
import time

def gameLoop():
    pass

def configureWindow():
    '''
    Will set up the window that the game is played in
    '''
    window.geometry("800x700")
    window.configure(background='#47587f')
    window.title("B l o c k   B u s t")

def configureCanvas():
    '''
    Initialises the canvas, creating the grid on which the game is played
    '''
    global canvas
    canvas = Canvas(window, width=800, height=700)
    gameGrid = canvas.create_rectangle(175, 50, 625, 500, fill='#37487f', outline='#17287f')
    for i in range(9):
        canvas.create_rectangle(175 + (i * 50), 50, 225 + (i * 50), 500, outline='#17287f')
    for i in range(9):
        canvas.create_rectangle(175, 50 + (i * 50), 625, 100 + (i * 50), outline='#17287f')
    canvas.configure(background='#47587f')
    canvas.pack(fill="both", expand=True)
    return canvas
    
def moveRight(event):
    '''
    Decides what will occur in the event of the user pressing the right key
    '''
    global blockArray, allBlocks
    for block in range(len(blockArray)):
        canvas.move(blockArray[block], 50, 0)

def moveLeft(event):
    '''
    Decides what will occur in the event of the user pressing the left key
    '''
    global blockArray, allBlocks
    for block in range(len(blockArray)):
        canvas.move(blockArray[block], -50, 0)

def moveUp(event):
    '''
    Decides what will occur in the event of the user pressing the up key
    '''
    global blockArray, allBlocks
    for block in range(len(blockArray)):
        canvas.move(blockArray[block], 0, -50)

def moveDown(event):
    '''
    Decides what will occur in the event of the user pressing the down key
    '''
    global blockArray, allBlocks
    for block in range(len(blockArray)):
        canvas.move(blockArray[block], 0, 50)

def placeBlock(event):
    '''
    Determines the logic for placing a block
    '''
    global blockArray, allBlocks, score, showScore
    inRange = True
    colliding = False
    for block in range(len(blockArray)):
        x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(blockArray[block])
        column = int(((min(x1, x2, x3, x4)-25)/50)-3)
        row = int((min(y1, y2, y3, y4)/50)-1)
        if (0 <= column) and (column < 9) and (0 <= row) and (row < 9):
            for checkBlock in range(len(allBlocks)):
                x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[checkBlock])
                checkColumn = int(((min(x1, x2, x3, x4)-25)/50)-3)
                checkRow = int((min(y1, y2, y3, y4)/50)-1)
                if (row == checkRow) and (column == checkColumn):
                    colliding = True
                    break
        else:
            inRange = False
            break
    if (inRange) and (not colliding):
        for block in range(len(blockArray)):
            allBlocks.append(blockArray[block])
        blockArray = []
        allBlocks, score = checkLine(allBlocks, score)
        displayScore(score, showScore)
        blocks()
            


def checkLine(allBlocks, score):
    '''
    Checks rows and columns to see if they are full, and deletes them if so
    '''
    delThese = []
    for checkBlock in range(len(allBlocks)):    #Loop through all blocks in the grid
        x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[checkBlock])   #gets the locations of the blocks
        checkColumn = int(((min(x1, x2, x3, x4)-25)/50)-3)
        checkRow = int((min(y1, y2, y3, y4)/50)-1)
        if checkColumn == 0:    #There is a block within the first column
            onRow = checkRow
            for nextBlock in range(len(allBlocks)):     #Loops through all blocks again
                x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[nextBlock])
                column = int(((min(x1, x2, x3, x4)-25)/50)-3)
                row = int((min(y1, y2, y3, y4)/50)-1)
                if (row == onRow):      #If a block is found in the same row
                    checkColumn += 1        #Next column must be checked
                if checkColumn == 9:        #If the row is full
                    for delBlocks in range(len(allBlocks)):
                        x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[delBlocks])
                        delRow = int((min(y1, y2, y3, y4)/50)-1)
                        if delRow == onRow:
                            delThese.append(allBlocks[delBlocks])    #Appends to a new array for blocks not to keep
    for checkBlock in range(len(allBlocks)):    #Loop through all blocks in the grid
        x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[checkBlock])   #gets the locations of the blocks
        checkColumn = int(((min(x1, x2, x3, x4)-25)/50)-3)
        checkRow = int((min(y1, y2, y3, y4)/50)-1)
        if checkRow == 0:    #There is a block within the first row
            onColumn = checkColumn
            for nextBlock in range(len(allBlocks)):     #Loops through all blocks again
                x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[nextBlock])
                column = int(((min(x1, x2, x3, x4)-25)/50)-3)
                row = int((min(y1, y2, y3, y4)/50)-1)
                if (column == onColumn):      #If a block is found in the same column
                    checkRow += 1        #Next row must be checked
                if checkRow == 9:       #If the row is full
                    for delBlocks in range(len(allBlocks)):
                        x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[delBlocks])
                        delColumn = int((min(x1, x2, x3, x4)-25)/50)-3
                        if delColumn == onColumn:
                            delThese.append(allBlocks[delBlocks])    #Appebds to a new array for blocks not to keep
    newArray = []
    for block in range(len(allBlocks)):
        if allBlocks[block] in delThese:
            canvas.delete(allBlocks[block])     #Deletes the blocks visually
            score += 1
        else:
            newArray.append(allBlocks[block])   #Deletes the blocks from the array
    allBlocks = newArray
    return allBlocks, score

def displayScore(score, showScore):
    '''
    Will display the score on the screen for the user to see
    '''
    canvas.itemconfig(showScore, text=("Score:", score))
    canvas.pack()
        
def blocks():
    '''
    Generates a random block out of 10 possible choices
    '''
    shape = random.randint(1, 11)
    colours = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#ffa500', '#800080']
    colour = colours[random.randint(0, 7)]
    global blockArray
    blockArray = []
    if shape == 1:
        #2x2
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(775, 600, 825, 600, 825, 650, 775, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(725, 700, 775, 700, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(825, 700, 775, 700, 775, 650, 825, 650, fill=colour, outline='#17287f')
    elif shape == 2:
        #Vertical 1x4
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(725, 650, 775, 650, 775, 700, 725, 700, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(725, 700, 775, 700, 775, 750, 725, 750, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(725, 800, 775, 800, 775, 750, 725, 750, fill=colour, outline='#17287f')
    elif shape == 3:
        #Horizontal 1x4
        block1 = canvas.create_polygon(725, 600, 925, 600, 925, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(825, 600, 775, 600, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(825, 600, 875, 600, 875, 650, 825, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(925, 600, 875, 600, 875, 650, 925, 650, fill=colour, outline='#17287f')
    elif shape == 4:
        #S
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(825, 600, 775, 600, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(825, 700, 775, 700, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(825, 700, 875, 700, 875, 650, 825, 650, fill=colour, outline='#17287f')
    elif shape == 5:
        #Backwards S
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(825, 600, 775, 600, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(825, 600, 775, 600, 775, 550, 825, 550, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(825, 600, 875, 600, 875, 550, 825, 550, fill=colour, outline='#17287f')
    elif shape == 6:
        #S Rotated 90 degrees clockwise
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(725, 700, 775, 700, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(725, 700, 675, 700, 675, 650, 725, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(725, 700, 675, 700, 675, 750, 725, 750, fill=colour, outline='#17287f')
    elif shape == 7:
        #Backwards S Rotated 90 degrees clockwise
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(725, 700, 775, 700, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(825, 700, 775, 700, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(825, 700, 775, 700, 775, 750, 825, 750, fill=colour, outline='#17287f')
    elif shape == 8:
        #T
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(725, 700, 775, 700, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(825, 700, 775, 700, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(725, 700, 675, 700, 675, 650, 725, 650, fill=colour, outline='#17287f')
    elif shape == 9:
        #T pointing up
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(725, 600, 775, 600, 775, 550, 725, 550, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(825, 600, 775, 600, 775, 550, 825, 550, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(725, 600, 675, 600, 675, 550, 725, 550, fill=colour, outline='#17287f')
    elif shape == 10:
        #T pointing right
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(725, 600, 675, 600, 675, 650, 725, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(725, 700, 675, 700, 675, 650, 725, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(725, 600, 675, 600, 675, 550, 725, 550, fill=colour, outline='#17287f')
    elif shape == 11:
        #T pointing left
        block1 = canvas.create_polygon(725, 600, 775, 600, 775, 650, 725, 650, fill=colour, outline='#17287f')
        block2 = canvas.create_polygon(825, 600, 775, 600, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block3 = canvas.create_polygon(825, 700, 775, 700, 775, 650, 825, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(825, 600, 775, 600, 775, 550, 825, 550, fill=colour, outline='#17287f')
    blockArray.append(block1)
    blockArray.append(block2)
    blockArray.append(block3)
    blockArray.append(block4) 
    return(blockArray)

def mainMenu():
    '''
    Generates the content of main menu and will allow the user to choose what to load next
    '''
    canvas = Canvas(window, width=800, height=700, bg='#47587f')
    canvas.pack()
    title = PhotoImage(file="title.png")        #Creates the title image and will display it at the top
    canvas.create_image(400, 100, image=title)
    canvas.image = title
    btn = None
    begin = True
    startBtn = Button(canvas, text=("Start Game"), command=lambda:startGame(begin, canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    startBtn.place(x=275, y=250)     #A button is created and placed here that will start the game when pressed
    ctrlBtn = Button(canvas, text=("Controls"), command=lambda:controls(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    ctrlBtn.place(x=275, y=350)     #A button is created and placed here that will start the game when pressed
    
def goBack(canvas):
    canvas.destroy()
    mainMenu()

def startGame(begin, canvas):
    '''
    Will initialise some variables for when the game begins
    '''
    global showScore
    if begin == True:
        canvas.destroy()
        canvas = configureCanvas()   #Destroys the current canvas and loads a new one
        showScore = canvas.create_text(325, 20, text=("Score:", score), fill='#ffffff', font=("Arial Bold", 50))
        blockArray = blocks()

def controls(canvas):
    '''
    Will allow the user to choose what controls to use
    '''
    canvas.destroy()
    canvas = Canvas(window, width=800, height=700, bg='#47587f')
    canvas.pack()
    rightBtn = Button(canvas, text=("Right"), command=lambda:inputs(True, "Right"), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    rightBtn.place(x=275, y=50)     
    leftBtn = Button(canvas, text=("Left"), command=lambda:inputs(True, "Left"), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    leftBtn.place(x=275, y=150)     
    upBtn = Button(canvas, text=("Up"), command=lambda:inputs(True, "Up"), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    upBtn.place(x=275, y=250)     
    downBtn = Button(canvas, text=("Down"), command=lambda:inputs(True, "Down"), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    downBtn.place(x=275, y=350)     
    enterBtn = Button(canvas, text=("Place"), command=lambda:inputs(True, "Return"), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    enterBtn.place(x=275, y=450)    
    backBtn = Button(canvas, text=("Return"), command=lambda:goBack(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    backBtn.place(x=275, y=600)     

def inputs(change, userInput):
    global r, l, u, d, enter
    if change == True:
        if userInput == "Right":
            window.bind('<KeyPress>', setRight)
            print("Bound to", r)
            change = False
        elif userInput == "Left":
            l = window.bind('<KeyPress>', setLeft)
            print("Bound to", l)
            change = False
        elif userInput == "Up":
            u = window.bind('<KeyPress>', setUp)
            print("Bound to", u)
            change = False
        elif userInput == "Down":
            d = window.bind('<KeyPress>', setDown)
            print("Bound to", d)
            change = False
        elif userInput == "Return":
            enter = window.bind('<KeyPress>', setPlace)
            print("Bound to", enter)
            change = False
        window.bind(r, moveRight)
        window.bind(l, moveLeft)
        window.bind(u, moveUp)
        window.bind(d, moveDown)
        window.bind(enter, placeBlock)

def setRight(event):
    global r
    print("Setting")
    got = False
    check = r
    while not got:
        r = event.keysym
        if r != check:
            got = True
    print(r)

def setLeft(event):
    l = StringVar()
    l.set(event.keysym)

def setUp(event):
    u = StringVar()
    u.set(event.keysym)

def setDown(event):
    d = StringVar()
    d.set(event.keysym)

def setPlace(event):
    enter = StringVar()
    enter.set(event.keysym)

window = Tk()
begin = False
allBlocks = []
blockArray = []
score = 0
r = "Right"
l = "Left"
u = "Up"
d = "Down"
enter = "Return"
configureWindow()
mainMenu()

gameLoop()
window.mainloop()