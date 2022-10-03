from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput



class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # layout for the inner box layout, which is the bottom 3 columns
        bottom_row = GridLayout(size_hint_y=1, cols=5)  # Defaults to horizontal orientation

        # Make the buttons
        button1 = TextInput()    

        # Add the first button and then bottom row to the layout. Add the bottom 3 buttons to the bottom_row box layout.
        layout.add_widget(button1)
        for i in range(10):
            bottom_row.add_widget(Button(text=str(i)))

        layout.add_widget(bottom_row)

        return layout

TestApp().run()