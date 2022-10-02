from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from utils import get_grid, get_zero, is_number, get_operation_symbol

class Calculator(App):
    def build(self):
        self.window = GridLayout()
        # put the number of columns
        self.window.cols = 4
        #put the result label in the first row
        self.result_label = Label(text="0", size_hint=(1, .5))
        self.window.add_widget(self.result_label)
        
        # Add a button
        grid_content = get_grid()
        for row in grid_content:
            for item in row:
                # set gray color for the buttons
                background_color = (0.5, 0.5, 0.5, 1)
                if get_operation_symbol(item):    
                    # put the operation buttons in orange color 
                    background_color = (1, 0.5, 0, 1)
                button = Button(text=item, font_size=40, background_color=background_color)    
                button.bind(on_press=self.callback_for_button)
                # button.center = self.window.center
                self.window.add_widget(button)  
                # self.window.add_widget(Button(text=item, font_size=50))
        return self.window

    def callback_for_button(self, instance):
        """ Callback for button press """
        # change the test when startes with 0
        if instance.text == get_zero() and (not get_operation_symbol(instance.text)):#and len(self.result_label.text) == 1:
            print(2)
            self.result_label.text = instance.text
        elif not get_operation_symbol(instance.text):
            print(3)
            self.result_label.text += instance.text            


Calculator().run()