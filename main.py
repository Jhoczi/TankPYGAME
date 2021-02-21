from game import Game

# GENERAL SETTINGS

# COLORS
COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0)
}


# PYGAME SETTINGS

# *============= GAME CLASS =============*



game = Game()
while game.start:
    game.play = True
    game.Run()
