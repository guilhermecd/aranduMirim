import pygame as pg
from pygame.locals import *
from src.database import start_model
from src.screens import ScreenStart
from src.utils.settings import FPS, WIDTH, HEIGHT, SHOW_FPS
from subprocess import Popen

def run(width, height, fps):
    # criar a base de dados se não houver com os valores padrões
    start_model()
    pg.init()
    size = (width, height)
    flags = pg.HWSURFACE | pg.DOUBLEBUF
    #flags = pg.FULLSCREEN
    screen = pg.display.set_mode(size, flags)
    clock = pg.time.Clock()
    pg.event.set_allowed([MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYDOWN, QUIT,
                          USEREVENT])
    # indica a cena inicial
    active_scene = ScreenStart(screen)
    pg.mixer.init()
    while active_scene != None:
        pressed_keys = pg.key.get_pressed()
        filtered_events = []
        for event in pg.event.get():
            quit_attempt = False
            if event.type == pg.QUIT:
                quit_attempt = True
            elif event.type == pg.KEYDOWN:
                alt_pressed = pressed_keys[pg.K_LALT] or \
                              pressed_keys[pg.K_RALT]
                # Caso seja pressionado Esc do teclado
                if event.key == pg.K_ESCAPE:
                    quit_attempt = True
                # Caso seja pressionado Alt+F4 do teclado
                elif event.key == pg.K_F4 and alt_pressed:
                    quit_attempt = True
            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)
        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render()
        # obtém a "chave" de todos os atributos, menos "next" que armazena o
        # fluxo de navegação
        del_attrs = [k for k in active_scene.__dict__.keys() \
            if k not in ('next', 'back')]
        # caso seja trocado a cena, todos os atributos são deletados da memória
        # com exceção do atributo "next", que armazena o fluxo p/ próxima tela
        if active_scene.next != active_scene:
            for key in del_attrs:
                del(active_scene.__dict__[key])
            active_scene = active_scene.next
        pg.display.flip()


if __name__ == '__main__':
    run(WIDTH, HEIGHT, FPS)
