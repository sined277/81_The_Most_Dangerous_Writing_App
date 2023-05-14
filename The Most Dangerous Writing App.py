from tkinter import *

# define constants for colors and fonts
BG_COLOR = "#E5E5E5"
FG_COLOR = "#222222"
BUTTON_BG_COLOR = "#FBD33B"
BUTTON_FG_COLOR = "#222222"
HEADING_FONT = ("Helvetica", 32, "bold")
INSTRUCTION_FONT = ("Helvetica", 18)
TEXT_FONT = ("Calibri", 14)
BUTTON_FONT = ("Calibri", 14)

timer = None


# define function to clear the text area
def clear_text():
    typing_area.delete(1.0, END)


# define function to start a new timer for clearing the text area
def start_timer(event=None):
    global timer
    if timer:
        # if a timer already exists, cancel it
        window.after_cancel(timer)
    # start a new timer for 5 seconds
    timer = window.after(5000, clear_text)


# define function to save the text to a file
def save_text():
    text = typing_area.get(1.0, END)
    with open('saved_text.txt', mode='w') as data:
        data.write(text)


# create the main window
window = Tk()
window.title("The Most Dangerous Writing App")
window.geometry("1000x800")
window.config(bg=BG_COLOR)

# create the heading label
heading_label = Label(window, text="The Most Dangerous Writing",
                      font=HEADING_FONT, fg=FG_COLOR, bg=BG_COLOR)
heading_label.pack(pady=(20, 0))

# create the instructions label
instructions_label = Label(window,
                           text="If you don't press any key for 5 seconds, the text you have written will disappear",
                           font=INSTRUCTION_FONT, fg=FG_COLOR, bg=BG_COLOR)
instructions_label.pack(pady=(10, 0))

# create the typing area
typing_area = Text(window, font=TEXT_FONT, bg=BG_COLOR, fg=FG_COLOR,
                   highlightbackground=FG_COLOR, highlightthickness=4,
                   padx=10, pady=10)
typing_area.pack(expand=True, fill=BOTH, padx=50, pady=20)

# attach the start_timer function to the typing area
typing_area.bind("<Key>", start_timer)

# create the save button
save_button = Button(window, text="Save", font=BUTTON_FONT, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR,
                     borderwidth=0, highlightthickness=0, command=save_text)
save_button.pack(side=RIGHT, padx=50, pady=(0, 20))

# create the reset button
reset_button = Button(window, text="Reset", font=BUTTON_FONT, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR,
                      borderwidth=0, highlightthickness=0, command=clear_text)
reset_button.pack(side=LEFT, padx=50, pady=(0, 20))

# start the main event loop
window.mainloop()
