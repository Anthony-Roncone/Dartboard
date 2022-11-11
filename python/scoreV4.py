from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('280x200+700+400')
global score1, score2, current
score1 = score2 = 360
current = 0

num_vars = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

#reset both players scores to 360
def resetScore():
    global score1, score2
    score1 = score2 = 360
    scoreLabel1.config(text=score1)
    scoreLabel2.config(text=score2)

#updates the score
def updateScores(event=4):
    global score1,score2,current
    try:
        temp1 = int(num_vars[0].get())
    except ValueError:
        temp1 = 0
        
    try:
        temp2 = int(num_vars[1].get())
    except ValueError:
        temp2 = 0
        
    try:
        temp3 = int(num_vars[2].get())
    except ValueError:
        temp3 = 0

    try:
        temp4 = int(num_vars[3].get())
    except ValueError:
        temp4 = 0
        
    try:
        temp5 = int(num_vars[4].get())
    except ValueError:
        temp5 = 0
        
    try:
        temp6 = int(num_vars[5].get())
    except ValueError:
        temp6 = 0
        
    Tscore1 = score1 - (temp1 + temp2 + temp3)
    Tscore2 = score2 - (temp4 + temp5 + temp6)
    numbers[0].delete(0,END)
    numbers[1].delete(0,END)
    numbers[2].delete(0,END)
    numbers[3].delete(0,END)
    numbers[4].delete(0,END)
    numbers[5].delete(0,END)
    current=0
    numbers[current].focus_set()
    if Tscore1 >= 0:
        score1 = Tscore1
    if Tscore2 >= 0:
        score2 = Tscore2
    scoreLabel1.config(text=score1)
    scoreLabel2.config(text=score2)

def changeFocus(event):
    global current
    current = (current+1) % 6
    numbers[current].focus_set()
    
def changeFocus2(event):
    global current
    try:
        temp = int(num_vars[current].get())
    except ValueError:
        temp = 0
    numbers[current].delete(0,END)
    numbers[current].insert(0,temp*2)
    current = (current+1) % 6
    numbers[current].focus_set()
    
def changeFocus3(event):
    global current
    try:
        temp = int(num_vars[current].get())
    except ValueError:
        temp = 0
    numbers[current].delete(0,END)
    numbers[current].insert(0,temp*3)
    current = (current+1) % 6
    numbers[current].focus_set()
    
def updateFocus(event,x):
    global current
    current = x

def char_limit(text):
    if len(text.get()) > 2:
        text.delete(2,END)

#frm = ttk.Frame(root, padding=50)
#frm.grid()
#frm.place()
ttk.Label(root, text="Player 1").grid(padx=15,column=0,row=0)
ttk.Label(root, text="Player 2").grid(padx=15,column=2,row=0)

scoreLabel1 = ttk.Label(root, text=score1)
scoreLabel2 = ttk.Label(root, text=score2)
scoreLabel1.grid(column=0,row=1)
scoreLabel2.grid(column=2,row=1)

#creating list of input boxes for score. one box per dart
numbers = []
numbers.append(Entry(root, textvariable=num_vars[0], width=2))
numbers.append(Entry(root, textvariable=num_vars[1], width=2))
numbers.append(Entry(root, textvariable=num_vars[2], width=2))
numbers.append(Entry(root, textvariable=num_vars[3], width=2))
numbers.append(Entry(root, textvariable=num_vars[4], width=2))
numbers.append(Entry(root, textvariable=num_vars[5], width=2))

#placing input boxes on screen
#ttk.Label(root).grid(column=0,row=2)
numbers[0].grid(column=0,row=2, sticky='W')
numbers[1].grid(column=1,row=2)
numbers[2].grid(column=2,row=2)

numbers[3].grid(column=2,row=2, sticky='W')
numbers[4].grid(column=1,row=2)
numbers[5].grid(column=2,row=2)

numbers[1].place(x=30,y=38)
numbers[2].place(x=60,y=38)

numbers[4].place(x=225,y=38)
numbers[5].place(x=255,y=38)

#creating and placing buttons to add functionality
ttk.Button(root, text="Remove points", command = updateScores).grid(pady=5,column=1,row=3)
ttk.Button(root, text="Reset Points", command = resetScore).grid(pady=5,column=1,row=4)
ttk.Button(root, text="Quit", command = root.destroy).grid(pady=5,column=1,row=5)

#when app first launches makes it auto focus on first input box
numbers[current].focus_set()

#updates a varibale that keeps track of wich input box has focus
numbers[0].bind("<FocusIn>", lambda event, x=0:updateFocus(event,x))
numbers[1].bind("<FocusIn>", lambda event, x=1:updateFocus(event,x))
numbers[2].bind("<FocusIn>", lambda event, x=2:updateFocus(event,x))
numbers[3].bind("<FocusIn>", lambda event, x=3:updateFocus(event,x))
numbers[4].bind("<FocusIn>", lambda event, x=4:updateFocus(event,x))
numbers[5].bind("<FocusIn>", lambda event, x=5:updateFocus(event,x))

#can press enter to go to next input box
numbers[0].bind("<Return>", changeFocus)
numbers[0].bind("<Shift-Return>", changeFocus2)
numbers[0].bind("<Control-Return>", changeFocus3)

numbers[1].bind("<Return>", changeFocus)
numbers[1].bind("<Shift-Return>", changeFocus2)
numbers[1].bind("<Control-Return>", changeFocus3)

numbers[2].bind("<Return>", changeFocus)
numbers[2].bind("<Shift-Return>", changeFocus2)
numbers[2].bind("<Control-Return>", changeFocus3)

numbers[3].bind("<Return>", changeFocus)
numbers[3].bind("<Shift-Return>", changeFocus2)
numbers[3].bind("<Control-Return>", changeFocus3)

numbers[4].bind("<Return>", changeFocus)
numbers[4].bind("<Shift-Return>", changeFocus2)
numbers[4].bind("<Control-Return>", changeFocus3)

numbers[5].bind("<Return>", changeFocus)
numbers[5].bind("<Shift-Return>", changeFocus2)
numbers[5].bind("<Control-Return>", changeFocus3)

#submit numbers entered in boxes to update the scores
numbers[0].bind("<Alt-Return>", updateScores)
numbers[1].bind("<Alt-Return>", updateScores)
numbers[2].bind("<Alt-Return>", updateScores)
numbers[3].bind("<Alt-Return>", updateScores)
numbers[4].bind("<Alt-Return>", updateScores)
numbers[5].bind("<Alt-Return>", updateScores)

#limit number of character that can be enter in input box
num_vars[0].trace("w", lambda *args: char_limit(numbers[0]))
num_vars[1].trace("w", lambda *args: char_limit(numbers[1]))
num_vars[2].trace("w", lambda *args: char_limit(numbers[2]))
num_vars[3].trace("w", lambda *args: char_limit(numbers[3]))
num_vars[4].trace("w", lambda *args: char_limit(numbers[4]))
num_vars[5].trace("w", lambda *args: char_limit(numbers[5]))

root.mainloop()        
        