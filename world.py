from settings import *
import button

#Bugs List

#Button overlapping (As the buttons are circles and the button selection area are rect. The selection area is larger than needed)
#Bug caused by issue above - Buttons will unlock due to proxy when funds are met.

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        #Coin Buttons
        self.coin_one = button.Button(30,25,coin1_img)
        self.coin_two = button.Button(30,125,coin2_img)
        self.coin_three = button.Button(30,225,coin3_img)
        self.coin_four = button.Button(30,325,coin4_img)
        self.coin_five = button.Button(30,425,coin5_img)

        #Coin values 

        self.black_value = 1
        self.green_value = 5
        self.red_value = 10
        self.blue_value = 20
        self.yellow_value = 50

        #Unlock Buttons
        self.lock_20 = button.Button(30, 25, lock_20)
        self.lock_50 = button.Button(30,130, lock_50)
        self.lock_100 = button.Button(30,235, lock_100)
        self.lock_250 = button.Button(30,335, lock_250)

        #Auto Buttons
        self.auto_black = button.Button(30, 600, white_auto)
        self.auto_green = button.Button(90, 600, green_auto)
        self.auto_red = button.Button(150, 600, red_auto)
        self.auto_blue = button.Button(210, 600, blue_auto)
        self.auto_yellow = button.Button(270, 600, yellow_auto)

        self.automatic_black = False
        self.automatic_green = False
        self.automatic_red = False
        self.automatic_blue = False
        self.automatic_yellow = False

        #Power up Buttons

        self.power_one = button.Button(30, 730, power_one)
        self.power_two = button.Button(90, 730, power_two)


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


        #Locks for higher tier coins
        self.unlock_20 = False
        self.unlock_50 = False
        self.unlock_100 = False
        self.unlock_250 = False

        self.coins = 100 #Playeres current coins.




    def draw_bars(self, colour, y_offset, draw, value, length, speed):

        if draw and length < 400:
            length += speed
        elif length >= 400:
            draw = False
            length = 0
            self.coins += value


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
        score_text = default_font.render(f'Coins: {self.coins}', True, 'Black')
        self.display_surface.blit(score_text, (600,25))

        #Titles
        auto_text = default_font.render('Auto Upgrade - 1000 Each', True, 'Black')
        self.display_surface.blit(auto_text,(30,550))

        power_text = default_font.render('Power Up - 500 Each', True, 'Black')
        self.display_surface.blit(power_text,(30,670))

        #Buttons
        if self.coin_one.draw(self.display_surface): 
            self.draw_black = True

        if self.coin_two.draw(self.display_surface): 
            self.draw_green = True

        if self.coin_three.draw(self.display_surface): 
            self.draw_red = True

        if self.coin_four.draw(self.display_surface): 
            self.draw_blue = True

        if self.coin_five.draw(self.display_surface): 
            self.draw_yellow = True

        #Progress bars
        self.black_length, self.draw_black = self.draw_bars('black', 35, self.black_value, self.draw_black, self.black_length, self.black_speed)
        self.green_length, self.draw_green = self.draw_bars('green', 135,self.green_value, self.draw_green, self.green_length, self.green_speed)
        self.red_length, self.draw_red = self.draw_bars('red', 235, self.red_value, self.draw_red, self.red_length, self.red_speed)
        self.blue_length , self.draw_blue = self.draw_bars('blue', 335, self.blue_value, self.draw_blue, self.blue_length, self.blue_speed)
        self.yellow_length, self.draw_yellow = self.draw_bars('yellow', 435, self.yellow_value, self.draw_yellow, self.yellow_length, self.yellow_speed)


        #Unlock Buttons

        if self.unlock_20 == False:
            if self.lock_20.draw(self.display_surface) and self.coins >= 20:
                self.unlock_20 = True
                self.coins -= 20

        
        if self.unlock_50 == False:
            if self.lock_50.draw(self.display_surface) and self.coins >= 50:
                self.unlock_50 = True
                self.coins -= 50

        if self.unlock_100 == False:
            if self.lock_100.draw(self.display_surface) and self.coins >= 100:
                self.unlock_100 = True
                self.coins -= 100

        if self.unlock_250 == False:
            if self.lock_250.draw(self.display_surface) and self.coins >= 250:
                self.unlock_250 = True
                self.coins -= 250


        #auto Buttons

        if self.auto_black.draw(self.display_surface):
            self.draw_black = True
            self.coins -= 1000
        

        if self.auto_green.draw(self.display_surface):
            self.draw_green = True
            self.coins -= 1000


        if self.auto_red.draw(self.display_surface):
            self.draw_red = True
            self.coins -= 1000

        if self.auto_blue.draw(self.display_surface):
            self.draw_blue = True
            self.coins -= 1000

        if self.auto_yellow.draw(self.display_surface):
            self.draw_yellow = True
            self.coins -= 1000


        #power up buttons

        if self.power_one.draw(self.display_surface) and self.coins >= 500:
            self.red_speed = self.red_speed * 2
            self.blue_speed = self.blue_length * 2
            self.black_speed = self.black_speed * 2
            self.green_speed = self.green_speed * 2
            self.yellow_speed = self.yellow_speed * 2
            self.coins -= 500

        if self.power_two.draw(self.display_surface) and self.coins >= 500:
                self.coins *= 2
                self.coins -= 500

