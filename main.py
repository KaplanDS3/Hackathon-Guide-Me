import kivy
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.size = (400, 700)


class MyGrid(Widget):
    pass


class Main(MDApp):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    Main().run()
