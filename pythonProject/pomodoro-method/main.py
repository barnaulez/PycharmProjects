from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    tomato.config(text="Timer", fg=GREEN)
    checkmark_label.config(fg=YELLOW)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_min = LONG_BREAK_MIN
    if reps % 8 == 0:
        count_down(long_break_min)
        tomato.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        tomato.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        tomato.config(text="Work", fg=GREEN)
#    while is_work:
#        if reps in [1,3,5,7]:
#            count_down(work_sec)
#            reps += 1
#        elif reps in [2,4,6]:
#            print(reps)
#            count_down(short_break_sec)
#            reps += 1
#        elif reps == 8:
#            print(reps)
#            count_down(long_break_min)
#            reps = 0
#        else:
#            print(reps)
#            reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_label.config(fg=GREEN)
        else:
            checkmark_label.config(fg=YELLOW)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


fg = GREEN
checkmark = "✔"

tomato = Label(text="Timer")
tomato.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
tomato.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

stat_btn = Button(text="Start", highlightthickness=0, command=start_timer)
stat_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

checkmark_label = Label(text=checkmark)
checkmark_label.config(fg=YELLOW, bg=YELLOW, font=(FONT_NAME))
checkmark_label.grid(row=3, column=1)

window.mainloop()
