from settings import *
from world import World

class Game:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Coin Clicker")

        self.clock = pygame.time.Clock()

        self.world_screen = World()
        


    def run(self):
        while True:
            fps = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()


            self.world_screen.run()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()