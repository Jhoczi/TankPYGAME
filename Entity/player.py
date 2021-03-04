from Entity.entity import Entity

class Player(Entity):
    def __init__(self,source,game):
        Entity.__init__(self)
        self.game = game
        self.SetEntityImage(source)
        self.name = "Player 1"
        self.hp = 100
        self.positionX = game.DISPLAY_WIDTH/2
        self.positionY = game.DISPLAY_HEIGHT/2
        self.velocity = 0.0
    # TODO: move function to update or render??
    def Move(self):
        self.positionY += self.velocity
    def Update(self):
        self.Move()
    def Display(self):
        pass