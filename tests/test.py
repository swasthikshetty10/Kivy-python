from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.layout import Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter 
from kivy.uix.textinput import TextInput 
from kivy.uix.floatlayout import FloatLayout  

    
class testapp(App):
    def build(self):
        b = BoxLayout(orientation ='vertical') 
        # Adding the text input 
        text = TextInput(font_size = 30, 
                      size_hint_y = None, 
                      height = 70) 
        f = FloatLayout() 
        s = Scatter() 
        l = Label(text ="Hello !", 
                  font_size = 50) 
        b.add_widget(self.send())
        btnlayout = AnchorLayout(
            
            anchor_y = 'bottom',
            
        )
        text.bind(text = l.setter('text')) 
        btnlayout.add_widget(text)
        b.add_widget(btnlayout)
        return b

    def send(self):
        btn = Button(
            text = "send",
            font_size=14,
            background_color = (1,1,1,1),
            size = (20 ,20),
            size_hint = (.2,.2),
            pos = (0 , 200)
            
        )
        btn.bind(on_press = self.callback) 
        return btn
    def callback(self, event):
        print(f'Button is is being pressed')


hw = testapp()
hw.run()