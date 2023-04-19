import  pygame
import sys
from screeninfo import get_monitors
import datetime
#import os

pygame.init()
pygame.font.init()

#classes
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height
        self.rect = self.img.get_rect(center=(self.x, 0))
        self.img.convert_alpha()
        self.img.set_colorkey((255, 255, 255))
        self.img.convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

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
player_icon = pygame.image.load('src/images/space-ship.png')

#global parameters
FPS = 60
screen_title = "Space shooter | rol506, donard506"
def_player_x = 0
def_player_y = 0

#screen set up
screen = pygame.display.set_mode(get_resolution())
pygame.display.set_caption(screen_title)
pygame.display.set_icon(screen_icon)

#fonts set up
font_ChiveMonoItalic = pygame.font.Font("src/fonts/ChivoMono-Italic-VariableFont_wght.ttf", 20)
font_ChiveMono = pygame.font.Font("src/fonts/ChivoMono-VariableFont_wght.ttf", 20)

#objects
player = Player(910, 620, player_icon, 300, 300)

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
    screen.blit(player.img, (player.x, player.y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pass