import pygame as pg
from src.screens import Base
from src.utils import ButtonImage, Button
from src.utils.settings import WHITE, BLACK

class ScreenSoletrar(Base):
    """Jogo para aprender a soletrar"""

    def __init__(self, screen):
        Base.__init__(self, "SOLETRAR", screen)
        self.screen = screen
        self.help_bt_img = ButtonImage('images/duvidas32_32.png', (980, 20),
                                    self.control_help_bt_img, ())
        self.close_help_bt_img = ButtonImage('images/close.png', (766, 120),
                                    self.control_help_bt_img, ())
        self.help_enable = False
        self.help_img = pg.image.load('images/helpme.jpg').convert_alpha()
        self.close_help_img = pg.image.load('images/close.png').convert_alpha()
        
        self.dic_esp32 = {1 : 'G', 2 : 'A', 3 : 'T', 4 : 'O'}
        self.scenario = (['a', 'g', 'o', 't', 'l'], ['e', 'r', 't', 'p', 'a'], ['a', 'c', 'g', 'i', 'f'])
        self.dic_words = (['GATO', 'GALO', 'LATA', 'GOL', 'TALO'], ['RETA', 'PARE', 'PERA'], ['FICA', 'FACA', 'CIA'])
        self.indice = 0
        self.current_scenario = self.scenario[self.indice]
        self.alfabeto_1_image = pg.image.load('images/soletra/' + self.current_scenario[0] + '.png').convert_alpha()
        self.alfabeto_2_image = pg.image.load('images/soletra/' + self.current_scenario[1] + '.png').convert_alpha()
        self.alfabeto_3_image = pg.image.load('images/soletra/' + self.current_scenario[2] + '.png').convert_alpha()
        self.alfabeto_4_image = pg.image.load('images/soletra/' + self.current_scenario[3] + '.png').convert_alpha()
        self.alfabeto_5_image = pg.image.load('images/soletra/' + self.current_scenario[4] + '.png').convert_alpha()
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
        pg.mixer.music.load('sounds/small-applause-6695.mp3')#test sound
        pg.mixer.music.play()
        if self.indice < len(self.scenario) - 1: 
            self.indice += 1
        else:
            self.indice = 0
        self.current_scenario = self.scenario[self.indice]
        self.alfabeto_1_image = pg.image.load('images/soletra/' + self.current_scenario[0] + '.png').convert_alpha()
        self.alfabeto_2_image = pg.image.load('images/soletra/' + self.current_scenario[1] + '.png').convert_alpha()
        self.alfabeto_3_image = pg.image.load('images/soletra/' + self.current_scenario[2] + '.png').convert_alpha()
        self.alfabeto_4_image = pg.image.load('images/soletra/' + self.current_scenario[3] + '.png').convert_alpha()
        self.alfabeto_5_image = pg.image.load('images/soletra/' + self.current_scenario[4] + '.png').convert_alpha()


    def process_input(self, events, pressed_keys):
        for event in events:
            self.skip_bt.check_event(event)
            self.menu_bt.check_event(event)
            self.help_bt_img.check_event(event)
            self.close_help_bt_img.check_event(event)

    def render(self):
        super(ScreenSoletrar, self).render()
        self.skip_bt.update(self.screen)
        self.menu_bt.update(self.screen)
        self.help_bt_img.update(self.screen)
        self.screen.blit(self.alfabeto_1_image, (105, 220)) #superior esquerdo
        self.screen.blit(self.alfabeto_4_image, (355, 220)) #superior direito
        self.screen.blit(self.alfabeto_2_image, (100, 410)) #inferior esquerdo
        self.screen.blit(self.alfabeto_3_image, (360, 410)) #inferior direito
        self.screen.blit(self.alfabeto_5_image, (230, 320)) #central
        if self.help_enable:
            self.screen.blit(self.help_img, (242, 140))
            self.close_help_bt_img.update(self.screen)
