from kivy.app import App
from kivy.core import text
from kivy.uix.behaviors import button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.layout import Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter 
from kivy.uix.textinput import TextInput 
from kivy.uix.floatlayout import FloatLayout  

    
# layout = BoxLayout(padding=10, orientation='vertical')
#         self.lbl1 = Label(text="test")
#         layout.add_widget(self.lbl1)
#         #creating text field
#         self.txt1 = TextInput(font_size = 30, 
#                       size_hint_y = None, 
#                       height = 70) 
#         # creating button
#         btn1 = self.send()
#         btn1.bind(on_press=self.buttonClicked)
#         bottomtextlayout = AnchorLayout(
            
#             anchor_y = 'bottom'
#         )
#         typeandsend = GridLayout(
#                         cols=1, 
#                         row_force_default=True, 
#                                 )
#         typeandsend.add_widget(self.txt1)
#         typeandsend.add_widget(btn1)
#         bottomtextlayout.add_widget(typeandsend)
#         layout.add_widget(bottomtextlayout)


class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')

        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(font_size = 30, 
                      size_hint_y = None, 
                      height = 70) 
        
        btn1 = self.send()
        
        btnlayout = AnchorLayout(
            
            anchor_y = 'bottom',
            
        )
        typeandsend = GridLayout(
                         cols=2, 
                         rows = 1,
                         row_default_height=10,
                         
                                 )
        
        typeandsend.add_widget(self.txt1)
        typeandsend.add_widget(btn1)
        btnlayout.add_widget(typeandsend)
        layout.add_widget(btnlayout)
        
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "You wrote " + self.txt1.text
        print(self.lbl1.text)
    def send(self ):
        btn = Button(
            text = "send",
            color = (1,1,1,1),
            size_hint_y = None, 
            height = 70,
            background_color = (0,.4,1,1),
            size_hint_x = .2
            ) 
            
           
        
        btn.bind(on_press=self.buttonClicked)
        return btn
    def callback(self, event):
        print(f'Button is is being pressed')

app = MyApp()
app.run()