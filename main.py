import threading
import time
import json
from cryptography.fernet import Fernet
import base64

from kivy.app import App
from kivy.animation import Animation
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
    authorisation_label: lab1
    organization_logo: logo
    checkbox_img1: chck1_img
    checkbox_button: chkbx_but
    rememberme_label: rembme_lab
    checkbox_img2: chck2_img
    hint2_txt: hint2_txt
    hint_txt: hint_txt
    loading_logo: load_logo
    blure: blure

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
                root.switch_to_main_screen()
        
        Label:
            id: hint_txt
            text: "Почта МТУСИ"
            color: "grey"
            pos_hint: {"center_x": 0.34, "center_y": 0.56}
            font_size: root.font_checker()-5
            padding: root.padding_fit()
            font_name:"font.ttf"
            size_hint: 0.7, 0.055
            
        TextInput:
            id:TI1
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
        
        TextInput:
            id:TI2
            background_color: 0, 0, 0, 0
            canvas.before:
                Color:
                    rgba: self.bg_color
                RoundedRectangle:
                    size: self.size[0]*1.19, self.size[1]
                    pos: self.pos
                    radius: [self.radius] * 4
                Color:
                    rgba: self.border_color
                Line:
                    width: 1.2
                    rounded_rectangle: (self.x, self.y, self.size[0]*1.19, self.size[1], self.radius)
        
        
            bg_color: 1, 1, 1, 0
            radius: 50
            border_color: [0.2, 0, 0.7, 0.8]
            border_width: 1.2
            cursor_color: [0.2, 0, 0.7, 0.8]
            color: [0.2, 0, 0.7, 0.8]
            font_name:"font_medium.ttf"
            multiline: False
            pos_hint: {"center_x": 0.4450825, "center_y": 0.46}
            font_size: root.font_checker()
            padding: root.padding_fit()
            on_focus: root.on_focus(self, self.focus)
            password: True
            size_hint: 0.590165, 0.055
        
        Image:
            id: open_eye
            source: "eye_open.png"
            size_hint: 0.56, 0.046
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
            size_hint: 0.54, 0.044
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
        
        EffectWidget:
            id: blure
            size_hint: (1, 1)
            opacity: 0
            
            canvas.before:
                Color:
                    rgba: (0.9, 0.9, 0.9, 0.8)
                Rectangle:
                    pos:self.pos
                    size:self.size
            
    FloatLayout:
        Image:
            id: load_logo
            source: "loading_logo.png"
            size_hint: 0.35, 0.35
            pos_hint: {"center_x":0.5, "center_y": 0.5}
            opacity:0
            
            

<RoundedButton@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ''
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
            width: self.border_width
            rounded_rectangle: (self.x, self.y, self.width, self.height, self.radius)
    border_color: 0, 0, 0, 0
    border_width: 2
    radius: 50
    color: "white"
    bg_color: [0.2, 0, 0.6, 0.8]
    text: "Войти"
    font_size: 50
    font_name:"font.ttf"
    size_hint: 0.5, 0.1
    pos_hint: {"center_x": 0.5, "center_y": 0.3}
  
  
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


<MainScreen>:

    test_button:but2
    logout_button:log_out
    
    FloatLayout:
        canvas.before:
            Color:
                rgba: 1, 1, 1, 0.95
            Rectangle:
                size: self.size
                pos: self.pos
        
        Label:
            text: "Главное окно"
            font_size: 40
            font_name: "font.ttf"
            color: (.2, .2, .7, 1)
            pos_hint: {"center_x":0.5, "center_y":0.7}
            size_hint: 0.4, 0.09
        
        Button:
            id:but2
            text: "GO_BACK"
            size_hint: 0.4, 0.2
            pos_hint: {"center_x":0.5, "center_y":0.2}
            on_release: root.switch_to_login_screen()
        
        Button:
            id:log_out
            text: "LOG_OUT"
            size_hint: 0.4, 0.4
            pos_hint:{"center_x": 0.8, "center_y": 0.8}
            on_release: root.to_logout()
        
