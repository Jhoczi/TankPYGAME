import pygame
import game
from abc import abstractmethod, ABC


class State(ABC):
    def __init__(self,game):
        self.game = game
        self.runDisplay = True
    @abstractmethod
    def DisplayState(self):
        pass
    def ResetKeys(self):
        self.game.UP_KEY = False
        self.game.DOWN_KEY = False
        self.game.START_KEY = False
        self.game.BACK_KEY = False
        self.game.Q_KEY = False
    @abstractmethod
    def UpdateStateEvents(self):
        pass
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def RenderState(self):
        pass