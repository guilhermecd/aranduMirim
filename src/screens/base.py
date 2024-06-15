import os
import pygame as pg
os.chdir(os.path.dirname(__file__))


class Base:
    """Cria uma classe que serve como base de todas as outras telas do projeto.
    """

    def __init__(self, title, screen):
        self.screen = screen
        self.next = self
        pg.init()
        self.black = (0, 0, 0)
        self.top_bar = pg.image.load("images/title_bar.png").convert_alpha()
        self.top_bar_rect = self.top_bar.get_rect()
        self.font_bar = pg.font.SysFont("Liberation Sans", 28)
        self.bar_label = self.font_bar.render(title, True, self.black)
        self.bar_rect = self.bar_label.get_rect()
        self.bar_rect.center = (512, 32)

    def change_scene(self, scene, arg=None):
        if arg:
            self.switch_to_scene(scene(self.screen, arg))
        else:
            self.switch_to_scene(scene(self.screen))


    def go_back(self, screen, arg=None):
        exec('from src.screens import {}'.format(screen))
        self.change_scene(eval(screen), arg)


    def process_input(self, events, pressed_keys):
        pass


    def update(self):
        pass


    def render(self):
        self.screen.fill((66, 66, 66))
        self.screen.blit(self.top_bar, self.top_bar_rect)
        self.screen.blit(self.bar_label, self.bar_rect)


    def switch_to_scene(self, next_scene):
        self.next = next_scene


    def terminate(self):
        self.switch_to_scene(None)
