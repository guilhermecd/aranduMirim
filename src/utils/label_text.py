import pygame as pg


class LabelText(object):
    """Utilizado para criar label text (sem input)

    :param text: Texto a ser exibido na label - tipo: string
    :param position: posicao do texto na scene - tipo: tupla com dois registros
    :param color: cor do texto (por padrao RGB (255, 255, 255)) - tipo: tupla
        com tres registros.
    :param size: tamanho do texto (por padrao tamanho 16) - tipo: int
    :param font: nome da fonte (por padrao None) - tipo: string
    :param background: utilizado com o box, (por padrao RGB (0, 0, 0)) -  tipo:
        tupla com tres registros
    :param box: se a label vai ter a cor do fundo da scene ou vai ter um caixa
        em volta (por padrao False) - tipo: Boolean

    Exemplo 1:

        from src.utils import LabelText
        screen = pg.display.set_mode((600, 1200))
        label = LabelText("teste", (200, 200))
        while True
            label.update(screen)

    Exemplo 2: com Box

        from src.utils import LabelText
        screen = pg.display.set_mode((600, 1200))
        label = LabelText("teste", (200, 200), box=1)
        while True
            label.update(screen)
    """

    def __init__(self, text, position=(0, 0), color=(255, 255, 255), size=16,
                 font=None, background=(0, 0, 0), box=False):
        self.box = box
        self.text = text
        self.position = position
        self.background = background
        self.color = color
        self.size = size
        self.fontt = font
        self.text_surface = None
        self.text_rect = None
        self.load_config()


    def load_config(self):
        self.font = pg.font.SysFont(self.fontt, self.size)
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.position
        if self.box == True:
            text_width, text_height = self.font.size(self.text)
            pos_width, pos_height = self.position
            self.rect = pg.Rect((pos_width, pos_height, text_width + 7,
                                 text_height + 2))
            self.rect.center = self.position


    def set_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.position
        if self.box == True:
            text_width, text_height = self.font.size(self.text)
            pos_width, pos_height = self.position
            self.rect = pg.Rect((pos_width, pos_height ,text_width + 3,
                                 text_height + 3))
            self.rect.center = self.position


    def get_text(self):
        return self.text


    def set_color(self, new_color):
        self.color = new_color
        self.text_surface = self.font.render(self.text, True, self.color)


    def get_color(self):
        return self.color


    def set_position(self, new_position):
        self.position = new_position
        self.text_rect.center = self.position
        if self.box == True:
            self.rect.center = self.position


    def get_position(self):
        return self.position


    def set_size(self, new_size):
        self.size = new_size
        self.load_config()


    def get_size(self):
        return self.size


    def set_font(self, new_font):
        self.fontt = new_font
        self.load_config()


    def get_font(self):
        return self.fontt


    def set_background(self, new_background):
        self.background = new_background


    def get_background(self):
        return self.background


    def update(self, screen):
        if self.box == True:
            screen.fill(self.background, self.rect)
        screen.blit(self.text_surface, self.text_rect)
