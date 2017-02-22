from tkinter import *
import messenger
    
class LoginWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Private Messenger") 
        self.window.geometry('{}x{}'.format(357, 667))

        loginImg = PhotoImage(file="Images/login.png")
        bg = Label(self.window, image=loginImg)
        bg.place(x = 0, y = 0)

        self.userNameVar = StringVar()
        userName = Entry(self.window, width=29, textvariable = self.userNameVar, justify = LEFT, fg="#2a2d36",
                           font = ("Helvetica Nuenue",12), bd=0)
        userName.insert(0, "Username")
        userName.place(x = 70, y=370)

        self.passwordVar = StringVar()
        password = Entry(self.window, show="*", width=29, textvariable = self.passwordVar, justify = LEFT, fg="#2a2d36",
                           font = ("Helvetica Nuenue",12), bd=0)
        password.insert(0, "Password")
        password.place(x = 70, y=423)

        btSubmitName = Button(self.window, width = 27, text="Login",
                              command = self.login, bg='#c81300', fg="white",font=("Helvetica CE 55 Roman",14), bd=0)
        btSubmitName.place(x=35, y=513)

        self.window.protocol('WM_DELETE_WINDOW', self.quit)
        
        self.window.mainloop()
        
    def login(self):
        if(self.userNameVar.get()=='1' or self.userNameVar.get()=='2'):
            self.window.destroy()
            messenger.MainWindow((self.userNameVar.get()))
        else:
            self.window.destroy()
            LoginWindow()
        
    def quit(self):
        self.window.destroy()

LoginWindow()
