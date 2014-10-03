from constants import *

class Player(object):

    def __init__(self):
        self.X = 0
        self.Y = 0

        self.destX = 0
        self.destY = 0

        self.STEP = 1
        self.SPEED = 0.1

        self.isActive = False
        self.isAtDestination = True

    def SetDestination(self, DIRECTION):

        if DIRECTION == UP:
            self.destY -= self.STEP
        elif DIRECTION == DOWN:
            self.destY += self.STEP
        elif DIRECTION == LEFT:
            self.destX -= self.STEP
        elif DIRECTION == RIGHT:
            self.destX += self.STEP

        elif DIRECTION == UPLEFT:
            self.destX -= self.STEP
            self.destY -= self.STEP
        elif DIRECTION == UPRIGHT:
            self.destX += self.STEP
            self.destY -= self.STEP
        elif DIRECTION == DOWNLEFT:
            self.destX -= self.STEP
            self.destY += self.STEP
        elif DIRECTION == DOWNRIGHT:
            self.destX += self.STEP
            self.destY += self.STEP

        if self.destX < 0:
            self.destX = 0
        elif self.destX >= FIELDWIDTH:
            self.destX = FIELDWIDTH - 1
        if self.destY < 0:
            self.destY = 0
        elif self.destY >= FIELDHEIGHT:
            self.destY = FIELDHEIGHT - 1

        self.isAtDestination = False

    def AnimateToDestination(self):

        if (abs(self.X - self.destX) < self.SPEED and abs(self.Y - self.destY) < self.SPEED):
            self.X = self.destX
            self.Y = self.destY
            self.isAtDestination = True
        else:
            if (self.X < self.destX):
                self.X += self.SPEED
            if (self.X > self.destX):
                self.X -= self.SPEED
            if (self.Y < self.destY):
                self.Y += self.SPEED
            if (self.Y > self.destY):
                self.Y -= self.SPEED
