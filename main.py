from kivy import *
from kivy.app import *
from kivy.uix.label import *
from kivy.uix.button import *


class Main(App):
    def build(self):
        return Button(text="shalom 2", size_hint=(0.5, 0.5))


Main().run()
