#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the buttons, the oval moves to the left or right

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="blue")

class MyApp:
	def __init__(self, parent):
	     
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		#left
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.grid(row=0,column=0)
		self.button1.bind("<Button-1>", self.button1Click)
		#right
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "purple")
		self.button2.grid(row=0,column=1)
	        self.button2.bind("<Button-1>", self.button2Click)
				
		
						
													
		
		
		drawpad.pack()
		

		
	def button1Click(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		
		drawpad.move(oval,-10,0)
		
	def button2Click(self, event):   
		
		global oval
		global drawpad
		
		drawpad.move(oval,10,0)
		
	
	# Add the event handler for the second button to make it move right!
	
		
myapp = MyApp(root)
root.mainloop()