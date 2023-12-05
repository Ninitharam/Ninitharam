###Visual Stdio IDE###

import pygame
import random

pygame.init()
winHeight = 600
winWidth = 700
win=pygame.display.set_mode((winWidth,winHeight))
pygame.display.set_caption("Hangman Game! BY SHOURYA PANT")

### Initializing The COLOURS that will be used in the PROJECT###

BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (50,205,50)
BLUE = (0,0,255)
LIGHT_BLUE = (51,161,201)
PURPLE=(150,0,211)
ORANGE=(255,69,0)
MAGENTA=(220,25,60)
YELLOW=(255,215,0)
RANDOMCOLOUR=(255,20,147)

#### Initializing The FONTS AND VARIABLES that will be used in the PROJECT####

btn_font = pygame.font.SysFont("Algerian", 30)
guess_font = pygame.font.SysFont("Permanentmarker", 40)
lost_font = pygame.font.SysFont('Ravie', 24)
word_font=pygame.font.SysFont('Jokerman', 30)
TITLE_FONT=pygame.font.SysFont('Permanentmarker',40)
word = ''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

limbs = 0

## DEFINING THE REDRAW GAME WINDOW FUNCTION THAT WILL PLAY A MAIN ROLE IN OUR PROJECT ##

def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    win.fill(LIGHT_BLUE)
    text = TITLE_FONT.render("HANGMAN BY SHOURYA PANT", 1, YELLOW)
    win.blit(text, (winWidth/2 - text.get_width()/2, 480))
    # Buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, PURPLE)
    rect = label1.get_rect()
    length = rect[2]
    
    win.blit(label1,(winWidth/2 - length/2, 400))

    pic = hangmanPics[limbs]
    win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
    pygame.display.update()
