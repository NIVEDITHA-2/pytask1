from tkinter import *
from tkinter import messagebox
import os

def login():
    user=username.get()
    code=password.get()

    if user=="Niveditha" and code=="0309":
        root=Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False,False)


        # Reset Function
        def Reset():
            entry_dosa.delete(0, END)
            entry_vada.delete(0, END)
            entry_samosa.delete(0, END)
            entry_cutlet.delete(0, END)
            entry_coffee.delete(0, END)
            entry_juice.delete(0, END)
            entry_puffs.delete(0, END)

        # Calculate Total Function
        def Total():
            try:
                a1 = int(Dosa.get())
            except:
                a1 = 0

            try:
                a2 = int(Vada.get())
            except:
                a2 = 0

            try:
                a3 = int(Samosa.get())
            except:
                a3 = 0

            try:
                a4 = int(Cutlet.get())
            except:
                a4 = 0

            try:
                a5 = int(Coffee.get())
            except:
                a5 = 0

            try:
                a6 = int(Juice.get())
            except:
                a6 = 0

            try:
                a7 = int(Puffs.get())
            except:
                a7 = 0

                # define cost of each item per quantity

                c1 = 60 * a1
                c2 = 10 * a2
                c3 = 25 * a3
                c4 = 30 * a4
                c5 = 35 * a5
                c6 = 20 * a6
                c7 = 25 * a7

                lbl_total = Label(f2,font=('aria', 20, 'bold'), text="Total", width=16, fg="lightyellow", bg="black")
                lbl_total.place(x=0, y=50)

                entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=15,
                                    bg="lightgreen")
                entry_total.place(x=20, y=100)

                totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7
                string_bill = "Rs.", str('%2f' % totalcost)
                Total_bill.set(string_bill)

        Label(root,text="Bill Management", bg="black", fg="white", font=("calibri", 33), width="300", height="4").pack()

        # menu card

        f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=370, height=400)
        f.place(x=30, y=250)

        Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=100, y=0)

        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Dosa....Rs.60/plate", fg="black",
              bg="lightgreen").place(x=10, y=80)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Vada....Rs.10/plate", fg="black",
              bg="lightgreen").place(x=10, y=110)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Samosa....Rs.25/plate", fg="black",
              bg="lightgreen").place(x=10, y=140)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Cutlet....Rs.30/plate", fg="black",
              bg="lightgreen").place(x=10, y=170)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Coffee....Rs.35/cup", fg="black",
              bg="lightgreen").place(x=10, y=200)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Juice....Rs.20/glass", fg="black",
              bg="lightgreen").place(x=10, y=230)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Puffs....Rs.25/plate", fg="black",
              bg="lightgreen").place(x=10, y=260)

        # Bill Frame
        f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=370, height=400)
        f2.place(x=880, y=250)

        Bill = Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow")
        Bill.place(x=160, y=10)
        # entry work
        f1 = Frame(root, bd=5, height=400, width=450, relief=RAISED)
        f1.pack()

        Dosa = StringVar()
        Vada = StringVar()
        Samosa = StringVar()
        Cutlet = StringVar()
        Coffee = StringVar()
        Juice = StringVar()
        Puffs = StringVar()
        Total_bill = StringVar()

        # Label
        lbl_dosa = Label(f1, font=("aria", 20, 'bold'), text="Dosa", width=12, fg="blue4")
        lbl_vada = Label(f1, font=("aria", 20, 'bold'), text="Vada", width=12, fg="blue4")
        lbl_samosa = Label(f1, font=("aria", 20, 'bold'), text="Samosa", width=12, fg="blue4")
        lbl_cutlet = Label(f1, font=("aria", 20, 'bold'), text="Cutlet", width=12, fg="blue4")
        lbl_coffee = Label(f1, font=("aria", 20, 'bold'), text="Coffee", width=12, fg="blue4")
        lbl_juice = Label(f1, font=("aria", 20, 'bold'), text="Juice", width=12, fg="blue4")
        lbl_puffs = Label(f1, font=("aria", 20, 'bold'), text="Puffs", width=12, fg="blue4")
        lbl_dosa.grid(row=1, column=0)
        lbl_vada.grid(row=2, column=0)
        lbl_samosa.grid(row=3, column=0)
        lbl_cutlet.grid(row=4, column=0)
        lbl_coffee.grid(row=5, column=0)
        lbl_juice.grid(row=6, column=0)
        lbl_puffs.grid(row=7, column=0)

        # Entry
        entry_dosa = Entry(f1, font=("aria", 20, 'bold'), textvariable=Dosa, bd=6, width=8, bg="lightpink")
        entry_vada = Entry(f1, font=("aria", 20, 'bold'), textvariable=Vada, bd=6, width=8, bg="lightpink")
        entry_samosa = Entry(f1, font=("aria", 20, 'bold'), textvariable=Samosa, bd=6, width=8, bg="lightpink")
        entry_cutlet = Entry(f1, font=("aria", 20, 'bold'), textvariable=Cutlet, bd=6, width=8, bg="lightpink")
        entry_coffee = Entry(f1, font=("aria", 20, 'bold'), textvariable=Coffee, bd=6, width=8, bg="lightpink")
        entry_juice = Entry(f1, font=("aria", 20, 'bold'), textvariable=Juice, bd=6, width=8, bg="lightpink")
        entry_puffs = Entry(f1, font=("aria", 20, 'bold'), textvariable=Puffs, bd=6, width=8, bg="lightpink")
        entry_dosa.grid(row=1, column=1)
        entry_vada.grid(row=2, column=1)
        entry_samosa.grid(row=3, column=1)
        entry_cutlet.grid(row=4, column=1)
        entry_coffee.grid(row=5, column=1)
        entry_juice.grid(row=6, column=1)
        entry_puffs.grid(row=7, column=1)

        # buttons

        btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("aerial", 16, 'bold'), width=10, text="Reset",
                           command=Reset)
        btn_reset.grid(row=8, column=0)

        btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("aerial", 16, 'bold'), width=10, text="Total",
                           command=Total)
        btn_total.grid(row=8, column=1)

    elif user == "" and code == "":
        messagebox.showerror("Invalid", "Please enter username and password")

    elif user == "":
        messagebox.showerror("Invalid", "Username is required")

    elif code == "":
        messagebox.showerror("Invalid", "The password field is required")

    elif user != "Niveditha" and code != "0309":
        messagebox.showerror("Invalid", "Invalid username and password")

    elif user != "Niveditha":
        messagebox.showerror("Invalid", "Please enter a valid username")

    elif code == "0309":
        messagebox.showerror("Invalid", "please enter a valid password")


def main_screen():
    global screen
    global username
    global password

    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    # icon
    image_icon = PhotoImage(file="img.png")
    screen.iconphoto(False, image_icon)
    screen.title("Login System")

    lblTitle = Label(text="Login System", font=("arial", 50, 'bold'), fg="black", bg="#d7dae2")
    lblTitle.pack(pady=50)

    bordercolor = Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)

    Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe, textvariable=username, width=12, bd=2, font=("arial", 30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(mainframe, textvariable=password, width=12, bd=2, font=("arial", 30), show="*")
    entry_password.place(x=400, y=150)

    def reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)

    Button(mainframe, text="Login", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=login).place(x=100,
                                                                                                               y=250)
    Button(mainframe, text="Reset", height="2", width=23, bg="#1089ff", fg="white", bd=0, command=reset).place(x=300,
                                                                                                               y=250)
    Button(mainframe, text="Exit", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=screen.destroy).place(
        x=500, y=250)

    screen.mainloop()


main_screen()

