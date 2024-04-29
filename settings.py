import pygame
from pygame.math import Vector2 as vector

FPS = 60 #Window FPS

WIDTH, HEIGHT = 1200, 800 #Controls the width and height on the game window.



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

