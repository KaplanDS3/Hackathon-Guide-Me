from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
import google_maps
import time

Window.size = (350, 600)


class FirstScreen(Widget):

    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        with self.canvas:
            # Color(0, 0, 0, 1)

            # Setting the size and position of canvas
            self.rect = Rectangle(source="redalert2.png",
                                  pos=self.center, size=self.size)
            origin_coordinates = (32.178176, 34.8520448)
            destination_coordinates = (32.1769302, 34.8545654)
            bomb_in_tlv = (32.1466254, 34.8820875)
            if google_maps.return_distance(origin_coordinates, destination_coordinates) > 65:
                google_maps.open_map(origin_coordinates, destination_coordinates)

            # Update the canvas as the screen size change
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class yes_boom_shelter(App):
    def build(self):
        return FirstScreen()
