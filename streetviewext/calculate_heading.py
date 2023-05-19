import math


def calculate_heading(lat1, lon1, lat2, lon2):
    # convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # calculate the difference between the longitudes
    dlon = lon2 - lon1

    # calculate the heading using the Haversine formula
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(
        dlon
    )
    heading = math.degrees(math.atan2(y, x))

    # normalize the heading to a value between 0 and 360 degrees
    if heading < 0:
        heading += 360

    return heading
