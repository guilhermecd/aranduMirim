import pygame as pg
from src.screens import (Base, ScreenSpelling)
from src.utils import ButtonImage, LabelText


class ScreenStart(Base):
    """Cria a tela inicial do programa com as seguintes opções: (1) abrir
    último trabalho, (2) demonstração, (3) configurações, (4) trabalho e
    (5) sair.
    """

    def __init__(self, screen):
        Base.__init__(self, "Menu Principal", screen)
        self.screen = screen
        self.demo_btn = ButtonImage('images/18.png', (163, 330),
                                    self.change_scene, (ScreenSpelling,))
        self.exit_btn = ButtonImage('images/20.png', (856, 440),
                                    self.terminate, ())
        self.navi_lb = LabelText ('Navegação', (240, 276), size=40)
        self.conf_lb = LabelText ('Configuração', (585, 276), size=40)
        self.demo_lb = LabelText ("Demo", (240, 506), size=40)
        self.job_lb = LabelText ("Trabalho", (585, 506), size=40)
        self.exit_lb = LabelText ("Desligar", (920, 576), size=30)
        self.update_lb = LabelText ("Atualização", (920, 216), size=30)
        self.event_empty_lb = LabelText('', (512, 190), (255, 255, 255), 36,
                                        background=(234, 67, 53), box=True)
        self.event_empty_warning = False


    def render(self):
        super(ScreenStart, self).render()
        self.navi_btn.update(self.screen)
        self.demo_btn.update(self.screen)
        self.exit_btn.update(self.screen)
        self.navi_lb.update(self.screen)
        self.conf_lb.update(self.screen)
        self.demo_lb.update(self.screen)
        self.job_lb.update(self.screen)
        self.exit_lb.update(self.screen)
        self.update_lb.update(self.screen)
        if self.event_empty_warning:
            self.event_empty_lb.update(self.screen)