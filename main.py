import random
from tkinter import *
from tkinter import messagebox
import pyperclip
#------------------------------------------------- Constants -------------------------------------------------#

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]
symbol = ['!', '@', '#', '$', '&', '?', '*']

#------------------------------------------------- Backend -------------------------------------------------#

def run():
    password.delete(0, END)
    if radio_state.get()==0:
        messagebox.showinfo(title="Warning",message="Please select User Mode or Auto mode!!!")

    if radio_state.get()==1:
        let = int(word_lenth.get())
        num = int(number_lenth.get())
        sym = int(symbol_lenth.get())
        if let <= 9 and let > 0 and num <= 9 and num > 0 and sym <= 7 and sym > 0:
            password_letters = [random.choice(letter) for _ in range(random.randint(let, let))]  # range(0, 1)
            password_symbol = [random.choice(symbol) for _ in range(random.randint(sym, sym))]
            password_number = [random.choice(number) for _ in range(random.randint(num, num))]

            password_list = password_letters + password_symbol + password_number
            random.shuffle(password_list)

            password_gen = "".join(password_list)
            password.insert(0, password_gen)

        else:
            messagebox.showinfo(title="Warning", message="please enter the values in specified length")


    elif radio_state.get()==2:
        word_lenth.delete(0, END) #this line can dlt the previous values entered in entry box
        symbol_lenth.delete(0, END)
        number_lenth.delete(0, END)

        password_letters = [random.choice(letter) for _ in range(random.randint(7, 9))]  # range(0, 1)
        password_symbol = [random.choice(symbol) for _ in range(random.randint(3, 4))]
        password_number = [random.choice(number) for _ in range(random.randint(6, 8))]

        password_list = password_letters + password_symbol + password_number
        random.shuffle(password_list)

        password_gen = "".join(password_list)
        password.insert(0, password_gen)

#----------------------------------------------- Copy Password -----------------------------------------------#

def copy_password():
    copy_function(password.get())
    messagebox.showinfo(title="info", message="Password Copied Successfully")

def copy_function(text):
    pyperclip.copy(text)

#--------------------------------------------------- UI ---------------------------------------------------#
windows = Tk()
windows.title("Password Generator")
windows.config(padx=50, pady=50)

#alphabet length label
word_lenth_label = Label(text="Alphabet length: ")
word_lenth_label.grid(column=0, row=0)

#symbol length label
symbol_lenth_label = Label(text="Symbol length:  ")
symbol_lenth_label .grid(column=0, row=1)

#symbol length label
number_lenth_label = Label(text="Number length:  ")
number_lenth_label.grid(column=0, row=2)

#generated Password
password = Entry(width=30)
password.grid(column=0,row=3, columnspan=2)

#alphabet length input
word_lenth = Entry( width=15)
word_lenth.grid(column=1, row=0)

#alphabet length input
symbol_lenth = Entry( width=15)
symbol_lenth.grid(column=1, row=1)

#alphabet length input
number_lenth = Entry( width=15)
number_lenth.grid(column=1, row=2)

#generate password button
gen_pass = Button(text="Generate Password", width=28, command=run)
gen_pass.grid(column=0, row=4, columnspan=2)

#copy password button
copy_pass = Button(text="Copy Password", width=28, command=copy_password)
copy_pass.grid(column=0, row=5, columnspan=2)
#Radio Buttons User
radio_state = IntVar()
user_define = Radiobutton(text="User", value=1, variable=radio_state)
user_define.grid(column=0, row=6)

#Radio Buttons Auto
auto_define = Radiobutton(text="Auto", value=2, variable=radio_state)
auto_define.grid(column=1, row=6)

#info Label
info = Label(text="Limits:    \nAlphabets limit upto 9\nSymbols limit upto 7\nNumbers limit upto 9")
info.grid(column=0, row=7, columnspan=2)

windows.mainloop()