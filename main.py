import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
from string import ascii_uppercase
from tkinter import messagebox

word_lists = {
        "fruits": ["apple", "banana", "orange", "kiwi", "pineapple"],
        "flowers": ["rose","lily","sunflower","lotus","tulips","marigold"],
        "Colours": ["yellow","pink","green","purple","voilet","black"],
        "Sports": ["football","volleyball","hockey","cricket","tennis"],
        "coding": ["python", "java", "javascript", "php", "ruby", "html", "css"]
    }

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Hangman App')
    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login,width=720,height=440,bg="#20B2AA")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="#20B2AA")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    heading = Label(login_frame,text="Hangman App Login",fg="black",bg="#20B2AA")
    heading.config(font=('Garamond 38'))
    heading.place(relx=0.1,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.19,rely=0.4)
    uname= Entry(login_frame,bg='#AFEEEE',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.19,rely=0.5)
    pas= Entry(login_frame,bg='#AFEEEE',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)
  
    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                menu(a)
                break
            else:
                error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
                error.place(relx=0.37,rely=0.7)
   
    #login button
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#20B2AA", relief = FLAT)
    log.place(relx=0.4,rely=0.6)


    login.mainloop()
    

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Hangman App')
    print('Welcome to game ')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#20B2AA")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#20B2AA")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Hangman Game SignUp",fg="black",bg="#20B2AA")
    heading.config(font=('Garamond 38'))
    heading.place(relx=0.082,rely=0.1)

    def validate_input(input_string):
        return input_string.isalpha()
    validate_alpha=sup_frame.register(validate_input)

    #full name
    flabel = Label(sup_frame,text="First Name",fg='white',bg='black')
    flabel.place(relx=0.18,rely=0.4)
    fname = Entry(sup_frame,bg='#AFEEEE',fg='black',textvariable = fname,validate="key",validatecommand=(validate_alpha,'%S'))
    fname.config(width=40)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.18,rely=0.5)
    user = Entry(sup_frame,bg='#AFEEEE',fg='black',textvariable = uname)
    user.config(width=40)
    user.place(relx=0.31,rely=0.5)

    #password
    plabel = Label(sup_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.18,rely=0.6)
    pas = Entry(sup_frame,bg='#AFEEEE',fg='black',textvariable = passW,show="*")
    pas.config(width=40)
    pas.place(relx=0.31,rely=0.6)
    
    #country
    clabel = Label(sup_frame,text="Country",fg='white',bg='black')
    clabel.place(relx=0.19,rely=0.7)
    c = Entry(sup_frame,bg='#AFEEEE',fg='black',textvariable = country,validate="key",validatecommand=(validate_alpha,'%S'))
    c.config(width=40)
    c.place(relx=0.31,rely=0.7)

    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()

        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            error = Label(text="Please Enter all the fields",fg='#929591',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Username and password can't be empty",fg='#929591',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Username can't be empty",fg='#929591',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='#929591',bg='white')
            error.place(relx=0.37,rely=0.7)

        else:
            conn = sqlite3.connect('hangman.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            conn.close()
            loginPage(z)
    def gotoLogin():
        conn = sqlite3.connect('hangman.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)

     #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#20B2AA", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin, bg="#20B2AA", fg="black")
    log.configure(width = 16,height=1, activebackground = "#20B2AA", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Hangman App')
    width = 598
    height = 540
    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    menu.geometry("%dx%d+%d+%d" % (width, height, x, y))
    menu.resizable(0, 0)
    

    
    def change_category(category):
        word = choose_word(None if category == "All" else category)
        menu.destroy()
        
    category_var = tk.StringVar()
    category_var.set("Select category")
    categories = ["All"] + list(word_lists.keys())
    category_menu = tk.OptionMenu(menu,category_var, *categories, command=change_category)
    category_menu.grid(row=0,column=4,columnspan=2)
    canvas = tk.Canvas(menu, width=160, height=250)
    canvas.grid(row=1, column=0, columnspan=3, rowspan=3, padx=10, pady=40) 
    images = [
        tk.PhotoImage(file="shadowhangy/hangman0.png"),
        tk.PhotoImage(file="shadowhangy/hangman1.png"),
        tk.PhotoImage(file="shadowhangy/hangman2.png"),
        tk.PhotoImage(file="shadowhangy/hangman3.png"),
        tk.PhotoImage(file="shadowhangy/hangman4.png"),
        tk.PhotoImage(file="shadowhangy/hangman5.png"),
        tk.PhotoImage(file="shadowhangy/hangman6.png"),
    ]
    hangman_image = canvas.create_image(110, 110, image=images[0])
    word_label = tk.Label(menu, text="_ _ _ _ _ _ ", font=("Arial", 20)) 
    word_label.grid(column=4,row=2,columnspan=4)

    info_label = tk.Label(menu, text="Guess a letter!", font=("Arial", 16))
    info_label.grid(column=2,row=3,columnspan=5)

    
    n=0 #alphabet buttons
    for letter in ascii_uppercase:
        Button(menu, text=letter, bg="#AFEEEE",activebackground="#48D1CC",font=('Helvetica 18'), width=4).grid(row=4+n//9,column=n%9)
        n+=1

    restart_button = tk.Button(menu, text="Restart",bg="#20B2AA", fg="black", font=('Garamond 12 bold'),width=15, relief="ridge")
    restart_button.grid(row=8, column=2, columnspan=5)

    ex = Button(menu,text="Exit",bd = 0,bg="#20B2AA",fg="black",font = ("Garamond 12 bold "),width = 6, relief="ridge")
    ex.grid(row=0,column=8)

    menu.mainloop()
        
    
def start():
    global root
    root = Tk()
    root.title('Welcome To Hangman App')
    canvas = Canvas(root,width = 720,height = 440, bg = 'black')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="homepage.png")
    canvas.create_image(1,1,image=img,anchor=NW)

    s1 = Button(root, text='Start',command=signUpPage,bg="#20B2AA",fg="black") 
    s1.configure(width =102,height=2, activebackground = "#20B2AA", relief = RAISED)
    s1.grid(column = 0 , row = 2)

    root.mainloop()


# Class for the game
class HangmanGame:
    def __init__(self, word):
        self.word = word.upper()
        self.guesses_left = 6
        self.letters_guessed = []
        # Choose a random index to fill in the guess
        guess_index = random.randint(0, len(self.word) - 1)
        self.display_word = "-" * len(self.word)
        self.display_word = self.display_word[:guess_index] + self.word[guess_index] + self.display_word[guess_index+1:]
        
        self.create_gui()

    # Function to update the display word when a letter is guessed correctly
    def update_display_word(self):
        new_display_word = ""
        for i in range(len(self.word)):
            if self.word[i] == self.display_word[i]:
                new_display_word += self.word[i]
            elif self.word[i] in self.letters_guessed:
                new_display_word += self.word[i]
            else:
                new_display_word += "-"
        self.display_word = new_display_word
        self.word_label.config(text=self.display_word)

    # Function to handle a letter guess
    def guess_letter(self, letter):
        if letter in self.letters_guessed:
            self.info_label.config(text="You already guessed that letter!")
        else:
            self.letters_guessed.append(letter)
            if letter in self.word:
                self.update_display_word()
                if "-" not in self.display_word:
                    self.info_label.config(text="Congratulations, you won!")
                    self.disable_buttons()
            else:
                self.guesses_left -= 1
                self.info_label.config(text="Sorry! wrong letter!")
                self.update_hangman()
                if self.guesses_left == 0:
                    self.info_label.config(text="Sorry, you lost! The word was {}".format(self.word))
                    self.disable_buttons()

    # Function to create the GUI
    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Hangman")
        
        # Create a dropdown menu for selecting category
        self.category_var = tk.StringVar()
        self.category_var.set("Select category")
        categories = ["All"] + list(word_lists.keys())
        self.category_menu = tk.OptionMenu(self.root, self.category_var, *categories, command=self.change_category)
        self.category_menu.grid(row=0, column=3, columnspan=2) 

        self.canvas = tk.Canvas(self.root, width=160, height=250)
        self.canvas.grid(row=1, column=0, columnspan=3, rowspan=4, padx=10, pady=40) 
        self.images = [
            tk.PhotoImage(file="shadowhangy/hangman0.png"),
            tk.PhotoImage(file="shadowhangy/hangman1.png"),
            tk.PhotoImage(file="shadowhangy/hangman2.png"),
            tk.PhotoImage(file="shadowhangy/hangman3.png"),
            tk.PhotoImage(file="shadowhangy/hangman4.png"),
            tk.PhotoImage(file="shadowhangy/hangman5.png"),
            tk.PhotoImage(file="shadowhangy/hangman6.png"),
        ]
        self.hangman_image = self.canvas.create_image(100, 110, image=self.images[0])

        self.word_label = tk.Label(self.root, text=self.display_word, font=("Arial", 24)) 
        self.word_label.grid(column=3,row=2,columnspan=4)

        self.info_label = tk.Label(self.root, text="Guess a letter!", font=("Arial", 16))
        self.info_label.grid(column=0,row=4,columnspan=6)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=5, column=0, columnspan=7)


        n=0 #alphabet buttons
        for letter in ascii_uppercase:
            button=tk.Button(self.button_frame, text=letter, command=lambda l=letter: self.guess_letter(l),bg="#AFEEEE",activebackground="#48D1CC",font=('Helvetica 12'), width=9,relief="ridge").grid(row=5+n//7,column=n%7)
            n+=1
            
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, bg="#20B2AA", fg="black", font=('Garamond 12 bold'),width=25, relief="ridge")
        self.restart_button.grid(row=8, column=2, columnspan=3)

        self.ex = tk.Button(self.root,text="Exit",bd = 0,command = self.close,bg="#20B2AA",fg="black",font = ("Garamond 12 bold "),width = 6, relief="ridge")
        self.ex.grid(row=0,column=6,columnspan=2)


    # Function to disable all letter buttons
    def disable_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.config(state="disabled")

    # Function to update the hangman image when a letter is guessed incorrectly
    def update_hangman(self):
        self.canvas.itemconfig(self.hangman_image, image=self.images[6-self.guesses_left])
    
    def change_category(self, category):
        word = choose_word(None if category == "All" else category)
        self.root.destroy()
        game = HangmanGame(word)
        game.start_game()

    def close(self):
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            self.root.destroy()
            
    
    

    # Function to start the game loop
    def start_game(self):
        self.root.mainloop()

    def restart_game(self):
        self.root.destroy()
        word = choose_word()
        self.__init__(word)
        self.start_game()

# Function to choose a word from the list
def choose_word(category=None):
    if category is None:
        # Choose a random category and word
        category = random.choice(list(word_lists.keys()))
    word_list = word_lists[category]
    return random.choice(word_list)

   
if __name__=='__main__':
    start()
    word = choose_word()
game = HangmanGame(word)
game.start_game()
    
