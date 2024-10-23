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
    open_eye: open_eye
    closed_eye: closed_eye
    eye_button: eye_bttn
    login_label: lab1
    organization_logo: logo
    checkbox_img1: chck1_img
    checkbox_button: chkbx_but
    rememberme_label: rembme_lab
    checkbox_img2: chck2_img
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
            pos_hint: {"center_x": 0.48, "center_y": 0.88}
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
            password: True
        
        Image:
            id: open_eye
            source: "eye_open.png"
            size_hint: 0.6, 0.05
            pos_hint: {"center_x": 0.78, "center_y": 0.46}
            opacity: 0
            
        Button:
            opacity: 0
            id: eye_bttn
            size_hint: 0.13, 0.06
            pos_hint: {"center_x": 0.78, "center_y": 0.46}
            on_release: root.eye_switch()
        
        Image:
            id: closed_eye
            source: "eye_close.png"
            size_hint: 0.58, 0.048
            pos_hint: {"center_x": 0.78, "center_y": 0.46}
            opacity: 1
        
        Image:
            id:chck1_img
            source: "CheckBpx1.png"
            pos_hint: {"center_y":0.38, "center_x":0.2}
            size_hint: 0.09, 0.09
        
        Button:
            id: chkbx_but
            background_color: 0, 0, 1, 0
            background_normal: ""
            pos_hint: {"center_y":0.38, "center_x":0.2}
            size_hint: 0.08, 0.076
            on_release:
                root.checkbox_switch()
        
        Image:
            id:chck2_img
            source: "CheckBpx2.png"
            pos_hint: {"center_y":0.38, "center_x":0.2}
            size_hint: 0.09, 0.09
            opacity: 0
        
        Label:
            id: rembme_lab
            font_name: "font.ttf"
            font_size: root.font_checker()-10
            text: "Запомнить меня"
            color: (30/255, 11/255, 156/255, 1)
            pos_hint: {"center_y":0.38, "center_x":0.44}
            
    


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
    border_color: 0, 0, 0, 0
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
    font_name:"font_medium.ttf"
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
    checkbox_img1: ObjectProperty()
    checkbox_button: ObjectProperty()
    rememberme_label: ObjectProperty()
    checkbox_img2: ObjectProperty()
    hint_txt = ObjectProperty()
    hint2_txt = ObjectProperty()
    open_eye = ObjectProperty()
    closed_eye = ObjectProperty()
    eye_button = ObjectProperty()

    skip_login_window = False


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_load_screen(self):
        if self.skip_login_window:
            pass                                                        #Написать сохранение личных данных
        self.manager.transition = SlideTransition(direction="down", duration=0.3)
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

    def checkbox_switch(self):
        if self.checkbox_img2.opacity==0:
            self.checkbox_img2.opacity=1
            self.skip_login_window = True
        else:
            self.checkbox_img2.opacity = 0
            self.skip_login_window = False

    def eye_switch(self):
        if self.open_eye.opacity == 1:
            self.open_eye.opacity = 0
            self.closed_eye.opacity = 1
            self.text_input2.password = True
        else:
            self.open_eye.opacity = 1
            self.closed_eye.opacity = 0
            self.text_input2.password = False



class LoadingScreen(Screen):
    test_button = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to_login_screen(self):
        self.manager.transition = SlideTransition(direction="up", duration=0.3)
        self.manager.current = 'login_sc'


class MTUCIApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginWindow(name='login_sc'))
        screen_manager.add_widget(LoadingScreen(name='load_sc'))

        return screen_manager

if __name__ == "__main__":
    MTUCIApp().run()