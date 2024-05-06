from tkinter import *
from PIL import Image, ImageTk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305a"
GREEN = "#54bf6f"
YELLOW = '#f0ebad'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks_text = ""
reset = False


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    global reset
    reset = True
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 42, "bold"), pady=0)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global reset
    reset = False
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 7:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=RED, font=(FONT_NAME, 36, "bold"), pady=3.5)
        timer_label.grid(column=1, row=0, pady=(3, 4))
    elif reps % 2 == 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 42, "bold"))
        timer_label.grid(pady=(0, 0))
    else:
        count_down(short_break_sec)
        timer_label.config(text="Short break", fg=PINK, font=(FONT_NAME, 36, "bold"))
        timer_label.grid(column=1, row=0, pady=(3, 4))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    global marks_text
    global reset
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count > 0 and not reset:
        canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
        window.after(1000, count_down, count - 1)
    elif not reset:
        reps += 1
        if reps == 8:
            reps = 0
            marks_text = ""
            check_marks.config(text=marks_text)
        elif reps % 2 != 0:
            marks_text += "✔"
            check_marks.config(text=marks_text)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=640, height=630)
window.maxsize(width=630, height=630)
window.config(padx=60, pady=75, bg=YELLOW)

canvas = Canvas(width=325, height=365, bg=YELLOW, highlightthickness=0)
img = Image.open("tomato.png")
resized_img = img.resize((320, 363))
tomato_img = ImageTk.PhotoImage(resized_img)
canvas.create_image(160, 180, image=tomato_img)
timer_text = canvas.create_text(160, 220, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), bg=YELLOW, fg=GREEN, pady=0)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, fg=GREEN, bg="white", font=(FONT_NAME, 16, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, fg=GREEN, bg="white", font=(FONT_NAME, 16, "bold"))
reset_button.grid(column=2, row=2)

sessions_label = Label(text="Sessions completed:", font=(FONT_NAME, 16, "bold"), bg=YELLOW, fg=GREEN)
sessions_label.grid(column=1, row=3)

check_marks = Label(text=marks_text, font=(FONT_NAME, 28, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=4)

window.mainloop()
