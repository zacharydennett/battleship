# This is a text version of a single player battleship game.
# No, it's not that much fun to play. But, interesting to code
# The ship is two squares long. 

import random

# Global variables
board = []  #Board is a list
shipLoc = {} # dictonary of ship coordinates
guess = {"col":0,"row":0} #Will be a set of coordinates in x,y
numMiss = 0 # Track the number of misses
numHits = 0 #Track number of hits

def createBoard(board):
	## Build Empty 5x5 board
	for x in range(0,5):
		board.append(["O"]*5)

def placeShip(shipLoc):
	## Figure out where the ship should go
	# First spot
	ship_row1 = random.randint(0,4)
	ship_col1 = random.randint(0,4)	

	# Direction
	direction = random.randint(0,1) # 0 means horizontal

	#Add second spot
	if direction == 0: #go horizontal
		if ship_col1 == 4: #already at right edge
			ship_col2 = 3
			ship_row2 = ship_row1
		else:
			ship_col2 = ship_col1 + 1
			ship_row2 = ship_row1
	else:
		if ship_row1 == 4: #already at bottom edge
			ship_row2 = 3
			ship_col2 = ship_col1
		else:
			ship_row2 = ship_row1 + 1
			ship_col2 = ship_col1
			
	shipLoc["ship_col1"] = ship_col1
	shipLoc["ship_col2"] = ship_col2
	shipLoc["ship_row1"] = ship_row1
	shipLoc["ship_row2"] = ship_row2

def printBoard(board):
	print "   A|B|C|D|E"
	print " -----------"
	for i in range(0,5):
		print str(i + 1) + "| " + " ".join(board[i])
		
def getUserGuess(guess):
	guessString = raw_input("Please enter a spot in the format A1: ")
	while len(guessString) != 2:
		guessString = raw_input("Invalid guess. Please enter a spot in the format A1: ")
	guessCol = guessString[0]
	guessRow = guessString[1]
	
	while guessRow.isdigit() == False or guessCol.isalpha() == False:
		guessString = raw_input("Invalid guess. Please enter a spot in the format A1: ")
		guessCol = guessString[0]
		guessRow = guessString[1]
	
	while int(guessRow) < 1 or int(guessRow) > 5:
		guessString = raw_input("Invalid guess. Row number must be 1 to 5. Guess again:")
		guessCol = guessString[0]
		guessRow = guessString[1]
	
	guessCol = guessCol.lower()	
	while guessCol != "a" and guessCol != "b" and guessCol != "c" and guessCol != "d" and guessCol != "e":
		guessString = raw_input("Invalid guess. Column must be A to E. Guess again: ")
		guessCol = guessString[0]
		guessRow = guessString[1]

	
	#Convert col to index
	colToIndex = {"a":0, "b":1, "c":2, "d":3, "e":4}
	guessCol = colToIndex[guessCol]
		
	guess["row"] = int(guessRow) - 1
	guess["col"] = int(guessCol)

def handleGuess(guess, shipLoc, board):
	""" Update the board based on user guess"""
	global numMiss
	global numHits
	if (guess["row"] == shipLoc["ship_row1"] and guess["col"] == shipLoc["ship_col1"])\
	or (guess["row"] == shipLoc["ship_row2"] and guess["col"] == shipLoc["ship_col2"]): # Correct guess
		print "****"
		print "HIT!"
		board[guess["row"]][guess["col"]] = "!"
		numHits += 1
	else:
		print "****"
		print "Miss"
		board[guess["row"]][guess["col"]] = "-"
		numMiss += 1
		
		
createBoard(board)
placeShip(shipLoc)

print "****** WELCOME TO ZACH'S VERSION OF BATTLESHIP ******"
printBoard(board)
for i in range(0,10): # set to 10 to catch my error when I set a non ending loop
	getUserGuess(guess)
	handleGuess(guess, shipLoc, board)
	printBoard(board)
	if numMiss > 10:
		print "You ran out of turns."
		break
	if numHits == 2:
		print "******* WINNER ********"
		break
	
# Show locations
if numHits != 2:
	board[shipLoc["ship_row1"]][shipLoc["ship_col1"]] = "!"
	board[shipLoc["ship_row2"]][shipLoc["ship_col2"]] = "!"
	printBoard(board)

print "Thanks for playing"

