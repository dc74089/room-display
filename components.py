import pyglet


class Components:
    def __init__(self, width, height):
        self.header = pyglet.text.Label("Today",
                                        font_name="Ubuntu",
                                        font_size=100,
                                        x=width//2, y=height,
                                        anchor_x='center', anchor_y='top')
