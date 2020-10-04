# main.py
# import os
import kivy
kivy.require('1.11.1')
from kivy.config import Config

Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 500)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TrueWind(BoxLayout):
    pass


class TrueWindApp(App):
    def build(self):
        return TrueWind()


if __name__ == '__main__':
    TrueWindApp().run()
