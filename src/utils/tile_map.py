import pygame as pg
from src.utils.settings import *


class Map:

    def __init__(self):
        self.tilewidth = 500000
        self.tileheight = 500000
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class Camera:

    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height


    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)


    def update(self, target):
        x = (-target.rect.x - target.sizeImage[0] / 2) + int(WIDTH / 2)
        y = (-target.rect.y - target.sizeImage[1] / 2) + int(HEIGHT / 2)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(x, y, self.width, self.height)
