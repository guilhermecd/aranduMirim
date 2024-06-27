import pygame as pg
import queue
from src.screens import Base
from src.utils import ButtonImage, InputBox, Button, LabelText
from src.utils.settings import WHITE, BLACK
import random
from src.utils.serial_info import SerialInfo
from src.utils.musics_effects import MusicEffects

class ScreenSpellingImage(Base):
    """Jogo para aprender ortografia"""
    
    def __init__(self, screen):
        Base.__init__(self, "", screen)
        self.screen = screen
        self.logo_game = pg.image.load('images/Arandu-Mirim-Ortografia.png').convert_alpha()
        #help buttons
        self.help_bt_img = ButtonImage('images/duvidas32_32.png', (980, 20),
                                    self.control_help_bt_img, ())
        self.close_help_bt_img = ButtonImage('images/close.png', (758, 153),
                                    self.control_help_bt_img, ())
        self.help_enable = False
        self.help_img = pg.image.load('images/Arandu-Mirim-Ortografia-com-FAQ.png').convert_alpha()

        self.musics = MusicEffects()
        self.data_queue = queue.Queue()
        self.slots_serial = SerialInfo(self.data_queue)
        self.slots_serial.start()
        self.dic_esp32 = self.slots_serial.slots_plataforma
        
        self.dic_image = {1 : "GATO", 2 : "URSO", 3 : "TATU", 4 : "LEAO", 5 : "VACA", 6 : "LOBO", 7: "RATO", 8 : "PATO", 9 : "FLOR",
                          10: "CAFE", 11 : "LUVA", 12: "LEGO", 13 : "SAPO", 14 : "BOLA"}
        self.image_name = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        random.shuffle(self.image_name) 
        self.indice = 0
        self.current_image = pg.image.load('images/ortografiaAnimais/' + str(self.image_name[self.indice]) + '.png').convert_alpha()
        self.letter1_lb = LabelText(self.dic_esp32['1'], (243, 410), WHITE, size=190)
        self.letter2_lb = LabelText(self.dic_esp32['2'], (345, 410), WHITE, size=190)
        self.letter3_lb = LabelText(self.dic_esp32['3'], (447, 410), WHITE, size=190)
        self.letter4_lb = LabelText(self.dic_esp32['4'], (549, 410), WHITE, size=190)
        self.letter1_img = pg.image.load('images/ortografia_grade.png').convert_alpha()
        self.letter2_img = pg.image.load('images/ortografia_grade.png').convert_alpha()
        self.letter3_img = pg.image.load('images/ortografia_grade.png').convert_alpha()
        self.letter4_img = pg.image.load('images/ortografia_grade.png').convert_alpha()

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
        self.slots_serial.stop()
        self.slots_serial.join()
        self.go_back('ScreenStart',)

    def control_help_bt_img(self):
        self.help_enable = not self.help_enable

    def control_skip_bt(self):
        if self.indice < len(self.image_name)-1:
            self.indice += 1
        else:
            self.indice = 0
        self.current_image = pg.image.load('images/ortografiaAnimais/' + str(self.image_name[self.indice]) + '.png').convert_alpha()

    def update_letters(self):
        self.letter1_lb = LabelText(self.dic_esp32['1'], (243, 410), WHITE, size=190)
        self.letter2_lb = LabelText(self.dic_esp32['2'], (345, 410), WHITE, size=190)
        self.letter3_lb = LabelText(self.dic_esp32['3'], (447, 410), WHITE, size=190)
        self.letter4_lb = LabelText(self.dic_esp32['4'], (549, 410), WHITE, size=190)

    def check_formed_word(self):
        palavra_cubos = ''.join([self.dic_esp32[key] for key in self.slots_serial.slots_plataforma.keys()])
        if len(palavra_cubos) > 3:
            if self.dic_image[self.image_name[self.indice]] == palavra_cubos:
                self.musics.congratulations()
                self.control_skip_bt()
            self.slots_serial.clean_slots()


    def process_input(self, events, pressed_keys):
        for event in events:
            self.skip_bt.check_event(event)
            self.menu_bt.check_event(event)
            self.help_bt_img.check_event(event)
            self.close_help_bt_img.check_event(event)

    def render(self):
        super(ScreenSpellingImage, self).render()
        self.screen.blit(self.logo_game, (0, 0))
        self.skip_bt.update(self.screen)
        self.menu_bt.update(self.screen)
        self.help_bt_img.update(self.screen)
        self.screen.blit(self.current_image, (437, 130))
        self.screen.blit(self.letter1_img, (193, 330))
        self.letter1_lb.update(self.screen)
        self.screen.blit(self.letter2_img, (295, 330))
        self.letter2_lb.update(self.screen)
        self.screen.blit(self.letter3_img, (397, 330))
        self.letter3_lb.update(self.screen)
        self.screen.blit(self.letter4_img, (499, 330))
        self.letter4_lb.update(self.screen)
        self.update_letters()
        self.check_formed_word()
        if self.help_enable:
            self.screen.fill((232, 232, 232))
            self.screen.blit(self.help_img, (0, 0))
            self.close_help_bt_img.update(self.screen)