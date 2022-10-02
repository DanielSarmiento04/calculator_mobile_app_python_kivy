from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from utils import get_grid, get_zero, is_number, verify_operation_symbol, verify_control_symbol, verify_special_symbol

class Calculator(App):
    def build(self):
        self.window = GridLayout()
        # put the number of columns
        self.window.cols = 4
        #put the result label in the first row and extend it to 4 columns
        self.result_label = Label(text="0", font_size=40, size_hint=(1, .5), halign="right", valign="top")
        self.window.add_widget(self.result_label)
        
        # Add a button
        grid_content = get_grid()
        for row in grid_content:
            for item in row:
                # set gray color for the buttons
                background_color = (0.5, 0.5, 0.5, 1)
                if verify_operation_symbol(item):    
                    # Put the operation buttons in orange color 
                    background_color = "#FFAA00"
                
                # Create the button 
                button = Button(text=item, font_size=40, 
                            background_color=background_color, 
                            bold=True,
                            # normalize the bacground color
                            background_normal='', 
                            )    
                button.bind(on_press=self.callback_for_button)
                # add the button to the window
                self.window.add_widget(button)  

        return self.window

    def callback_for_button(self, instance):
        """ Callback for button press """
        # When the first number is pressed, change the result_label,
        # separe the number from the operation symbol and the control symbol
        if self.result_label.text == "0" and (not verify_operation_symbol(instance.text)) and not verify_control_symbol(instance.text) and not verify_special_symbol(instance.text):
            print("First number pressed")
            self.result_label.text = instance.text
        # When press another number, add the number to the result_label
        elif self.result_label.text != "0" and (not verify_operation_symbol(instance.text)) and not verify_control_symbol(instance.text):
            print('Another number pressed and comma')
            self.result_label.text += instance.text
        elif verify_control_symbol(instance.text):
            print('Control symbol pressed')
            if instance.text == "AC":
                self.result_label.text = "0"
            elif instance.text == "+/-":
                if self.result_label.text[0] == "-":
                    self.result_label.text = self.result_label.text[1:]
                else:
                    self.result_label.text = "-" + self.result_label.text
            elif instance.text == "%":
                self.result_label.text = str(float(self.result_label.text)/100)


        elif verify_operation_symbol(instance.text):
            pass


Calculator().run()