from settings import *
import button

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        play_img = pygame.image.load('Assets\Play_Button.png')
        play_img = pygame.transform.scale(play_img, (150,150))
        self.play_button = button.Button(230,220,play_img)
                


    def run(self):
        self.display_surface.fill('white') #Window Colour

        if self.play_button.draw(self.display_surface):
            print("click")
