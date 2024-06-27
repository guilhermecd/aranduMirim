import queue
import pygame as pg
import time
from src.screens import Base
from src.utils import ButtonImage, Button
from src.utils.settings import WHITE, BLACK, LIGHTGREY, T_DARK_GREEN
from src.utils.serial_info import SerialInfo
from src.utils.musics_effects import MusicEffects

class ScreenSoletrar(Base):
    """Jogo para aprender a soletrar"""

    def __init__(self, screen):
        Base.__init__(self, "", screen)
        self.logo_game = pg.image.load('images/Arandu-Mirim-Soletrando.png').convert_alpha()
        self.screen = screen
        self.help_bt_img = ButtonImage('images/duvidas32_32.png', (980, 20),
                                       self.control_help_bt_img, ())
        self.close_help_bt_img = ButtonImage('images/close.png', (758, 153),
                                             self.control_help_bt_img, ())
        self.help_enable = False
        self.help_img = pg.image.load('images/Arandu-Mirim-Soletrando-com-FAQ.png').convert_alpha()

        self.musics = MusicEffects()
        self.data_queue = queue.Queue()
        self.slots_serial = SerialInfo(self.data_queue)
        self.slots_serial.start()

        self.dic_esp32 = self.slots_serial.slots_plataforma

        # CUBO 1- T,U,R,L,C,E
        # CUBO 2 - O, I, U, B,S, V
        # CUBO 3 - D,E,A,B,U,F
        # CUBO 4 - A, O, P, G, B, U

        self.scenario = (['a', 'g', 'o', 't', 'l'], ['e', 'r', 't', 'p', 'a'], ['a', 'c', 'g', 'i', 'f'])
        self.dic_words = (['GATO', 'GALO', 'GOL', 'AGTO', 'GOTA', 'AGOA', 'GOTA', 'ALGA', 'LOGO'],
                  ['RETA', 'PARE', 'PERA', 'REPA', 'PARA', 'RAPA', 'ETAR', 'TERA', 'PATA', 'PETA', 'AERO', 'RETA', 'PERE'],
                  ['FICA', 'FACA', 'CIA', 'FIGA', 'CIGA', 'CIGA', 'FICA', 'FACA', 'FIGA', 'FICA', 'CIFA', 'CIFRA', 'FICAR', 'RIFA', 'RIFA', 'FICRA', 'CIFRA', 'FIGA', 'CIFRA', 'FICA'])


        self.indice = 0
        self.cache_images()
        self.load_scenario_images()

        BUTTON_STYLE = {
            'hover_color': BLACK,
            'clicked_color': BLACK,
            'clicked_font_color': WHITE,
            'hover_font_color': WHITE,
            'text': "PULAR",
            'font_color': BLACK,
            'font': pg.font.Font(None, 34)
        }
        # self.skip_bt = Button((670, 520, 150, 40), WHITE, self.control_skip_bt, **BUTTON_STYLE)
        BUTTON_STYLE['text'] = "MENU"
        self.menu_bt = Button((840, 520, 150, 40), WHITE, self.control_menu_bt, **BUTTON_STYLE)

        self.timer_active = True  # Controle para saber se o timer está ativo
        self.seconds_left = 60    # Tempo inicial em segundos (1 minuto)
        self.start_time = time.time()  # Inicializa o tempo de início do timer

        # Lista para armazenar palavras acertadas em cada cenário
        self.palavras_acertadas = [[], [], []]
        self.total_palavras_acertadas = 0

    def cache_images(self):
        self.images_cache = {}
        for scenario in self.scenario:
            for letter in scenario:
                if letter not in self.images_cache:
                    self.images_cache[letter] = pg.image.load(f'images/soletra/{letter}.png').convert_alpha()

    def load_scenario_images(self):
        self.start_time = time.time()  # Reinicia o tempo de início do timer
        self.timer_active = True
        self.current_scenario = self.scenario[self.indice]
        self.alfabeto_images = [self.images_cache[letter] for letter in self.current_scenario]

    def control_menu_bt(self):
        self.go_back('ScreenStart',)

    def control_help_bt_img(self):
        self.help_enable = not self.help_enable

    def control_skip_bt(self):
        if self.indice < len(self.scenario) - 1:
            self.indice += 1
        else:
            self.indice = -1
            self.timer_active = False
            
        self.load_scenario_images()

    def check_formed_word(self):
        palavra_cubos = ''.join([self.dic_esp32[key] for key in self.slots_serial.slots_plataforma.keys()])
        if len(palavra_cubos) > 3:
            if palavra_cubos in self.dic_words[self.indice] and palavra_cubos not in self.palavras_acertadas[self.indice]:

                # self.musics.congratulations()
                self.palavras_acertadas[self.indice].append(palavra_cubos)  # Adiciona a palavra ao cenário atual
                self.total_palavras_acertadas += 1
                self.musics.points()
                # self.control_skip_bt()
            else:
                # self.musics.game_Over()
                self.slots_serial.clean_slots()

    def process_input(self, events, pressed_keys):
        for event in events:
            # self.skip_bt.check_event(event)
            self.menu_bt.check_event(event)
            self.help_bt_img.check_event(event)
            self.close_help_bt_img.check_event(event)

    def render(self):
        while not self.data_queue.empty():
            self.dic_esp32 = self.data_queue.get()
        self.check_formed_word()
        print(self.dic_esp32)
        super(ScreenSoletrar, self).render()
        self.screen.blit(self.logo_game, (0, 0))
        # self.skip_bt.update(self.screen)
        self.menu_bt.update(self.screen)
        self.help_bt_img.update(self.screen)
        positions = [(105, 160), (355, 160), (100, 350), (360, 350), (230, 260)]
        for img, pos in zip(self.alfabeto_images, positions):
            self.screen.blit(img, pos)
        if self.help_enable:
            self.screen.fill((232, 232, 232))
            self.screen.blit(self.help_img, (0, 0))
            self.close_help_bt_img.update(self.screen)

        # Desenhar o timer na tela
        font = pg.font.Font(None, 60)
        timer_text = font.render(f'Tempo: {self.seconds_left}', True, BLACK)
        self.screen.blit(timer_text, (560, 160))

        # Exibir palavras acertadas por cenário
        font_palavras = pg.font.Font(None, 25)
        for i, palavras in enumerate(self.palavras_acertadas):
            text = ', '.join(palavras)
            text_render = font_palavras.render(f'Palavras Acertadas Cenário {i+1}: {text}', True, LIGHTGREY)
            self.screen.blit(text_render, (570, 210 + i * 30))

        # Atualizar o timer
        if self.timer_active:
            now = time.time()
            elapsed = now - self.start_time
            self.seconds_left = max(0, 60 - int(elapsed))  # Tempo total ajustado para 60 segundos

            # print(self.indice)
            if self.seconds_left <= 0:
                self.timer_active = False
                self.control_skip_bt()
            

        # Mostrar total de palavras acertadas no final dos 3 cenários
        # if self.indice == 0 and not self.timer_active:
        if self.indice == -1:
            font_total = pg.font.Font(None, 36)
            text_total = font_total.render(f'Total de Palavras Acertadas: {self.total_palavras_acertadas}', True, T_DARK_GREEN)
            # print(self.total_palavras_acertadas)
            self.screen.blit(text_total, (560, 310))
            pg.display.flip()
            self.musics.congratulations()
            # time.sleep(3)
            self.control_menu_bt()

    def cleanup(self):
        self.slots_serial.stop()
        self.slots_serial.join()

def main():
    try:
        pg.init()
        screen = pg.display.set_mode((1024, 600))
        screen_soletrar = ScreenSoletrar(screen)
        clock = pg.time.Clock()

        running = True
        while running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    running = False

            pressed_keys = pg.key.get_pressed()

            screen.fill((255, 255, 255))
            screen_soletrar.process_input(events, pressed_keys)
            screen_soletrar.render()

            pg.display.flip()
            clock.tick(30)  # Limita a taxa de quadros a 30 FPS

    finally:
        screen_soletrar.cleanup()
        pg.quit()

if __name__ == '__main__':
    main()
