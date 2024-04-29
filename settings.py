import pygame
from pygame.math import Vector2 as vector

FPS = 60 #Window FPS

WIDTH, HEIGHT = 800, 800 #Controls the width and height on the game window.



#Font

pygame.init()
default_font = pygame.font.Font('MPLUSRounded1c-Regular.ttf',25)



#Images

#Coin 1 Image
coin1_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_1.png')
coin1_img = pygame.transform.scale(coin1_img, (75,75))

#Coin 2 Image
coin2_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_2.png')
coin2_img = pygame.transform.scale(coin2_img, (75,75))

#Coin 3 Image
coin3_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_3.png')
coin3_img = pygame.transform.scale(coin3_img, (75,75))

#Coin 4 Image
coin4_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_4.png')
coin4_img = pygame.transform.scale(coin4_img, (75,75))

#Coin 5 Image
coin5_img = pygame.image.load('Assets\Coin_Buttons\Info_Coin_5.png')
coin5_img = pygame.transform.scale(coin5_img, (75,75))


#Lock Images
lock_20 = pygame.image.load('Assets\Locks\Lock_20.png')
lock_20 = pygame.transform.scale(lock_20, (500,280))

lock_50 = pygame.image.load('Assets\Locks\Lock_50.png')
lock_50 = pygame.transform.scale(lock_50, (500,280))

lock_100 = pygame.image.load('Assets\Locks\Lock_100.png')
lock_100 = pygame.transform.scale(lock_100, (500,280))

lock_250 = pygame.image.load('Assets\Locks\Lock_250.png')
lock_250 = pygame.transform.scale(lock_250, (500,280))


#Auto Images
white_auto = pygame.image.load('Assets\Auto_Buttons\white_auto.png')
white_auto = pygame.transform.scale(white_auto, (50,50))


green_auto = pygame.image.load('Assets\Auto_Buttons\green_auto.png')
green_auto = pygame.transform.scale(green_auto, (50,50))

red_auto = pygame.image.load('Assets\Auto_Buttons\cred_auto.png')
red_auto = pygame.transform.scale(red_auto, (50,50))

blue_auto = pygame.image.load('Assets\Auto_Buttons\cblue_auto.png')
blue_auto = pygame.transform.scale(blue_auto, (50,50))

yellow_auto = pygame.image.load('Assets\Auto_Buttons\yellow_auto.png')
yellow_auto = pygame.transform.scale(yellow_auto, (50,50))



#Sounds

poor_sfx = pygame.mixer.Sound('Assets\Sounds\incorrect_ding.mp3')
