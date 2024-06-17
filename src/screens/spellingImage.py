import pygame as pg
from src.screens import Base
from src.utils import ButtonImage, InputBox
from src.utils.settings import WHITE

import random

class ScreenSpellingImage(Base):
    """Jogo para aprender ortografia"""
    
    def __init__(self, screen):
        Base.__init__(self, "ORTOGRAFIA", screen)
        self.screen = screen
        self.back_btn = ButtonImage('images/back.png', (960, 15),
                                    self.go_back, ('ScreenStart',))
        self.dic_image = {1 : "GATO", 2 : "URSO", 3 : "TATU", 4 : "LEAO", 5 : "VACA", 6 : "LOBO", 7: "RATO", 8 : "PATO"}
        self.image_name = ['1', '2', '3', '4', '5', '6', '7', '8']
        random.shuffle(self.image_name)
        self.current_image = pg.image.load('images/ortografiaAnimais/' + self.image_name[0] + '.png').convert_alpha()
        self.letter1_ibox = InputBox(193, 330, 100, 150, WHITE, WHITE, font_size=190, text='G')
        self.letter2_ibox = InputBox(293, 330, 100, 150, WHITE, WHITE, font_size=190, text='A')
        self.letter3_ibox = InputBox(393, 330, 100, 150, WHITE, WHITE, font_size=190, text='T')
        self.letter4_ibox = InputBox(493, 330, 100, 150, WHITE, WHITE, font_size=190, text='O')

    def process_input(self, events, pressed_keys):
        for event in events:
            self.back_btn.check_event(event)


    def render(self):
        super(ScreenSpellingImage, self).render()
        self.back_btn.update(self.screen)
        self.letter1_ibox.draw(self.screen)
        self.letter1_ibox.update()
        self.letter2_ibox.draw(self.screen)
        self.letter2_ibox.update()
        self.letter3_ibox.draw(self.screen)
        self.letter3_ibox.update()
        self.letter4_ibox.draw(self.screen)
        self.letter4_ibox.update()
        self.screen.blit(self.current_image, (240, 90))