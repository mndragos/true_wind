# main.py
# import os
import kivy
kivy.require('1.11.1')
from kivy.config import Config

Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 500)

from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from true_wind.resources.true_wind_angle import t_w_angle
from true_wind.resources.true_wind_direction import (t_w_direction, t_w_reduction,
                                                     t_w_pretty_view)
from true_wind.resources.true_wind_speed import t_w_speed
from true_wind.resources.draw_wind import DrawWind


class TrueWind(BoxLayout):
    s_heading = ObjectProperty()
    s_speed = ObjectProperty()
    aw_side = ObjectProperty()
    aw_angle = ObjectProperty()
    aw_speed = ObjectProperty()
    tw_direction = ObjectProperty()
    tw_speed = ObjectProperty()
    drawing = DrawWind()

    def wind_data(self):
        speed = t_w_speed(self.s_speed.text, self.aw_speed.text, self.aw_angle.text)
        angle = t_w_angle(self.aw_speed.text, speed, self.s_speed.text)
        direction = t_w_direction(self.s_heading.text, self.aw_side.text, angle)
        true_direction = t_w_reduction(direction)

        self.tw_direction.text = t_w_pretty_view(true_direction)
        self.tw_speed.text = f'{speed} knots'

    def show_graphic_solution(self):
        self.drawing.show_popup('value')


class TrueWindApp(App):
    resource_add_path("true_wind\\templates")

    def build(self):
        return TrueWind()


if __name__ == '__main__':
    TrueWindApp().run()
