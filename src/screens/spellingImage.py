import pygame as pg
from src.screens import Base
from src.utils import ButtonImage, InputBox, Button
from src.utils.settings import WHITE, BLACK

import random

class ScreenSpellingImage(Base):
    """Jogo para aprender ortografia"""
    
    def __init__(self, screen):
        Base.__init__(self, "ORTOGRAFIA", screen)
        self.screen = screen
        #help buttons
        self.help_bt_img = ButtonImage('images/duvidas32_32.png', (980, 20),
                                    self.control_help_bt_img, ())
        self.close_help_bt_img = ButtonImage('images/close.png', (766, 120),
                                    self.control_help_bt_img, ())
        self.help_enable = False
        self.help_img = pg.image.load('images/helpme.jpg').convert_alpha()
        self.close_help_img = pg.image.load('images/close.png').convert_alpha()

        self.dic_image = {1 : "GATO", 2 : "URSO", 3 : "TATU", 4 : "LEAO", 5 : "VACA", 6 : "LOBO", 7: "RATO", 8 : "PATO"}
        self.image_name = [1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(self.image_name) 
        self.indice = 0
        self.current_image = pg.image.load('images/ortografiaAnimais/' + str(self.image_name[self.indice]) + '.png').convert_alpha()
        self.letter1_ibox = InputBox(193, 330, 100, 150, WHITE, WHITE, font_size=190, text='G')
        self.letter2_ibox = InputBox(293, 330, 100, 150, WHITE, WHITE, font_size=190, text='A')
        self.letter3_ibox = InputBox(393, 330, 100, 150, WHITE, WHITE, font_size=190, text='T')
        self.letter4_ibox = InputBox(493, 330, 100, 150, WHITE, WHITE, font_size=190, text='O')
        self.dic_esp32 = {1 : 'G', 2 : 'A', 3 : 'T', 4 : 'O'}
        BUTTON_STYLE = {
            'hover_color': BLACK,
            'clicked_color': BLACK,
            'clicked_font_color': WHITE,
            'hover_font_color': WHITE,
            'text': "PULAR",
            'font_color': BLACK,
            'font': pg.font.Font(None, 34)
        }
        self.skip_bt = Button((670, 520, 150, 40), WHITE, self.control_skip_bt, **BUTTON_STYLE)
        BUTTON_STYLE['text'] = "MENU" 
        self.menu_bt = Button((840, 520, 150, 40), WHITE, self.control_menu_bt, **BUTTON_STYLE)

    def control_menu_bt(self):
        self.go_back('ScreenStart',)

    def control_help_bt_img(self):
        self.help_enable = not self.help_enable

    def control_skip_bt(self):
        if self.indice < len(self.image_name)-1:
            self.indice += 1
        else:
            self.indice = 0
        self.current_image = pg.image.load('images/ortografiaAnimais/' + str(self.image_name[self.indice]) + '.png').convert_alpha()

    def check_formed_word(self):
        palavra_cubos = ''
        for key in self.dic_esp32.keys() :
            palavra_cubos += self.dic_esp32[key]
        if self.dic_image[self.image_name[self.indice]] == palavra_cubos:
            self.indice += 1
            self.current_image = pg.image.load('images/ortografiaAnimais/' + str(self.image_name[self.indice]) + '.png').convert_alpha()


    def process_input(self, events, pressed_keys):
        for event in events:
            self.skip_bt.check_event(event)
            self.menu_bt.check_event(event)
            self.help_bt_img.check_event(event)
            self.close_help_bt_img.check_event(event)

    def render(self):
        super(ScreenSpellingImage, self).render()
        self.skip_bt.update(self.screen)
        self.menu_bt.update(self.screen)
        self.letter1_ibox.draw(self.screen)
        self.letter1_ibox.update()
        self.letter2_ibox.draw(self.screen)
        self.letter2_ibox.update()
        self.letter3_ibox.draw(self.screen)
        self.letter3_ibox.update()
        self.letter4_ibox.draw(self.screen)
        self.letter4_ibox.update()
        self.help_bt_img.update(self.screen)
        self.screen.blit(self.current_image, (240, 90))
        if self.help_enable:
            self.screen.blit(self.help_img, (242, 140))
            self.close_help_bt_img.update(self.screen)
        self.check_formed_word()