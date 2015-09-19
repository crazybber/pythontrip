# GUI
# python for tkinter nature

from tkinter import *

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel=Label(self,text='Hello World')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit app')
		self.quitButton.pack()


app = Application()
app.master.title('Hello world gui')
app.mainloop()