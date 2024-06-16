import pygame as pg
from src.screens import Base
from src.utils import ButtonImage

class ScreenSpellingImage(Base):
    """Jogo para aprender ortografia"""

    def __init__(self, screen):
        Base.__init__(self, "Jogo para aprender ortografia", screen)
        self.screen = screen
        self.back_btn = ButtonImage('images/back.png', (960, 15),
                                    self.go_back, ('ScreenStart',))

    def process_input(self, events, pressed_keys):
        for event in events:
            self.back_btn.check_event(event)


    def render(self):
        super(ScreenSpellingImage, self).render()
        self.back_btn.update(self.screen)