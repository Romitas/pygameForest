import pygame
import math
from pygame.locals import *
from random import *

from constants import *

class Field:

    def __init__(self):
        self.FIELDWIDTH  = 100
        self.FIELDHEIGHT = 100
    
        self.GRIDWIDTH  = 10
        self.GRIDHEIGHT = 10

        self.X = 0
        self.Y = 0
    
        self.SetupField()

    def SetupField(self):

        self.field = []
        for i in xrange(FIELDWIDTH):
            column = []
            for j in xrange(FIELDHEIGHT):
                column.append(NONE)
            self.field.append(column)

        self.SetupGrass()
        self.SetupPath()
        self.SetupTrees()

    def SetupGrass(self):

        for i in xrange(FIELDWIDTH):
            for j in xrange(FIELDHEIGHT):
                newCell = dict.fromkeys(['terrain', 'color'])
                newCell['terrain'] = TRNGRASS
                newCell['color'] = GRASSCOLORS[randint(0, len(GRASSCOLORS) - 1)]

                self.field[i][j] = newCell

    def SetupPath(self):

        j = 0
        for i in xrange(FIELDWIDTH):
            if randint(0, 1) == 0:
                newCell = dict.fromkeys(['terrain', 'color'])
                newCell['terrain'] = TRNPATH
                newCell['color'] = PATHCOLORS[randint(0, len(PATHCOLORS) - 1)]
                self.field[i][j] = newCell
            else:
                newCell = dict.fromkeys(['terrain', 'color'])
                newCell['terrain'] = TRNPATH
                newCell['color'] = PATHCOLORS[randint(0, len(PATHCOLORS) - 1)]
                self.field[i][j] = newCell
                j += 1
                newCell = dict.fromkeys(['terrain', 'color'])
                newCell['terrain'] = TRNPATH
                newCell['color'] = PATHCOLORS[randint(0, len(PATHCOLORS) - 1)]
                self.field[i][j] = newCell

    def SetupTrees(self):

        for i in xrange(FIELDWIDTH):
            for j in xrange (FIELDHEIGHT):
                if randint(0, 10) == 0 and self.field[i][j]['terrain'] != TRNPATH:
                    self.field[i][j]['hasTree'] = True
                    self.field[i][j]['treeWidth'] = CELLWIDTH * uniform(0.4, 0.8)
                else:
                    self.field[i][j]['hasTree'] = False
                    self.field[i][j]['treeWidth'] = 0

    def DrawField(self, DISPLAYSURF, player):

        anotherSurface = DISPLAYSURF.convert_alpha()
        treeSurface = DISPLAYSURF.convert_alpha()

        pX = player.X
        pY = player.Y

        pXSolid = int(pY)
        pYSolid = int(pX)

        left = pX - (GRIDWIDTH  / 2)
        top  = pY - (GRIDHEIGHT / 2)
        right  = pX + (GRIDWIDTH  / 2)
        bottom = pY + (GRIDHEIGHT / 2)

        if left < 0:
            left = 0
            right = 0 + GRIDWIDTH
        if top < 0:
            top = 0
            bottom = 0 + GRIDHEIGHT
        if right > FIELDWIDTH:
            right = FIELDWIDTH
            left = FIELDWIDTH - GRIDWIDTH
        if bottom > FIELDHEIGHT:
            bottom = FIELDHEIGHT
            top = FIELDHEIGHT - GRIDHEIGHT

        leftSolid   = int(left) + 1
        topSolid    = int(top) + 1
        rightSolid  = int(right)
        bottomSolid = int(bottom)

        leftFrac   = leftSolid - left
        topFrac    = topSolid - top
        rightFrac  = right - rightSolid
        bottomFrac = bottom - bottomSolid

        screenPX = pX - left
        screenPY = pY - top

        dist = GRIDWIDTH / 2

        for i in xrange(leftSolid - 1, rightSolid + 1):
            for j in xrange(topSolid - 1, bottomSolid + 1):

                if i >= FIELDWIDTH:
                    i = FIELDWIDTH - 1
                if j >= FIELDHEIGHT:
                    j = FIELDHEIGHT - 1

                color = self.field[i][j]['color']

                alpha = (math.sqrt((pX - i) ** 2 + (pY - j) ** 2) / dist) * 255.0
                if (alpha > 255):
                    alpha = 255
                
                alphaColor = pygame.Color(0, 0, 0, int(alpha))

                cellX = (leftFrac + i - leftSolid) * CELLWIDTH
                cellY = (topFrac + j - topSolid) * CELLHEIGHT

                cellWidth = CELLWIDTH
                cellHeight = CELLHEIGHT
                
                if i == leftSolid - 1:
                    cellX = 0
                    cellWidth = CELLWIDTH * leftFrac
                if j == topSolid - 1:
                    cellY = 0
                    cellHeight = CELLHEIGHT * topFrac
                if i == rightSolid + 1:
                    cellWidth = CELLWIDTH * rightFrac
                    cellX = GRIDWIDTH - cellWidth
                if j == bottomSolid + 1:
                    cellHeight = CELLHEIGHT * bottomFrac
                    cellY = GRIDHEIGHT - cellHeight

                pygame.draw.rect(DISPLAYSURF, color, (cellX, cellY, cellWidth, cellHeight))
                pygame.draw.rect(treeSurface, (0, 0, 0, 0), (cellX, cellY, cellWidth, cellHeight))

                if (self.field[i][j]['hasTree']):
                    treeWidth = self.field[i][j]['treeWidth']
                    treeHeight = cellY + cellHeight * 0.75
#                    treeHeight = cellHeight * 0.5
                    treeX = cellX + (cellWidth - treeWidth) / 2.0
                    treeY = 0
#                    treeY = cellY + 0.25 * cellHeight

#                    pygame.draw.rect(DISPLAYSURF, (30, 20, 20), (treeX, 0, treeWidth, treeHeight))

                    if (j > pY):
                        pygame.draw.rect(treeSurface, (30, 20, 20, 128), (treeX, treeY, treeWidth, treeHeight))
                    if (j <= pY):
                        pygame.draw.rect(DISPLAYSURF, (30, 20, 20), (treeX, treeY, treeWidth, treeHeight))

                pygame.draw.rect(anotherSurface, alphaColor, (cellX, cellY, cellWidth, cellHeight))

        playerX = (pX - left) * CELLWIDTH + (CELLWIDTH - PLAYERWIDTH) / 2
        playerY = (pY - top) * CELLHEIGHT + (CELLHEIGHT - PLAYERHEIGHT) / 2

        pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (playerX, playerY, PLAYERWIDTH, PLAYERHEIGHT))

        DISPLAYSURF.blit(treeSurface, (0, 0))
        DISPLAYSURF.blit(anotherSurface, (0, 0))
