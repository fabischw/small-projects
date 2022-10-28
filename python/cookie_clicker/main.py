import tkinter as tk
import PIL
import json
import easygui
import hashlib
from tkinter import messagebox






#loading the user profiles
with open("cookie_count.json","r") as file:
    cookie_count = json.load(file)



# username = easygui.enterbox("Please enter your username ")

possible_load_options = ["log in","create account"]

choice = easygui.choicebox("Select an option below.", "starting", possible_load_options)

# logging in user
if choice == "log in":
    fields = ["username","password"]

    login_data = easygui.multpasswordbox("Enter your login details below", "login", fields,)

    try:
        user_cookie_count = cookie_count[login_data[0]]
    except KeyError:
        messagebox.showerror("Cookie Clicker","Your login details are incorrect")
        quit()

    # hashing input
    entered_pass_raw = str(login_data[1])
    entered_pass_hash_p1 = hashlib.sha256(entered_pass_raw.encode("utf-8"))
    entered_pass_hash = entered_pass_hash_p1.hexdigest()

    if cookie_count[login_data[0]]["pass"] != entered_pass_hash:# checking if the hash is correct
        messagebox.showerror("Cookie Clicker","Your login details are incorrect")
        quit()



    current_cookie_count = int(cookie_count[login_data[0]]["count"])

    messagebox.showinfo("Cookie Clicker","Login successfull")




# creating a new user account
elif choice == "create account":
    fields = ["username","password"]

    login_data = easygui.multpasswordbox("Enter your login details below", "login", fields,)

    # checking if the account already exists
    try:
        test_existance = cookie_count[login_data[0]]
        messagebox.showerror("Cookie Clicker","That account already exists")
        quit()
    except KeyError:
        pass


    #creating the new user account

    # creating the password hash
    password = login_data[1].encode("utf-8")
    password = hashlib.sha256(password).hexdigest()

    cookie_count[login_data[0]] = {
        "pass": password,
        "count": 0
    }



    # writing the new user to the json
    with open("cookie_count.json", "w") as file:
        file.write(json.dumps(cookie_count, indent=4))

    current_cookie_count = 0


else:
    messagebox.showerror("An error occured")
    quit()




# intializing the GUI
master = tk.Tk()
master.title("Cookie-Clicker game")
master.geometry("500x500")

cookie_text = tk.StringVar()

# function to increase the cookie count by 1
def increase_cookie_count():
    global current_cookie_count # ! not the best solution but hard to make it work without
    current_cookie_count += 1
    cookie_text.set(current_cookie_count)


cookie_text.set(current_cookie_count)
cookie_button = tk.Button(master, textvariable=cookie_text, command=increase_cookie_count, font=50)
cookie_button.place(relx=.5, rely=.5,anchor= "center")



#GUI mainloop
master.mainloop()


# saving current cookie count if use quits program


cookie_count[login_data[0]]["count"] = current_cookie_count

with open("cookie_count.json","w") as file:
    file.write(json.dumps(cookie_count,indent=4))


