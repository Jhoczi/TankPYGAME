import pygame
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.FPS = 30
        self.DISPLAY_WIDTH = 640
        self.DISPLAY_HEIGHT = 420
        self.start = True
        self.play = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.display = pygame.Surface((self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.font_name = 'Fonts/tank.ttf'     
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.mainMenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.currentMenu = self.mainMenu
        pygame.display.set_caption("Tank Game")
        
    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.start = False
                self.play = False
                self.currentMenu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.start = False
                    self.play = False
                    self.currentMenu.run_display = False
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    def ResetKeys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
    def DrawText(self, text, size, x,y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    def Update(self):
        self.UpdateEvents()
        pygame.display.update()
        #self.clock.tick(self.FPS)
        self.ResetKeys()
    def Render(self):
        self.display.fill(self.BLACK)
        self.DrawText('Thanks for playing',48,self.DISPLAY_WIDTH/2, self.DISPLAY_HEIGHT/2)
        self.window.blit(self.display, (0,0))

    def Run(self):
        while self.play:
            self.Update()
            if self.START_KEY:
                self.play = False
            self.Render()
            