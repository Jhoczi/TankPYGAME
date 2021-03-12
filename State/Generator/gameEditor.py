from State.state import *
from State.Generator.button import *

class GameEditor(State):
    def __init__(self, game):
        super().__init__(game)
        self.TILESIZE = 32
        self.LOWERMARGIN = 100
        self.SIDEMARGIN = 200
        self.ROWS = ( self.game.DISPLAY_WIDTH - self.LOWERMARGIN ) // self.TILESIZE
        self.COLS = 30
        self.scrollLeft = False
        self.scrollRight = False
        self.scroll = 0
        self.scrollSpeed = 1
        self.level = 0
        self.imgList = []
        self.saveButtonImg = ''
        self.loadButtonImg = ''
        self.worldData = []
        self.buttonList = []
        self.currentTile = 0
        self.init = True
    def InitImages(self):
        # load images
        groundTileTypes = 9
        # load button img
        self.saveButtonImg = pygame.image.load('img/saveButton.png').convert_alpha()
        self.loadButtonImg = pygame.image.load('img/loadButton.png').convert_alpha()
        # store tiles in a list
        for i in range(groundTileTypes):
            img = pygame.image.load(f'Assets/ground{i+1}.png').convert_alpha()
            self.imgList.append(img)
        self.imgList.append(pygame.image.load('Assets/platform.png').convert_alpha())
    def InitWorldData(self):
        for row in range(self.ROWS):
            r = [-1] * self.COLS
            self.worldData.append(r)
    def InitButtons(self):
        buttonCol = 0
        buttonRow = 0
        for i in range(len(self.imgList)):
            tileButton = Button(self.game.DISPLAY_WIDTH - self.SIDEMARGIN + (75 * buttonCol) + 50, 75 * buttonRow + 50, self.imgList[i],1)
            self.buttonList.append(tileButton)
            buttonCol += 1
            if buttonCol == 3:
                buttonRow += 1
                buttonCol = 0
        self.saveButton = Button(0.15 * self.game.DISPLAY_WIDTH, self.game.DISPLAY_HEIGHT - self.LOWERMARGIN // 2, self.saveButtonImg, 0.35)
        self.loadButton = Button(0.15 * self.game.DISPLAY_WIDTH + 75, self.game.DISPLAY_HEIGHT - self.LOWERMARGIN // 2, self.loadButtonImg, 0.35)
        print("Init buttons")
    def InitEditorSettings(self):
        self.InitImages()
        self.InitWorldData()
        self.InitButtons()
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
    def DrawGrid(self):
        # vertical
        for i in range(self.COLS + 1):
            pygame.draw.line(self.game.display, self.game.WHITE, (i * self.TILESIZE - self.scroll,0),(i * self.TILESIZE - self.scroll,self.game.DISPLAY_HEIGHT - self.LOWERMARGIN))
        # horizontal
        for i in range(self.ROWS):
            pygame.draw.line(self.game.display, self.game.WHITE, (0,i * self.TILESIZE),(self.game.DISPLAY_WIDTH - self.SIDEMARGIN,i * self.TILESIZE))
    def DrawGameEditorPanel(self):
        pygame.draw.rect(self.game.display, self.game.LIGHTDARK, (self.game.DISPLAY_WIDTH - self.SIDEMARGIN, 0, self.SIDEMARGIN, self.game.DISPLAY_HEIGHT+self.LOWERMARGIN))
        pygame.draw.rect(self.game.display, self.game.LIGHTDARK, (0, self.game.DISPLAY_HEIGHT - self.LOWERMARGIN, self.game.DISPLAY_WIDTH, self.game.DISPLAY_HEIGHT - self.LOWERMARGIN))
        buttonCount = 0
        for buttonCount,i in enumerate(self.buttonList):
            if i.Draw(self.game.display):
                self.currentTile = buttonCount
        # highlight the selected tile
        pygame.draw.rect(self.game.display, self.game.WHITE, self.buttonList[self.currentTile].rect, 3)
        self.game.DrawText(f'Level - {self.level}',30, 0.4 * self.game.DISPLAY_WIDTH, self.game.DISPLAY_HEIGHT - self.LOWERMARGIN // 2)
        self.saveButton.Draw(self.game.display)
        self.loadButton.Draw(self.game.display)
    def RenderState(self):
        self.game.display.fill(self.game.RED)
        pygame.draw.rect(self.game.display, self.game.RED, (self.game.DISPLAY_WIDTH, 0, self.SIDEMARGIN, self.game.DISPLAY_HEIGHT+self.LOWERMARGIN))
        self.DrawGrid()
        self.DrawGameEditorPanel()
        self.BlitScreen()
    def DisplayState(self):
        self.runDisplay = True
        if (self.init):
            self.InitEditorSettings()
            self.init = False
        while self.runDisplay:
            self.Update()
            self.RenderState()