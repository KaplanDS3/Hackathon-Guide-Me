from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.config import Config

Window.size = (350, 600)

Config.set('graphics', 'resizable', True)


class Button_yes(App):
    def build(self):
        btn = Button(background_normal='button_yes.png',
                     size_hint=(.5, 0.1),
                     pos_hint={"x": 0.1, "y": 0.2}
                     )
        return btn


class FirstScreen(Widget):

    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        with self.canvas:
            # Color(0, 0, 0, 1)

            # Setting the size and position of canvas
            self.rect = Rectangle(source="asking.png",
                                  pos=self.center, size=self.size)

            # Update the canvas as the screen size change
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ask_screen(App):
    def build(self):
        return FirstScreen()


#root = Button_yes()
#root.run()
ask_screen().run()
