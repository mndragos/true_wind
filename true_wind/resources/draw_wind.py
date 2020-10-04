import kivy
kivy.require('1.11.1')

from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class DrawWind(Popup):
    draw_label = ObjectProperty

    def show_popup(self, value):
        drawing = DrawWind()
        drawing.open()
