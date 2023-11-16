from tkinter import *
from tkinter import ttk


a = [['', '', ''],
     ['', '', ''],
     ['', '', '']]


def proverka(a):
    win = False
    if a[0][1] != '' and a[0][0] == a[0][1] == a[0][2] or \
        a[1][1] != '' and a[1][0] == a[1][1] == a[1][2] or \
        a[2][1] != '' and a[2][0] == a[2][1] == a[2][2] or \
        a[1][0] != '' and a[0][0] == a[1][0] == a[2][0] or \
        a[1][1] != '' and a[0][1] == a[1][1] == a[2][1] or \
        a[1][2] != '' and a[0][2] == a[1][2] == a[2][2] : win = True
    return win


root = Tk()
root.title("XO_game")
root.geometry("500x650")

pr = False
s = 0
f1, f2, f3, f4, f5, f6, f7, f8, f9 = 1, 1, 1, 1, 1, 1, 1, 1, 1

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
    global s, pr
    global f1, f2, f3, f4, f5, f6, f7, f8, f9

    if s == 1 and pr != True and f1 == 1:
        btn_a1["text"] = btn_X["text"]
        a[0][0] = btn_a1["text"]
        pr = proverka(a)
        f1 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 2 and pr != True and f2 == 1:
        btn_a2["text"] = btn_X["text"]
        a[0][1] = btn_a2["text"]
        pr = proverka(a)
        f2 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 3 and pr != True and f3 == 1:
        btn_a3["text"] = btn_X["text"]
        a[0][2] = btn_a3["text"]
        pr = proverka(a)
        f3 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 4 and pr != True and f4 == 1 :
        btn_a4["text"] = btn_X["text"]
        a[1][0] = btn_a4["text"]
        pr = proverka(a)
        f4 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 5 and pr != True and f5 == 1:
        btn_a5["text"] = btn_X["text"]
        a[1][1] = btn_a5["text"]
        pr = proverka(a)
        f5 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 6 and pr != True and f6 == 1:
        btn_a6["text"] = btn_X["text"]
        a[1][2] = btn_a6["text"]
        pr = proverka(a)
        f6 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 7 and pr != True and f7 == 1:
        btn_a7["text"] = btn_X["text"]
        a[2][0] = btn_a7["text"]
        pr = proverka(a)
        f7 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 8 and pr != True and f8 == 1:
        btn_a8["text"] = btn_X["text"]
        a[2][1] = btn_a8["text"]
        pr = proverka(a)
        f8 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 9 and pr != True and f9 == 1:
        btn_a9["text"] = btn_X["text"]
        a[2][2] = btn_a9["text"]
        pr = proverka(a)
        f9 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

def show_btn0_text():
    global s, pr
    global f1, f2, f3, f4, f5, f6, f7, f8, f9
    if s == 1 and pr != True and f1 == 1:
        btn_a1["text"] = btn_O["text"]
        a[0][0] = btn_a1["text"]
        pr = proverka(a)
        f1 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 2 and pr != True and f2 == 1:
        btn_a2["text"] = btn_O["text"]
        a[0][1] = btn_a2["text"]
        pr = proverka(a)
        f2 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 3 and pr != True and f3 == 1:
        btn_a3["text"] = btn_O["text"]
        a[0][2] = btn_a3["text"]
        pr = proverka(a)
        f3 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 4 and pr != True and f4 == 1:
        btn_a4["text"] = btn_O["text"]
        a[1][0] = btn_a4["text"]
        pr = proverka(a)
        f4 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 5 and pr != True and f5 == 1:
        btn_a5["text"] = btn_O["text"]
        a[1][1] = btn_a5["text"]
        pr = proverka(a)
        f5 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 6 and pr != True and f6 == 1:
        btn_a6["text"] = btn_O["text"]
        a[1][2] = btn_a6["text"]
        pr = proverka(a)
        f6 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 7 and pr != True and f7 == 1:
        btn_a7["text"] = btn_O["text"]
        a[2][0] = btn_a7["text"]
        pr = proverka(a)
        f7 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 8 and pr != True and f8 == 1:
        btn_a8["text"] = btn_O["text"]
        a[2][1] = btn_a8["text"]
        pr = proverka(a)
        f8 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"

    if s == 9 and pr != True and f9 == 1:
        btn_a9["text"] = btn_O["text"]
        a[2][2] = btn_a9["text"]
        pr = proverka(a)
        f9 = 0
        if pr == True:
            lbl1["text"] = "Ты победил!!!"


lbl1 = Label(font=20)
lbl1.place(relx=0.39, rely=0.2)

btn_w = 70
btn_h = 72


# ряд 1
btn_a1 = ttk.Button(command=btn1_click)
btn_a1.place(relx=0.2, rely=0.4, width=btn_w, height=btn_h)

btn_a2 = ttk.Button(command=btn2_click)
btn_a2.place(relx=0.45, rely=0.4, width=btn_w, height=btn_h)

btn_a3 = ttk.Button(command=btn3_click)
btn_a3.place(relx=0.70, rely=0.4, width=btn_w, height=btn_h)

# ряд 2
btn_a4 = ttk.Button(command=btn4_click)
btn_a4.place(relx=0.2, rely=0.55, width=btn_w, height=btn_h)

btn_a5 = ttk.Button(command=btn5_click)
btn_a5.place(relx=0.45, rely=0.55, width=btn_w, height=btn_h)

btn_a6 = ttk.Button(command=btn6_click)
btn_a6.place(relx=0.70, rely=0.55, width=btn_w, height=btn_h)

# ряд 3
btn_a7 = ttk.Button(command=btn7_click)
btn_a7.place(relx=0.2, rely=0.71, width=btn_w, height=btn_h)

btn_a8 = ttk.Button(command=btn8_click)
btn_a8.place(relx=0.45, rely=0.71, width=btn_w, height=btn_h)

btn_a9 = ttk.Button(command=btn9_click)
btn_a9.place(relx=0.70, rely=0.71, width=btn_w, height=btn_h)


btn_X = ttk.Button(command=show_btnx_text)
btn_X["text"] = "X"
btn_X.place(relx=0.3, rely=0.9, width=40, height=30)

btn_O = ttk.Button(command=show_btn0_text)
btn_O["text"] = "O"
btn_O.place(relx=0.6, rely=0.9, width=40, height=30)


root.mainloop()

print(a)
