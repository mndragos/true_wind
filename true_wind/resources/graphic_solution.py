import kivy
kivy.require('1.11.1')
from kivy.uix.popup import Popup
from kivy.properties import (ListProperty, ObjectProperty)
from kivy.graphics import Color, Line
from math import cos, radians, sin


class GraphicSolution(Popup):
    ORIGIN = ListProperty([255, 200])
    s_line = ObjectProperty()
    aw_line = ObjectProperty()
    tw_line = ObjectProperty()
    scaler = ObjectProperty()

    def __init__(self, **kwargs):
        super(GraphicSolution, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1)
            self.s_line = Line(points=[self.ORIGIN[0], self.ORIGIN[1], self.ORIGIN[0],
                                       self.ORIGIN[1]], width=2)
            Color(0, 1, 0, 1)
            self.aw_line = Line(points=[self.ORIGIN[0], self.ORIGIN[1], self.ORIGIN[0],
                                        self.ORIGIN[1]], width=2)
            Color(0, 0, 1, 1)
            self.tw_line = Line(points=[self.ORIGIN[0], self.ORIGIN[1], self.ORIGIN[0],
                                        self.ORIGIN[1]], width=2)

    def show_popup(self, aw_positions, s_speed):
        drawing = GraphicSolution()
        drawing.s_line.points[3] = self.ORIGIN[1] + float(s_speed)
        drawing.aw_line.points[2:] = [aw_positions[0], aw_positions[1]]
        drawing.tw_line.points[1] = self.ORIGIN[1] + float(s_speed)
        drawing.tw_line.points[2:] = [aw_positions[0], aw_positions[1]]
        drawing.s_line.points = drawing.s_line.points
        drawing.aw_line.points = drawing.aw_line.points
        drawing.tw_line.points = drawing.tw_line.points
        drawing.open()

    def vector_position(self, angle: float, speed: float, side: str) -> list:
        """Determines the vector position by taking the angle into account.

        Args:
            angle (float): wind angle.
            speed (float]): wind speed.
            side (str): wind side relative to the ship.

        Returns:
            list: [description]
        """

        angle = float(angle)
        speed = float(speed)
        side = str(side)
        ORIGIN = self.ORIGIN
        pos = [0, 0]
        alfa = 90 - angle

        if side.lower() == "port" and (alfa > 0 or alfa < 0):
            pos[0] = round(ORIGIN[0] - speed*cos(radians(alfa)), 1)
            pos[1] = round(ORIGIN[1] + speed * sin(radians(alfa)), 1)
            return pos
        elif side.lower() == "starboard" and (alfa > 0 or alfa < 0):
            pos[0] = round(ORIGIN[0] + speed*cos(radians(alfa)), 1)
            pos[1] = round(ORIGIN[1] + speed * sin(radians(alfa)), 1)
            return pos
        elif side.lower() == "bow" or side.lower() == "stern":
            pos[0] = ORIGIN[0]
            pos[1] = ORIGIN[1] + speed
            return pos

        if side.lower() == "port" and alfa == 0:
            pos[0] = ORIGIN[0] - speed
            pos[1] = ORIGIN[1]
            return pos
        elif side.lower() == "starboard" and alfa == 0:
            pos[0] = ORIGIN[0] + speed
            pos[1] = ORIGIN[1]
            return pos
