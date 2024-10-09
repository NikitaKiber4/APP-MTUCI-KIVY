from kivy.app import App

from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder

#В БИЛДОЗЕР ЕЩЕ ДОБАВИТЬ ffpyplayer (requirements)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Builder.load_string("""


<LoginWindow>:
    login_button: but1
    text_input1: TI1
    text_input2: TI2
    login_label: lab1
    organization_logo: logo
    check_box1: chk_bx1
    
    FloatLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 0.95
            Rectangle:
                size: self.size
                pos: self.pos
        
        LoginBorder:
            id: lb1
        
        Image:
            id: logo
            source: "logo.png"
            pos_hint: {"center_x": 0.5, "center_y": 0.88}
            size_hint: 0.6, 0.6
        
        CCheckbox:
            id: chk_bx1
        
        Label:
            pos_hint: {"center_x":0.44, "center_y":0.39}
            size_hint: 0.05, 0.05
            text: "Запомнить меня"
            color: [0.3, 0, 0.7, 0.8]
            font_size:30
            font_name: "font.ttf"
    
        
        Label:
            id: lab1
            font_name: "font.ttf"
            text: "Авторизация"
            font_size: 60
            color: [0.2, 0, 0.7, 0.8]
            pos_hint: {"center_x": 0.5, "center_y": 0.66}

        RoundedButton:
            id:but1
            on_press: root.switch_to_load_screen()

        RoundedTextInput:
            id:TI1
            pos_hint: {"center_x": 0.5, "center_y": 0.56}

        RoundedTextInput:
            id:TI2
            pos_hint: {"center_x": 0.5, "center_y": 0.46}

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


<LoginBorder@Widget>:
    background_color: 0, 0, 0, 0
    background_normal: ""
    canvas:
        Color:
            rgba: self.border_color
        Line:
            width: self.border_width
            rounded_rectangle: (self.x + self.width/9, self.y + self.height/5.5, self.width*7/9, self.height*3/5.5, self.radius)

    radius: 50
    border_width: 3
    border_color: [0.2, 0, 0.7, 0.8]


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
    border_width: 2
    bg_color: 0, 1, 0, 0.1
    radius: 50
    color: "white"
    bg_color: [0.2, 0, 0.6, 0.8]
    text: "Войти"
    font_size: 50
    font_name: "font.ttf"
    size_hint: 0.62, 0.1
    pos_hint: {"center_x": 0.5, "center_y": 0.3}

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
    border_color: [0.2, 0, 0.7, 0.8]
    border_width: 1.2
    cursor_color: [0.2, 0, 0.7, 0.8]
    padding:26
    color: [0.2, 0, 0.7, 0.8]
    font_size: 50
    font_name: "font.ttf"
    size_hint: 0.7, 0.055

<CCheckbox@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ""
    pos_hint: {"center_x":0.26, "center_y":0.39}
    size_hint: 0.08, 0.04
    canvas.before:
        Color:
            rgba: self.border_color
        Line:
            width: self.border_width
            rounded_rectangle: (self.x, self.y, self.width, self.height, self.radius)
    
    border_color: [150/255, 150/255, 150/255, 1]
    radius: 15
    border_width: 1.5
        
""")


class LoginWindow(Screen):
    text_input1 = ObjectProperty()
    text_input2 = ObjectProperty()
    login_button = ObjectProperty()
    login_label = ObjectProperty()
    login_border = ObjectProperty()
    organization_logo = ObjectProperty()
    check_box1 = ObjectProperty()


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