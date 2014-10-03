import pygame
from pygame.locals import *
import sys
import time
from math import *
from random import *

from classes.field import Field
from classes.player import Player
from classes.constants import *

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    # set up the window
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('My Test Game')

    DISPLAYSURF.fill(BGCOLOR)

    field = Field()
    player = Player()

    curKey = NONE
    curKey2 = NONE
    posKey1 = NONE
    posKey2 = NONE

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT):
                player.isActive = True

                if curKey == NONE:
                    curKey = event.key
                elif event.key == posKey1 or event.key == posKey2:
                    curKey2 = event.key
                    posKey1 = NONE
                    posKey2 = NONE
 
                if curKey2 == NONE:
                    if curKey == K_UP:
                        DIRECTION = UP
                        posKey1 = K_LEFT
                        posKey2 = K_RIGHT
                    elif curKey == K_DOWN:
                        DIRECTION = DOWN
                        posKey1 = K_LEFT
                        posKey2 = K_RIGHT
                    elif curKey == K_LEFT:
                        DIRECTION = LEFT
                        posKey1 = K_UP
                        posKey2 = K_DOWN
                    elif curKey == K_RIGHT:
                        DIRECTION = RIGHT
                        posKey1 = K_UP
                        posKey2 = K_DOWN
                else:
                    if (curKey == K_UP and curKey2 == K_LEFT) or (curKey == K_LEFT and curKey2 == K_UP):
                        DIRECTION = UPLEFT
                    elif (curKey == K_UP and curKey2 == K_RIGHT) or (curKey == K_RIGHT and curKey2 == K_UP):
                        DIRECTION = UPRIGHT
                    elif (curKey == K_DOWN and curKey2 == K_LEFT) or (curKey == K_LEFT and curKey2 == K_DOWN):
                        DIRECTION = DOWNLEFT
                    elif (curKey == K_DOWN and curKey2 == K_RIGHT) or (curKey == K_RIGHT and curKey2 == K_DOWN):
                        DIRECTION = DOWNRIGHT

            elif event.type == KEYUP and (event.key == curKey or event.key == curKey2):
                if event.key == curKey:
                    if curKey2 != NONE:
                        curKey = curKey2
                        curKey2 = NONE
                    elif curKey2 == NONE:
                        player.isActive = False
                        DIRECTION = NONE
                        curKey = NONE
                        curKey2 = NONE
                        posKey1 = NONE
                        posKey2 = NONE
                elif event.key == curKey2:
                    curKey2 = NONE

                if curKey == K_UP:
                    DIRECTION = UP
                    posKey1 = K_LEFT
                    posKey2 = K_RIGHT
                elif curKey == K_DOWN:
                    DIRECTION = DOWN
                    posKey1 = K_LEFT
                    posKey2 = K_RIGHT
                elif curKey == K_LEFT:
                    DIRECTION = LEFT
                    posKey1 = K_UP
                    posKey2 = K_DOWN
                elif curKey == K_RIGHT:
                    DIRECTION = RIGHT
                    posKey1 = K_UP
                    posKey2 = K_DOWN
 
        if player.isAtDestination and player.isActive:
            player.SetDestination(DIRECTION)

        if not player.isAtDestination:
            player.AnimateToDestination()

        field.DrawField(DISPLAYSURF, player)
        pygame.display.update()

        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
