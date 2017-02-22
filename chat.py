from tkinter import *
import messenger, translator
    
class ChatWindow:
    def __init__(self, userName, d, n):
        self.window = Tk()
        self.window.title("Private Messenger") 
        self.window.geometry('{}x{}'.format(357, 667))

        loginImg = PhotoImage(file="Images/Chat.png")
        bg = Label(self.window, image=loginImg)
        bg.place(x = 0, y = 0)
        self.user = userName
        self.n = n
        self.d = d

        self.infoVar = StringVar()
        infoLabel = Label(self.window, textvariable=self.infoVar, justify = LEFT, wraplength=295, padx=10, pady=10,
                          bg="#2a2d36", fg="white",font = ("Helvetica Nuenue",16), bd=0)
        if(self.user=='1'):
            self.infoVar.set("Chat with user 2")
        elif (self.user=='2'):
            self.infoVar.set("Chat with user 1")
        infoLabel.place(x = 31, y=105)

        self.inboxVar = StringVar()
        self.inboxLabel = Label(self.window, textvariable=self.inboxVar, justify = LEFT, wraplength=295, padx=10, pady=10, bg="#c81300", fg="white",font = ("Helvetica Nuenue",12), bd=0)
        self.inboxVar.set(self.fetchMsg())
        self.inboxLabel.place(x = 35, y=194)
        
        self.messageVar = StringVar()
        self.message = Entry(self.window,width=26, textvariable = self.messageVar, justify = LEFT, fg="#2a2d36",
                           font = ("Helvetica Nuenue",12), bd=0)
        self.message.insert(0, "Your message here")
        self.message.place(x = 40, y=564)

        btSubmitName = Button(self.window, width = 4, text=">",
                              command = self.send, bg='#c81300', fg="white",font=("Calibri 18 bold"), bd=0)
        btSubmitName.place(x=287, y=550)

        self.window.protocol('WM_DELETE_WINDOW', self.quit)
        
        self.window.mainloop()

    def fetchInfo(self):
        if(self.user=='1'):
            text_file = open("Info_2.txt", "r")
        elif(self.user=='2'):
            text_file = open("Info_1.txt", "r")
        lines = text_file.read().split('\n')
        pubE = int(lines[0])
        pubN = int(lines[1])
        return (pubE, pubN)

    def fetchMsg(self):
        if(self.user=='1'):
            text_file = open("Storage_1.txt", "r")
        elif(self.user=='2'):
            text_file = open("Storage_2.txt", "r")
        lines = text_file.read().split('\n')
        del lines[-1]
        msg = list(map(int, lines))
        return translator.decrypt(self.d, self.n, msg)
        
    def send(self):
        pubE, pubN = self.fetchInfo()
        encrypted = translator.encrypt(pubE, pubN, self.messageVar.get())
        if(self.user=='1'):
            with open("Storage_2.txt", "w") as text_file:
                    for i in encrypted:
                        print(i, file=text_file)
        elif(self.user=='2'):
            with open("Storage_1.txt", "w") as text_file:
                    for i in encrypted:
                        print(i, file=text_file)
        self.message.delete(0, 'end')
        
    def quit(self):
        self.window.destroy()
