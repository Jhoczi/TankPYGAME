import pygame
import game
from abc import abstractmethod, ABC
class Entity(ABC,pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.positionX = 0
        self.positionY = 0
        self.width = 10
        self.height = 10
        self.velocity = 0
        # INIT FUNCTION INSIDE CONSTRUCTOR
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255,255,255)) #WHITE
        self.rect = self.image.get_rect()
    def SetEntityImage(self,source):
        self.entityImage = pygame.image.load(source)
        
class Tank(Entity):
    def __init__(self,source):
        Entity.__init__(self)
        self.SetEntityImage(source)

