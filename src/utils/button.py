import pygame as pg
import time

class Button(object):
    """Classe para adição de botão simples."""

    def __init__(self, rect, color, function, **kwargs):
        self.rect = pg.Rect(rect)
        self.color = color
        self.function = function
        self.clicked = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_text()
                

    def process_kwargs(self, kwargs):
        """Customizações que podem ser passadas por meio de kwargs."""

        settings = {"text" : None,
                    "font" : pg.font.Font(None, 16),
                    "call_on_release" : True,
                    "hover_color" : None,
                    "clicked_color" : None,
                    "font_color" : pg.Color("white"),
                    "hover_font_color" : None,
                    "clicked_font_color" : None}
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def set_position(self, new_posicion):
        self.rect.x = new_posicion[0]
        self.rect.y = new_posicion[1]

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def render_text(self):
        """Pré-renderização do button text."""

        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text, True, color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text, True, color)
            self.text = self.font.render(self.text, True, self.font_color)

    def check_event(self,event):
        """O button precisa ser passado para o event loop."""
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.function()

    def on_release(self, event):
        if self.clicked and self.call_on_release:
            self.function()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
        else:
            self.hovered = False

    def update(self, surface):
        """Update precisa ser chamado em todo frame."""

        color = self.color
        text = self.text
        self.check_hover()
        if self.clicked and self.clicked_color:
            color = self.clicked_color
            if self.clicked_font_color:
                text = self.clicked_text
        elif self.hovered and self.hover_color:
            color = self.hover_color
            if self.hover_font_color:
                text = self.hover_text
        surface.fill(pg.Color("black"), self.rect)
        surface.fill(color, self.rect.inflate(-4, -4))
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)