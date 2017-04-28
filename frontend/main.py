from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout


class ConvertorGridLayout(GridLayout):
    currency = StringProperty()
    result = StringProperty()

    def open_drop(self):
        self.drop_down = CustomDrop()
        self.drop_down.open(self.ids.butt)
        self.drop_down.root = self

    def convert(self, sum):
        print self.currency, sum
        self.result = sum

class CustomDrop(DropDown):

    def choose_currency(self, text):
        self.root.currency = text


class ConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        return ConvertorGridLayout()


convApp = ConverterApp()
convApp.run()
