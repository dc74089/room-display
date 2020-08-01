import os

import pyglet
from pyowm import OWM


class Title:
    def __init__(self, x1, y1, x2, y2):
        self.header = pyglet.text.Label("Today",
                                        font_name="Ubuntu",
                                        font_size=100,
                                        x=(x2-x1)//2, y=(y2-y1),
                                        anchor_x='center', anchor_y='top')

    def draw(self):
        self.header.draw()


class Weather:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.weather = {}

    def update(self):
        owm = OWM(os.getenv("OWM_API_KEY"))
        mgr = owm.weather_manager()
        self.weather = mgr.one_call(28.5705302, -81.2221211)

        print(self.weather)
