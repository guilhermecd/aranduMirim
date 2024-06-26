import pygame as pg
from src.screens import (Base, ScreenSpellingImage, ScreenSoletrar, Ranking)
from src.utils import ButtonImage, LabelText


class ScreenStart(Base):

    def __init__(self, screen):
        Base.__init__(self, "", screen)
        self.screen = screen
        self.soletrar_btn = ButtonImage('images/soletrar.png', (193, 330),
                                    self.change_scene, (ScreenSoletrar,))
        self.spelling_btn = ButtonImage('images/spelling.png', (675, 330),
                                    self.change_scene, (ScreenSpellingImage,))
        self.ranking_btn = ButtonImage('images/ranking.png', (675, 114),
                                    self.change_scene, (Ranking,))
        self.soletrar_lb = LabelText ("Soletrar", (270, 506), size=40)
        self.spelling_lb = LabelText ("Ortografia", (752, 506), size=40)
        self.ranking_lb = LabelText ("Ranking", (752, 290), size=40)
        self.logo_game = pg.image.load('images/aranduMain.png').convert_alpha()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pg.USEREVENT:
                pg.time.set_timer(pg.USEREVENT, 0)
                self.event_empty_warning = False
            self.soletrar_btn.check_event(event)
            self.spelling_btn.check_event(event)
            self.ranking_btn.check_event(event)

    def render(self):
        super(ScreenStart, self).render()
        self.screen.blit(self.logo_game, (0, 0))
        #buttons
        self.soletrar_btn.update(self.screen)
        self.spelling_btn.update(self.screen)
        self.ranking_btn.update(self.screen)
        #labels
        self.soletrar_lb.update(self.screen)
        self.spelling_lb.update(self.screen)
        self.ranking_lb.update(self.screen)
