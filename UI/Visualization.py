import pygame as pg
from pygame_widgets import Button
from UI.Extract_results import get_results
from UI.Check_box import Checkbox

# ANDRUHUS, PLEASE FORMAT CODE - ctrl + l
# Bitte schön


# TODO add two asc and desc gener arr ord

class MainVisual:
    def __init__(self):
        self.screen = pg.display.set_mode((640, 480))

        self.font = pg.font.Font(None, 32)
        self.input_boxes = [
            pg.Rect(150, 50, 140, 32),
            pg.Rect(150, 100, 140, 32),
            pg.Rect(150, 150, 140, 32)
        ]
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.color = [
            self.color_inactive,
            self.color_inactive,
            self.color_inactive
        ]
        self.labels_text_for_input_boxes = [
            'min: ',
            'max: ',
            'quantity: '
        ]

        self.active = [False, False, False]
        self.text = ['', '', '']
        self.done = False

        self.checkboxes = [
            Checkbox(
                self.screen, 150, 230,
                caption='Random initial order', color=self.color_inactive,
                text_offset=(125, 0), font_color=self.color_inactive,
                font_size=32
            ),
            Checkbox(
                self.screen, 150, 270,
                caption='Descending initial order', color=self.color_inactive,
                text_offset=(140, 0), font_color=self.color_inactive,
                font_size=32
            ),
            Checkbox(
                self.screen, 150, 310,
                caption='Ascending initial order', color=self.color_inactive,
                text_offset=(135, 0), font_color=self.color_inactive,
                font_size=32
            )
        ]
        self.checkboxes[0].checked = True

        self.button = Button(
            self.screen, 220, 400, 100, 50, text='OK',
            fontSize=18,
            inactiveColour=self.color_inactive,
            pressedColour=self.color_active,
            onClick=lambda: get_results(self.text, [x.checked for x in self.checkboxes])
        )

    def update_checkboxes(self, event):
        previous_index = None
        for index in range(3):
            if self.checkboxes[index].checked:
                previous_index = index
        for index in range(3):
            self.checkboxes[index].update_checkbox(event)
        count_of_active_checkbox = 0
        for index in range(3):
            if self.checkboxes[index].checked:
                count_of_active_checkbox += 1
        if count_of_active_checkbox > 1 and not previous_index == None:
            self.checkboxes[previous_index].checked = False
        if count_of_active_checkbox < 1 and not previous_index == None:
            self.checkboxes[previous_index].checked = True
        if count_of_active_checkbox < 1 and previous_index == None:
            self.checkboxes[0].checked = True

    def mouse_event(self, event):
        for index in range(3):
            if self.input_boxes[index].collidepoint(event.pos):
                self.active[index] = not self.active[index]
            else:
                self.active[index] = False
            self.color[index] = self.color_active if self.active[index] else self.color_inactive

    def key_event(self, event):
        for index in range(3):
            if self.active[index]:
                if event.key == pg.K_BACKSPACE:
                    self.text[index] = self.text[index][:-1]
                else:
                    self.text[index] += event.unicode

    def text_render(self, txt_surface_for_input_boxes, labels_for_input_boxes):
        for index in range(3):
            txt_surface_for_input_boxes.append(self.font.render(self.text[index], True, self.color[index]))
            labels_for_input_boxes.append(
                self.font.render(self.labels_text_for_input_boxes[index], True, self.color[index]))

    def box_resize(self, txt_surface_for_input_boxes, labels_for_input_boxes):
        for index in range(3):
            width = max(200, txt_surface_for_input_boxes[index].get_width() + 10)
            self.input_boxes[index].w = width
            # Blit the text.
            self.screen.blit(txt_surface_for_input_boxes[index],
                             (self.input_boxes[index].x + 5, self.input_boxes[index].y + 5))
            self.screen.blit(labels_for_input_boxes[index],
                             (self.input_boxes[index].x - labels_for_input_boxes[index].get_width(),
                              self.input_boxes[index].y + 5))
            pg.draw.rect(self.screen, self.color[index], self.input_boxes[index], 2)

    def last_part(self, events):
        warning = self.font.render('The array will be always sorted in acsending order', True, self.color_active)
        self.screen.blit(warning, (50, 340))
        self.button.listen(events)
        self.button.draw()
        for item in self.checkboxes:
            item.render_checkbox()
        pg.display.flip()

    def run(self):
        while not self.done:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mouse_event(event)

                if event.type == pg.KEYDOWN:
                    self.key_event(event)

                self.update_checkboxes(event)
            self.screen.fill((30, 30, 30))
            # Render the current text.
            txt_surface_for_input_boxes = []
            labels_for_input_boxes = []

            self.text_render(txt_surface_for_input_boxes, labels_for_input_boxes)
            self.box_resize(txt_surface_for_input_boxes, labels_for_input_boxes)
            self.last_part(events)


def main():
    screen = pg.display.set_mode((640, 480))

    font = pg.font.Font(None, 32)
    input_boxes = [
        pg.Rect(150, 50, 140, 32),
        pg.Rect(150, 100, 140, 32),
        pg.Rect(150, 150, 140, 32)
    ]
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = [
        color_inactive,
        color_inactive,
        color_inactive
    ]
    labels_text_for_input_boxes = [
        'min: ',
        'max: ',
        'quantity: '
    ]

    active = [False, False, False]
    text = ['', '', '']
    done = False
    chkbox = Checkbox(
        screen, 150, 230,
        caption='Randomize', color=color_inactive,
        text_offset=(75, 0), font_color=color_inactive,
        font_size=32
    )

    button = Button(
        screen, 220, 350, 100, 50, text='OK',
        fontSize=18,
        inactiveColour=color_inactive,
        pressedColour=color_active,
        onClick=lambda: get_results(text, chkbox.checked)
    )

    while not done:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                for index in range(3):
                    if input_boxes[index].collidepoint(event.pos):
                        active[index] = not active[index]
                    else:
                        active[index] = False
                    color[index] = color_active if active[index] else color_inactive

            if event.type == pg.KEYDOWN:
                for index in range(3):
                    if active[index]:
                        if event.key == pg.K_BACKSPACE:
                            text[index] = text[index][:-1]
                        else:
                            text[index] += event.unicode

            chkbox.update_checkbox(event)
        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface_for_input_boxes = []
        labels_for_input_boxes = []

        for index in range(3):
            txt_surface_for_input_boxes.append(font.render(text[index], True, color[index]))
            labels_for_input_boxes.append(font.render(labels_text_for_input_boxes[index], True, color[index]))
        # Resize the box if the text is too long.
        for index in range(3):
            width = max(200, txt_surface_for_input_boxes[index].get_width() + 10)
            input_boxes[index].w = width
            # Blit the text.
            screen.blit(txt_surface_for_input_boxes[index], (input_boxes[index].x + 5, input_boxes[index].y + 5))
            screen.blit(labels_for_input_boxes[index],
                        (input_boxes[index].x - labels_for_input_boxes[index].get_width(), input_boxes[index].y + 5))
            # Blit the input_box rect.
            pg.draw.rect(screen, color[index], input_boxes[index], 2)
        warning = font.render('The array will be always sorted in acsending order', True, color_active)
        screen.blit(warning, (50, 280))
        button.listen(events)
        button.draw()
        chkbox.render_checkbox()
        pg.display.flip()
