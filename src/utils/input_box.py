import pygame as pg


class InputBox(object):
    """Utilizado para criar caixas de texto.

    :param x: posição horizontal da esquerda para a direita.
    :param y: posição vertical de cima para baixo.
    :param w: largura da caixa de texto.
    :param h: altura da caixa de texto.
    :param color_active: cor da caixa de texto e fonte quando ativa.
    :param color_inactive: cor da caixa de texto e fonte quando inativa.
    :param font_family: nome da fonte, usa None se não especificar.
    :param font_size: tamanho da fonte, usa 32 se não especificar.
    :param text: texto inicial padrão.
    """

    def __init__(self, x, y, w, h, color_active, color_inactive,
                 font_family=None, font_size=32, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color_active = pg.Color(color_active)
        self.color_inactive = pg.Color(color_inactive)
        self.color = self.color_inactive
        self.font = pg.font.SysFont(font_family, font_size)
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Se o usuário clicou no retângulo no input_box
            if self.rect.collidepoint(event.pos):
                self.active = True
            self.re_render_text()
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.re_render_text()


    def re_render_text(self):
        self.color = self.color_active if self.active else self.color_inactive
        self.txt_surface = self.font.render(self.text, True, self.color)


    def update(self):
        # Transforma o tamanho da caixa de texto se ele for muito longo
        # width = max(200, self.txt_surface.get_width()+10)
        self.rect.w


    def draw(self, screen):
        # Mostra o texto
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Mostra o retângulo
        pg.draw.rect(screen, self.color, self.rect, 2)