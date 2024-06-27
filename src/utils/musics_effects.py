import pygame as pg

class MusicEffects():
    def __init__(self):
        pass

    def congratulations(self):
        pg.mixer.music.load('sounds/small-applause-6695.mp3')#test sound
        pg.mixer.music.play()
        while pg.mixer.music.get_busy() == True:
            continue

    def game_Over(self):
        pg.mixer.music.load('sounds/error-10-206498.mp3')#test sound
        pg.mixer.music.play()
        while pg.mixer.music.get_busy() == True:
            continue