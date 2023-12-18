from geopy.distance import geodesic
import webbrowser

def return_distance(origin_coordinates, destination_coordinates):
        meter = geodesic(origin_coordinates, destination_coordinates).m
        return meter


def open_map(origin_coordinates, destination_coordinates):

        return webbrowser.open(f"https://www.google.com/maps/dir/{origin_coordinates[0]},{origin_coordinates[1]}/%D7%9E%D7%A7%D7%9C%D7%98,%E2%80%AD/@{destination_coordinates[0]},{destination_coordinates[1]}z/am=t/data=!4m9!4m8!1m1!4e1!1m5!1m1!1s0x151d47fb2625134d:0xf89a0a10e5d3f51d!2m2!1d{origin_coordinates[1]}!2d{destination_coordinates[0]}?hl=iw&entry=ttu")


def check_destanetion_correcct(origin_coordinates, destination_coordinates):
    if return_distance(origin_coordinates, destination_coordinates) < 65:
        return True
    return False





if __name__ == '__main__':
    # Example coordinates (replace with your own)
    origin_coordinates = (32.178176, 34.8520448)
    destination_coordinates = (32.1769302, 34.8545654)
    bomb_in_tlv = (32.1466254, 34.8820875)
    if return_distance(origin_coordinates,destination_coordinates)>65:
        open_map(origin_coordinates,destination_coordinates)





