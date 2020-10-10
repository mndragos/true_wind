import kivy
kivy.require('1.11.1')
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Line
from math import cos, radians, sin


class GraphicSolution(Popup):
    s_line = ObjectProperty()
    aw_line = ObjectProperty()
    tw_line = ObjectProperty()
    scaler = ObjectProperty()

    def __init__(self, **kwargs):
        super(GraphicSolution, self).__init__(**kwargs)
        with self.canvas.after:
            Color(1, 0, 0, 1)
            self.s_line = Line(points=[0, 0, 0, 0], width=2)
            Color(0, 1, 0, 1)
            self.aw_line = Line(points=[0, 0, 0, 0], width=2)
            Color(0, 0, 1, 1)
            self.tw_line = Line(points=[0, 0, 0, 0], width=2)

    def ORIGIN(self, side: str, angle: float) -> list:
        """Determines the origin for the graphic solution,
        depending of the wind side and angle.

        Args:
            side (str): The apparent wind side, which is relative to the ship.
            angle (float): The angle under which the apparent wind is meeting the ship.

        Returns:
            ORIGIN(list): The point from where the ship's and apparent wind vectors
                        are draws onto the canvas.
        """
        side = str(side)
        angle = float(angle)

        if angle <= 90:
            if side.lower() == "port":
                ORIGIN = [360, 200]
            elif side.lower() == "bow":
                ORIGIN = [250, 200]
            elif side.lower() == "starboard":
                ORIGIN = [120, 200]
        elif angle >= 90:
            if side.lower() == "port":
                ORIGIN = [360, 300]
            elif side.lower() == "stern":
                ORIGIN = [250, 300]
            elif side.lower() == "starboard":
                ORIGIN = [120, 300]

        return ORIGIN

    def show_popup(self, aw_positions, s_speed, graphic_origin):
        ORIGIN = graphic_origin
        drawing = GraphicSolution()
        drawing.ORIGIN = ORIGIN
        drawing.s_line.points = [ORIGIN[0], ORIGIN[1], ORIGIN[0],
                                 ORIGIN[1] + float(s_speed)]
        drawing.aw_line.points = [ORIGIN[0], ORIGIN[1], ORIGIN[0] + aw_positions[0],
                                  ORIGIN[1] + aw_positions[1]]
        drawing.tw_line.points = [ORIGIN[0], ORIGIN[1] + float(s_speed),
                                  ORIGIN[0] + aw_positions[0], ORIGIN[1] +
                                  aw_positions[1]]
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
            list: [angle, speed, side]
        """
        angle = float(angle)
        speed = float(speed)
        side = str(side)
        pos = [0, 0]
        alfa = 90 - angle

        if side.lower() == "port":
            if alfa < 0 or alfa > 0:
                pos[0] = round(- speed*cos(radians(alfa)), 1)
                pos[1] = round(speed * sin(radians(alfa)), 1)
            elif alfa == 0:
                pos[0] = - speed
                pos[1] = 0
        elif side.lower() == "starboard":
            if alfa < 0 or alfa > 0:
                pos[0] = round(speed*cos(radians(alfa)), 1)
                pos[1] = round(speed * sin(radians(alfa)), 1)
            elif alfa == 0:
                pos[0] = speed
                pos[1] = 0
        elif side.lower() == "bow":
            pos[0] = 0
            pos[1] = speed
        elif side.lower() == "stern":
            pos[0] = 0
            pos[1] = - speed
        return pos
