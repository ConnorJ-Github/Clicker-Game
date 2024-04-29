from settings import *
import button

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        coin1_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_1.png')
        coin1_img = pygame.transform.scale(coin1_img, (75,75))
        self.coin_one = button.Button(30,25,coin1_img)

        coin2_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_2.png')
        coin2_img = pygame.transform.scale(coin2_img, (75,75))
        self.coin_two = button.Button(30,125,coin2_img)

        coin3_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_3.png')
        coin3_img = pygame.transform.scale(coin3_img, (75,75))
        self.coin_three = button.Button(30,225,coin3_img)

        coin4_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_4.png')
        coin4_img = pygame.transform.scale(coin4_img, (75,75))
        self.coin_four = button.Button(30,325,coin4_img)

        coin5_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_5.png')
        coin5_img = pygame.transform.scale(coin5_img, (75,75))
        self.coin_five = button.Button(30,425,coin5_img)
                


    def run(self):
        self.display_surface.fill('grey') #Window Colour

        if self.coin_one.draw(self.display_surface): 
            print("coin 1")
        
        if self.coin_two.draw(self.display_surface): 
            print("coin 2")

        if self.coin_three.draw(self.display_surface): 
            print("coin 3")

        if self.coin_four.draw(self.display_surface): 
            print("coin 4")

        if self.coin_five.draw(self.display_surface): 
            print("coin 5")
