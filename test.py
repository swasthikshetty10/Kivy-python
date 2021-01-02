from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
class Helloworld(App):
    def build(self):
        layout = AnchorLayout(   #anchor layout helps to lay out the widgit
            anchor_x = 'right',
            anchor_y = 'bottom',
        )
        Button()
        btn1 = Button(
            text = "Hello world",
            size_hint = (.2,.2),
            background_color = (0.0,25.86,1.0),
            color = (0,0,0,1)
            
        )
        layout.add_widget(btn1)
        return layout





hw = Helloworld()
hw.run()