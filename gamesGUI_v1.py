# PythonBook: GamesGUI

from tkinter import *  # spelled in lowercase

import rps_gui_v3

# import hangman_v1
# import poker_dice_v2
root = Tk()
root.title("PythonBook Games GUI")

mainFrame = Frame(root, height=300, width=500)
mainFrame.pack_propagate(0)
mainFrame.pack(padx=5, pady=5)

intro = Label(mainFrame, text="""Welcome to PythonBook Games Collection
Please select one of the following games to play:""")
intro.pack(side=TOP)

rps_button = Button(mainFrame, text="Rock, Paper, Scissors", command=rps_gui_v3.gui)
rps_button.pack()

exit_button = Button(mainFrame, text="Quit", command=root.destroy)
exit_button.pack()

root.mainloop()
