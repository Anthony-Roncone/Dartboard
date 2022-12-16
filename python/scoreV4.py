from tkinter import *
from tkinter import ttk
#from tkinter.ttk import *
#import tkinter as tk
#import ttk

root = Tk()
#root.geometry('285x200+700+400')
root.attributes('-fullscreen',True)
root.config(bg='#808080')
global score1, score2, tScore1, tScore2, current, total, tempTF, win
tempTF = [False,False,False,False,False,False]
win = False
total = 501
score1 = score2 = tScore1 = tScore2 = total
current = 0

num_vars = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

#reset both players scores
def resetScore(event):
    global score1, score2, total, win
    score1 = score2 = total
    numbers[0].delete(0,END)
    numbers[1].delete(0,END)
    numbers[2].delete(0,END)
    numbers[3].delete(0,END)
    numbers[4].delete(0,END)
    numbers[5].delete(0,END)
    numbers[0].focus_set()
    win = False
    scoreLabel1.config(text=score1)
    scoreLabel2.config(text=score2)

#updates the score
def updateScores(event=4):
    global score1,score2,tScore1,tScore2,current,tempTF
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
    tScore1 = score1
    tScore2 = score2
    tempTF = [False,False,False,False,False,False]
    scoreLabel1.config(text=score1)
    scoreLabel2.config(text=score2)

def changeTempScore(temp, double=False):
    global tScore1,tScore2,tempTF,current
    if current < 3 and tempTF[current] == False:
        temp = tScore1 - temp
        tempTF[current] = True
        if double == True and temp == 0:
            scoreLabel1.config(text="Winner!!!")
            winner()
        elif temp >= 2:
            tScore1 = temp 
            scoreLabel1.config(text=tScore1)
        else:
            tScore1 = score1
            scoreLabel1.config(text=tScore1)
            numbers[0].delete(0,END)
            numbers[1].delete(0,END)
            numbers[2].delete(0,END)
            current = 2
            numbers[current].focus_set()
    if current > 2 and tempTF[current] == False:
        temp = tScore2 - temp
        tempTF[current] = True
        if double == True and temp == 0:
            scoreLabel2.config(text="Winner!!!")
        elif temp >= 2:
            tScore2 = temp
            scoreLabel2.config(text=tScore2)
        else:
            tScore2 = score2
            scoreLabel1.config(text=tScore2)
            numbers[3].delete(0,END)
            numbers[4].delete(0,END)
            numbers[5].delete(0,END)
            current = 5
            numbers[current].focus_set()

def correctTempScore(place):
    global tScore1,tScore2,tempTF
    try:
        temp = int(num_vars[place].get())
    except ValueError:
        temp = 0
    tempTF[place] = False
    if place == 0 or place == 1 or place == 2:
        tScore1 = tScore1 + temp
        scoreLabel1.config(text=tScore1)
    else:
        tScore2 = tScore2 + temp
        scoreLabel2.config(text=tScore2)

def changeFocus(event):
    global current, tScore1, tScore2
    try:
        temp = int(num_vars[current].get())
    except ValueError:
        temp = 0
    changeTempScore(temp)
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
    changeTempScore(temp*2, True)
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
    changeTempScore(temp*3)
    current = (current+1) % 6
    numbers[current].focus_set()
    
def updateFocus(event,x):
    global current
    current = x

def char_limit(text):
    if len(text.get()) > 2:
        text.delete(2,END)

def clearInput(event):
    global current,tempTF
    if event.keysym == 'F1':
        current = 1
    elif event.keysym == 'F2':
        current = 2
    elif event.keysym == 'F3':
        current = 3
    elif event.keysym == 'F5':
        current = 4
    elif event.keysym == 'F6':
        current = 5
    elif event.keysym == 'F7':
        current = 0
    #check to see if score has been entered
    correctTempScore(current-1)
    numbers[current-1].delete(0,END)
    numbers[current-1].insert(0,0)
    numbers[current].focus_set()

def changeInput(event):
    global current
    if event.keysym == 'F1':
        current = 0
    elif event.keysym == 'F2':
        current = 1
    elif event.keysym == 'F3':
        current = 2
    elif event.keysym == 'F5':
        current = 3
    elif event.keysym == 'F6':
        current = 4
    elif event.keysym == 'F7':
        current = 5
    #check to see if score has been entered
    correctTempScore(current)
    numbers[current].delete(0,END)
    numbers[current].focus_set()

def winner():
    root.focus_set()

s = ttk.Style()
s.configure('My.TFrame', background = '#808080')

frm = ttk.Frame(root, style='My.TFrame')
frm.grid_propagate(0)
frm.pack_propagate(0)
frm.config(width=405,height=300)
frm.place(relx=0.5, rely=0.25, anchor=CENTER)
ttk.Label(frm, text="Player 1", font=("Arial",25), background='#808080').grid(padx=15,column=0,row=0)
ttk.Label(frm, text="Player 2", font=("Arial",25), background='#808080').grid(padx=15,column=2,row=0)

