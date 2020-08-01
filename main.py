import pyglet

import components

components.Weather(0, 0, 0, 0).update()

display = pyglet.canvas.get_display()
screens = display.get_screens()
window = None

# Only take vertical screen
for screen in screens:
    if screen.width < screen.height:
        window = pyglet.window.Window(fullscreen=True, screen=screen)

if not window:
    exit()

title = components.Title(0, 0, window.width, window.height)


@window.event
def on_draw():
    title.draw()


# pyglet.app.run()
