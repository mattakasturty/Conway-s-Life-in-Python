from tkinter import *
from CellArray import *
import time
from tkinter import filedialog


class CellCanvas(Canvas):
	def __init__(self,master,*args,**kwargs):
		Canvas.__init__(self, master=master, *args, **kwargs)
		
		self.buttonFrame = Frame(master)
		self.buttonFrame.pack(side = BOTTOM)

		self.bind("<Button-1>", self.click)

		self.gameArray =  CellArray(20)
		
		self.stepButton = Button(self.buttonFrame, text = "Step", command = self.Step)
		self.runButton = Button(self.buttonFrame, text = "Run", command = self.Run)
		self.clearButton = Button(self.buttonFrame, text = "Clear", command = self.Clear)
		self.saveButton = Button(self.buttonFrame, text = "Save", command = self.Save)
		self.loadButton = Button(self.buttonFrame, text = "Load", command = self.Load)
		self.exitButton = Button(self.buttonFrame, text = "Quit", command = self.Quit)
		

		self.stepButton.pack(side = LEFT)
		self.runButton.pack(side = LEFT)
		self.clearButton.pack(side = LEFT)
		self.saveButton.pack(side = LEFT)
		self.loadButton.pack(side = LEFT)
		self.exitButton.pack(side = LEFT)

		self.Update()

	def Step(self, i = 0):
		self.gameArray.step()
		self.Update()
		if(i):
			if(self.runButton["text"] == "Run"):
				return
			self.after(500, lambda: self.Step(i))


	def Run(self):
		if(self.runButton["text"] == "Run"):
			self.runButton["text"] = "Stop"
			self.Step(1)
		else:
			self.runButton["text"] = "Run"


	def Clear(self):
		self.gameArray = CellArray(20)
		self.Update()

	def Quit(self):
		quit()

	def Update(self):
		for row in range(0, self.gameArray.size, 1):
			for col in range(0, self.gameArray.size, 1):
				if(self.gameArray.board[row][col]):
					self.create_rectangle(row*25, col*25, row*25+25, col*25+25, fill="white", outline = "black")
				else:
					self.create_rectangle(row*25,col*25 , row*25+25, col*25+25, fill="black", outline = "white")

	def click(self, event):
		i = event.x // 25
		j = event.y // 25
		if(self.gameArray.board[i][j] == 1):
			self.gameArray.board[i][j] = 0
		else:
			self.gameArray.board[i][j] = 1
		self.Update()

	def Save(self):
		file = filedialog.asksaveasfile(mode='w',
			defaultextension=".pylife",
			title = "Select a file to save to, or enter your own",
			filetypes=(("PyLife files", "*.pylife"),("All files", "*.*") ))
		if(file == None):
			return
		file.write(str(self.gameArray.size)+"\n")
		for i in self.gameArray.board:
			for j in i:
				file.write(str(j) + " ")
			file.write("\n")
		file.close()

	def Load(self):
		#file = open("test", "r")
		file = filedialog.askopenfile(mode ='r', 
			title = "Select a file to load from", 
			filetypes=(("PyLife files", "*.pylife"),("All files", "*.*") ))
		if(file == None):
			return
		nums = []
		lines = file.readlines()
		self.gameArray =  CellArray(int(lines[0].rstrip("\n")))
		lines = lines[1:]
		for line in lines:
			line = line[:-2]
			nums.append(line.split(" "))
		for i in range(0, len(nums), 1):
			nums[i] = list(map(int, nums[i]))
		self.gameArray.board = nums
		file.close()
		self.Update()
		

if __name__ == "__main__":
	window = Tk()
	window.geometry("500x550")
	canvas = CellCanvas(window, width=500, height=500)
	canvas.pack()
	window.mainloop()
	

