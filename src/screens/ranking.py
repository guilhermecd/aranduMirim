import pygame as pg
from src.screens import Base
from src.utils import ButtonImage, ScrollList, Button
from src.utils.settings import WHITE, BLACK
from datetime import datetime

class Ranking(Base):
    """RANKING COM PONTUAÇÃO DOS JOGADORES"""

    def __init__(self, screen):
        Base.__init__(self, "", screen)
        self.screen = screen
        self.content = list()
        self.content_id = list()
        self.load_ranking()

        self.logo_game = pg.image.load('images/Arandu-Mirim-Ranking.png').convert_alpha()
        list_content = ('1', 'Guilherme', '95', '27/06/24',
                        '2', 'Michel', '80', '26/06/24',
                        '3', 'Marri', '80', '27/06/24',
                        '4', 'Débora', '60', '22/06/24',
                        '5', 'Luiza', '30', '23/06/24',)

        self.scrollist = ScrollList(('Posição', 'Nome', 'Pontos', 'Data'),
                                    list_content, (50, 150))
        
        BUTTON_STYLE = {
            'hover_color': BLACK,
            'clicked_color': BLACK,
            'clicked_font_color': WHITE,
            'hover_font_color': WHITE,
            'text': "MENU",
            'font_color': BLACK,
            'font': pg.font.Font(None, 34)
        }
        self.menu_bt = Button((840, 520, 150, 40), WHITE, self.control_menu_bt, **BUTTON_STYLE)

    def control_menu_bt(self):
        self.go_back('ScreenStart',)

    def load_ranking(self):
        pass
            
    def process_input(self, events, pressed_keys):
        for event in events:
            self.scrollist.check_event(event)
            self.menu_bt.check_event(event)


    def render(self):
        super(Ranking, self).render()
        self.screen.blit(self.logo_game, (0, 0))
        self.scrollist.update(self.screen)
        self.menu_bt.update(self.screen)