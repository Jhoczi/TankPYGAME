import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.DISPLAY_WIDTH / 2
        self.mid_h = self.game.DISPLAY_HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def DrawCursor(self):
        self.game.DrawText('*', 30, self.cursor_rect.x, self.cursor_rect.y + 5)

    def BlitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.ResetKeys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
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
        self.MoveCursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.play = True
            elif self.state == 'Options':
                self.game.currentMenu = self.game.options
            elif self.state == 'Credits':
                self.game.currentMenu = self.game.credits
            self.run_display = False

    def DisplayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.UpdateEvents()
            self.CheckInput()
            self.game.display.fill(self.game.BLACK)
            self.game.DrawText('Main Menu', 48, self.mid_w, self.mid_h - 100)
            self.game.DrawText('Start Game', 38, self.mid_w, self.start_Y)
            self.game.DrawText('Options', 38, self.mid_w, self.options_Y)
            self.game.DrawText('Credits', 38, self.mid_w, self.credits_Y)
            self.DrawCursor()
            self.BlitScreen()


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volumeX = self.mid_w
        self.volumeY = self.mid_h + 30
        self.controlsX = self.mid_w
        self.controlsY = self.mid_h + 70
        self.cursor_rect.midtop = (self.volumeX + self.offset, self.volumeY)

    def CheckInput(self):
        if self.game.BACK_KEY:
            self.game.currentMenu = self.game.mainMenu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsX + self.offset, self.controlsY)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volumeX + self.offset, self.volumeY)
        elif self.game.START_KEY:
            # TODO: Create a functionaliyty of Volume Menu and Controls Menu
            pass

    def DisplayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.UpdateEvents()
            self.CheckInput()
            self.game.display.fill(self.game.BLACK)
            self.game.DrawText('Options', 48, self.mid_w, self.mid_h - 100)
            self.game.DrawText('Volume', 38, self.volumeX, self.volumeY)
            self.game.DrawText('Controls', 38, self.controlsX, self.controlsY)
            self.DrawCursor()
            self.BlitScreen()
            
class CreditsMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
        
    def DisplayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.UpdateEvents()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.currentMenu = self.game.mainMenu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.DrawText('Credits',48,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 100)
            self.game.DrawText('Author - Jakub Hoczek',38,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 + 10)
            self.game.DrawText('Great thanks for Christian Duenas',38,self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 + 50)
            self.BlitScreen()