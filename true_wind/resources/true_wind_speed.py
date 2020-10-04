# true_wind_speed.py

# t_w_speed:
# represens True Wind Speed (TWS) and is the actual speed of the wind over the water.
# Generally it is expressed in knots.
########################################################################################
# v_speed:
# represents vessel speed and is usually the vessel speed over ground (SOG)
# as measured with the GPS.

# a_w_speed:
# represents Apparent Wind Speed (AWS) and is the speed of the wind in knots
# that is measured from a moving vessel. It is a combination of the true wind speed
# and the effective wind created by the vessel's motion.

# a_w_angle:
# represents Apparent wind angle (AWA) and is the direction of the apparent wind
# relative to the head of the vessel,
# usually listed as port or starboard. It varies from 0° (wind on the bow),
# through 90° (wind on the beam),
# on around to 180° (wind on the stern).

from math import cos, pow, radians, sqrt


def t_w_speed(v_speed: float, a_w_speed: float, a_w_angle: float) -> float:
    """Returns the true wind speed (TWS), which is the actual speed of the wind over
    the water.

    Args:
        v_speed (float): vessel speed over ground (SOG) as measured with the GPS.
        a_w_speed (float): apparent wind speed (AWS).
        a_w_angle (float): apparent wind angle (AWA).

    Returns:
        float: actual speed of the wind over the water (TWS).
    """

    v_speed = float(v_speed)
    a_w_speed = float(a_w_speed)
    a_w_angle = float(a_w_angle)

    if 0 <= a_w_angle <= 180:

        t_w_speed = sqrt(
            pow(v_speed, 2)
            + pow(a_w_speed, 2)
            - (2 * v_speed * a_w_speed * cos(radians(a_w_angle)))
        )

        return round(t_w_speed, 1)
    else:
        return "Apparent wind angle (a_w_angle) values are between 0 - 180"
