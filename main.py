from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Hand-to-Hand Combat")
root.configure(background="#9b59b6")

# pictures
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
sc_img = ImageTk.PhotoImage(Image.open("sc.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))

rock_img_comp = ImageTk.PhotoImage(Image.open("rock user.png"))
sc_img_comp = ImageTk.PhotoImage(Image.open("sc user.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper user.png"))

# insert images
user_label = Label(root, image=sc_img, bg="#9b59b6")
comp_label = Label(root, image=sc_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=4)
user_label.grid(row=1, column=0)

# scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=1)
comp_indicator.grid(row=0, column=3)

# messages
msg = Label(root, font=("Helvetica", 30), bg="#9b59b6", fg="white")
msg.grid(row=1, column=2)

# update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update comp score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateUserScore()
        else:
            updateMessage("You Win")
            updateCompScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose")
            updateUserScore()
        else:
            updateMessage("You win")
            updateCompScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose")
            updateUserScore()
        else:
            updateMessage("You win")
            updateCompScore()
    else:
        pass

# Update choices
choices = ["rock", "paper", "scissor"]
def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]

    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:  # compChoice == "scissor":
        comp_label.configure(image=sc_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=sc_img)
    
    checkWin(x, compChoice)

# button
rock = Button(root, width=20, height=2, text="Rock",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="Paper",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="Scissor",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)
exit = Button(root, width=20, height=2, text="Exit",
              bg="cyan4", fg="white", command = root.destroy).grid(row=0, column=4)
root.mainloop()
