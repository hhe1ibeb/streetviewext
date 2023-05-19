from .calculate_heading import calculate_heading

from streetview import search_panoramas
from streetview import get_streetview
from streetview import get_panorama
import googlemaps
import polyline
from shapely.geometry import LineString
from PIL import Image


def sv_among_route(
    origin: str,
    destination: str,
    mode: str,
    dir_key: str,
    street_key: str,
    save_destination: str = "",
    width: int = 640,
    height: int = 640,
    fov: int = 120,
    pitch: int = 0,
):
    gmaps = googlemaps.Client(key=dir_key)

    if mode not in ["driving", "walking", "bicycling", "transit", "flight"]:
        print("Mode not allowed")
        return

    directions_result = gmaps.directions(origin, destination, mode=mode)
    polyline_str = directions_result[0]["overview_polyline"]["points"]
    coords = polyline.decode(polyline_str)
    line = LineString(coords)
    simplified_line = line.simplify(tolerance=0, preserve_topology=False)
    simplified_coords = list(simplified_line.coords)

    for i in range(len(simplified_coords) - 1):
        pos1 = simplified_coords[i]
        pos2 = simplified_coords[i + 1]
        lat, lon = pos1[0], pos1[1]
        heading = calculate_heading(pos1[0], pos1[1], pos2[0], pos2[1])

        panoids = search_panoramas(lat, lon)
        pano = panoids[-1]

        image = get_streetview(
            pano.pano_id, street_key, width, height, heading, fov, pitch
        )
        output_path = "{0}/{1}.jpg".format(save_destination, str(i + 1))
        image.save(output_path, "jpeg")
    return


def panorama_among_route(
    origin: str,
    destination: str,
    mode: str,
    dir_key: str,
    save_destination: str = "",
):
    gmaps = googlemaps.Client(key=dir_key)

    if mode not in ["driving", "walking", "bicycling", "transit", "flight"]:
        print("Mode not allowed")
        return

    directions_result = gmaps.directions(origin, destination, mode=mode)
    polyline_str = directions_result[0]["overview_polyline"]["points"]
    coords = polyline.decode(polyline_str)
    line = LineString(coords)
    simplified_line = line.simplify(tolerance=0, preserve_topology=False)
    simplified_coords = list(simplified_line.coords)

    for i in range(len(simplified_coords) - 1):
        pos = simplified_coords[i]
        lat, lon = pos[0], pos[1]

        panoids = search_panoramas(lat, lon)
        pano = panoids[-1]
        image = get_panorama(pano.pano_id)
        output_path = "{0}/{1}.jpg".format(save_destination, str(i + 1))
        image.save(output_path, "jpeg")
    return
