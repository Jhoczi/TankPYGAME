from State.state import *
from Entity.player import *

class GameState(State):
    def __init__(self,game):
        super().__init__(game)
        self.playerSpriteSRC = 'Assets/tank1_32x32.png'
        self.bitMapSRC = 'Assets/tankbitmap.png'
        self.player = Player(self.playerSpriteSRC,self.game)
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
    def CheckInput(self):
        if self.game.BACK_KEY:
            print('wciskam backspace')
            self.runDisplay = False
            self.game.ChangeState()
    def Update(self):
        self.UpdateStateEvents()
        self.CheckInput()
        self.player.Update()
    def RenderState(self):
        self.game.display.fill(self.game.RED)
        self.game.display.blit(self.player.entityImage,(self.player.positionX,self.player.positionY))
        #self.bitmap.Draw(self.game.display)
        self.BlitScreen()
    def DisplayState(self):
        self.runDisplay = True
        while self.runDisplay:
            self.Update()
            self.RenderState()