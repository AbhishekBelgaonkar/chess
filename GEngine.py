# determines the valid moves
class game():
	def __init__(self): #constructor
		self.board = [ #first char of element represents color "--" is empty space
			["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
			["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
			["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
		]
		self.whitetomove = True
		self.movelog = []
	def makemove(self, move):
		self.board[move.startrow][move.startcol] = "--" # sets old location as empty space
		self.board[move.endrow][move.endcol] = move.piecemoved
		self.movelog.append(move) # logs the moves made
		self.whitetomove = not self.whitetomove # witch players
	def undomove(self):
		if len(self.movelog) != 0:
			move = self.movelog.pop() # removes latest entry from movelog
			self.board[move.startrow][move.startcol] = move.piecemoved
			self.board[move.endrow][move.endcol] = move.captured
			self.whitetomove = not self.whitetomove # switch turns

class move():
	# maps keys to values
	# key : value
	# a rank is the number of a sqaure like a8 that means 8 is the rank it is the row
	# a file is the column like a8 that means a is the file
	rankstorows = {"1":7,"2":6,"3":5,"4":4,
				   "5":3,"6":2,"7":1,"8":0} # dictionary mapping ranks to the rows
	rowstoranks = {v :k for k, v in rankstorows.items()} # idk how this works
	filestocols = {"a":0,"b":1,"c":2,"d":3,
				   "e":4,"f":5,"g":6,"h":7} # mappping files to columns
	colstofiles = {v :k for k, v in filestocols.items()}
	def __init__(self, startsq, endsq, board):
		self.startrow = startsq[0]
		self.startcol = startsq[1]
		self.endrow = endsq[0]
		self.endcol = endsq[1]
		self.piecemoved = board[self.startrow][self.startcol]
		self.captured = board[self.endrow][self.endcol]
	def getchessnotation(self):
		return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)
	def getrankfile(self, r, c):
		return self.colstofiles[c] + self.rowstoranks[r] # we doing col + rank cause the position is always written with letter first then rank


