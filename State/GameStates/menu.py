import pygame
from State.state import *

class Menu(State):
    def __init__(self, game):
        State.__init__(self,game)
        self.mid_w = self.game.DISPLAY_WIDTH / 2
        self.mid_h = self.game.DISPLAY_HEIGHT / 2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
    def DrawCursor(self):
        self.game.DrawText('*', 30, self.cursor_rect.x, self.cursor_rect.y + 5)
    def BlitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.ResetKeys()
    def UpdateStateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runDisplay = False
                self.game.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runDisplay = False
                    self.game.ChangeState()
                if event.key == pygame.K_RETURN:
                    self.game.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.game.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.game.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.game.UP_KEY = True
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def RenderState(self):
        pass
    @abstractmethod
    def DisplayState(self):
        pass

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.start_X = self.mid_w
        self.start_Y = self.mid_h
        self.options_X = self.mid_w
        self.options_Y = self.mid_h + 50
        self.credits_X = self.mid_w
        self.credits_Y = self.mid_h + 100
        self.cursor_rect.midtop = (self.start_X + self.offset, self.start_Y)
    def MoveCursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.options_X + self.offset, self.options_Y)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.credits_X + self.offset, self.credits_Y)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.start_X + self.offset, self.start_Y)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.credits_X + self.offset, self.credits_Y)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.start_X + self.offset, self.start_Y)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.options_X + self.offset, self.options_Y)
                self.state = 'Options'
    def CheckInput(self):
        if self.game.START_KEY:
            if self.state == 'Start':
                print("odpalam giere")
                self.game.AddState(self.game.gameState)
                self.runDisplay = False
            elif self.state == 'Options':
                print('odpalam opcje')
                self.game.AddState(self.game.options)
                self.runDisplay = False
                #self.game.ChangeState()
            elif self.state == 'Credits':
                self.game.AddState(self.game.credits)
                self.runDisplay = False
    def Update(self):
        self.UpdateStateEvents()
        self.CheckInput()
        self.MoveCursor()
        self.ResetKeys()
    def RenderState(self):
        self.game.display.fill(self.game.BLACK)
        self.game.DrawText('Main Menu', 48, self.mid_w, self.mid_h - 100)
        self.game.DrawText('Start Game', 38, self.mid_w, self.start_Y)
        self.game.DrawText('Options', 38, self.mid_w, self.options_Y)
        self.game.DrawText('Credits', 38, self.mid_w, self.credits_Y)
        self.DrawCursor()
        self.BlitScreen()
    def DisplayState(self):
        print("jestem w main state")
        while self.runDisplay:
            self.Update()
            self.RenderState()

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Graphic'
        self.graphicX = self.mid_w
        self.graphicY = self.mid_h + 30
        self.volumeX = self.mid_w
        self.volumeY = self.mid_h + 70
        self.controlsX = self.mid_w
        self.controlsY = self.mid_h + 110
        self.cursor_rect.midtop = (self.graphicX + self.offset, self.graphicY)
    def MoveCursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Graphic':
                self.cursor_rect.midtop = (self.graphicX + self.offset, self.graphicY)
                #self.state = 'Volume'
            elif self.state == 'Volume':
                self.cursor_rect.midtop = (self.volumeX + self.offset, self.volumeY)
                #self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.controlsX + self.offset, self.controlsY)
                #self.state = 'Graphic'
        elif self.game.UP_KEY:
            if self.state == 'Graphic':
                self.cursor_rect.midtop = (self.graphicX + self.offset, self.graphicY)
                #self.state = 'Controls'
            elif self.state == 'Volume':
                self.cursor_rect.midtop = (self.volumeX + self.offset, self.volumeY)
                #self.state = 'Graphic'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.controlsX + self.offset, self.controlsY)
                #self.state = 'Volume'
    def CheckInput(self):
        if self.game.BACK_KEY:
            print('wciskam backspace')
            self.runDisplay = False
            self.game.ChangeState()
        elif self.game.DOWN_KEY:
            if self.state == 'Graphic':
                self.state = 'Volume'
                #self.cursor_rect.midtop = (self.controlsX + self.offset, self.controlsY)
            elif self.state == 'Volume':
                self.state = 'Controls'
                #self.cursor_rect.midtop = (self.volumeX + self.offset, self.volumeY)
            elif self.state == 'Controls':
                self.state = 'Graphic'
        elif self.game.UP_KEY:
            if self.state == 'Graphic':
                self.state = 'Controls'
                #self.cursor_rect.midtop = (self.controlsX + self.offset, self.controlsY)
            elif self.state == 'Volume':
                self.state = 'Graphic'
                #self.cursor_rect.midtop = (self.volumeX + self.offset, self.volumeY)
            elif self.state == 'Controls':
                self.state = 'Volume'
        elif self.game.START_KEY:
            # TODO: Create a functionaliyty of Volume Menu and Controls Menu
            pass
    def Update(self):
        self.UpdateStateEvents()
        self.CheckInput()
        self.MoveCursor()
        self.ResetKeys()
    def RenderState(self):
        self.game.display.fill(self.game.BLACK)
        self.game.DrawText('Options', 48, self.mid_w, self.mid_h - 100)
        self.game.DrawText('Graphic', 38, self.graphicX, self.graphicY)
        self.game.DrawText('Volume', 38, self.volumeX, self.volumeY)
        self.game.DrawText('Controls', 38, self.controlsX, self.controlsY)
        self.DrawCursor()
        self.BlitScreen()
    def DisplayState(self):
        self.runDisplay = True
        while self.runDisplay:
            self.Update()
            self.RenderState()

class CreditsMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)

    def CheckInput(self):
        if self.game.BACK_KEY:
            print('wciskam backspace')
            self.runDisplay = False
            self.game.ChangeState()

    def Update(self):
        self.UpdateStateEvents()
        self.CheckInput()
        self.ResetKeys()

    def RenderState(self):
        self.game.display.fill(self.game.BLACK)
        self.game.DrawText('Credits',48,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 100)
        self.game.DrawText('Author - Jakub Hoczek',38,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 + 10)
        self.game.DrawText('Great thanks for Christian Duenas',38,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 + 50)
        self.BlitScreen()

    def DisplayState(self):
        self.runDisplay = True
        while self.runDisplay:
            self.Update()
            self.RenderState()

    def DisplayMenu(self):
        #self.run_display = True
        while self.run_display:
            self.Update()
            self.RenderState() 
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.currentMenu = self.game.mainMenu
                self.run_display = False
            #self.game.display.fill(self.game.BLACK)
            #self.game.DrawText('Credits',48,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 100)
            #self.game.DrawText('Author - Jakub Hoczek',38,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 + 10)
            #self.game.DrawText('Great thanks for Christian Duenas',38,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 + 50)
            #self.BlitScreen()