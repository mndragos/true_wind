# true_wind_angle.py

# t_w_angle:
# represents true wind angle (TWA) and is the direction of the true wind
# relative to the head of the vessel, usually listed as port or starboard.
# It varies from 0° (wind on the bow), through 90° (wind on the beam),
# on around to 180° (wind on the stern).
##########################################################################
# a_w_speed:
# represents Apparent Wind Speed (AWS) and is the speed of the wind in knots
# that is measured from a moving vessel. It is a combination of the true wind speed
#  and the effective wind we create with our motion.

# t_w_speed:
# represens True Wind Speed (TWS) and is the actual speed of the wind over the water.
# Generally it is expressed in knots.

# v_speed:
# represents vessel speed and is usually the vessel speed over ground (SOG)
# as measured with the GPS.

from math import acos, degrees


def t_w_angle(a_w_speed: float, t_w_speed: float, v_speed: float) -> float:
    """Returns the true wind angle (TWA) and is the direction of the true wind
    relative to the head of the vessel.

    Args:
        a_w_speed (float): apparent wind speed (AWS).
        t_w_speed (float): actual speed of the wind over the water (TWS).
        v_speed (float): vessel speed over ground (SOG) as measured with the GPS.

    Returns:
        float: true wind angle (TWA).
    """
    a_w_speed = float(a_w_speed)
    t_w_speed = float(t_w_speed)
    v_speed = float(v_speed)

    inverse_angle = (pow(a_w_speed, 2) - pow(t_w_speed, 2) - pow(v_speed, 2)) / (
        2 * t_w_speed * v_speed
    )
    t_w_angle = degrees(acos(inverse_angle))

    return round(t_w_angle, 1)
