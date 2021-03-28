import pygame as pg
from pygame_widgets import Button
from Extract_results import get_results
from Check_box import Checkbox

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
        'max: ',
        'min: ',
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
        onClick=lambda: get_results(text,chkbox.checked)
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
        screen.blit(warning,(50,280))
        button.listen(events)
        button.draw()
        chkbox.render_checkbox()
        pg.display.flip()


pg.init()
main()
pg.quit()
"""
def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    #clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        #clock.tick(30)
        pass


pg.init()
main()
pg.quit()
"""