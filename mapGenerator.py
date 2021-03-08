﻿import pygame
from Generator.button import *
pygame.init()

#gamewindow
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300
FPS = 60
clock = pygame.time.Clock()

currentTile = 0
TILESIZE = 32
ROWS = (SCREEN_WIDTH - LOWER_MARGIN) // TILESIZE
COLS = 150
GROUNDTILETYPES = 9
# define game variables
scrollLeft = False
scrollRight = False
scroll = 0
scrollSpeed = 1

screen = pygame.display.set_mode([SCREEN_WIDTH + SIDE_MARGIN,SCREEN_HEIGHT + LOWER_MARGIN])
pygame.display.set_caption("TANK Level Editor")


# load images
bitmap = pygame.image.load('Assets/tankbitmap.png').convert_alpha()
g1_img = pygame.image.load('Assets/ground1.png').convert_alpha()
g2_img = pygame.image.load('Assets/ground2.png').convert_alpha()
g3_img = pygame.image.load('Assets/ground3.png').convert_alpha()
g4_img = pygame.image.load('Assets/ground4.png').convert_alpha()
g5_img = pygame.image.load('Assets/ground5.png').convert_alpha()
g6_img = pygame.image.load('Assets/ground6.png').convert_alpha()
g7_img = pygame.image.load('Assets/ground7.png').convert_alpha()
g8_img = pygame.image.load('Assets/ground8.png').convert_alpha()
g9_img = pygame.image.load('Assets/ground9.png').convert_alpha()
platfrom_img = pygame.image.load('Assets/platform.png').convert_alpha()

# store tiles in a list
imgList = []
for i in range(GROUNDTILETYPES):
    img = pygame.image.load(f'Assets/ground{i+1}.png')
    imgList.append(img)
imgList.append(pygame.image.load('Assets/platform.png'))


# define colours
GREEN = (144,201,120)
WHITE = (255,255,255)
RED = (200,25,25)
ORANGE = (255,183,74)

# create empty tile list
worldData = []
for row in range(ROWS):
    r = [-1] * COLS
    worldData.append(r)

# create bottom border:
for tile in range(0,COLS):
    worldData[ROWS - 1][tile] = 0
    
print(worldData)

# function for drawing background:
def DrawBackground():
    screen.fill(GREEN)
    #widthG1 = g1_img.get_width()
    #screen.blit(g1_img,((widthG1 + 128) - scroll * 0.5,0))
    """
    widthG1 = g1_img.get_width()
    widthG2 = g2_img.get_width()
    tileCountX = int(SCREN_WIDTH / (tileSize)/2)
    mn = 1
    for x in range(tileCountX):
        screen.blit(g1_img,((2 * x * widthG1) - scroll,0))
        screen.blit(g2_img,((x * widthG2) - scroll,0))
    """
def DrawGrid():
    # vertical
    for i in range(COLS + 1):
        pygame.draw.line(screen, WHITE, (i * TILESIZE - scroll,0),(i * TILESIZE - scroll,SCREEN_HEIGHT))
    # horizontal
    for i in range(ROWS):
        pygame.draw.line(screen, WHITE, (0,i * TILESIZE),(SCREEN_WIDTH,i * TILESIZE))
# function for drawing world tiles
def DrawWorld():
    for y, row in enumerate(worldData):
        for x,tile in enumerate(row):
            if tile >= 0:
                #screen.blit(imgList[tile],(x * TILESIZE - scroll,y * tile))
                screen.blit(imgList[tile],(x * TILESIZE - scroll,y * TILESIZE))
                #screen.blit(imgList[tile],(x * TILESIZE - scroll,SCREEN_HEIGHT - TILESIZE))
                

# create buttons
buttonList = []
buttonCol = 0
buttonRow = 0
for i in range(len(imgList)):
    tileButton = Button(SCREEN_WIDTH + (75 * buttonCol) + 50, 75 * buttonRow + 50, imgList[i],1)
    buttonList.append(tileButton)
    buttonCol += 1
    if buttonCol == 3:
        buttonRow += 1
        buttonCol = 0
run = True
while run:

    # scroll the map
    if scrollLeft == True and scroll > 0:
        scroll -= 5 * scrollSpeed
    if scrollRight == True:
        scroll += 5 * scrollSpeed

    # add new tiles to the screen
    # get mouse position
    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll) // TILESIZE
    y = pos[1] // TILESIZE
    
    # check that the coordinates are within the tile area
    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        # update tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if worldData[y][x] != currentTile:
                worldData[y][x] = currentTile
    #print(x)
    #print(y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scrollLeft = True
            if event.key == pygame.K_RIGHT:
                scrollRight = True
            if event.key == pygame.K_RSHIFT:
                scrollSpeed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scrollLeft = False
            if event.key == pygame.K_RIGHT:
                scrollRight = False
            if event.key == pygame.K_RSHIFT:
                scrollSpeed = 1
    DrawBackground()
    DrawGrid()
    DrawWorld()
    # Draw panel area
    pygame.draw.rect(screen, ORANGE, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT+LOWER_MARGIN))
    # Draw buttons with my tiles:
    # choose a tile
    buttonCount = 0
    for buttonCount,i in enumerate(buttonList):
        if i.Draw(screen):
            currentTile = buttonCount
    #print(currentTile)
    # highlight the selected tile
    pygame.draw.rect(screen, RED, buttonList[currentTile].rect, 3)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()