# true_wind_direction.py

# t_w_direction:
# represents the true wind direction (TWD) and is generally the true wind
# blowing across the land or across the water.It is always the direction
# from which the wind is blowing. A north wind blows from the north,
# toward the south.
#########################################################################
# heading:
# represents the true heading of the vessel, that is, if steering a
# compass course, correct the compass course first with the variation so you can
# input here your actual true heading at the time the wind data was collected.

# v_side:
# represents the observed side from which the aparent wind is blowing.

# t_w_angle:
# represents true wind angle (TWA) and is the direction of the true wind
# relative to the head of the vessel


def t_w_direction(heading: float, v_side: str, t_w_angle: float) -> float:
    """Returns the true wind direction (TWD) and is generally the true wind
    blowing across the land or across the water.

    Args:
        heading (float): true heading of the vessel (HDG).
        v_side (str): what side is observed the apparent wind (Port or Starboard)
        t_w_angle (float): true wind angle (TWA).

    Returns:
        float: true wind direction (TWD).
    """

    heading = float(heading)
    v_side = str(v_side)
    t_w_angle = float(t_w_angle)

    if v_side.lower() == "port":
        return heading - t_w_angle
    elif v_side.lower() == "starboard":
        return heading + t_w_angle
    elif v_side.lower() == "bow":
        return heading
    elif v_side.lower() == "stern":
        return heading + 180


def t_w_reduction(t_w_direction: float) -> float:
    """Returns the reduced true wind direction.First is substacting (Port)
    or adding (Starboard) the true wind angle to the ship's HDG, then if from
    calculus is returned a greater value than 360°, a further substraction is made.
    Example:
    for a TWD of 410° the reduced TWD= 410°-360°= 50°, so the final TWD is 50°.

    Args:
        t_w_direction (float): true wind direction (TWD)

    Returns:
        float: reduced true wind direction (TWD)
    """

    if t_w_direction > 360:
        return round((t_w_direction - 360), 1)
    elif t_w_direction < 0:
        return round((360 + t_w_direction), 1)
    elif t_w_direction == 360:
        return float(0)
    elif t_w_direction < 360:
        return round(t_w_direction, 1)


def t_w_pretty_view(t_w_reduction: float) -> str:
    """Returns a string formated as degree.
    example: takes float 3.0 and returns 003.0°
    Args:
        t_w_reduction (float): true wind direction value between 0 - 360

    Returns:
        string: returns a string with the same value, but represended like  in
            the example.
    """
    DEG = "\u00b0"  # degree sign
    t_w_reduction = f"{t_w_reduction}{DEG}"

    return t_w_reduction.zfill(6)
