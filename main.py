import tkinter
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
          'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# the initial score
score = 0

# timer of 30 seconds
timeleft = 30


def startGame(event):

    if timeleft == 30:
        # start the counter
        countdown()

    # to select the next color
    nextColor()


def nextColor():
    global score
    global timeleft

    if timeleft > 0:
        # make the text entry box active
        e.focus_set()

        # if the color matches increase the score
        if e.get().lower() == colors[1].lower():
            score += 1

        # clear the text entry box
        e.delete(0, tkinter.END)

        random.shuffle(colors)

        # change the text and the color of text to random value
        label.config(fg=str(colors[1]), text=str(colors[0]))

        # update the score
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
    timeLabel.config(text="Time left: " + str(timeleft))

    # run the function agian after 1 second
    timeLabel.after(1000, countdown)


# create a GUI window
root = tkinter.Tk()

root.title("Color Game")
root.geometry("375x200")

# add an instruction label
instructions = tkinter.Label(root, text="Type in the colour"
                             "of the words, not the word text!",
                             font=('Helvetica', 12))

instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

# add a label for displaying the colors
label = tkinter.Label(root, font=('Helvetica', 50))
label.pack()

# add a text entry box for typing
e = tkinter.Entry(root)

# run the game when pressed Enter
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
