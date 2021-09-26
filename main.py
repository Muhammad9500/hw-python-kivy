from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.factory import Factory


class SuperButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.txt = Label()
        self.screen = screen
        self.goal = goal
        self.direction = direction

    def change_text(self, text):
        self.txt.text = text

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScr(Screen):
    def __init__(self, name="main", **kwargs):
        super().__init__(name=name, **kwargs)
        v1 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        h1 = BoxLayout()
        txt = Label(text="Выбери экран")
        v1.add_widget(SuperButton(self, direction='down', goal='first', text='1'))
        v1.add_widget(SuperButton(self, direction='up', goal='second', text='2'))
        v1.add_widget(SuperButton(self, direction='left', goal='third', text='3'))
        v1.add_widget(SuperButton(self, direction='right', goal='fourth', text='4'))
        h1.add_widget(txt)
        h1.add_widget(v1)
        self.add_widget(h1)


#
#
class FirstScr(Screen):
    def __init__(self, name="first", **kwargs):
        super().__init__(name=name, **kwargs)
        v1 = BoxLayout(orientation='vertical',
                       size_hint=(.5, .5),
                       pos_hint={'center_x': 0.75, 'center_y': 0.5})
        btn = Button(text='Экран 1', size_hint=(.5, 1), pos_hint={'right': 0})
        btn_back = SuperButton(self,
                               direction='up', goal='main', text='Назад', size_hint=(.5, 1))
        v1.add_widget(btn)
        v1.add_widget(btn_back)
        self.add_widget(v1)


class SecondScr(Screen):
    def __init__(self, name="second", **kwargs):
        super().__init__(name=name, **kwargs)
        layout1 = BoxLayout(orientation="vertical")
        layout2 = BoxLayout(orientation="horizontal")
        layout3 = BoxLayout()
        txtv = Label(text="Выбор: 2")
        input1 = TextInput(size_hint=(0.8, 0.13), pos_hint={'center_y': 0})
        txtinp = Label(text="Введите пароль:", pos_hint={'center_y': 0})
        btn11 = Button(text="ОК!", size_hint=(0.2, 0.50))
        btn22 = SuperButton(self, direction='down', goal='main', text='Назад', size_hint=(0.2, 0.50))
        layout1.add_widget(txtv)
        layout2.add_widget(txtinp)
        layout2.add_widget(input1)
        layout3.add_widget(btn11)
        layout3.add_widget(btn22)
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        self.add_widget(layout1)


class ThirdScr(Screen):
    def __init__(self, name="third", **kwargs):
        super().__init__(name=name, **kwargs)
        layout = BoxLayout()
        btncol = Button(text="белый фон", size_hint=(0.1, 0.20))
        btncol2 = Button(text="красный фон", size_hint=(0.1, 0.20))
        btnBack = SuperButton(self, direction='right', goal='main', text='Назад', size_hint=(0.1, 0.20))
        btncol.on_press = self.color
        btncol2.on_press = self.discolor
        layout.add_widget(btncol)
        layout.add_widget(btncol2)
        layout.add_widget(btnBack)
        self.add_widget(layout)

    def color(self):
        Window.clearcolor = (.9, .9, .9, 1)

    def discolor(self):
        Window.clearcolor = ([1, 0, 0, 1])


class FourthScr(Screen):
    def __init__(self, name="fourth", **kwargs):
        super().__init__(name=name, **kwargs)
        


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        return sm


app = MyApp()
app.run()
