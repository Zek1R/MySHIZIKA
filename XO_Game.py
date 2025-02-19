from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

a = [['', '', ''],
     ['', '', ''],
     ['', '', '']]


def proverka(a):
    win = False
    if (a[0][1] != '' and a[0][0] == a[0][1] == a[0][2]) or \
        (a[1][1] != '' and a[1][0] == a[1][1] == a[1][2]) or \
        (a[2][1] != '' and a[2][0] == a[2][1] == a[2][2]) or \
        (a[1][0] != '' and a[0][0] == a[1][0] == a[2][0]) or \
        (a[1][1] != '' and a[0][1] == a[1][1] == a[2][1]) or \
        (a[1][2] != '' and a[0][2] == a[1][2] == a[2][2]) or \
        (a[1][1] != '' and (a[0][0] == a[1][1] == a[2][2] or a[0][2] == a[1][1] == a[2][0])): win = True
    return win


root = Tk()
root.title("XO_Game")
root.geometry("500x650")
root.resizable(width=False, height=False)
bg = ImageTk.PhotoImage(file="XOwlpp.png")

canvas = Canvas(root, width=350, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(250, 325, image=bg,)

pr = False
s = 0
f1, f2, f3, f4, f5, f6, f7, f8, f9 = 1, 1, 1, 1, 1, 1, 1, 1, 1
is_true_win = 1

def summ(f1,f2,f3,f4,f5,f6,f7,f8,f9):
    return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
def btn1_click():
    global s
    s = 1
def btn2_click():
    global s
    s = 2
def btn3_click():
    global s
    s = 3
def btn4_click():
    global s
    s = 4
def btn5_click():
    global s
    s = 5
def btn6_click():
    global s
    s = 6
def btn7_click():
    global s
    s = 7
def btn8_click():
    global s
    s = 8
def btn9_click():
    global s
    s = 9


def show_btnx_text():
    global s, pr, is_true_win
    global f1, f2, f3, f4, f5, f6, f7, f8, f9

    if s == 1 and pr != True and f1 == 1:
        btn_a1["text"] = btn_X["text"]
        a[0][0] = btn_a1["text"]
        f1 = 0

    if s == 2 and pr != True and f2 == 1:
        btn_a2["text"] = btn_X["text"]
        a[0][1] = btn_a2["text"]
        f2 = 0

    if s == 3 and pr != True and f3 == 1:
        btn_a3["text"] = btn_X["text"]
        a[0][2] = btn_a3["text"]
        f3 = 0

    if s == 4 and pr != True and f4 == 1 :
        btn_a4["text"] = btn_X["text"]
        a[1][0] = btn_a4["text"]
        f4 = 0

    if s == 5 and pr != True and f5 == 1:
        btn_a5["text"] = btn_X["text"]
        a[1][1] = btn_a5["text"]
        f5 = 0

    if s == 6 and pr != True and f6 == 1:
        btn_a6["text"] = btn_X["text"]
        a[1][2] = btn_a6["text"]
        f6 = 0

    if s == 7 and pr != True and f7 == 1:
        btn_a7["text"] = btn_X["text"]
        a[2][0] = btn_a7["text"]
        f7 = 0

    if s == 8 and pr != True and f8 == 1:
        btn_a8["text"] = btn_X["text"]
        a[2][1] = btn_a8["text"]
        f8 = 0

    if s == 9 and pr != True and f9 == 1:
        btn_a9["text"] = btn_X["text"]
        a[2][2] = btn_a9["text"]
        f9 = 0

    pr = proverka(a)
    if pr == True and is_true_win == 1:
        lbl1["text"] = "Победа", btn_X["text"], "!"
        is_true_win = 0

    if pr != True and summ(f1, f2, f3, f4, f5, f6, f7, f8, f9) < 2:
        f1 = f2 = f3 = f4 = f5 = f6 = f7 = f8 = f9 = 0
        lbl1["text"] = "Ничья!"


def show_btn0_text():
    global s, pr, is_true_win
    global f1, f2, f3, f4, f5, f6, f7, f8, f9

    if s == 1 and pr != True and f1 == 1:
        btn_a1["text"] = btn_O["text"]
        a[0][0] = btn_a1["text"]
        f1 = 0

    if s == 2 and pr != True and f2 == 1:
        btn_a2["text"] = btn_O["text"]
        a[0][1] = btn_a2["text"]
        f2 = 0

    if s == 3 and pr != True and f3 == 1:
        btn_a3["text"] = btn_O["text"]
        a[0][2] = btn_a3["text"]
        f3 = 0

    if s == 4 and pr != True and f4 == 1:
        btn_a4["text"] = btn_O["text"]
        a[1][0] = btn_a4["text"]
        f4 = 0

    if s == 5 and pr != True and f5 == 1:
        btn_a5["text"] = btn_O["text"]
        a[1][1] = btn_a5["text"]
        f5 = 0

    if s == 6 and pr != True and f6 == 1:
        btn_a6["text"] = btn_O["text"]
        a[1][2] = btn_a6["text"]
        f6 = 0

    if s == 7 and pr != True and f7 == 1:
        btn_a7["text"] = btn_O["text"]
        a[2][0] = btn_a7["text"]
        f7 = 0

    if s == 8 and pr != True and f8 == 1:
        btn_a8["text"] = btn_O["text"]
        a[2][1] = btn_a8["text"]
        f8 = 0

    if s == 9 and pr != True and f9 == 1:
        btn_a9["text"] = btn_O["text"]
        a[2][2] = btn_a9["text"]
        f9 = 0

    pr = proverka(a)
    if pr == True and is_true_win == 1:
        lbl1["text"] = "Победа", btn_O["text"], "!"
        is_true_win = 0

    if pr != True and summ(f1,f2,f3,f4,f5,f6,f7,f8,f9) < 2:
        f1 = f2 = f3 = f4 = f5 = f6 = f7 = f8 = f9 = 0
        lbl1["text"] = "Ничья!"


lbl1 = Label(text="Играй!", font=40)

lbl1.place(relx=0.39, rely=0.2)

btn_w = 70
btn_h = 72


# ряд 1
btn_a1 = ttk.Button(command=btn1_click)
btn_a1.place(relx=0.2, rely=0.37, width=btn_w, height=btn_h)

btn_a2 = ttk.Button(command=btn2_click)
btn_a2.place(relx=0.45, rely=0.37, width=btn_w, height=btn_h)

btn_a3 = ttk.Button(command=btn3_click)
btn_a3.place(relx=0.70, rely=0.37, width=btn_w, height=btn_h)

# ряд 2
btn_a4 = ttk.Button(command=btn4_click)
btn_a4.place(relx=0.2, rely=0.52, width=btn_w, height=btn_h)

btn_a5 = ttk.Button(command=btn5_click)
btn_a5.place(relx=0.45, rely=0.52, width=btn_w, height=btn_h)

btn_a6 = ttk.Button(command=btn6_click)
btn_a6.place(relx=0.70, rely=0.52, width=btn_w, height=btn_h)

# ряд 3
btn_a7 = ttk.Button(command=btn7_click)
btn_a7.place(relx=0.2, rely=0.67, width=btn_w, height=btn_h)

btn_a8 = ttk.Button(command=btn8_click)
btn_a8.place(relx=0.45, rely=0.67, width=btn_w, height=btn_h)

btn_a9 = ttk.Button(command=btn9_click)
btn_a9.place(relx=0.70, rely=0.67, width=btn_w, height=btn_h)


btn_X = ttk.Button(command=show_btnx_text)
btn_X["text"] = "X"
btn_X.place(relx=0.3, rely=0.83, width=80, height=80)

btn_O = ttk.Button(command=show_btn0_text)
btn_O["text"] = "O"
btn_O.place(relx=0.57, rely=0.83, width=80, height=80)


root.mainloop()

print(a)