""")

class LoginWindow(Screen):

    text_input1 = ObjectProperty()
    text_input2 = ObjectProperty()
    login_button = ObjectProperty()
    authorisation_label = ObjectProperty()
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
    loading_logo = ObjectProperty()
    blure = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blure_active = False
        self.scheduled_event = None
        self.user_exists = False
        self.successfully_downloaded = False

        self.lang_authorization = 'Авторизация'
        self.lang_rememberme = 'Запомнить меня'
        self.lang_hinttxt = 'почта МТУСИ'
        self.lang_hinttxt2 = 'Пароль'
        self.lang_loginbutton = 'Войти'
        self.language()

        self.user_checking_thread = threading.Thread(target=self.user_checking)
        self.data_downloading_thread = threading.Thread(target=self.data_downloading)

        self.users_json = None
        self.config_json = None
        self.skip_login_window = False   # это настоящее значение чекбокса(не из конфига)

        self.key = None
        self.keyy = None

    def language(self):
        with open('config.json', "r") as file1:
            self.config_json = json.load(file1)

        if self.config_json['language']!='EN':
            self.lang_authorization = 'Авторизация'
            self.lang_rememberme = 'Запомнить меня'
            self.lang_hinttxt = 'почта МТУСИ'
            self.lang_hinttxt2 = 'Пароль'
            self.lang_loginbutton = 'Войти'
        else:
            self.lang_authorization = 'Authorisation'
            self.authorisation_label.text = 'Authorisation'
            self.lang_rememberme = 'Remember me'
            self.rememberme_label.text = 'Remember me'
            self.lang_hinttxt = 'MTUCI mail     ' #5 spaces
            self.hint_txt.text = 'MTUCI mail     '
            self.lang_hinttxt2 = '    Password' #1 tab
            self.hint2_txt.text = '    Password'
            self.lang_loginbutton = 'Enter'
            self.login_button.text = 'Enter'

    def switch_to_main_screen(self):
        if self.skip_login_window:
            pass                                                   #Написать сохранение личных данных

        if self.text_input1.text == "" or self.text_input2.text == "":
            if self.text_input1.text == "" and self.text_input2.text == "":
                self.empty_strings(False)
                self.empty_strings(True)
            else:
                self.empty_strings(self.text_input1.text == "")
            return 0

        self.loading_starter()

        self.user_checking_thread.start()


    def loading_process(self, start):
        blure_anim = Animation(opacity=1 if not self.blure_active else 0, duration=0.1)
        blure_anim.start(self.blure)

        self.text_input1.disabled = not self.text_input1.disabled
        self.text_input2.disabled = not self.text_input2.disabled
        self.eye_button.disabled = not self.eye_button.disabled
        self.checkbox_button.disabled = not self.checkbox_button.disabled
        self.login_button.disabled = not self.login_button.disabled

        pulsing_down = Animation(opacity = 0.3, size_hint=(.3, .3), duration=0.4)
        pulsing_up = Animation(opacity=1, size_hint=(0.35, 0.35), duration=0.3)

        def cycle(dt):
            pulsing_down.bind(on_complete=lambda *args: pulsing_up.start(self.loading_logo))
            pulsing_down.start(self.loading_logo)

        if start:
            if self.scheduled_event is None:
                self.loading_logo.pos_hint = {"center_x":0.5, "center_y":0.5}
                cycle(0)
                self.scheduled_event = Clock.schedule_interval(cycle, 1.4)
        else:
            if self.scheduled_event is not None:
                Clock.unschedule(self.scheduled_event)
                self.scheduled_event = None
                self.loading_logo.pos_hint = {"center_x":-0.5, "center_y":-0.5}


    def user_checking(self):
        with open('USERS.json', "r") as file:  #ЗАПРОС НА НАЛИЧИЕ ЮЗЕРА В БД
            self.users_json = json.load(file)

        for i in self.users_json['users']:
            if i['login']==self.text_input1.text and i['password']==self.text_input2.text:
                self.user_exists = True

        if self.user_exists:
            self.write_user(self.text_input1.text)
            with open('config.json', "r") as file1:
                self.config_json = json.load(file1)

            to_crypt_remembered = Crypter(self.text_input1.text, self.text_input2.text, 'remembered.txt', 'fontt.tff', user_id="user_id")
            to_crypt_current = Crypter(self.text_input1.text, self.text_input2.text, 'current_session.txt', 'font_high.tff', user_id="user_id2")

            self.write_rememberme(self.text_input1.text, to_crypt_current.password_enc(), "current_session.txt")
            to_crypt_current.file_enc()


            if self.skip_login_window:
                if not self.config_json['first_launch']:
                    try:
                        to_crypt_remembered.file_decr()
                    except:
                        pass
                    self.write_rememberme(self.text_input1.text, to_crypt_remembered.password_enc(),
                                          "remembered.txt")
                    to_crypt_remembered.file_enc()

                else:
                    self.write_rememberme(self.text_input1.text, to_crypt_remembered.password_enc(), "remembered.txt")
                    to_crypt_remembered.file_enc()

                self.config_json["checkbox_active"] = True
                self.config_json['first_launch'] = False
                with open("config.json", "w") as file2:
                    json.dump(self.config_json, file2)
            else:
                self.config_json['first_launch'] = False

                with open("config.json", "w") as file2:
                    json.dump(self.config_json, file2)

            Clock.schedule_once(self.start_downloading_thread)
        else:
            self.loading_starter()
            self.user_checking_thread = threading.Thread(target=self.user_checking)
            Clock.schedule_once(self.on_user_checking_complete)

    def data_downloading(self):
        time.sleep(1)  # СКАЧИВАНИЕ ДАННЫХ С БД
        self.successfully_downloaded = True
        if self.successfully_downloaded:
            Clock.schedule_once(self.on_data_downloading_complete)
        else:
            pass                           #ТУТ НАДО НАВЕРНО ВООБНОВИТЬ ЗАГРУЗКУ И ПРИ НЕСКОЛЬКИХ НЕУДАЧАХ ПУСКАТЬ ОФФЛАЙН СЕССИЮ

    def on_user_checking_complete(self, dt):
        if not self.user_exists:
            self.double_shaking()

    def on_data_downloading_complete(self, dt):
        self.data_downloading_thread = threading.Thread(target=self.data_downloading)
        self.loading_starter()
        self.manager.transition = SlideTransition(direction="down", duration=0.3)
        self.manager.current = 'main_sc'

    def start_downloading_thread(self, dt):
        self.user_checking_thread = threading.Thread(target=self.user_checking)
        self.data_downloading_thread = threading.Thread(target=self.data_downloading)
        self.data_downloading_thread.start()

    def on_resize(self, *args):
        self.blure_rect.size = (Window.size[0], Window.size[1])

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
                self.hint_txt.text = self.lang_hinttxt
        elif instance == self.text_input2:
            if value == 1 and instance.text=="":
                self.hint2_txt.text = ""
            elif value == 0 and instance.text=="":
                self.hint2_txt.text = self.lang_hinttxt2

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

    def empty_strings(self, first_is_empty):
        if first_is_empty:
            target = self.hint_txt
            poz1 = self.return_poz1()
            poz2 = self.return_poz2()
            poz3 = self.return_poz3()
        else:
            target = self.hint2_txt
            poz1 = {"center_x": 0.29}
            poz2 = {"center_x": 0.25}
            poz3 = {"center_x": 0.27}

        target.color = (230/255, 10/255, 30/255, .8)
        shake_login1 = Animation(pos_hint=poz1, duration=0.05)
        shake_login2 = Animation(pos_hint=poz2, duration=0.05)
        shake_login3 = Animation(pos_hint=poz1, duration=0.05)
        shake_login4 = Animation(pos_hint=poz2, duration=0.05)
        shake_login5 = Animation(pos_hint=poz3, duration=0.05)

        shake_login1.bind(on_complete=lambda *args: shake_login2.start(target))
        shake_login2.bind(on_complete=lambda *args: shake_login3.start(target))
        shake_login3.bind(on_complete=lambda *args: shake_login4.start(target))
        shake_login4.bind(on_complete=lambda *args: shake_login5.start(target))
        shake_login5.bind(on_complete=lambda *args: self.hint_txt_grey(target))
        shake_login1.start(target)


    def hint_txt_grey(self, target):
        target.color = "grey"

    def return_poz1(self):
        return {"center_x": 0.36}
    def return_poz2(self):
        return {"center_x": 0.32}
    def return_poz3(self):
        return {"center_x": 0.34}

    def double_shaking(self):
        self.text_input1.text = ""
        self.text_input2.text = ""
        self.empty_strings(True)
        self.empty_strings(False)
        self.hint_txt.text = self.lang_hinttxt
        self.hint2_txt.text = self.lang_hinttxt2


    def loading_starter(self):
        self.loading_process(not self.blure_active)
        self.blure_active = not self.blure_active

    def entry(self):
        self.text_input1.text = ""
        self.text_input2.text = ""
        self.hint_txt.text = self.lang_hinttxt
        self.hint2_txt.text = self.lang_hinttxt2

    def write_user(self, login):
        with open("users.txt", "r") as file4:
            already_exists = False
            userlist=[]
            for i in file4.readlines():
                if i!=0:
                    userlist.append(i)
                if i == login+"\n" or i == login:
                    already_exists = True
                    break
        if not already_exists:
            to_write = ""
            with open("users.txt", "w") as file:
                for i in range(len(userlist)):
                    to_write += f"{userlist[i]}"
                file.write(f"{to_write}\n{login}")

    def write_rememberme(self, login, password, where_to_write):
        password = base64.urlsafe_b64encode(password).decode('utf-8')
        with open(where_to_write, "w") as file5:
            file5.write(f"{login}\n{password}")



class MainScreen(Screen):
    test_button = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config_json = None

    def switch_to_login_screen(self):  #НИЖЕ ГДЕ КРИПТЫ ЭТО ВСЁ ТЕСТЫ. ЭТО ПРИМЕРНОЕ ВЗ-Е С КРИПТАНУТЫМ.
        """to_crypt2_remembered = Crypter(file='remembered.txt', where='fontt.tff', user_id="user_id")
        to_crypt2_current = Crypter(file='current_session.txt', where='font_high.tff', user_id="user_id2")


        try:
            to_crypt2_remembered.file_decr()
            print(f"REMEMBERED Логин: {to_crypt2_remembered.login}. Пароль: {to_crypt2_remembered.password_decr()}")
            to_crypt2_remembered.file_enc()
        except:
            pass

        to_crypt2_current.file_decr()
        print(f"CURRENT Логин: {to_crypt2_current.login}. Пароль: {to_crypt2_current.password_decr()}")
        to_crypt2_current.file_enc()"""

        firstwindow = self.manager.get_screen('login_sc')
        firstwindow.entry()
        self.manager.transition = SlideTransition(direction="up", duration=0.3)
        self.manager.current = 'login_sc'

    def to_logout(self):
        with open('remembered.txt', "r") as rem:
            is_empty = (rem.read()=="")
        if not is_empty:
            to_crypt2_remembered = Crypter(file='remembered.txt', where='fontt.tff', user_id="user_id")
            to_crypt2_remembered.file_decr()
            with open('remembered.txt', "w") as rem2:
                rem2.write("")
        to_crypt2_current = Crypter(file='current_session.txt', where='font_high.tff', user_id="user_id2")
        to_crypt2_current.file_decr()
        with open('current_session.txt', "w") as cur:
            cur.write("")

        with open("config.json", "r") as f:
            self.config_json = json.load(f)

        self.config_json['checkbox_active'] = False

        with open("config.json", "w") as ff:
            json.dump(self.config_json, ff)

        firstwindow = self.manager.get_screen('login_sc')
        firstwindow.entry()
        self.manager.transition = SlideTransition(direction="up", duration=0.3)
        self.manager.current = 'login_sc'



class Crypter:
    def __init__(self, login = None, password = None, file = None, where = None, user_id = None):
        self.key = None
        self.keyy = None
        self.file = file
        self.where = where
        self.login = login
        self.password = password
        self.config_json = None
        self.user_id = user_id

    def password_enc(self): #пароль
        self.key = Fernet.generate_key()
        f = Fernet(self.key)

        password = f.encrypt(self.password.encode('utf-8'))

        self.key = base64.urlsafe_b64encode(self.key).decode('utf-8')
        with open('user_id.json', "r") as file6:
            self.config_json = json.load(file6)
        self.config_json[self.user_id] = self.key
        with open("user_id.json", "w") as file321:
            json.dump(self.config_json, file321)

        return password

    def password_decr(self):
        with open(self.file, "r") as file7:
            file = file7.readlines()[1].strip()
        with open('user_id.json', "r") as file8:
            self.config_json = json.load(file8)
            user_id = self.config_json[self.user_id]
        user_id = base64.urlsafe_b64decode(user_id)
        file = base64.urlsafe_b64decode(file.encode('utf-8'))

        f = Fernet(user_id)
        new = f.decrypt(file)
        return new.decode('utf-8')

    def file_enc(self):
        self.keyy = Fernet.generate_key()

        with open(self.where, "wb") as file8:
            file8.write(self.keyy)

        f = Fernet(self.keyy)
        with open(self.file, "rb") as data:
            data = data.read()
        new_file = f.encrypt(data)
        with open(self.file, "wb") as file9:
            file9.write(new_file)

    def file_decr(self):
        with open(self.where, "rb") as file10:
            test = file10.read()
        f = Fernet(test)

        with open(self.file, "rb") as file11:
            new11 = file11.read()
        new11 = f.decrypt(new11)

        with open(self.file, "wb") as file12:
            file12.write(new11)

        with open(self.file, "rb") as file13:
            self.login = file13.readline().strip().decode('utf-8')



class MTUCIApp(App):
    def build(self):
        Window.set_icon('loading_logo.png')
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginWindow(name='login_sc'))
        screen_manager.add_widget(MainScreen(name='main_sc'))

        with open("config.json", "r") as q:
            config_json = json.load(q)
        if config_json['checkbox_active']:
            screen_manager.transition = SlideTransition(direction="up", duration=0.001)
            screen_manager.current = 'main_sc'

        return screen_manager

if __name__ == "__main__":
    MTUCIApp().run()