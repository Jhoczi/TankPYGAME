from game import Game

game = Game()
while game.start:
    game.currentMenu.DisplayMenu()
    game.Run()
