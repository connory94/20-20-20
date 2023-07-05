import tkinter as tk
from tkinter import *
from playsound import playsound
import os

minutes = 20
seconds = 0
lookAway = False
paused = True
alarm = False

root = tk.Tk()
root.resizable(width=False, height=False)

#background
root.geometry('175x256')
canvas = tk.Canvas(root, height=256, width=175, bg="#f2e9e4")

#title
title2 = canvas.create_text(87.5, 20, text="20/20/20", fill="#34302D", font="Helvitica 26 bold")
title1 = canvas.create_text(87.5, 20, text="20/20/20", fill="#6B6A65", font="Helvitica 25 bold")

#instructions
canvas.create_text(87.5, 160, text="every 20 minutes",fill="#34302D", font="Times 12")
canvas.create_text(87.5, 180, text="look 20 feet away", fill="#34302D", font="Times 12")
canvas.create_text(87.5, 200, text="for 20 seconds", fill="#34302D", font="Times 12")

canvas.create_text(80.5, 160, text="20",fill="#395C78", font="Times 12 bold")
canvas.create_text(73.9, 180, text="20", fill="#BD3B3B", font="Times 12 bold")
canvas.create_text(73, 200, text="20", fill="#395C78", font="Times 12 bold")

#sounds
def alarmSound():
    playsound('elevator.wav')
def testSound():
    playsound('honk.wav')

#secret sound button
    # used to test if sound can play
soundButton = Button(root, text=".", width=1, height=1, bd="2", bg="#f2e9e4", font="Helvitica 2", command=testSound)
soundButton.place(x=170,y=250)

#pause outline
line = canvas.create_line(56,116.4,118,116.4, fill="#BD3B3B", width=29)

# toggles pause (and alarm b/c it's convenient)
def pause():
    global paused
    global alarm

    if alarm == True:
        alarm = False

    if paused == False:
        paused = True
        canvas.itemconfigure(line, fill="#BD3B3B")
    elif paused == True:
        paused = False
        canvas.itemconfigure(line, fill="#395C78")


pauseButton = Button(root, text='>/II', width=7, height=1, bd='1', bg="#CACACA", command=pause)
pauseButton.place(x=58.5,y=105)

#timer
m = canvas.create_text(73, 60, text=minutes, fill="#34302d", font='Consolas 16')
s = canvas.create_text(103, 60, text=seconds, fill="#34302d", font='Consolas 16')
zero = canvas.create_text(888, 888, text="0", fill="#34302d", font='Consolas 16')
zero0 = canvas.create_text(888, 888, text="0", fill="#34302d", font='Consolas 16')
colon = canvas.create_text(87, 60, text=":", fill="#34302d", font="Consolas 14")

def countdown():
    global minutes
    global seconds
    global lookAway
    global alarm
    
    #counts down when not paused
    if paused == False:
        seconds -= 1

    #decreases minutes when seconds = 0
    if seconds < 0 and minutes > 0:
        seconds = 59
        minutes -= 1

    #moves the extra 0s in the timer
    if seconds < 10 and seconds > -1:
        canvas.coords(s, 108, 60)
        canvas.coords(zero, 96, 60)
    else:
        canvas.coords(s, 103, 60)
        canvas.coords(zero, 888, 888)

    if minutes < 10 and minutes > -1:
      canvas.coords(m, 79, 60)
      canvas.coords(zero0, 66.5, 60)
    else:
      canvas.coords(m, 73, 60)
      canvas.coords(zero0, 888, 888)

    #sets time when timer reaches 0
    if seconds < 0 and minutes == 0 and lookAway == False:
        lookAway = True
        alarm = True
        seconds = 20
        minutes = 0
        pause()
    elif seconds < 0 and minutes == 0 and lookAway == True:
        lookAway = False
        seconds = 0
        minutes = 20
        alarmSound()

        #I didn't really want to change coords outside of the thing above but I couldn't find another way to fix it
        canvas.coords(s, 108, 60)
        canvas.coords(zero, 96, 60)
        canvas.coords(m, 73, 60)
        canvas.coords(zero0, 888, 888)

    #plays the alarm sound
    if lookAway and paused == True:
        alarmSound()

    #controls color of the timer text
    if lookAway == False:
        canvas.itemconfigure(m, fill="#34302D")
        canvas.itemconfigure(s, fill="#34302D")
        canvas.itemconfigure(zero, fill="#34302D")
        canvas.itemconfigure(zero, fill="#34302D")
        canvas.itemconfigure(colon, fill="#34302D")
    elif lookAway == True:
        canvas.itemconfigure(m, fill="#913A1E")
        canvas.itemconfigure(s, fill="#913A1E")
        canvas.itemconfigure(zero, fill="#913A1E")
        canvas.itemconfigure(zero0, fill="#913A1E")
        canvas.itemconfigure(colon, fill="#913A1E")

    canvas.itemconfigure(m, text=minutes)
    canvas.itemconfigure(s, text=seconds)
    canvas.after(1000, countdown) 

countdown()
canvas.pack()
root.mainloop()