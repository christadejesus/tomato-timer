import os
import sys
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import math
import pygame

window = Tk()

def resource_path(relative_path):
    """ Get absolute path to resource, works for both dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------------------- SOUND ------------------------------- #
pygame.mixer.init()
break_sound = pygame.mixer.Sound(resource_path("sound/hotel-bell-ding-3-202587.wav"))
work_sound = pygame.mixer.Sound(resource_path("sound/hotel-bell-ding-1-174457.wav"))
end_sound = pygame.mixer.Sound(resource_path("sound/hotel-bell-ding-4-202588.wav"))

# ---------------------------- IMAGES ------------------------------- #
icon_image = PhotoImage(file=resource_path("images/tomato_icon.png"))
tomato_img = PhotoImage(file=resource_path("images/tomato.png"))

# ---------------------------- FONTS ------------------------------- #
font_path = "fonts/Pacifico-Regular.ttf"
window.tk.call('font', 'create', 'Pacifico', '-family', 'Pacifico')
window.tk.call('font', 'create', 'Poppins', '-family', 'Poppins')
PACIFICO_FONT_LG = tkFont.Font(family="Pacifico", size=32, weight="bold")
PACIFICO_FONT_MD = tkFont.Font(family="Pacifico", size=28, weight="bold")
PACIFICO_FONT_SM = tkFont.Font(family="Pacifico", size=14, weight="bold")
POPPINS_FONT = tkFont.Font(family="Poppins", size=12)

# ---------------------------- COLOR CONSTANTS ------------------------------- #
PINK = "#f13f48"
RED = "#df2e38"
GREEN = "#529e4c"
DARK_GREEN = "#286324"
YELLOW = "#ffeeaa"
WHITE = "#ffffff"

# ---------------------------- TIME CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- COUNTER VARIABLES ------------------------------- #
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    start_button.state(["!disabled"])
    heading_label.config(text="Tomato Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    counter_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *  60
    start_button.state(["disabled"])

    # If it's the 9th rep:
    if reps == 9:
        window.after_cancel(timer)
        end_sound.play()
        heading_label.config(text="Great job!", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")
    # If it's the 8th rep:
    elif reps % 8 == 0:
        count_down(long_break_sec)
        break_sound.play()
        heading_label.config(text="Break", fg=RED)
    # If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        break_sound.play()
        heading_label.config(text="Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)  
        work_sound.play()
        heading_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer 
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔"
            counter_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window.title("Tomato Timer")
window.config(padx=60, pady=40, bg=YELLOW)
window.iconphoto(False, icon_image)

# ---------------------------- HEADING ------------------------------- #
heading_label = Label(window, text="Tomato Timer", font=PACIFICO_FONT_MD, fg=GREEN, bg=YELLOW, width=10)
heading_label.grid(column=1, row=0)

# ---------------------------- TIMER ------------------------------- #
canvas = Canvas(width=216, height=225, bg=YELLOW, highlightthickness=0)
canvas.create_image(108, 110, image=tomato_img) # (x-axis position, y-axis position, image variable)
timer_text = canvas.create_text(108, 110, text="00:00", fill=WHITE, font=PACIFICO_FONT_LG)
canvas.grid(column=1, row=1)

# ---------------------------- CONTROLS ------------------------------- #
style = ttk.Style()
style.configure("TButton", foreground=DARK_GREEN, background=GREEN, font=POPPINS_FONT)

style.map("TButton",
    background=[('pressed', DARK_GREEN), ('active', DARK_GREEN)]
)

start_button = ttk.Button(text="Start", takefocus=False, command=start_timer, width=10)
start_button.grid(column=0, row=2)

counter_label = Label(font=PACIFICO_FONT_SM, fg=GREEN, bg=YELLOW)
counter_label.grid(column=1, row=3)

reset_button = ttk.Button(text="Reset", takefocus=False, command=reset_timer, width=10)
reset_button.grid(column=2, row=2)

window.mainloop()