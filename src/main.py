import  pygame
import sys
from screeninfo import get_monitors
import datetime
#import os

pygame.init()
pygame.font.init()

#getting resolution info
def get_resolution(need_print=False):
    for m in get_monitors():
        global width_res, height_res, resolution
        width_res = m.width
        height_res = m.height
        resolution = (width_res, height_res)
        if need_print:
            print(resolution)
            return resolution
        return resolution

#images
screen_icon = pygame.image.load('src/images/test_icon.png')
screen_background = pygame.image.load("src/images/background.png")

#global parameters
FPS = 60
screen_title = "Space shooter | rol506, donard506"

#screen set up
screen = pygame.display.set_mode(get_resolution())
pygame.display.set_caption(screen_title)
pygame.display.set_icon(screen_icon)

#fonts set up
font_ChiveMonoItalic = pygame.font.Font("src/fonts/ChivoMono-Italic-VariableFont_wght.ttf", 20)
font_ChiveMono = pygame.font.Font("src/fonts/ChivoMono-VariableFont_wght.ttf", 20)

#game
running_game = True
while running_game:

    #current time
    current_date_time = datetime.datetime.now()
    game_current_time = str(current_date_time.time())[0:7]
    game_current_time_text = font_ChiveMono.render(game_current_time, True, "Red")

    screen_background.convert()
    screen.blit(screen_background, (0, 0))
    screen.blit(game_current_time_text, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pass