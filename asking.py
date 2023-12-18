from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.button import Button
import no_alert
from kivy.config import Config

Window.size = (350, 600)

Config.set('graphics', 'resizable', True)


class FirstScreen(Widget):

    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        with self.canvas:
            # Color(0, 0, 0, 1)

            # Setting the size and position of canvas
            self.rect = Rectangle(source="asking.png",
                                  pos=self.center, size=self.size)

            btn_yes = Button(background_normal='button_yes.png',
                             size=(300, 70),
                             pos=(70, 170)
                             )

            btn_no = Button(background_normal='no_button.png',
                            size=(320, 80),
                            pos=(65, 80)
                            )

            btn_yes.bind(on_press=self.finished())
            return btn_yes



    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def finished(self):
        no_alert.no_alert().run()


class ask_screen(App):
    def build(self):
        return FirstScreen()


# root = Button_yes()
# root.run()
ask_screen().run()