scoreLabel1 = ttk.Label(frm, text=score1, font=("Arial",25), background='#808080')
scoreLabel2 = ttk.Label(frm, text=score2, font=("Arial",25), background='#808080')
scoreLabel1.grid(column=0,row=1)
scoreLabel2.grid(column=2,row=1)

#creating list of input boxes for score. one box per dart
numbers = []
numbers.append(Entry(frm, textvariable=num_vars[0], width=2, font=("Arial",25)))
numbers.append(Entry(frm, textvariable=num_vars[1], width=2, font=("Arial",25)))
numbers.append(Entry(frm, textvariable=num_vars[2], width=2, font=("Arial",25)))
numbers.append(Entry(frm, textvariable=num_vars[3], width=2, font=("Arial",25)))
numbers.append(Entry(frm, textvariable=num_vars[4], width=2, font=("Arial",25)))
numbers.append(Entry(frm, textvariable=num_vars[5], width=2, font=("Arial",25)))

#placing input boxes on screen
numbers[0].grid(column=0,row=2, sticky='W')
numbers[1].grid(column=1,row=2)
numbers[2].grid(column=2,row=2)

numbers[3].grid(column=2,row=2, sticky='W')
numbers[4].grid(column=1,row=2)
numbers[5].grid(column=2,row=2)

numbers[1].place(in_=numbers[0], relx=0, x=60, y=-2)
numbers[2].place(in_=numbers[1], relx=0, x=60, y=-2)

numbers[4].place(in_=numbers[3], relx=0,x=60, y=-2)
numbers[5].place(in_=numbers[4], relx=0,x=60, y=-2)

#creating and placing buttons to add functionality
ttk.Button(frm, text="Remove points", command = updateScores).grid(pady=5,column=1,row=3)
ttk.Button(frm, text="Reset Points", command = resetScore).grid(pady=5,column=1,row=4)
ttk.Button(frm, text="Quit", command = root.destroy).grid(pady=5,column=1,row=5)

#when app first launches makes it auto focus on first input box
numbers[current].focus_set()

#updates a varibale that keeps track of wich input box has focus
numbers[0].bind("<FocusIn>", lambda event, x=0:updateFocus(event,x))
numbers[1].bind("<FocusIn>", lambda event, x=1:updateFocus(event,x))
numbers[2].bind("<FocusIn>", lambda event, x=2:updateFocus(event,x))
numbers[3].bind("<FocusIn>", lambda event, x=3:updateFocus(event,x))
numbers[4].bind("<FocusIn>", lambda event, x=4:updateFocus(event,x))
numbers[5].bind("<FocusIn>", lambda event, x=5:updateFocus(event,x))

root.bind("<Return>", changeFocus)#chnage focus to next input box if Return button pressed
root.bind("<Shift-Return>", changeFocus2)#doubles score in current input box then focues on next one if Shift and Return button pressed
root.bind("<Control-Return>", changeFocus3)#triples score in current input box then focues on next one if Control and Return button pressed
root.bind("<Alt-Return>", updateScores)#submits scores in input boxes to update total score if Alt and return are pressed

#limit number of character that can be enter in input box
num_vars[0].trace("w", lambda *args: char_limit(numbers[0]))
num_vars[1].trace("w", lambda *args: char_limit(numbers[1]))
num_vars[2].trace("w", lambda *args: char_limit(numbers[2]))
num_vars[3].trace("w", lambda *args: char_limit(numbers[3]))
num_vars[4].trace("w", lambda *args: char_limit(numbers[4]))
num_vars[5].trace("w", lambda *args: char_limit(numbers[5]))

#enter 0 in input boxes 
root.bind("<KeyPress-F1>", clearInput)
root.bind("<KeyPress-F2>", clearInput)
root.bind("<KeyPress-F3>", clearInput)
root.bind("<KeyPress-F5>", clearInput)
root.bind("<KeyPress-F6>", clearInput)
root.bind("<KeyPress-F7>", clearInput)

#jumps to specifed input box to change the value inside
root.bind("<Alt-KeyPress-F1>", changeInput)
root.bind("<Alt-KeyPress-F2>", changeInput)
root.bind("<Alt-KeyPress-F3>", changeInput)
root.bind("<Alt-KeyPress-F5>", changeInput)
root.bind("<Alt-KeyPress-F6>", changeInput)
root.bind("<Alt-KeyPress-F7>", changeInput)

#pressing escape quits the program
root.bind("<KeyPress-Escape>", lambda *args: root.destroy())

root.bind("<KeyPress-F8>", resetScore)

root.mainloop()        
        