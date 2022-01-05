from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image

# Functions

def login():
    global email , password
    email = box1.get()
    password = box2.get()
    if len(email) > 0 and len(password) > 5:
        loginW.quit()
    else :
        pass

# General Configuration
loginW = Tk()
loginW.title("MRU Student System")
loginW.iconbitmap(r'icon.ico')
loginW.option_add("*tearOff", False)                            # for remove dashed line from ui\ux
loginW.geometry("1000x650")                                     # for default size of window
loginW.resizable(False, FALSE)                                  # for resizing of window
loginW.columnconfigure(index=0 , weight=1)
loginW.columnconfigure(index=1 , weight=2)
loginW.columnconfigure(index=2 , weight=1)
loginW.rowconfigure(index=0 , weight=1)
loginW.rowconfigure(index=1 , weight=1)
loginW.rowconfigure(index=2 , weight=1)
style = ttk.Style(loginW)

# Setting Login Frame
loginframe = ttk.Frame(loginW,padding=(20,0, 0, 10))
loginframe.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
loginframe.columnconfigure(index=0, weight=1)

# setting the theme
loginW.call("source", r"Azure-ttk-theme-main\azure.tcl")
loginW.call("set_theme", "dark")

# setting Logo
logo = Image.open(r"Logo.png")  # open image
r_logo = logo.resize((150,139), Image.ANTIALIAS)               # resizing image
F_logo = ImageTk.PhotoImage(r_logo)                            # make image photo
logolbl = Label(image=F_logo)                                  # make image as label

# setting login button
loginbtn = ttk.Button(loginframe,text = "Login",style="Accent.TButton" , width=15 , command=login ) # ttk is module from class for themed widgets

# setting Boxes Entry & Labels
box1 = ttk.Entry(loginframe)
box2 = ttk.Entry(loginframe , show="x")
lbl1 = ttk.Label(loginframe,text="Email",font=("arial" , 11 , "bold"),foreground="white")
lbl2 = ttk.Label(loginframe,text="Password",font=("arial" , 11 , "bold"),foreground="white")
lbl3 = ttk.Label(loginframe,text="Forgotten password?",font=("arial" , 10),foreground="grey")

# Setting widgets on the screen
logolbl.grid(row=0, column=1 , pady=(10,30) ,sticky=EW)
lbl1.grid(row=1 , column=0 , columnspan=1 , pady=(185,10) , padx=(190,200) , sticky=W)
box1.grid(row=2 ,column=0 , columnspan=1 , pady=(0,10) , padx=(190,200) , sticky=EW)
lbl2.grid(row=3 , column=0 , columnspan=1 , pady=(10,10) , padx=(190,200) , sticky=W)
box2.grid(row=4 , column=0 , columnspan=1 , pady=(0,20) , padx=(190,200) , sticky=EW)
lbl3.grid(row=5 , column=0 , columnspan=1 , pady=(20,10) , padx=(190,200))
loginbtn.grid(row=6 ,column=0 , columnspan=1 , pady=20 , padx=(190,200))

# Loops Running
loginW.mainloop()
