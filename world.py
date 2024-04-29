from settings import *
import button
import bars

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        #Coin Buttons
        self.coin_one = button.Button(30,25,coin1_img)
        self.coin_two = button.Button(30,125,coin2_img)
        self.coin_three = button.Button(30,225,coin3_img)
        self.coin_four = button.Button(30,325,coin4_img)
        self.coin_five = button.Button(30,425,coin5_img)

        self.coins = 0 #Playeres current coins.



    def run(self):
        #Window Colour
        self.display_surface.fill('grey') #Window Colour

        #Player Coin Count
        self.score_text = default_font.render(f'Coins: {self.coins}', True, 'Black')
        self.display_surface.blit(self.score_text, (1025,25))

        #Buttons
        if self.coin_one.draw(self.display_surface): 
            print("coin 1")
            self.coins += 1
        
        if self.coin_two.draw(self.display_surface): 
            print("coin 2")
            self.coins += 10

        if self.coin_three.draw(self.display_surface): 
            print("coin 3")

        if self.coin_four.draw(self.display_surface): 
            print("coin 4")

        if self.coin_five.draw(self.display_surface): 
            print("coin 5")
