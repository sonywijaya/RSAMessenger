import pygame, generator, chat
from pygame.locals import *

class MainWindow:
    def __init__(self, userName):
        pygame.init()
        displayWidth = 357
        displayHeight = 667

        self.screen = pygame.display.set_mode((displayWidth,displayHeight))
        self.menuImg = pygame.image.load('Images/Menu.png')
        pygame.display.set_caption('Private Messenger')

        self.red = (205,24,1)
        self.hoverRed = (184,17,0)
        self.white = (255, 255, 255)

        self.user = userName
        self.key = generator.getPrime()
        self.n = self.key[0]*self.key[1]
        self.z = (self.key[0]-1)*(self.key[1]-1)
        self.e = generator.getE(self.n, self.z)
        self.d = generator.getD(self.z, self.e)
        self.shareInfo()
        self.menu()

    def shareInfo(self):
        if(self.user=='1'):
            with open("Info_1.txt", "w") as text_file:
                    print(self.e, file=text_file)
                    print(self.n, file=text_file)
        elif(self.user=='2'):
            with open("Info_2.txt", "w") as text_file:
                    print(self.e, file=text_file)
                    print(self.n, file=text_file)

    def textObjects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def menuButton(self, text, x, y, h, w, c, sc, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+50 > mouse[1] > y:
            pygame.draw.rect(self.screen, sc, (x,y,w,h))
            if click[0] == 1 and action != None:
                action()
                
        else:
            pygame.draw.rect(self.screen, c, (x,y,w,h))
            
        buttonFont = pygame.font.Font("Fonts/HelveticaRoman.ttf",20)
        textSurf, textRect = self.textObjects(text, buttonFont, self.white)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        self.screen.blit(textSurf, textRect)

    def menu(self):
        open("Storage_1.txt", 'w').close()
        open("Storage_2.txt", 'w').close()
        menu = True
        while menu:
            self.screen.blit(self.menuImg, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skor = False
                    pygame.quit()
                    quit()
            self.menuButton("Start Chatting", 30, 353, 45,307, self.red, self.hoverRed, self.chat)
            self.menuButton("Exit", 30, 413, 45,307, self.red, self.hoverRed, self.exitApp)
            pygame.display.update()

    def chat(self):
        chat.ChatWindow(self.user, self.d, self.n)

    def exitApp(self):
        pygame.quit()
        quit()
        
