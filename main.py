from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
import no_boom_shelter
import yes_boom_shelter
import no_alert
from kivy.core.window import Window

Window.size = (400, 700)


class Main():
    alarm = True
    hasBoomShelter = True
    if not alarm:
        no_alert.no_alert().run()
    else:
        if hasBoomShelter:
            yes_boom_shelter.yes_boom_shelter().run()
        else:
            no_boom_shelter.noBoomShelter().run()


if __name__ == '__main__':
    Main()
