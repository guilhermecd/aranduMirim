import pygame as pg
from src.screens import Base
from src.utils import ButtonImage, Button
from src.utils.settings import WHITE, BLACK

class ScreenSoletrar(Base):
    """Jogo para aprender a soletrar"""

    def __init__(self, screen):
        Base.__init__(self, "SOLETRAR", screen)
        self.screen = screen
        self.dic_alfabeto = {'a' : 'A', 'b' : 'B', 'c' : 'C', 'd' : 'D',
                          'e' : 'E', 'f' : 'F', 'g' : 'G', 'h' : 'H',
                          'i' : 'I', 'j' : 'J', 'k' : 'K', 'l' : 'L',
                          'm' : 'M', 'n' : 'N', 'o' : 'O', 'p' : 'P',
                          'q' : 'Q', 'r' : 'R', 's' : 'S', 't' : 'T',
                          'u' : 'U', 'v' : 'V', 'v' : 'V', 'x' : 'X',
                          'y' : 'Y', 'z' : 'Z'}
        self.conjunto1 = ['a', 'g', 'o', 't']
        self.alfabeto_1_image = pg.image.load('images/soletra/' + self.conjunto1[0] + '.png').convert_alpha()
        self.alfabeto_2_image = pg.image.load('images/soletra/' + self.conjunto1[1] + '.png').convert_alpha()
        self.alfabeto_3_image = pg.image.load('images/soletra/' + self.conjunto1[2] + '.png').convert_alpha()
        self.alfabeto_4_image = pg.image.load('images/soletra/' + self.conjunto1[3] + '.png').convert_alpha()
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


    def control_skip_bt(self):
        pass


    def process_input(self, events, pressed_keys):
        for event in events:
            self.skip_bt.check_event(event)
            self.menu_bt.check_event(event)

    def render(self):
        super(ScreenSoletrar, self).render()
        self.skip_bt.update(self.screen)
        self.menu_bt.update(self.screen)
        self.screen.blit(self.alfabeto_1_image, (100, 280))
        self.screen.blit(self.alfabeto_2_image, (160, 420))
        self.screen.blit(self.alfabeto_3_image, (310, 420))
        self.screen.blit(self.alfabeto_4_image, (370, 280))                