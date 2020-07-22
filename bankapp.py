from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from dbhelper import DBHelper
from tkinter import filedialog
import shutil, os


class JK_bank:

    def __init__(self):

        self.db = DBHelper()
        # Load GUI
        self.load_login_window()

    def load_login_window(self):
        self._root = Tk()

        self._root.title("JK_bank™")
        self._root.minsize(420, 600)
        self._root.maxsize(420, 600)
        self._root.config(background="#FE3C72")

        self._label = Label(self._root, text="♠JK BaNk", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 30))
        self._label.pack(pady=(20, 0))

        self._label = Label(self._root, text="♥ India's International Bank ♥", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(1, 20))

        self._email = Label(self._root, text="Account Number:", fg="#fff", bg="#FE3C72")
        self._email.config(font=("Times", 16))
        self._email.pack(pady=(10, 0))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 15), ipady=10, ipadx=30)

        self._password = Label(self._root, text="Password:", fg="#fff", bg="#FE3C72")
        self._password.config(font=("Times", 16))
        self._password.pack(pady=(5, 0))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(1, 35), ipady=10, ipadx=30)

        self._login = Button(self._root, text="Login ☼", fg="#fff", bg="#FE3C72", width=25, height=2,
                             command=lambda: self.check_login())
        self._login.config(font=("sans-serif", 10))
        self._login.pack()

        self._label = Label(self._root, text="-" * 10 + "or" + '-' * 10, fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(10, 0))

        self._label = Label(self._root, text="Register today for bright future ☻", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(1, 20))

        self._reg = Button(self._root, text="Sign up ■", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.regwindow())
        self._reg.config(font=("sans-serif", 10))
        self._reg.pack()

        self._L6 = Label(self._root, text="Copyright©2020 JK BANK.All rights reserved", fg="#fff", bg="#FE3C72")
        self._L6.config(font=("Comic Sans MS", 7))
        self._L6.pack(pady=(70, 0))

        self._root.mainloop()

    def check_login(self):
        account_num = self._emailInput.get()
        password = self._passwordInput.get()
        data = self.db.check_login(account_num, password)
        # print(data)
        if len(data) == 0:
            # print("Invalid Credentials")
            messagebox.showerror("Error", "Invalid Credentials")
        else:
            self.user_id = data[0][0]
            self.is_logged_in = 1
            self.login_handler()

    def regwindow(self):
        self.clear()
        self._name = Label(self._root, text="Name:", fg="#fff", bg="#FE3C72")
        self._name.config(font=("Comic Sans MS", 16))
        self._name.grid(row=1, column=0, pady=(20, 0))

        self._nameInput = Entry(self._root)
        self._nameInput.grid(row=1, column=1, ipady=5, ipadx=30, pady=(20, 0))

        self._account_no = Label(self._root, text="Account Number:", fg="#fff", bg="#FE3C72")
        self._account_no.config(font=("Comic Sans MS", 16))
        self._account_no.grid(row=2, column=0, pady=(20, 0))

        self._account_noInput = Entry(self._root)
        self._account_noInput.grid(row=2, column=1, ipady=4, ipadx=30, pady=(20, 0))

        self._password = Label(self._root, text="Password:", fg="#fff", bg="#FE3C72")
        self._password.config(font=("Comic Sans MS", 16))
        self._password.grid(row=3, column=0, pady=(20, 0))

        self._passwordInput = Entry(self._root)
        self._passwordInput.grid(row=3, column=1, ipady=4, ipadx=30, pady=(20, 0))

        self._gender = Label(self._root, text="Gender:", fg="#fff", bg="#FE3C72")
        self._gender.config(font=("Comic Sans MS", 16))
        self._gender.grid(row=4, column=0, pady=(20, 0))

        self._genderInput = Entry(self._root)
        self._genderInput.grid(row=4, column=1, ipady=4, ipadx=30, pady=(20, 0))

        self._age = Label(self._root, text="Age:", fg="#fff", bg="#FE3C72")
        self._age.config(font=("Comic Sans MS", 16))
        self._age.grid(row=5, column=0, pady=(20, 0))

        self._ageInput = Entry(self._root)
        self._ageInput.grid(row=5, column=1, ipady=5, ipadx=30, pady=(20, 0))

        self._city = Label(self._root, text="City:", fg="#fff", bg="#FE3C72")
        self._city.config(font=("Comic Sans MS", 16))
        self._city.grid(row=6, column=0, pady=(20, 0))

        self._cityInput = Entry(self._root)
        self._cityInput.grid(row=6, column=1, ipady=4, ipadx=30, pady=(20, 0))

        self._amount = Label(self._root, text="Enter Amount:", fg="#fff", bg="#FE3C72")
        self._amount.config(font=("Comic Sans MS", 16))
        self._amount.grid(row=7, column=0, pady=(20, 0))

        self._amountInput = Entry(self._root)
        self._amountInput.grid(row=7, column=1, ipady=4, ipadx=30, pady=(20, 0))

        self.dp = Button(self._root, text="Select a picture", command=lambda: self.select_dp())
        self.dp.grid(row=8, column=0, pady=(20, 0))

        self.dp_filename = Label(self._root)
        self.dp_filename.grid(row=8, column=1, pady=(20, 0))

        self._reg = Button(self._root, text="Sign Up ►", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.reg_handler())
        self._reg.config(font=("Comic Sans MS", 10))
        self._reg.grid(row=9, column=0, pady=(50, 0))

        self._reg = Button(self._root, text="←- Back", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.logout())
        self._reg.config(font=("Comic Sans MS", 10))
        self._reg.grid(row=9, column=1, pady=(50, 0))

    def select_dp(self):
        self.filename = filedialog.askopenfilename(initialdir="/images", title="Somrhting")
        self.dp_filename.config(text=self.filename)

    def reg_handler(self):

        actual_filename = self.filename.split("/")[-1]

        flag = self.db.register(self._nameInput.get(), self._account_noInput.get(), self._passwordInput.get(),
                                self._ageInput.get(), self._genderInput.get(), self._cityInput.get(), self._amountInput.get(),
                                actual_filename)

        if flag == 1:

            # File upload

            destination = "C:\\Users\\jawed\\PycharmProjects\\bankapi\\images\\" + actual_filename
            shutil.copyfile(self.filename, destination)
            messagebox.showinfo("Success", "Registered Successfully. Login to proceed")
            self._root.destroy()
            self.load_login_window()
        else:
            messagebox.showerror("Error", "Try again!")

    def mainWindow(self, data, flag=0, index=0):
        # Display remaining info about the user

        L1 = str(data[index][1]) + "," + str(data[index][4])
        L2 = str(data[index][5]) + " | " + str(data[index][6])
        dp = data[index][8]

        imageUrl = "images/{}".format(data[index][8])

        load = Image.open(imageUrl)
        load = load.resize((350, 320), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render

        img.pack(pady=(5, 5))

        L1_label = Label(self._root, text=L1, fg="#472A23", bg="#fff")
        L1_label.config(font=("Comic Sans MS", 16))
        L1_label.pack(pady=(7, 0), ipady=4, ipadx=150)

        L2_label = Label(self._root, text=L2, fg="#472A23", bg="#fff")
        L2_label.config(font=("Times New Roman", 12))
        L2_label.pack(pady=(0, 10), ipady=4, ipadx=180)


        self._A1 = Button(self._root, text="View Balance ■", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.view_balance())
        self._A1.config(font=("sans-serif", 10))
        self._A1.pack(pady=(5,0))

        self._A2 = Button(self._root, text="Credit ■", fg="#fff", bg="#FE3C72", width=25, height=2,
                         command=lambda: self.credit())
        self._A2.config(font=("sans-serif", 10))
        self._A2.pack(side=LEFT,pady=(0,2))

        self._A3 = Button(self._root, text="Debit ■", fg="#fff", bg="#FE3C72", width=25, height=2,
                         command=lambda: self.debit())
        self._A3.config(font=("sans-serif", 10))
        self._A3.pack(side=RIGHT, pady=(0,2))


    def login_handler(self):
        # To load user's profile
        # clear screen
        self.clear()
        self.headerMenu()
        data = self.db.fetch_userdata(self.user_id)
        self.mainWindow(data, flag=0)

    def clear(self):
        for i in self._root.pack_subordinates():
            print(i.destroy())

    def logout(self):

        self.is_logged_in = 0
        self._root.destroy()
        self.load_login_window()

    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Menu", menu=filemenu)
        filemenu.add_command(label="Edit Profile", command=lambda: self.edit_user())
        filemenu.add_command(label="LogOut ←┘", command=lambda: self.logout())


    def credit(self, ):
        self.clear()

        self._label = Label(self._root, text="♠JK BaNk", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 30))
        self._label.pack(pady=(20, 0))

        self._label = Label(self._root, text="♥ India's International Bank ♥", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(1, 20))

        self._l1 = Label(self._root, text="Enter amount you will add:", fg="#fff", bg="#FE3C72")
        self._l1.config(font=("Comic Sans MS", 20))
        self._l1.pack(pady=(40, 0))

        self._l1Input = Entry(self._root)
        self._l1Input.pack(pady=(0, 15), ipady=10, ipadx=30)

        self._sub = Button(self._root, text="Submit ►", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.update_credit())
        self._sub.config(font=("Comic Sans MS", 10))
        self._sub.pack(pady=(50, 0))

        self._back = Button(self._root, text="←- Back", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.login_handler())
        self._back.config(font=("Comic Sans MS", 10))
        self._back.pack(pady=(50, 0))


    def update_credit(self, index=0):
        data = self.db.fetch_userdata(self.user_id)

        balance = str(data[index][7])
        new_balance = float(balance)+float(self._l1Input.get())

        flag = self.db.update_amount(new_balance, self.user_id)

        if flag == 1:
            messagebox.showinfo("Success", "Credit Successful")
            self.clear()
            self.login_handler()
        else:
            messagebox.showerror("Error", "Try Again!")

    def debit(self, index=0):
        self.clear()

        self._label = Label(self._root, text="♠JK BaNk", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 30))
        self._label.pack(pady=(20, 0))

        self._label = Label(self._root, text="♥ India's International Bank ♥", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(1, 20))

        self._l1 = Label(self._root, text="Enter amount you will debit:", fg="#fff", bg="#FE3C72")
        self._l1.config(font=("Comic Sans MS", 20))
        self._l1.pack(pady=(40, 0))

        self._l1Input = Entry(self._root)
        self._l1Input.pack(pady=(0, 15), ipady=10, ipadx=30)

        self._sub = Button(self._root, text="Submit ►", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.update_debit())
        self._sub.config(font=("Comic Sans MS", 10))
        self._sub.pack(pady=(50, 0))

        self._back = Button(self._root, text="←- Back", fg="#fff", bg="#FE3C72", width=25, height=2,
                            command=lambda: self.login_handler())
        self._back.config(font=("Comic Sans MS", 10))
        self._back.pack(pady=(50, 0))

    def update_debit(self, index=0):
        data = self.db.fetch_userdata(self.user_id)
        balance = float(str(data[index][7]))
        Input_bal = float(self._l1Input.get())

        if Input_bal <= balance:
            new_balance = balance - Input_bal
            self.db.update_amount(new_balance, self.user_id)
            messagebox.showinfo("Success", "debit Successful")
            self.clear()
            self.login_handler()
        else:
            messagebox.showerror("Error", "Insufficient balance!")
            self.clear()
            self.login_handler()


    def view_balance(self, index=0):
        self.clear()
        data = self.db.fetch_userdata(self.user_id)

        self._label = Label(self._root, text="♠JK BaNk", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 30))
        self._label.pack(pady=(20, 0))

        self._label = Label(self._root, text="♥ India's International Bank ♥", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(1, 20))

        self._label = Label(self._root, text="Your Available balance:", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(60, 0))

        Avail_bal = str(data[index][7])+" .cr"

        result = Label(self._root, text=Avail_bal, fg="#fff", bg="#FE3C72")
        result.config(font=("Comic Sans MS", 20))
        result.pack(pady=(0, 40))

        self._back = Button(self._root, text="←- Back", fg="#fff", bg="#FE3C72", width=25, height=2,
                            command=lambda: self.login_handler())
        self._back.config(font=("Comic Sans MS", 10))
        self._back.pack(pady=(50, 0))

    def edit_user(self):

        data = self.db.fetch_userdata(self.user_id)
        self.clear()

        self._age = Label(self._root, text="Age", fg="#fff", bg="#FE3C72")
        self._age.config(font=("Comic Sans MS", 16))
        self._age.pack(pady=(10, 0))

        self._ageInput = Entry(self._root)
        self._ageInput.insert(0, data[0][4])
        self._ageInput.pack(pady=(1, 20), ipady=5, ipadx=30)

        self._gender = Label(self._root, text="Gender", fg="#fff", bg="#FE3C72")
        self._gender.config(font=("Comic Sans MS", 16))
        self._gender.pack(pady=(10, 0))

        self._genderInput = Entry(self._root)
        self._genderInput.insert(0, data[0][5])
        self._genderInput.pack(pady=(1, 20), ipady=5, ipadx=30)

        self._city = Label(self._root, text="City", fg="#fff", bg="#FE3C72")
        self._city.config(font=("Comic Sans MS", 16))
        self._city.pack(pady=(10, 0))

        self._cityInput = Entry(self._root)
        self._cityInput.insert(0, data[0][6])
        self._cityInput.pack(pady=(1, 20), ipady=5, ipadx=30)

        self.dp = Button(self._root, text="Update Info", fg="#fff", bg="#FE3C72", width=25, height=2, command=lambda: self.update_info())
        self.dp.pack(pady=(5, 5))

        self._back = Button(self._root, text="←- Back", fg="#fff", bg="#FE3C72", width=25, height=2,
                            command=lambda: self.login_handler())
        self._back.config(font=("Comic Sans MS", 10))
        self._back.pack(pady=(50, 0))

    def update_info(self):

        flag = self.db.update_info(self._genderInput.get(), self._ageInput.get(), self._cityInput.get(), self.user_id)

        if flag == 1:
            messagebox.showinfo("Success", "Profile Updated")
            self.clear()
            self.login_handler()
        else:
            messagebox.showerror("Error", "Try Again!")


obj = JK_bank()
