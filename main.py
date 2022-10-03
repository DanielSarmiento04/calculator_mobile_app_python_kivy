from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from utils import get_grid, get_zero, is_number, verify_operation_symbol, verify_control_symbol, verify_special_symbol, operaction_symbols
from kivy.uix.boxlayout import BoxLayout

class Calculator(App):
    def build(self):
        # Create the main layout with numbers and operations and the result label
        self.window =  BoxLayout(orientation='vertical')
        #put the result label in the first row and extend it to 4 columns
        self.result_label = Label(text="0", font_size=40,  halign="right", valign="center", size_hint_y = 0.1, size_hint_x = 1.5)
        # Add the result label to the main layout
        self.window.add_widget(self.result_label,)
        # create a axuiliary variable to put the buttons in the grid
        self.aux_result_variable = ""
        # Create the grid with the buttons
        self.grid_buttons = GridLayout(cols=4, size_hint=(1, .4), spacing=3, padding=3)
        # Add a button
        grid_content = get_grid()
        # add the first row to the penultimate row
        for row in grid_content[0:]:
            for item in row:
                # set gray color for the buttons
                background_color = (0.5, 0.5, 0.5, 1)
                if verify_control_symbol(item):
                    background_color = "#525F60"
                elif verify_operation_symbol(item)  :    
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
                self.grid_buttons.add_widget(button)  
        self.window.add_widget(self.grid_buttons)
        return self.window

    def callback_for_button(self, instance):
        """ Callback for button press """
        # When the first number is pressed, change the result_label,
        # separe the number from the operation symbol and the control symbol
        if self.result_label.text == "0" and (not verify_operation_symbol(instance.text)) and not verify_control_symbol(instance.text) and not verify_special_symbol(instance.text):
            print("First number pressed")
            self.result_label.text = instance.text
            self.aux_result_variable += instance.text

        # When press another number, add the number to the result_label
        elif self.result_label.text != "0" and (not verify_operation_symbol(instance.text)) and not verify_control_symbol(instance.text)  and not verify_special_symbol(instance.text):
            print('Another number pressed')
            self.result_label.text += instance.text
            self.aux_result_variable += instance.text

        # When press control symbol, change the result_label
        elif verify_control_symbol(instance.text):
            print('Control symbol pressed')
            # Clear the label
            if instance.text == "AC":
                self.result_label.text = "0"
                self.aux_result_variable = ""
            # Change the signal of the number
            elif instance.text == "+/-":
                if self.result_label.text[0] == "-":
                    self.result_label.text = self.result_label.text[1:]
                    self.aux_result_variable = self.aux_result_variable[1:]
                else:
                    self.result_label.text = "-" + self.result_label.text
                    self.aux_result_variable = "-" + self.aux_result_variable
            # Divide the number by 100
            elif instance.text == "%":
                self.result_label.text = str(float(self.result_label.text)/100)
                self.aux_result_variable = self.result_label.text

        elif verify_operation_symbol(instance.text) and (not self.aux_result_variable[-1] in operaction_symbols):
            print('Operation symbol pressed')
            # When the opreation symbol is pressed, add the opreation to the aux_result_variable and refresh the result_label
            if instance.text == "+":
                self.aux_result_variable += "+"
                self.result_label.text = "0"
            elif instance.text == "-":
                self.aux_result_variable += "-"
                self.result_label.text = "0"
            elif instance.text == "x":
                self.aux_result_variable += "*"
                self.result_label.text = "0"
            elif instance.text == "/":
                self.aux_result_variable += "/"
                self.result_label.text = "0"

        elif verify_special_symbol(instance.text):
            print('Special symbol pressed')
            if instance.text == ",":
                # Verify if the number already has a comma if not add only one
                if not "," in self.result_label.text:
                    self.result_label.text += ","
                    self.aux_result_variable += "."
            elif instance.text == "=":
                print("Equal pressed")
                print(self.aux_result_variable)
                self.result_label.text = str(eval(self.aux_result_variable)).replace(".", ",")
                self.aux_result_variable = self.result_label.text.replace(",", ".")


        print(self.aux_result_variable, self.aux_result_variable[-1], self.aux_result_variable[-1] in operaction_symbols)

Calculator().run()