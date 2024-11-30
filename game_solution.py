'''
File name: BlockBust.py
Author: Max Donnelly
Version: 1.1.14
'''

from tkinter import *
from PIL import Image, ImageTk
import random
import time
from threading import Thread

def gameLoop():
    pass

def configureWindow():
    '''
    Will set up the window that the game is played in
    '''
    window.geometry("900x700")  # Sets the size of the window
    window.configure(background='#47587f')  # Sets the background colour of the window
    window.title("B l o c k   B u s t")     # Creates a title for the game window

def configureCanvas():
    '''
    Initialises the canvas, creating the grid on which the game is played
    '''
    global canvas
    canvas = Canvas(window, width=800, height=700)  #Creates a canvas to draw the game onto
    gameGrid = canvas.create_rectangle(175, 50, 625, 500, fill='#37487f', outline='#17287f')
    for i in range(9):  # Loops through every column, creating the columns of the grid
        canvas.create_rectangle(175 + (i * 50), 50, 225 + (i * 50), 500, outline='#17287f')
    for i in range(9):  # Loops through every row, creating the wors of the grid
        canvas.create_rectangle(175, 50 + (i * 50), 625, 100 + (i * 50), outline='#17287f')
    canvas.configure(background='#47587f')
    quitBtn = Button(canvas, text=("Surrender"), command=lambda:gameOver(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    quitBtn.place(x=50, y=600)  # Creates and places a button that lets the user give up and go to the lose screen
    canvas.pack(fill="both", expand=True)
    return canvas
    
def gameOver(canvas):
    canvas.destroy()    # Removes everything from the canvas
    canvas = Canvas(window, width=900, height=700, bg='#47587f')
    canvas.pack(fill="both", expand=True)
    loseText = Label(canvas, text=("Game over"), font=("Arial Bold", 50), bg='#47587f')     # Displays the game over text
    scoreText = Label(canvas, text=("You scored: " + str(score)), font=("Arial Bold", 50), bg='#47587f')    # Displays the players final score
    loseText.grid(column=4, row=1, sticky=N)
    scoreText.grid(column=4, row=2, sticky=N)   # Places the game over text and the players score
    nameBox = Text(canvas, height = 3, width = 40)
    canvas.create_window(200, 200, window=nameBox)  # Creates a window for the user to input their name
    submitName = None
    submitName = Button(canvas, text="Submit", command=lambda:getUserInput(nameBox))    # Records the users name to put on th leaderboard
    submitName.place(x=50, y=250)
    leaderboardBtn = Button(canvas, text=("Leaderboard"), command=lambda:leaderboard(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    leaderboardBtn.place(x=50, y=300)   # Places a button for the user to submit their score to the leaderboard
    backBtn = Button(canvas, text=("Main Menu"), command=lambda:backToMenu(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    backBtn.place(x=50, y=400)  # Places a button for the user to return to the start screen

def leaderboard(canvas):
    '''
    Takes in the canvas as a parameter
    Searches through the leaderboard text file amd displays the top five names in order
    '''
    canvas.destroy()    # Clears all items on the canavs
    canvas = Canvas(window, width=800, height=700, bg='#47587f')
    canvas.pack(fill="both", expand=True)
    count = 0   # Initialises a value called count to keep track of where it is in the text file
    file = open("leaderboard.txt", "r") # Opens the leaderboard text file
    first = 0
    second = 0
    third = 0
    fourth = 0
    fivth = 0   # Initialises five variables to hold the scores of the top 5 players
    firstPlayer = ""
    secondPlayer = ""
    thirdPlayer = ""
    fourthPlayer = ""
    fivthPlayer = ""    # Initialises five variables to store the names of the top 5 playes
    for line in file:   # Increments through each line in the text file
        length = len(line)
        line = line[0:length-1] # Removes the new line character at the end of each line when taking it in
        if (count % 2) == 1:    # Reads only the scores
            gotScore = int(line)
            count += 1
            if int(gotScore) > first:   # Will sort the names into the top 5 using their scores
                first = gotScore
                firstPlayer = gotName
            elif int(gotScore) > second:
                second = gotScore
                secondPlayer = gotName
            elif int(gotScore) > third:
                third = gotScore
                thirdPlayer = gotName
            elif int(gotScore) > fourth:
                fourth = gotScore
                fourthPlayer = gotName
            elif int(gotScore) > fivth:
                fivth = gotScore
                fivthPlayer = gotName
        else:
            gotName = line
            count += 1
    file.close()    # Closes the leaderboard file
    firstText = Label(canvas, text=("1: " + firstPlayer + "    " + str(first)), font=("Arial Bold", 50), bg='#47587f')
    secondText = Label(canvas, text=("2: " + secondPlayer + "    " + str(second)), font=("Arial Bold", 50), bg='#47587f')
    thirdText = Label(canvas, text=("3: " + thirdPlayer + "    " + str(third)), font=("Arial Bold", 50), bg='#47587f')
    fourthText = Label(canvas, text=("4: " + fourthPlayer + "    " + str(fourth)), font=("Arial Bold", 50), bg='#47587f')
    fivthText = Label(canvas, text=("5: " + fivthPlayer + "    " + str(fivth)), font=("Arial Bold", 50), bg='#47587f')  # Displays the top five players along with their scores
    firstText.grid(column=4, row=1, sticky=N)
    secondText.grid(column=4, row=2, sticky=N)
    thirdText.grid(column=4, row=3, sticky=N)
    fourthText.grid(column=4, row=4, sticky=N)
    fivthText.grid(column=4, row=5, sticky=N)
    backBtn = Button(canvas, text=("Main Menu"), command=lambda:backToMenu(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    backBtn.place(x=50, y=500)  # Creates and displays a button that allows the user to return to the start screen

def getUserInput(nameBox):
    '''
    Takes in nameBox, where the user inputs their name, as an input
    Writes the users inputted name and their score to the leaderboard file
    '''
    global name
    name = nameBox.get("1.0", "end-1c") # Reads the name that the user has inputted
    names = open("leaderboard.txt", "a")    # Opens the leaderboard file and writes to it
    names.write(name)
    names.write("\n")
    names.write(str(score))
    names.write("\n")
    names.close()
    

def keyPressed(event):
    '''
    Takes in event as a parameter, so will run when a bound key is pressed
    Decides what will occur in the event of the user pressing a key
    '''
    move = event.keysym     # Reads the players input
    global blockArray, allBlocks, score, showScore, timerID, firstTime, countDown
    if (move == "Right") or (move == "d"):  # Will check if the user is pressing a key bound to right
        if paused == False:     # Will check if the game is paused or not
            for block in range(len(blockArray)):    # Moves every block that is in the active block array in the directin the user wants
                canvas.move(blockArray[block], 50, 0)
    elif (move == "Left") or (move == "a"): #   Checks if the user is pressing a key bound to left
        if paused == False:
            for block in range(len(blockArray)):
                canvas.move(blockArray[block], -50, 0)
    elif (move == "Up") or (move == "w"):   # Checks if the user is pressing a key bound to up
        if paused == False:
            for block in range(len(blockArray)):
                canvas.move(blockArray[block], 0, -50)
    elif (move == "Down") or (move == "s"):     # Checks if the user is pressing a key bound to down
        if paused == False:
            for block in range(len(blockArray)):
                canvas.move(blockArray[block], 0, 50)
    elif (move == "Return") or (move == "space"):   # Checks if the user is pressing a key bound to place
        if paused == False:
            inRange = True
            colliding = False   # Sets the flags colliding and inRange to check if the block can be placed validly
            for block in range(len(blockArray)):    # Icrements through every block in the active block array   
                x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(blockArray[block])   # Gets the coordinates of each corner of each block
                column = int(((min(x1, x2, x3, x4)-25)/50)-3)   # Calculates the column and row that the block is in
                row = int((min(y1, y2, y3, y4)/50)-1)
                if (0 <= column) and (column < 9) and (0 <= row) and (row < 9):     # Checks that the block is within the grid where the game is played
                    for checkBlock in range(len(allBlocks)):    # Searches through every block again to get their positions to ensure that the new block is not being placed on top of another
                        x1, y1, x2, y2, x3, y3, x4, y4 = canvas.coords(allBlocks[checkBlock])
                        checkColumn = int(((min(x1, x2, x3, x4)-25)/50)-3)
                        checkRow = int((min(y1, y2, y3, y4)/50)-1)
                        if (row == checkRow) and (column == checkColumn):   # Will run if there is a collision between blocks
                            colliding = True    # Sets this flag to true to show there is a collision
                            break
                else:
                    inRange = False     # If the user tries to place the block outside of the game grid, this flag is set to false
                    break
            if (inRange) and (not colliding):   # Runs if the conditions are met to place a block successfully
                for block in range(len(blockArray)):    # Increments through every block in the active array and adds them to the all blocks array
                    allBlocks.append(blockArray[block])
                blockArray = []     # Sets the active block array to empty, so the user cannot move the blocks anymore
                allBlocks, score = checkLine(allBlocks, score)  # Checks to see if nine blocks are in a row
                countDown = 30
                showTime = Label(canvas, text=("Time:", countDown), background='#47587f', font=("Arial Bold", 40))
                showTime.place(x=500, y=-15)
                displayScore(score, showScore)  # Displays the score that the user is at on the screen
                if firstTime == False:  # Will run if this function has been ran befpre
                    window.after_cancel(timerID)    # Displays the timer
                else:
                    firstTime = False
                t1 = Thread(target = timer(True, showTime, False, False, False, paused))
                t2 = Thread(target = blocks)    # Simultaniously sets the timer and allows the user to control the blocks
                t1.start()
                t2.start()
    elif move == "1":   # If the first cheatcode is pressed
        window.after_cancel(timerID)    # Stops the old timer
        countDown = 3   # Sets the timer to only have 3 seconds left
        showTime = Label(canvas, text=("Time:", countDown), background='#47587f', font=("Arial Bold", 40))
        timer(False, showTime, True, False, True, paused)   # Calls the timer function
    elif move == "2":   # If the second cheatcode is pressed
        window.after_cancel(timerID) 
        countDown = 1000    # Sets the time to 1000
        showTime = Label(canvas, text=("Time:", countDown), background='#47587f', font=("Arial Bold", 40))
        timer(False, showTime, False, True, True, paused)   # Calls the timer function
    elif move == "3":   # If the third cheatcode is pressed
        for block in range(len(allBlocks)):     # Increments through every block and sets them to red
            canvas.itemconfig(allBlocks[block], fill='#ff0000')
    elif move == "p":   # If the user presses pause
        pause()
    elif move == "b":   # If the user presses the boss key
        bossKey()

def bossKey():
    '''
    Wil enable or disable the boss key image if the correct key is pressed
    '''
    global bossActive, bossImage
    boss = PhotoImage(file="boss.png") # Sets the boss key to the image named boss.png
    if bossActive == False:        # Creates the title image and will display it at the top
        bossImage = canvas.create_image(400, 350, image=boss)   # Creates the image on the canvas
        canvas.image = boss
        canvas.pack()
        bossActive = True
    else:
        canvas.delete(bossImage)    # If the boss key is pressed a second time the image will be deleted
        bossActive = False

def pause():
    '''
    Will run if the pause key is pressed and will pause/unpause the timer and the players ability to move or place blocks
    '''
    global paused, pauseTimer, timePaused, countDown
    if paused == False: # If the game is not already paused
        timePaused = countDown
        window.after_cancel(timerID)    # Closes the pause
        paused = True
    else:
        resume()    # Runs if the game is already paused

def resume():
    '''
    Will run if the pause key is pressed to unpause the game, resuming block movement and the timer
    '''
    global paused, pauseTimer, timePaused, countDown
    if paused == True:
        paused = False
        showTime = Label(canvas, text=("Time:", timePaused), background='#47587f', font=("Arial Bold", 40))
        showTime.place(x=500, y=-15)    # Initialises and places the timer again
        countDown = timePaused
        pauseTimer = window.after(1000, timer, True, showTime, False, False, False, False)  # Restart the timer from where it left off
        displayScore(score, showScore)  # Shows the players score

def timer(reset, showTime, cheat1, cheat2, cheated, paused):
    '''
    Takes in mutiple paramaters - reset if a new timer is being initiallised, showTime to display the function, cheat1 if the first cheat is active, cheat2 if the second cheat is active, cheated if a cheat was ran, and paused if the game is paused
    Will run the logic for counting down the score or setting it to new values when cheats are ran. Loads the game over screen if time reaches 0
    '''
    global timerID, countDown, pauseTimer
    cheated = False
    if cheat1 == True:  # Will run if the first cheat is active
        maxTime = 3     # Sets the timer to 3
        countDown = 3
        showTime.configure(text=("Time: Pressed"))
        cheat1 = False
        cheated = True
    elif cheat2 == True:    # Will run if the second cheat is active
        maxTime = 1000      # Sets tje timer to 10000
        countDown = 1000
        showTime.configure(text=("Time:", countDown))
        cheat2 = False
        cheated = True
    elif cheated == False:  # If a cheat was not run, gradually decreases maxtime based on score
        if score > 150:
            maxTime = 3
        elif score > 100:
            maxTime = 5
        elif score > 70:
            maxTime = 10
        elif score > 50:
            maxTime = 15
        elif score > 20:
            maxTime = 20
        else:
            maxTime = 30
    if reset:   # Runs when the code needs to be initialised 
        countDown = maxTime  # Reset the timer to the max time when it's first called.
        reset = False
    elif paused == False:   # Runs if the game is paused
        countDown -= 1      # Decrements the timer
    if countDown <= 0:      # If the timer reaches 0, run the gameover screen
        gameOver(canvas)
    else:
        # Call the startTimer function again after 1000 ms (1 second)
        showTime.configure(text=("Time:", countDown))
        timerID = window.after(1000, timer, False, showTime, cheat1, cheat2, cheated, paused)

def checkLine(allBlocks, score):
    '''
    Takes in allBlocks as a paramater, which is an array holding every block on the grid, and the players score is taken in too
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
    Takes in the players score and the label showing it as paramaters
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
        block3 = canvas.create_polygon(825, 700, 875, 700, 875, 650, 825, 650, fill=colour, outline='#17287f')
        block4 = canvas.create_polygon(925, 700, 875, 700, 875, 650, 925, 650, fill=colour, outline='#17287f')
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
    startBtn.place(x=250, y=250)     #A button is created and placed here that will start the game when pressed
    ctrlBtn = Button(canvas, text=("Controls"), command=lambda:controls(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    ctrlBtn.place(x=250, y=350)     #A button is created and placed here that will start the game when pressed
    leaderboardBtn = Button(canvas, text=("Leaderboard"), command=lambda:leaderboard(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    leaderboardBtn.place(x=250, y=450)

def startGame(begin, canvas):
    '''
    Takes in begin - if the game needs to be ran - and the canvas that the game is drawn on as parameters
    Will initialise some variables for when the game begins
    '''
    global showScore, score
    if begin == True:
        canvas.destroy()
        score = 0
        canvas = configureCanvas()   #Destroys the current canvas and loads a new one
        showScore = canvas.create_text(325, 20, text=("Score:", score), fill='#ffffff', font=("Arial Bold", 50))
        blockArray = blocks()   # Generates a random block

def controls(canvas):
    '''
    Takes in the canvas that the game is drawn in as a paramater
    Will allow the user to choose what controls to use
    '''
    canvas.destroy()    # Destroys and creates a new canvas
    canvas = Canvas(window, width=800, height=700, bg='#47587f')
    canvas.pack()
    moveBtn = Button(canvas, text=(moveText), command=lambda:moveBinds(moveBtn), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    moveBtn.place(x=250, y=250)     # Creates and displays a button to change the move controls
    placeBtn = Button(canvas, text=(placeText), command=lambda:placeBinds(placeBtn), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    placeBtn.place(x=250, y=350)    # Creates and displays a button to change the place contols
    backBtn = Button(canvas, text=("Return"), command=lambda:backToMenu(canvas), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
    backBtn.place(x=250, y=500)     # Creates and displays a button to return back to the main menu

def backToMenu(canvas):
    '''
    Takes in the current canvas as a paramater
    Will clear the canvas before loading the main menu
    '''
    canvas.destroy()
    mainMenu()

def moveBinds(moveBtn):
    '''
    Takes in the move button as a paramater
    Binds the movement keys to arrows or WASD depending on the players choice
    '''
    moveText = getMoveText(1)
    if moveText == "Move: WASD":    # If move is currently set to WASD, change it to arrows
        moveBtn.configure(text=moveText)    # Changes the text on the move button
        window.bind('<w>', keyPressed)  # binds the new keys
        window.bind('<a>', keyPressed)
        window.bind('<s>', keyPressed)
        window.bind('<d>', keyPressed)
        window.unbind('<Right>')    # Unbinds the old keys
        window.unbind('<Left>')
        window.unbind('<Up>')
        window.unbind('<Down>')
    elif moveText == "Move: Arrows":    # If move is currently set to arrows, change it to WASD
        moveBtn.configure(text=moveText)
        window.bind('<Right>', keyPressed)  # Binds the new keys
        window.bind('<Left>', keyPressed)
        window.bind('<Up>', keyPressed)
        window.bind('<Down>', keyPressed)
        window.unbind('<w>')    # Unbinds the old keys
        window.unbind('<a>')
        window.unbind('<s>')
        window.unbind('<d>')

def getMoveText(num):
    '''
    Takes in  number as a parameter, either 1 or 0 to tell it what operation to do
    If the number is 1, initiallises movement ot the arrows. Otherwise change the movement to the opposite
    '''
    global moveText
    if num == 0:
        moveText = "Move: Arrows"
    elif num ==1:
        if moveText == "Move: Arrows":
            moveText = "Move: WASD"
        elif moveText == "Move: WASD":
            moveText = "Move: Arrows"
    return moveText

def getPlaceText(num):
    '''
    Takes in  number as a parameter, either 1 or 0 to tell it what operation to do
    If the number is 1, initiallises placement as enter. Otherwise change the placement to the opposite
    '''
    global placeText
    if num == 0:
        placeText = "Place: Enter"
    elif num == 1:
        if placeText == "Place: Enter":
            placeText = "Place: Space"
        elif placeText == "Place: Space":
            placeText = "Place: Enter"
    return placeText

def placeBinds(placeBtn):
    '''
    Takes in the place button as a paramater
    Binds the players place key to either enter or space depending on the users choice
    '''
    placeText = getPlaceText(1)
    if placeText == "Place: Enter":
        placeText = "Place: Space"
        placeBtn.configure(text=placeText)
        window.bind('<space>', keyPressed)
        window.unbind('<Return>')
    elif placeText == "Place: Space":
        placeText = "Place: Enter"
        placeBtn.configure(text=placeText)
        window.bind('<Return>', keyPressed)
        window.unbind('<space>')

window = Tk()
begin = False
allBlocks = []
global score
score = 0
paused = False
timePaused = 0
pauseTimer = 0
bossActive = False
bossImage = None
global moveText, placeText, firstTime
firstTime = True
moveText = getMoveText(0)
moveBtn = Button(window, text=(moveText), command=lambda:moveBinds(moveBtn), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
placeText = getPlaceText(0)
placeBtn = Button(window, text=(placeText), command=lambda:placeBinds(placeText, placeBtn), background='#AAAAAA', font=('Arial Bold', 30), width = 10, height = 1)
moveBinds(moveBtn)
placeBinds(placeBtn)
configureWindow()
mainMenu()

window.bind('1', keyPressed)    # Binds keys
window.bind('2', keyPressed)
window.bind('3', keyPressed)
window.bind('p', keyPressed)
window.bind('b', keyPressed)

gameLoop()
window.mainloop()