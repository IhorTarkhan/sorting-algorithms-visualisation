import pygame as pg
from Extract_results import get_results
pg.init()


class Checkbox:
    def __init__(self, surface, x, y, color=(230, 230, 230), caption="", outline_color=(0, 0, 0),
                 check_color=(0, 0, 0), font_size=22, font_color=(0, 0, 0), text_offset=(28, 1)):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        # checkbox object
        self.checkbox_obj = pg.Rect(self.x, self.y, 18, 18)
        self.checkbox_outline = self.checkbox_obj.copy()
        # variables to test the different states of the checkbox
        self.checked = False
        self.active = False
        self.unchecked = True
        self.click = False

    def _draw_button_text(self):
        self.font = pg.font.Font(None, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + 18 / 2 - w / 2 + self.to[0], self.y + 18 / 2 - h / 2 + self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_checkbox(self):
        if self.checked:
            pg.draw.rect(self.surface, self.color, self.checkbox_obj)
            pg.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            pg.draw.circle(self.surface, self.cc, (self.x + 9, self.y + 9), 6)

        elif not self.checked:
            pg.draw.rect(self.surface, self.color, self.checkbox_obj)
            pg.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = event_object.pos
        # self.x, self.y, 12, 12
        px, py, w, h = self.checkbox_obj  # getting check box dimensions
        if px < x < px + w and px < x < px + w:
            self.active = True
        else:
            self.active = False

    def _mouse_up(self):
            if self.active and not self.checked and self.click:
                    self.checked = True
            elif self.checked:
                self.checked = False
                self.unchecked = True

            if self.click is True and self.active is False:
                if self.checked:
                    self.checked = True
                if self.unchecked:
                    self.unchecked = True
                self.active = False

    def update_checkbox(self, event_object):
        if event_object.type == pg.MOUSEBUTTONDOWN:
            x, y = event_object.pos
            px, py, w, h = self.checkbox_obj
            if px < x < px + w and px < x < px + w:
                self.checked = not self.checked
            #print(self.checked)



    def is_checked(self):
        if self.checked is True:
            return True
        else:
            return False

    def is_unchecked(self):
        if self.checked is False:
            return True
        else:
            return False




def main():
    WIDTH = 800
    HEIGHT = 600
    display = pg.display.set_mode((WIDTH, HEIGHT))

    chkbox = Checkbox(display, 300, 400,caption='text')

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()
            chkbox.update_checkbox(event)

        display.fill((200, 200, 200))
        chkbox.render_checkbox()
        pg.display.flip()

if __name__ == '__main__': main()