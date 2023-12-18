from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

Window.size = (350, 600)


class FirstScreen(Widget):

    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        with self.canvas:
            # Color(0, 0, 0, 1)

            # Setting the size and position of canvas
            self.rect = Rectangle(source="no_alert.png",
                                  pos=self.center, size=self.size)

            # Update the canvas as the screen size change
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class no_alert(App):
    def build(self):
        return FirstScreen()
