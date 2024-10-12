from kivy.app import App

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_string("""


<LoginWindow>:
    
    login_button: but1
    text_input1: TI1
    text_input2: TI2
    login_label: lab1
    organization_logo: logo
    check_box1: chk_bx1
    hint2_txt: hint2_txt
    hint_txt: hint_txt

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

        Label:
            id: lab1
            text: "Авторизация"
            font_size: 60
            color: [0.2, 0, 0.7, 0.8]
            pos_hint: {"center_x": 0.5, "center_y": 0.66}
            font_name:"font.ttf"

        RoundedButton:
            id:but1
            on_press: 
                self.bg_color =  [0.4, 0, 0.8, 0.8]
                root.button_blure()
            on_release:
                self.bg_color =  [0.2, 0, 0.7, 0.8]
                root.switch_to_load_screen()
        
        Label:
            id: hint_txt
            text: "Почта МТУСИ"
            color: "grey"
            pos_hint: {"center_x": 0.34, "center_y": 0.56}
            font_size: root.font_checker()-5
            padding: root.padding_fit()
            font_name:"font.ttf"
            size_hint: 0.7, 0.055
            
        RoundedTextInput:
            id:TI1
            pos_hint: {"center_x": 0.5, "center_y": 0.56}
            font_size: root.font_checker()
            padding: root.padding_fit()
            on_focus: root.on_focus(self, self.focus)
            
        Label:
            id: hint2_txt
            text: "Пароль"
            color: "grey"
            pos_hint: {"center_x": 0.27, "center_y": 0.46}
            font_size: root.font_checker()-5
            padding: root.padding_fit()
            font_name:"font.ttf"
            size_hint: 0.7, 0.055
        
        RoundedTextInput:
            id:TI2
            pos_hint: {"center_x": 0.5, "center_y": 0.46}
            font_size: root.font_checker()
            padding: root.padding_fit()
            on_focus: root.on_focus(self, self.focus)
            
            
    BoxLayout:
        Label:
            size_hint: 0.0028, 0.05
            pos_hint: {"center_y":0.39}

        CCheckbox:
            id: chk_bx1

        Label:
            size_hint: 0.0005, 0.05
            pos_hint: {"center_y":0.39}

        Label:
            pos_hint: {"x": root.return_label_x(), "center_y":0.39}
            size_hint: 0.005, 0.03
            text: "Запомнить меня"
            color: [0.3, 0, 0.7, 0.8]
            font_size:30
            font_name:"font.ttf"

        Label:
            size_hint: 0.005, 0.05
            pos_hint: {"center_y":0.39}

<CCheckbox@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ""
    pos_hint: {"center_y":0.39}
    size_hint: 0.0016, 0.04
    canvas.before:
        Color:
            rgba: self.border_color
        Line:
            width: self.border_width
            rounded_rectangle: (self.x, self.y, self.width, self.height, self.radius)

    border_color: [150/255, 150/255, 150/255, 1]
    radius: 15
    border_width: 1.5

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
    font_name:"font.ttf"
    size_hint: 0.5, 0.1
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
    color: [0.2, 0, 0.7, 0.8]
    font_name:"font.ttf"
    size_hint: 0.7, 0.055
    multiline: False
    
    

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


""")


class LoginWindow(Screen):

    text_input1 = ObjectProperty()
    text_input2 = ObjectProperty()
    login_button = ObjectProperty()
    login_label = ObjectProperty()
    login_border = ObjectProperty()
    organization_logo = ObjectProperty()
    check_box1 = ObjectProperty()
    hint_txt = ObjectProperty()
    hint2_txt = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_load_screen(self):
        self.manager.transition = SlideTransition(direction="down")
        self.manager.current = 'load_sc'

    def button_blure(self):
        Clock.schedule_once(lambda dt: self.return_button_color(), 0.5)

    def return_button_color(self):
        self.login_button.bg_color = [0.2, 0, 0.7, 0.8]

    def return_label_x(self):
        return int((0.55+0.08)*Window.size[0])/1000

    def padding_fit(self):
        wwidth = Window.size[1]
        approx_wide = 650
        padding = 2
        while wwidth > approx_wide:
            approx_wide += 100
            padding += 1.5
        return padding

    def font_checker(self):
        if Window.size[1]<1600:
            return 40
        else:
            return 50

    def on_focus(self, instance, value):
        if instance == self.text_input1:
            if value == 1 and instance.text=="":
                self.hint_txt.text = ""
            elif value == 0 and instance.text=="":
                self.hint_txt.text = "Почта МТУСИ"
        elif instance == self.text_input2:
            if value == 1 and instance.text=="":
                self.hint2_txt.text = ""
            elif value == 0 and instance.text=="":
                self.hint2_txt.text = "Пароль"




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