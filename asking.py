from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window
import kivy.uix.button as Button

Window.size = (350, 600)


class Background(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class ask_screen(App):
    def build(self):
        return Background()


if __name__ == '__main__':
    ask_screen().run()
