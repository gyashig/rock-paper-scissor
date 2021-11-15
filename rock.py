from tkinter import *
import random
from random import choice, randint
from tkinter import font
from PIL import Image,ImageTk
#main window
root=Tk()
root.title("ROCK PAPER SCISSOR GAME")
root.configure(background="light blue")
#image
rockimg=ImageTk.PhotoImage(Image.open("rock.png"))
paperimg=ImageTk.PhotoImage(Image.open("paper.png"))
scissorimg=ImageTk.PhotoImage(Image.open("scissor.png"))
rockuserimg=ImageTk.PhotoImage(Image.open("rock_comp.png"))
scissoruserimg=ImageTk.PhotoImage(Image.open("scirror_comp.png"))
paperuserimg=ImageTk.PhotoImage(Image.open("paper_comp.png"))
#insert picture
userimage=Label(root,image=rockimg,bg="light blue")
compimage=Label(root,image=scissoruserimg,bg="light blue")
compimage.grid(row=1,column=4)
userimage.grid(row=1,column=0)
#score
userscore=Label(root, text=0, font=100,bg="light blue", fg="black")
compscore=Label(root, text=0, font=100,bg="light blue", fg="black")
userscore.grid(row=1,column=1)
compscore.grid(row=1,column=3)
#indicator
userindicator=Label(root,font=50,text="YOU",bg="light blue",fg="black")
compindicator=Label(root,font=50,text="COMPUTER",bg="light blue",fg="black")
userindicator.grid(row=0,column=1)
compindicator.grid(row=0,column=3)
#message
msg=Label(root,font=50,bg="light blue",fg="black")
msg.grid(row=3,column=2)
#update message
def updatemessgae(x):
    msg['text']=x
#update user score
def updateuserscore():
    score=int(userscore["text"])
    score+=1
    userscore["text"]=str(score)
#update comp score
def updatecompscore():
    score=int(compscore["text"])
    score+=1
    compscore["text"]=str(score)
#check winner
def checkwin(player,computer):
    if player==computer:
        updatemessgae("Its a  tie!!")
    elif player=="rock":
        if computer=="paper":
            updatemessgae("You Loose")
            updatecompscore()
        else:
            updatemessgae("You Win")
            updateuserscore()  
    elif player=="paper":
        if computer=="scissor":
            updatemessgae("You Loose")
            updatecompscore()
        else:
            updatemessgae("You Win")
            updateuserscore()   
    elif player=="scissor":
        if computer=="rock":
            updatemessgae("You Loose")
            updatecompscore()
        else:
            updatemessgae("You Win")
            updateuserscore()  
    else:
        pass

#update choice
choices=["rock","paper","scissor"]
def updatechoice(x):
    compchoice=choices[randint(0,2)]
    if compchoice=="rock":
        compimage.configure(image=rockuserimg)
    elif compchoice=="paper":
        compimage.configure(image=paperuserimg)
    else:
        compimage.configure(image=scissoruserimg)
    if x=="rock":
        userimage.configure(image=rockimg)
    elif x=="paper":
         userimage.configure(image=paperimg)
    else:
         userimage.configure(image=scissorimg)
    checkwin(x,compchoice)

#button
rock=Button(root, width=20, height=2, text="Rock", 
           bg="red", fg="black",command=lambda:updatechoice("rock")).grid(row=2, column=1)
paper=Button (root, width=20, height=2, text="Paper", 
           bg="yellow", fg="black",command=lambda:updatechoice("paper")).grid(row=2,column=2)
scissor=Button(root, width=20, height=2, text="Scissor",  
            bg="green", fg="black",command=lambda:updatechoice("scissor")).grid(row=2,column=3)
root.mainloop()