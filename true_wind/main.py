# main.py
import kivy
kivy.require('1.11.1')
from kivy.config import Config

Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'borderless', 0)
Config.set('graphics', 'resizable', 0)
Config.set('kivy', 'window_icon', r'true_wind\img\ship_bow.png')

from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from true_wind.resources.true_wind_angle import t_w_angle
from true_wind.resources.true_wind_direction import (t_w_direction, t_w_reduction,
                                                     t_w_pretty_view)
from true_wind.resources.true_wind_speed import t_w_speed
from true_wind.resources.graphic_solution import GraphicSolution
from true_wind.resources.error_message import ErrorMessage


class TrueWind(BoxLayout):
    s_heading = ObjectProperty()
    s_speed = ObjectProperty()
    aw_side = ObjectProperty()
    aw_angle = ObjectProperty()
    aw_speed = ObjectProperty()
    tw_angle = ObjectProperty()
    tw_direction = ObjectProperty()
    tw_speed = ObjectProperty()
    graphic = GraphicSolution()
    error_message = ErrorMessage()

    def scaling_speed(self) -> tuple:
        """Compares the ship and wind speed and scales them up for
        the graphic solution.
        Returns:
            tuple: (s_speed, aw_speed)
        """
        s_speed = float(self.s_speed.text)
        aw_speed = float(self.aw_speed.text)

        if s_speed <= 25 and aw_speed <= 25:
            if s_speed >= 15 or aw_speed >= 15:
                s_speed = s_speed*5
                aw_speed = aw_speed*5
            elif s_speed < 15 or aw_speed < 15:
                s_speed = s_speed*10
                aw_speed = aw_speed*10
        elif s_speed > 25 or aw_speed > 25:
            s_speed = s_speed*2
            aw_speed = aw_speed*2
        return s_speed, aw_speed

    def graphic_origin(self) -> list:
        """Uses ORIGIN() from GraphicSolution() and
        inputs of apparent angle and ship's side from GUI.

        Returns:
            list[str, float]: returns a list [side, angle]
        """
        side = self.aw_side.text
        angle = self.aw_angle.text
        return self.graphic.ORIGIN(side, angle)

    def positions(self) -> list:
        """Uses the vector_position() from GraphicSolution() and inputs
        from the GUI.

        Returns:
            list[float, float, str]: returns list [angle, speed, side]
        """
        return self.graphic.vector_position(
            self.aw_angle.text, self.scaling_speed()[1], self.aw_side.text)

    def wind_data(self) -> None:
        """The fuction is bound to 'Solution' button in truewind.kv.
        Listens to the GUI inputs and calculates the true wind
        speed and direction.
        Returns the result to a text label in the GUI.
        """
        try:
            # Takes values from user.
            speed = t_w_speed(self.s_speed.text, self.aw_speed.text, self.aw_angle.text)
            angle = t_w_angle(self.aw_speed.text, speed, self.s_speed.text)
            direction = t_w_direction(self.s_heading.text, self.aw_side.text, angle)
            true_direction = t_w_reduction(direction)
            # returns results to user.
            self.tw_angle.text = t_w_pretty_view(angle)
            self.tw_direction.text = t_w_pretty_view(true_direction)
            self.tw_speed.text = f'{speed} knots'
        except ValueError:
            return self.error_message.show_error(
                "Please,\nfill in the required fields\ncorrectly.")

    def show_graphic_solution(self) -> None:
        """The fuction is bound to 'Graphic Solution' button in truewind.kv and
        opens up GraphicSolution Popup.
        """
        try:
            aw_positions = self.positions()
            s_speed = self.scaling_speed()[0]
            graphic_origin = self.graphic_origin()
            self.graphic.show_popup(aw_positions, s_speed, graphic_origin)
        except ValueError:
            return self.error_message.show_error(
                "Please,\nfill in the required fields\ncorrectly.")


class TrueWindApp(App):
    resource_add_path(r"true_wind\templates")

    def build(self):
        return TrueWind()


if __name__ == '__main__':
    TrueWindApp().run()
