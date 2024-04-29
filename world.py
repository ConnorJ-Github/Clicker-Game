from settings import *
import button

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        #Coin Buttons
        self.coin_one = button.Button(30,25,coin1_img)
        self.coin_two = button.Button(30,125,coin2_img)
        self.coin_three = button.Button(30,225,coin3_img)
        self.coin_four = button.Button(30,325,coin4_img)
        self.coin_five = button.Button(30,425,coin5_img)


        #Unlock Buttons
        self.lock_20 = button.Button(30, 25, lock_20)
        self.lock_50 = button.Button(30,130, lock_50)
        self.lock_100 = button.Button(30,235, lock_100)
        self.lock_250 = button.Button(30,335, lock_250)


        #Progress bar values.
        self.draw_black = False
        self.draw_green = False
        self.draw_red = False
        self.draw_blue = False
        self.draw_yellow = False

        #Length of the progress bar
        self.black_length = 0
        self.green_length = 0
        self.red_length = 0
        self.blue_length = 0
        self.yellow_length = 0

        #pygame CE is used, so if you are experiencing errors here. That may be why.
        #Speed at which progress is earned. 
        self.black_speed = 5
        self.green_speed = 2.5
        self.red_speed = 1.25
        self.blue_speed = 0.625
        self.yellow_speed = 0.3125

        self.unlock_20 = False

        self.coins = 0 #Playeres current coins.
        self.value = 0 #The values that coins have



    def draw_bars(self, colour, y_offset, draw, length, speed):

        if draw and length < 400:
            length += speed
        elif length >= 400:
            draw = False
            length = 0
            self.coins += self.value


        pygame.draw.rect(self.display_surface, colour, [120, y_offset, 400,50 ])
        pygame.draw.rect(self.display_surface, 'white', [125, y_offset + 5, 390,40 ])
        pygame.draw.rect(self.display_surface, colour, [125, y_offset, length,50 ])

        return length, draw

        # pygame.draw.rect(self.display_surface, 'black', [120, 35, 400,50 ])
        # pygame.draw.rect(self.display_surface, 'white', [125, 40, 390,40 ])
        



    def run(self):
        #Window Colour
        self.display_surface.fill('grey') #Window Colour

        #Player Coin Count
        self.score_text = default_font.render(f'Coins: {self.coins}', True, 'Black')
        self.display_surface.blit(self.score_text, (1025,25))

        #Buttons
        if self.coin_one.draw(self.display_surface): 
            self.draw_black = True
            self.value = 1

        if self.coin_two.draw(self.display_surface): 
            self.draw_green = True
            self.value = 5

        if self.coin_three.draw(self.display_surface): 
            self.draw_red = True
            self.value = 10

        if self.coin_four.draw(self.display_surface): 
            self.draw_blue = True
            self.value = 20

        if self.coin_five.draw(self.display_surface): 
            self.draw_yellow = True
            self.value = 50

        #Progress bars
        self.black_length, self.draw_black = self.draw_bars('black', 35, self.draw_black, self.black_length, self.black_speed)
        self.green_length, self.draw_green = self.draw_bars('green', 135, self.draw_green, self.green_length, self.green_speed)
        self.red_length, self.draw_red = self.draw_bars('red', 235, self.draw_red, self.red_length, self.red_speed)
        self.blue_length , self.draw_blue = self.draw_bars('blue', 335, self.draw_blue, self.blue_length, self.blue_speed)
        self.yellow_length,self.draw_yellow = self.draw_bars('yellow', 435, self.draw_yellow, self.yellow_length, self.yellow_speed)


        #Unlock Buttons

        if self.unlock_20 == False:
            if self.lock_20.draw(self.display_surface):
                if self.coins >= 20:
                    self.unlock_20 = True
                else:
                    pass

        if self.lock_50.draw(self.display_surface): 
            pass

        if self.lock_100.draw(self.display_surface): 
            pass

        if self.lock_250.draw(self.display_surface): 
            pass
