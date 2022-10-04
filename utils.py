import numpy as np
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


first_row = np.array(['AC',"+/-","%","/"], dtype=object)
second_row = np.array(['7','8','9','x'], dtype=object)
third_row = np.array(['4','5','6','-'], dtype=object)
fourth_row = np.array(['1','2','3','+'], dtype=object)
fifth_row = np.array(['0',',','='], dtype=object)
operaction_symbols = np.array(['+','-','x','/'], dtype=object)
control_symbols = np.array(['AC','+/-','%'], dtype=object)
special_symbols = np.array([',','='], dtype=object)

def verify_special_symbol(value) -> bool:
    """Return the special symbol \n
        special symbol => ['\t,\t',\t'\t=\t'], dtype=object
    """ 
    if value in special_symbols:
        return True
    else:
        return False

def get_zero() -> str:
   """ Return the zero """
   return fifth_row[0]

def get_grid() -> np.array:
    """Return a 5x4 grid of buttons of calculator"""
    return np.array([first_row, second_row, third_row, fourth_row, fifth_row])

def is_number(value) -> bool:
    """Return True if value is a number"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def verify_operation_symbol(value) -> bool:
    """Return the operation symbol \n
        operation symbol => ['+'\t,\t'-'\t,\t'x'\t,\t'/'], dtype=object
    """
    if value in operaction_symbols:
        return True
    else:
        return False

def verify_control_symbol(value) -> bool:
    """Return the control symbol\n
        control symbol => ['AC',\t'+/-'\t,\t'%'], dtype=object
    """
    if value in control_symbols:
        return True
    else:
        return False


def configure_grid_layout(self,  grid_row_content:np.array, cols:int=4):
    """ This method configure a default grid layout with the content of the grid_row_content """
    grid = GridLayout(cols=cols, size_hint=(1.001, .1), spacing=3, padding=3)
            
    for item in grid_row_content:
        #  set gray color for the buttons
        print(item)
        background_color = (0.5, 0.5, 0.5, 1)
        size_hint_x = 1
        if verify_control_symbol(item):
            background_color = "#525F60"
        elif verify_operation_symbol(item) or item == '=':   
            # Put the operation buttons in orange color 
            background_color = "#FFAA00"
        if item == "0":
            # Put the button 0 in the first column of the last row
            size_hint_x = 2
        # Create the button 
        button = configure_button_layout(self, item, size_hint_x, 1, 40, background_color)
        grid.add_widget(button)
    
    return grid


def configure_button_layout(self, text:str, size_hint_x:float=1, size_hint_y:float=1, font_size:int=40, background_color:str='') -> Button:
    """ This method configure a default button layout with the content of the text """
    # Create the buttons
    button = Button(text=text, font_size=font_size, 
                    background_color=background_color, 
                    bold=True,
                    # normalize the bacground color
                    background_normal='', 
                    size_hint_x=size_hint_x,
                    size_hint_y=size_hint_y
                    )    
    button.bind(on_press=self.callback_for_button)
    return button