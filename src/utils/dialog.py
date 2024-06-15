import pygame as pg
from src.utils import ButtonImage, Button, LabelText
from src.utils.settings import BGCOLOR, RED, LIGHTGREY, HEIGHT, WIDTH, WHITE


class Dialog(object):

    def __init__(self, msg1, msg2, function_confirm, function_cancel):
        self.dialog = False
        BUTTON_STYLE = {
            'hover_color': WHITE,
            'clicked_color': WHITE,
            'clicked_font_color': WHITE,
            'hover_font_color': WHITE
        }
        pos_y = (HEIGHT / 2) - (150 / 2)
        pos_x = (WIDTH / 2)- (300 / 2)
        self.backdialog = Button((pos_x, pos_y, 300, 150), WHITE, lambda: (),
                                 **BUTTON_STYLE)
        self.button_confirm = ButtonImage('images/confirm.png', (412, 305),
                                          function_confirm, ())
        self.button_cancel = ButtonImage('images/cancel.png', (538, 305),
                                         function_cancel, ())
        self.msg1_lb = LabelText(msg1, (510, 255) , size=32, color=(0, 0, 0))
        self.msg2_lb = LabelText(msg2, (510, 285) , size=32, color=(0, 0, 0))
        self.clear_status = False
        self.info_clr_lb = LabelText('Dados apagados!', (300, 500),
                                     (76, 175, 80), 32)
        self.check_in_img = pg.image.load('images/ok.png').convert_alpha()
        self.position_ok = (130, 463)


    def get_dialog(self):
        return self.dialog


    def set_dialog(self, value):
        self.dialog = value


    def set_position_clear_msg(self, new_position):
        self.info_clr_lb = LabelText('Dados apagados!', new_position,
                                     (76, 175, 80), 32)
        self.position_ok = ((new_position[0] - 170, new_position[1] - 37))


    def set_clear(self, value):
        self.clear_status = value
        if self.clear_status:
            pg.time.set_timer(pg.USEREVENT, 2000)


    def check_event(self,event):
        if self.dialog:
            self.button_confirm.check_event(event)
            self.button_cancel.check_event(event)
        if event.type == pg.USEREVENT:
            pg.time.set_timer(pg.USEREVENT, 0)
            self.clear_status = False


    def update(self, screen):
        if self.dialog:
            self.backdialog.update(screen)
            self.msg1_lb.update(screen)
            self.msg2_lb.update(screen)
            self.button_confirm.update(screen)
            self.button_cancel.update(screen)
        if self.clear_status:
            screen.blit(self.check_in_img, self.position_ok)
            self.info_clr_lb.update(screen)
