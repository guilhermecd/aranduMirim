import pygame as pg
import time

class ButtonImage(object):
    """Cria um botão utilizando uma imagem.

    :param image_name: String com o nome da imagem com o seu formato ou uma
        string com o caminho completo da imagem.
        Exemplo 1: "teste.png"
        Exemplo 2: "/home/user/Documents/teste.png"
    :param position: tupla com dois registros, um representando x e outro y.
        Exemplo 1: (200, 100)
        Exemplo 2: (200, 50)
    :param function: Função ou método previamente definido que será chamada
        quando o botão for clicado
        Exemplo 1: nextPage
        Exemplo 2: self.calculaArea
    :param args: lista de argumentos que serão passados por parâmetro em funcion

    Exemplos:

        from src.utils import ButtonImage
        screen = pg.display.set_mode((600, 1200))
        button = ButtonImage('./teste.png', (200, 50), next_page)
        def next_page():
            pass
        while True
            button.update(screen)
    """

    def __init__(self, image_name, position, function, args=()):
        self.position = position
        self.image = pg.image.load(image_name).convert_alpha()
        img_hover = image_name.split('.')
        img_hover = img_hover[0] + '_h.' + img_hover[1]
        try:
            self.image_h = pg.image.load(img_hover).convert_alpha()
        except:
            self.image_h = pg.image.load(image_name).convert_alpha()
        self.rect = pg.Rect(position, self.image.get_rect().size)
        self.function = function
        self.args = args
        self.clicked = False
        self.hovered = False
        self.call_on_release = True
        self.visible = True
        self.enable = True


    def change_image(self, new_img):
        self.image = pg.image.load(new_img).convert_alpha()
        img_hover = new_img.split('.')
        img_hover = img_hover[0] + '_h.' + img_hover[1]
        try:
            self.image_h = pg.image.load(img_hover).convert_alpha()
        except:
            self.image_h = pg.image.load(new_img).convert_alpha()
        self.rect = pg.Rect(self.position, self.image.get_rect().size)


    def get_size(self):
        return self.image.get_rect().size


    def set_enable(self, value):
        self.enable = value


    def set_visible(self):
        self.visible = True


    def set_invisible(self):
        self.visible = False


    def check_event(self, event):
        if self.enable and self.visible:
            """The button needs to be passed events from your program event loop."""
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.on_click(event)
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.on_release(event)


    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True

    def on_release(self, event):
        if self.clicked and self.call_on_release:
            if self.args:
                self.function(*self.args)
            else:
                self.function()
        self.clicked = False            


    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
        else:
            self.hovered = False


    def set_position(self, newPosicion):
        self.rect.center = newPosicion


    def get_position(self):
        return self.rect.center


    def update(self,screen):
        if self.visible:
            self.check_hover()
            if not self.enable:
                screen.blit(self.image_h, self.rect)
            elif self.clicked:
                screen.blit(self.image_h, self.rect)
            elif self.hovered:
                screen.blit(self.image, self.rect)
            else:
                screen.blit(self.image, self.rect)
