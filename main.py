import pyglet

import components

display = pyglet.canvas.get_display()
screens = display.get_screens()
window = None

# Only take vertical screen
for screen in screens:
    if screen.width < screen.height:
        window = pyglet.window.Window(fullscreen=True, screen=screen)

if not window:
    exit()

comps = components.Components(window.width, window.height)


@window.event
def on_draw():
    comps.header.draw()


pyglet.app.run()
