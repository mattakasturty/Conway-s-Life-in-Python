#CellArray.py
class CellArray:

	def __init__(self, size):
		"""
		Constructor - All cells initialized as dead (0)
		"""
		self.size = size
		self.board = []
		new = []
		for i in range(0, size, 1):
			for j in range(0, size, 1):
				new.append(0)
			self.board.append(new)
			new = []

	def __str__(self):
		"""
		Pretty prints a 2D array of 1's and 0's
		"""
		string = ""
		for i in self.board:
			for j in i:
				string += str(j)
			string += "\n"
		return string

	def step(self):
		"""
		Takes the next step in determining who lives and who dies
		"""
		newBoard = CellArray(self.size)
		for i in range(0, self.size, 1):
			for j in range(0, self.size, 1):
				newBoard.board[i][j] = self.changeCell(i, j)
		self.board = newBoard.board

	def changeCell(self, i, j):
		"""
		Takes a cell, and determines if it will live and die
		"""
		#If Cell is on Top row
		if(i==0):
			if(j==0):
				n = self.board[0][1] + self.board[1][0] + self.board[1][1]
			elif(j==(self.size-1)):
				n = self.board[0][self.size-2] + self.board[1][self.size-2] + self.board[1][self.size-1]
			else:
				n = self.board[0][j-1] + self.board[1][j] + self.board[0][j+1] + self.board[1][j-1] + self.board[1][j+1]
			
			if((n == 2 and self.board[i][j] == 1) or n == 3):
				return 1
			else:
				return 0
		#If Cell on Bottom row
		elif(i==(self.size-1)):
			if(j==0):
				n = self.board[self.size-1][1] + self.board[self.size-2][0] + self.board[self.size-2][1]
			elif(j==(self.size-1)):
				n = self.board[self.size-1][self.size-2] + self.board[self.size-2][self.size-2] + self.board[self.size-2][self.size-1]
			else:
				n = self.board[self.size-1][j-1] + self.board[self.size-2][j] + self.board[self.size-1][j+1] + self.board[self.size-2][j-1] + self.board[self.size-2][j+1]
			if((n == 2 and self.board[i][j] == 1) or n == 3):
				return 1
			else:
				return 0
		#If Cell is in a middle row
		else:
			if(j==0):
				n = self.board[i-1][j] + self.board[i+1][j] + self.board[i][j+1] + self.board[i-1][j+1] + self.board[i+1][j+1]
			elif(j==(self.size-1)):
				n = self.board[i-1][j] + self.board[i+1][j] + self.board[i][j-1] + self.board[i-1][j-1] + self.board[i+1][j-1]
			else:
				n = self.board[i-1][j] + self.board[i+1][j] + self.board[i][j-1] + self.board[i-1][j-1] + self.board[i+1][j-1] + self.board[i][j+1] + self.board[i-1][j+1] + self.board[i+1][j+1]
			if((n == 2 and self.board[i][j] == 1) or n == 3):
				return 1
			else:
				return 0


#Test, please ignore
if __name__ == "__main__":
	c = CellArray(4)
	c.board[0][1] = 1
	c.board[1][1] = 1
	c.board[1][0] = 1

	c.board[3][1] = 1
	c.board[2][1] = 1
	c.board[2][0] = 1

	c.board[1][2] = 1

	print(c)
	c.step()
	print(c)
	c.step()
	print(c)
