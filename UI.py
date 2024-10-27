from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import OneLineIconListItem
from kivymd.icon_definitions import md_icons

from conver_text import speaker
from conver_text import tts

speak = False

text_for_speach : str

genders = {'man' : 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0',
           'woman' : "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
           'rus' : 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'}
gender = 'men'
language = 'ru'
volume = 1
speed = 100


KV = '''
BoxLayout:
    padding: "10dp"

    
    
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            orientation: "horizontal"
            MDLabel:
                text: "Громкость"
                halign: "center"
                pos_hint: {"center_x": .5,"center_y": .5}
            
            MDSlider:
                min: 0
                max: 120
                value: 100
                pos_hint: {"center_x": 1}
                on_value: app.set_volume_voise(self.value)
        BoxLayout:
            orientation: "horizontal"
            MDLabel:
                text: "Скорость"
                halign: "center"
                pos_hint: {"center_x": .5,"center_y": .5}
            
            MDSlider:
                min: 0
                max: 200
                value: 100
                pos_hint: {"center_x": 1}
                on_value: app.set_speed_voise(self.value)
        
        BoxLayout:
            orientation: "horizontal"
            MDTextField:
                id: text_field_error
                mode: "rectangle"
                color_mode: 'custom'
                hint_text: "Введите текст"
                line_color_focus: .69, .63, 0.00, 0.62
                line_color_normal: app.theme_cls.accent_color
                pos_hint: {"down_y": 1}
                multiline: False
                on_text_validate: app.on_enter()
            MDIconButton:
                icon: "volume-high"
                style: "tonal"
                theme_font_size: "Custom"
                font_size: "48sp"
                radius: [self.height / 2.1, ]
                size_hint: None, None
                size: "76dp", "76dp"
                on_press: app.say_hello()
            
'''

def set_text_for_speach(txt: str):
    return txt

class Test(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True


    def set_volume_voise(self, value):
        global volume
        volume =  value #int(self.root.ids.ibi_value.text)
        tts.setProperty('volume', volume/100)

    def set_speed_voise(self, spd):
        global speed
        speed =  spd #int(self.root.ids.ibi_value.text)
        tts.setProperty('rate', speed)


    def say_hello(self):
        global text_for_speach
        speaker.speak(txt=text_for_speach)


    def on_enter(self):
        global text_for_speach
        text = self.root.ids.text_field_error.text
        # self.list.append(text)
        # for i in range(len(self.list)):
        #     self.item = OneLineListItem(text=f"{self.list[i]}")
        #     self.root.ids.contaniner.add_widget(self.item)
        text_for_speach = text
        speaker.speak(txt=text_for_speach)




Test().run()
