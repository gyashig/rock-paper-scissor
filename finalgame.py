from tkinter import *
import random
from random import choice, randint
from tkinter import font
from PIL import Image,ImageTk
import pygame
#main window
root=Tk()
root.title("ROCK PAPER SCISSOR GAME ")
root.configure(background="blue")
root.geometry("1600x700")
pygame.mixer.init()
f1=Frame(background="dark blue")
#image
f1.place(x=0,y=0,width=1600,height=700)
boyimg=ImageTk.PhotoImage(Image.open("boy.png"))
girlimg=ImageTk.PhotoImage(Image.open("girl.png"))
boimage=Label(f1,image=boyimg,bg="dark blue")
giimage=Label(f1,image=girlimg,bg="dark blue")
boimage.place(x=50,y=110)
giimage.place(x=1100,y=80)
Label(root,
     text="Rock Paper Scissor",
     font="normal 60 bold",
     fg="black",bg="orange").pack(pady=20)
frame=Frame(root)
frame.pack()
l1=Label(root,
         text="Welcome to our Game !", 
         font="normal 40 bold",fg="yellow",bg="dark blue")
l1.place(x=480,y=200)
#music
#def play():
pygame.mixer.music.load("gamemusic.mp3")
pygame.mixer.music.play(loops=5)
def stop():
    pygame.mixer.music.stop()
stop=Button(f1,text="Music off",font=2,bg="white",fg="black",width=7,height=1,command=stop)
stop.place(x=160,y=650)
#third slide
def welcome():
    f2=Frame(background="dark blue")
    f2.place(x=0,y=0,width=1600,height=700)
    rockimg=ImageTk.PhotoImage(Image.open("rock.png"))
    paperimg=ImageTk.PhotoImage(Image.open("paper.png"))
    scissorimg=ImageTk.PhotoImage(Image.open("scissor.png"))
    rockuserimg=ImageTk.PhotoImage(Image.open("rock_comp.png"))
    scissoruserimg=ImageTk.PhotoImage(Image.open("scirror_comp.png"))
    paperuserimg=ImageTk.PhotoImage(Image.open("paper_comp.png"))
    #insert picture
    userimage=Label(f2,image=rockimg,bg="light blue")
    compimage=Label(f2,image=scissoruserimg,bg="light blue")
    compimage.place(x=1200,y=200)
    userimage.place(x=50,y=200)
    def new():
        exit()
    #score
    userscore=Label(f2, text=0, font="normal 50 bold",bg="light blue", fg="black")
    compscore=Label(f2, text=0, font="normal 50 bold",bg="light blue", fg="black")
    userscore.place(x=500,y=250)
    compscore.place(x=1000,y=240)
    #indicator
    userindicator=Label(f2,font="normal 20 bold",text="YOU",bg="orange",fg="black")
    compindicator=Label(f2,font="normal 20 bold",text="COMPUTER",bg="orange",fg="black")
    userindicator.place(x=480,y=150)
    compindicator.place(x=940,y=150)
    #message
    msg=Label(f2,font="normal 20 bold",bg="orange",fg="black")
    msg.place(x=670,y=550)
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
    rock=Button(f2, width=20, height=2, text="Rock",font="normal 14 bold", 
           bg="red", fg="black",command=lambda:updatechoice("rock"))
    rock.place(x=380,y=450)
    paper=Button (f2, width=20, height=2, text="Paper",font="normal 14 bold",
           bg="yellow", fg="black",command=lambda:updatechoice("paper"))
    paper.place(x=620,y=450)
    scissor=Button(f2, width=20, height=2, text="Scissor",font="normal 14 bold",
            bg="green", fg="black",command=lambda:updatechoice("scissor"))
    scissor.place(x=870,y=450)
    #reset button
    reset=Button(f2, width=20, height=2, text="Exit",font="normal 10 bold", 
           bg="grey", fg="black",command=new)
    reset.place(x=1250,y=610)
def rules():
    f3=Frame(background="dark blue")
    f3.place(x=0,y=0,width=1600,height=700)
    res="Welcome"+"  "+e1.get()+"  "+"to the game. Here are rules of the game :- "
    head=Label(f3,text=res,font="normal 30 bold",bg="dark blue",fg="light blue")
    head.place(x=80,y=20)
    info1=Label(f3,text="1 - ROCK will win against SCISSOR",font="normal 20 bold",bg="dark blue",fg="white")
    info1.place(x=150,y=200)
    info2=Label(f3,text="2 - SCISSOR will win against PAPER",font="normal 20 bold",bg="dark blue",fg="white")
    info2.place(x=150,y=250)
    info3=Label(f3,text="3 - PAPER will win against ROCK",font="normal 20 bold",bg="dark blue",fg="white")
    info3.place(x=150,y=300)
    info4=Label(f3,text="4 - If BOTH are Same, then its a TIE",font="normal 20 bold",bg="dark blue",fg="white")
    info4.place(x=150,y=350)
    info5=Label(f3,text="If you have read all the rules, click next to start the game",font="normal 10 bold",bg="dark blue",fg="yellow")
    info5.place(x=150,y=450)
    next=Button(f3,width=20,height=2,text=" NEXT",font="normal 10 bold",bg="yellow",fg="black",command=welcome)
    next.place(x=800,y=500)
submit=Button(f1,width=40,height=3,text="SUBMIT",font="normal 10 bold",bg="red",fg="white",command=rules)
submit.place(x=600,y=550)
u1=Label(root,text="Enter your name",font="normal 20 bold",fg="yellow",bg="dark blue")
u1.place(x=480,y=400)
e1=Entry(root,font=("",20))
e1.place(x=720,y=400)
root.mainloop()