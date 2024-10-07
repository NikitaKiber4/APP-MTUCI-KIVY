from kivy.app import App

from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder

import cv2

#В БИЛДОЗЕР ЕЩЕ ДОБАВИТЬ ffpyplayer (requirements)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Builder.load_string("""


<LoginWindow>:
    login_button: but1
    text_input1: TI1
    text_input2: TI2
    login_label: lab1
    FloatLayout:
        Label:
            id: lab1
            text: "Авторизация"
            font_size: 60
            color: 1, 1, 1, 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.7}

        RoundedButton:
            id:but1
            color: "black"
            bg_color: [0.2, 0, 0.7, 0.8]
            text: "Войти"
            size_hint: 0.6, 0.09
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            on_press: root.switch_to_load_screen()

        RoundedTextInput:
            id:TI1
            pos_hint: {"center_x": 0.5, "center_y": 0.6}

        RoundedTextInput:
            id:TI2
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

<LoadingScreen>:
    test_button:but2
    FloatLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 0.95
            Rectangle:
                size: self.size
                pos: self.pos
        Button:
            id:but2
            size_hint: 0.5, 0.5
            on_release: root.switch_to_login_screen()

<RoundedButton@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ''
    canvas.before:
        Color:
            rgba: self.bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [self.radius] * 4 #b

        Color:
            rgba: self.border_color
        Line:
            width: self.border_width
            rounded_rectangle: (self.x, self.y, self.width, self.height, self.radius)
    border_color: 0, 0, 0, 1
    border_width: 1.5

    bg_color: 0, 1, 0, 0.1
    radius: 50

<RoundedTextInput@TextInput>:
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: self.bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [self.radius] * 4

        Color:
            rgba: self.border_color
        Line:
            width: 1.2   #СЕЛФ ПИДАРАС НЕ РАБОТАЕТ
            rounded_rectangle: (self.x, self.y, self.width, self.height, self.radius)

    bg_color: 1, 1, 1, 0
    radius: 50
    border_color: 1, 1, 1, 1
    border_width: 1.2
    cursor_color: "white"
    padding:20
    color: "white"
    font_size: 50
    size_hint: 0.7, 0.05
""")


class LoginWindow(Screen):
    text_input1 = ObjectProperty()
    text_input2 = ObjectProperty()
    login_button = ObjectProperty()
    login_label = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_load_screen(self):
        self.manager.transition = SlideTransition(direction="down")
        self.manager.current = 'load_sc'


class LoadingScreen(Screen):
    test_button = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_login_screen(self):
        self.manager.transition = SlideTransition(direction="up")
        self.manager.current = 'login_sc'


class MTUCIApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginWindow(name='login_sc'))
        screen_manager.add_widget(LoadingScreen(name='load_sc'))

        return screen_manager


if __name__ == "__main__":
    MTUCIApp().run()
