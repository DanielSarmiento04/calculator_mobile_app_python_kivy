from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from utils import get_grid, get_zero, is_number, get_operation_symbol, get_control_symbol

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
                    background_color = "#FFAA00"
                button = Button(text=item, font_size=40, 
                            background_color=background_color, 
                            bold=True,
                            background_normal='', # remove the default background_color of the button when pressed       
                            )    
                button.bind(on_press=self.callback_for_button)
                # button.center = self.window.center
                self.window.add_widget(button)  
                # self.window.add_widget(Button(text=item, font_size=50))
        return self.window

    def callback_for_button(self, instance):
        """ Callback for button press """
        # When the first number is pressed, change the result_label,
        # separe the number from the operation symbol and the control symbol
        if self.result_label.text == "0" and (not get_operation_symbol(instance.text)) and not get_control_symbol(instance.text):
            print("First number pressed")
            self.result_label.text = instance.text
        # When press another number, add the number to the result_label
        elif self.result_label.text != "0" and (not get_operation_symbol(instance.text)) and not get_control_symbol(instance.text):
            self.result_label.text += instance.text
        elif get_operation_symbol(instance.text):
            pass


Calculator().run()