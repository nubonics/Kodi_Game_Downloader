from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


# LOCAL IMPORTS
from automated_file_downloader import afld


class MainMenu(GridLayout, Screen):
    def close_application(self, obj):
        App.get_running_app().stop()

    def callback(self, evt=None):
        return self.text_input.text

    def my_program(self, evt=None):
        afld(download_link=self.callback())

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        self.cols = 1
        self.padding = 200
        self.spacing = 20

        # Title
        self.add_widget(Label(text='Automated Kodi Game Downloader', font_size=30))

        # add textinput field
        self.text_input = TextInput(multiline=False, hint_text="Generator Link")
        self.add_widget(self.text_input)

        self.printbutton = Button(text='Save')
        self.printbutton.bind(on_press=self.callback)
        self.add_widget(self.printbutton)

        # add buttons
        self.add_widget(Button(text='Start', on_press=self.my_program))
        self.add_widget(Button(text='QUIT ~> Don\'t press this while running...', on_press=self.close_application))


class AKGD_GUI(App):
    def build(self):
        self.title = "Automated Kodi Game Downloader"
        return sm


if __name__ == '__main__':
    Config.set('graphics', 'resizable', True)
    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '500')
    Config.set('graphics', 'fullscreen', '0')
    Window.size = (1000, 1000)
    Config.write()
    sm = ScreenManager(transition=FadeTransition())
    sm.add_widget(MainMenu(name='MainMenu'))
    AKGD_GUI().run()
