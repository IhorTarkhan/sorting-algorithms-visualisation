import pygame as pg


def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    input_boxes = [
        pg.Rect(100, 100, 140, 32),
        pg.Rect(100, 150, 140, 32),
        pg.Rect(100, 200, 140, 32)
    ]
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = [
        color_inactive,
        color_inactive,
        color_inactive
    ]
    active = [False,False,False]
    text = ['','','']
    done = False
    while not done:
        for event in pg.event.get():
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
                        if event.key == pg.K_RETURN:
                            print(text[index])
                            text[index] = ''
                        elif event.key == pg.K_BACKSPACE:
                            text[index] = text[index][:-1]
                        else:
                            text[index] += event.unicode
        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = []
        for index in range(3):
            txt_surface.append( font.render(text[index], True, color[index]))
        # Resize the box if the text is too long.
        for index in range(3):
            width = max(200, txt_surface[index].get_width() + 10)
            input_boxes[index].w = width
        # Blit the text.
            screen.blit(txt_surface[index], (input_boxes[index].x + 5, input_boxes[index].y + 5))
        # Blit the input_box rect.
            pg.draw.rect(screen, color[index], input_boxes[index], 2)

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