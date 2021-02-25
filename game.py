﻿import pygame, time
from menu import *
from GameStates.EndState import EndState
from State import *

class Game():
    def __init__(self):
        pygame.init()
        self.__FPS = 30
        self.DISPLAY_WIDTH = 640
        self.DISPLAY_HEIGHT = 420
        self.start = True
        self.active = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.Q_KEY = False
        self.display = pygame.Surface((self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.font_name = 'Fonts/tank.ttf'
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.mainMenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.endState = EndState(self)
        self.stateGroup = []
        self.currentState = self.mainMenu

    def InitGameSettings(self):
        pygame.display.set_caption("Tank Game")
        self.stateGroup.append(self.mainMenu)
        self.stateGroup.append(self.endState)
    def ChangeState(self,state):
        self.currentState = state
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
        self.currentState.ResetKeys()
    def Render(self):
        self.display.fill(self.BLACK)
        self.window.blit(self.display, (0,0))
    def Run(self):
        self.InitGameSettings()
        while self.start:
            self.currentState.DisplayState()
            self.Update()
            if self.START_KEY:
                self.active = False
            self.Render()
