import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint
from tkinter import font
from PIL import Image,ImageTk
import pygame
#main window
root=Tk()
root.title("ROCK PAPER SCISSOR GAME ")
# root.geometry("1600x700")
width1= root.winfo_screenwidth()
height1= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width1, height1))
root.configure(background="blue")
pygame.mixer.init()
f1=Frame(background="dark blue")
count = 0
uscount=0
cscount=0
#image
f1.place(x=0,y=0,relwidth=1, relheight=1)
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
pygame.mixer.music.load("backmusic.mp3")
pygame.mixer.music.play(loops=5)
def startt():
    pygame.mixer.music.unpause()
def stop():
    pygame.mixer.music.pause()
stop=Button(f1,text="Music off",font=2,bg="white",fg="black",width=7,height=1,command=stop)
stop.place(x=200,y=650)
start=Button(f1,text="Music on",font=2,bg="white",fg="black",width=7,height=1,command=startt)
start.place(x=80,y=650)
 

#third slide
def nenter():
    tkinter.messagebox.showerror("Warning","Please enter your name")
def welcome():
    f2=Frame(background="dark blue")
    f2.place(x=0,y=0,relwidth=1, relheight=1)
    chance = Label(f2, text="", font=("", 20),bg="dark blue",fg="white")
    chance.place(x=700, y=50)
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
            Mg= tkinter.messagebox.askquestion("Exit App", "Are you sure you want to exit the game ?")
            if (Mg == "yes"):
                exit()
            else:
                pass
                  
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
    msg=Label(f2,font="normal 20 bold",bg="dark blue",fg="white")
    msg.place(x=670,y=550)
    #update message
    def updatemessgae(x):
        msg['text']=x
    #update user score
    def updateuserscore():
        global uscount
        uscount+=1
        score=int(userscore["text"])
        score+=1
        userscore["text"]=str(score)
    #update comp score
    def updatecompscore():
        global cscount
        cscount+=1
        score=int(compscore["text"])
        score+=1
        compscore["text"]=str(score)

    def checkfwin():
        global count
        global cscount
        global uscount
        if(uscount>cscount):
            tkinter.messagebox.showinfo("Result","Congralutions,You Win")
            res=tkinter.messagebox.askquestion("Exit App", "You want to play again ?")
            if(res=="yes"):
                count=0
                cscount=0
                uscount=0
                msg.configure(text="")
                chance.configure(text="")
                userscore.configure(text="0")
                compscore.configure(text="0")
            else:
                exit()
        elif(cscount>uscount):
            tkinter.messagebox.showinfo("Result", "You loose, Better Luck Next Time ")
            res = tkinter.messagebox.askquestion("Exit App", "You want to play again ?")
            if (res == "yes"):
                count = 0
                cscount = 0
                uscount = 0
                msg.configure(text="")
                chance.configure(text="")
                userscore.configure(text="0")
                compscore.configure(text="0")
            else:
                exit()
        else:
            tkinter.messagebox.showinfo("Result", "Its a tie !")
            res = tkinter.messagebox.askquestion("Exit App", "You want to play again ?")
            if (res == "yes"):
                count = 0
                cscount = 0
                uscount = 0
                msg.configure(text="")
                chance.configure(text="")
                userscore.configure(text="0")
                compscore.configure(text="0")
            else:
                exit()
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
      global count
      count+=1
      chance.config(text="Round "+str(count),font="normal 30 bold",bg="dark blue",fg="white")
      compchoice=choices[randint(0,2)]
      if (count == 5):
       checkfwin()
      else:
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
 if (e1.get() == ""):
        nenter()
 else:
    f3=Frame(background="dark blue")
    f3.place(x=0,y=0,relwidth=1, relheight=1)
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
    info6=Label(f3,text=" You have 5 rounds in this game ",font="normal 20 bold",bg="dark blue",fg="white")
    info6.place(x=150,y=400)
    info5=Label(f3,text="If you have read all the rules, start the game",font="normal 15 bold",bg="dark blue",fg="yellow")
    info5.place(x=150,y=500)
    next=Button(f3,width=20,height=2,text=" START",font="normal 10 bold",bg="yellow",fg="black",command=welcome)
    next.place(x=800,y=600)
submit=Button(f1,width=40,height=3,text="SUBMIT",font="normal 10 bold",bg="red",fg="white",command=rules)
submit.place(x=600,y=550)
u1=Label(root,text="Enter your name",font="normal 20 bold",fg="yellow",bg="dark blue")
u1.place(x=480,y=400)
e1=Entry(root,font=("",20))
e1.place(x=720,y=400)
root.mainloop()