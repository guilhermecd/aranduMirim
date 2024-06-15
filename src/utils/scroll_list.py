import pygame as pg
from src.utils import ButtonImage, Button


class ScrollList(object):
    """Utilizado para criar ScrollList
        list_content = ('Lote 01', '04,50', '02/05/19', 'Adubação',
                        'Lote 02', '18,50', '04/05/19', 'Herbicida',
                        'Lote 03', '25,50', '10/05/19', 'Inseticida',
                        'Lote 04', '14,30', '13/05/19', 'Herbicida',
                        'Lote 05', '32,22', '20/05/19', 'Inseticida',
                        'Lote 06', '27,00', '22/05/19', 'Adubação',
                        'Lote 07', '32,22', '20/05/19', 'Inseticida',
                        'Lote 08', '32,22', '20/05/19', 'Inseticida',
                        'Lote 09', '32,22', '20/05/19', 'Inseticida',
                        'Lote 10', '32,22', '20/05/19', 'Inseticida',
                        'Lote 11', '32,22', '20/05/19', 'Inseticida',
                        'Lote 12', '32,22', '20/05/19', 'Inseticida')

        self.scrollist = ScrollList(('Nome', 'HA', 'Dia', 'Evento'),
                                    list_content, (50, 30))

        def event_loop(self):
            self.scrollist.check_event(event)

        def main_loop(self):
            while 1:
                self.scrollist.update(self.screen)
    """

    def __init__(self, list_header, list_content, position):
        self.position = position
        self.list_header = list_header

        self.list_content = list_content
        self.color_lines = ((29, 110, 166), (86, 81, 78))
        self.color_header = (0, 0,0)
        self.__load_data()
        self.__load_config()
        self.__create_bar()
        self.__draw_header()
        self.__draw_content_header()
        self.__draw_table()
        self.__draw_content_table()


    def status_select_row(self):
        return self.select_row


    def __load_data(self):
        self.qtd_lines_view = (int) (len(self.list_content) / \
            (len(self.list_header))) + 1
        if self.qtd_lines_view > 5:
            self.qtd_lines_view = 6
        self.colunms = len(self.list_header)
        self.lines = (len(self.list_content) / self.colunms)
        self.border_size = 2
        self.border_color = (255, 255, 255)
        self.qtd_width_border = self.colunms+1
        self.qtd_height_border= self.lines+1
        self.width_cell = 900 / self.colunms
        self.height_cell = 40
        self.type_font = None
        self.color_text = (255, 255, 255)
        self.size_text = 32
        self.speed_scroll = 15
        self.scroll_y = 0
        self.move_up = 1
        self.move_down = 1
        self.size_bar = 10
        self.pressed = 0
        self.position_pressed = None
        self.select_row = None


    def __load_config(self):
        self.width = (self.qtd_width_border * self.border_size) + \
            (self.colunms * self.width_cell)
        self.height = (self.qtd_height_border * self.border_size) + \
            (self.lines * self.height_cell)
        self.width_view = self.width
        self.height_view = ((self.qtd_lines_view + 1) * self.border_size) + \
            (self.qtd_lines_view * self.height_cell)
        self.button_down = ButtonImage('images/46.png',
                                       (self.width_view + self.position[0],
                                        self.height_view - 40 + \
                                        self.position[1] - self.border_size),
                                        self.control_button_down, ())
        self.button_up = ButtonImage('images/45.png',
                                     (self.width_view + self.position[0],
                                      self.border_size + self.position[1]),
                                      self.control_button_up, ())
        self.button_up_down_size = self.button_down.get_size()
        if self.lines > self.qtd_lines_view-1:
            self.view = pg.Surface((self.width_view + \
                self.button_up_down_size[0] + \
                    self.border_size, self.height_view))
        else:
            self.view = pg.Surface((self.width_view, self.height_view))
        self.view.fill(self.border_color)
        self.surface_main = pg.Surface((self.width, self.height))
        self.surface_main.fill(self.border_color)
        self.position_size = self.surface_main.get_rect()
        self.font = pg.font.SysFont(self.type_font, self.size_text)
        self.scroll_y = self.border_size + self.height_cell


    def __create_bar(self):
        BUTTON_STYLE = {"hover_color" : (86, 81, 78),
                        "clicked_color" : (76, 71, 68),
                        "clicked_font_color" : (0,0,0),
                        "hover_font_color" : (255,180,0)}
        self.min_size_bar = int (self.height_cell / 2)

        self.limit_init_bar = self.border_size*2 + self.position[1] + \
            self.button_up_down_size[1]
        self.limit_end_bar = self.height_view - 40 + self.position[1] - \
            self.border_size*2 - self.min_size_bar
        self.total_space_bar = (7 * self.min_size_bar) + self.border_size * 3
        if self.lines > 5:
            self.speed_view_with_bar = self.total_space_bar/(self.lines - \
                self.qtd_lines_view+1)
            self.speed_view_with_bar += 0.33
        else:
            self.speed_view_with_bar = 0
        self.button_bar = Button((self.width_view + self.position[0],
                                  self.limit_init_bar,
                                  self.button_up_down_size[0],
                                  self.min_size_bar),
                                  (86, 81, 78), self.control_button_bar,
                                  **BUTTON_STYLE)



    def __draw_header(self):
        self.height_header = self.border_size * 2 + self.height_cell
        self.surface_header = pg.Surface((self.width, self.height_header))
        self.surface_header.fill(self.border_color)
        x = self.position_size[0] + self.border_size
        y = self.position_size[1] + self.border_size
        while y < self.position_size[2]:
            pg.draw.rect(self.surface_header, self.color_header,
                         (y, x, self.width_cell, self.height_cell))
            if y < self.position_size[2]:
                y += self.width_cell + self.border_size


    def __draw_content_header(self):
        x = self.position_size[0] + self.border_size
        y = self.position_size[1] + self.border_size
        for l in self.list_header:
            text_width, text_height = self.font.size(l)
            pos_y_text = ((self.width_cell - text_width ) / 2)
            pos_x_text = ((self.height_cell - text_height) / 2)
            self.surface_header.blit(
                self.font.render(l, True, self.color_text), (pos_y_text + y,
                                                             pos_x_text + x))
            y += self.width_cell + self.border_size


    def __draw_table_select(self):
        x = self.position_size[0] + self.border_size
        y = self.position_size[1] + self.border_size
        i = 1
        color = False
        move = self.move_down - 1
        selected = (int) (self.position_pressed[1] / (self.height_cell+self.border_size*2))+move
        if self.select_row == selected:
            self.select_row = None
            self.pressed = 0
        while y < self.position_size[3]:
            x_value = (int)(y / self.height_cell)
            if self.pressed == 1:
                if selected == x_value:
                    color = (217, 211, 207)
                    self.select_row = selected
                    pg.draw.rect(self.surface_main, color,
                        (x, y, self.width_cell, self.height_cell))
                else:
                    pg.draw.rect(self.surface_main, self.color_lines[i],
                                 (x, y, self.width_cell, self.height_cell))
            else:
                pg.draw.rect(self.surface_main, self.color_lines[i],
                    (x, y, self.width_cell, self.height_cell))

            if x < self.position_size[2]:
                x += self.width_cell + self.border_size
            else:
                y += self.height_cell + self.border_size
                x = self.position_size[0] + self.border_size
                i += 1
                if i >= len(self.color_lines):
                    i = 0


    def __draw_table(self):
        x = self.position_size[0] + self.border_size
        y = self.position_size[1] + self.border_size
        i = 1
        while y < self.position_size[3]:
            pg.draw.rect(self.surface_main, self.color_lines[i],
                (x, y, self.width_cell, self.height_cell))

            if x < self.position_size[2]:
                x += self.width_cell + self.border_size
            else:
                y += self.height_cell + self.border_size
                x = self.position_size[0] + self.border_size
                i += 1
                if i >= len(self.color_lines):
                    i = 0


    def resize_content(self, text):
        w, _ = self.font.size(text)
        if w > self.width_cell - 10:
            while w > self.width_cell - 25:
                text = text[:-1]
                w, _ = self.font.size(text)
            return text + '...'
        return text


    def __draw_content_table(self):
        x = self.position_size[0] + self.border_size
        y = self.position_size[1] + self.border_size
        for l in self.list_content:
            l = self.resize_content(l)
            text_width, text_height = self.font.size(l)
            pos_y_text = ((self.width_cell - text_width) / 2)
            pos_x_text = ((self.height_cell - text_height) / 2)
            self.surface_main.blit(self.font.render(l, True, self.color_text),
                                                    (pos_y_text + y,
                                                     pos_x_text + x))
            if y < self.position_size[2] - self.width_cell - self.border_size:
                y += self.width_cell + self.border_size
            else:
                y = self.position_size[1] + self.border_size
                x += self.height_cell + self.border_size


    def __draw_selection(self):
        pressed, trash, trash2 = pg.mouse.get_pressed()
        if pressed == 1:
            self.pressed = 1
            self.position_pressed = pg.mouse.get_pos()
            self.position_pressed = (self.position_pressed[0] - \
                self.position[0], self.position_pressed[1] - self.position[1]);
            self.position_pressed =  (self.position_pressed[0],
                                      self.position_pressed[1] - 45)
            if self.position_pressed [0] > 0 and self.position_pressed[1] > 0:
                if self.position_pressed[0] < self.width_view and \
                    self.position_pressed[1] < self.height_view:
                    self.__draw_table_select()
                    self.__draw_content_table()
                    pg.time.wait(200)
            self.pressed = 0


    def control_button_down(self):
        position_bar = self.button_bar.get_position()
        limit_down = self.height_view - self.position_size[3]
        self.scroll_y = max(self.scroll_y - self.height_cell - self.border_size,
                            limit_down)
        move_bar = position_bar[1] + self.speed_view_with_bar
        move_bar = min(move_bar, self.limit_end_bar)
        self.button_bar.set_position((position_bar[0], move_bar))
        if self.move_down <= int (self.lines+1 - self.qtd_lines_view):
            self.move_down += 1
        if self.move_up > 1:
            self.move_up -= 1


    def control_button_bar(self):
        pass


    def control_button_up(self):
        position_bar = self.button_bar.get_position()
        limit_up = self.height_cell + self.border_size
        self.scroll_y = min(self.scroll_y + self.height_cell + self.border_size,
                            limit_up)
        move_bar = position_bar[1] - self.speed_view_with_bar
        move_bar = max(move_bar, self.limit_init_bar)
        self.button_bar.set_position((position_bar[0], move_bar))
        if self.move_up <= int (self.lines+1 - self.qtd_lines_view):
            self.move_up += 1
        if self.move_down > 1:
            self.move_down -= 1

    def delete_element_scroll_list(self):
        if self.select_row != None:
            init_del = self.select_row * self.colunms
            del self.list_content[init_del:init_del+self.colunms]

    def update_scrooll_list(self):
        self.__load_data()
        self.__load_config()
        self.__create_bar()
        self.__draw_header()
        self.__draw_content_header()
        self.__draw_table()
        self.__draw_content_table()


    def check_event(self, e):
        self.button_down.check_event(e)
        self.button_up.check_event(e)
        self.button_bar.check_event(e)


    def update(self, screen):
        self.view.blit(self.surface_main, (self.position_size[0],
                                           self.scroll_y))
        screen.blit(self.view, self.position)
        screen.blit(self.surface_header, self.position)
        if self.lines > self.qtd_lines_view-1:
            self.button_down.update(screen)
            self.button_up.update(screen)
            self.button_bar.update(screen)
        self.__draw_selection()
