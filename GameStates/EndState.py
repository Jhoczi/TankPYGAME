import pygame
from State.state import *
import game


class EndState(State):
    def __init__(self,game):
        State.__init__(self,game)

    def UpdateStateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.game.start = False
                #self.game.play = False
                self.runDisplay = False
                self.game.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runDisplay = False
                    self.game.currentState = self.game.mainMenu
                if event.key == pygame.K_RETURN:
                    self.game.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.game.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.game.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.game.UP_KEY = True
                if event.key == pygame.K_q:
                    self.game.Q_KEY = True
                    self.game.currentMenu = self.game.endState

    def Update(self):
        self.UpdateStateEvents()
        pygame.display.update()

    def RenderState(self):
        self.game.display.fill(self.game.BLACK)
        self.game.DrawText('Thanks for playing', 48, self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2)
        self.game.window.blit(self.game.display, (0,0))

    def DisplayState(self):
        print("jestem w end state")
        while self.runDisplay:
            self.Update()
            self.RenderState()




