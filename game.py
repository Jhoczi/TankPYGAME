import pygame
from State.GameStates.menu import *
from State.GameStates.endstate import *
from State.GameStates.gamestate import *
from Entity.entity import *
from Entity.player import *

class Game():
    def __init__(self):
        pygame.init()
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.DISPLAY_WIDTH = 800
        self.DISPLAY_HEIGHT = 640
        self.start = True
        self.active = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.display = pygame.Surface((self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.tileSize = 32
        self.font_name = 'Fonts/tank.ttf'
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.gameState = GameState(self)
        self.mainMenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.endState = EndState(self)
        self.stateGroup = []
        self.currentState = self.endState
    def InitGameSettings(self):
        pygame.display.set_caption("Tank Game")
        self.stateGroup.append(self.endState)
        self.stateGroup.append(self.mainMenu)
        self.currentState = self.stateGroup[self.stateGroup.count(self.stateGroup)-1]
    def ChangeState(self):
        self.stateGroup.pop()
        self.currentState = self.stateGroup[self.stateGroup.count(self.stateGroup)-1]
        self.currentState.runDisplay = True
    def AddState(self,state):
        self.stateGroup.append(state)
        self.currentState = self.stateGroup[self.stateGroup.count(self.stateGroup)-1]
    """
    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.start = False
                self.play = False
                self.currentState.runDisplay = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.start = False
                    self.play = False
                    self.currentState.run_display = False
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_q:
                    self.Q_KEY = True
                    self.currentState = self.endState
    """
    def DrawText(self, text, size, x,y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    def Update(self):
        #self.UpdateEvents()
        pygame.display.update()
        self.clock.tick(self.FPS) #<- DELTA TIME HERE
        self.currentState.ResetKeys()
    def Render(self):
        #self.display.fill(self.BLACK)
        self.currentState.DisplayState()
        self.window.blit(self.display, (0,0))
    def Run(self):
        self.InitGameSettings()
        while self.start:
            self.Update()
            self.Render()
