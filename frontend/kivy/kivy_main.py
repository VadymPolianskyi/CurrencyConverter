from kivy.app import App
from kivy.core.window import Window

from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout

from service.converter.converter import Converter


class ConvertorGridLayout(GridLayout):
    currency = StringProperty()
    result = StringProperty()

    def open_drop(self):
        """
        @param drop_down:   a object representation of the choice box
        """
        self.drop_down = CustomDrop()
        self.drop_down.open(self.ids.butt)
        self.drop_down.root = self #send this object in the child class to make changes

    def convert(self, sum):
        """
        @param result:     a string representation of the converted data
        """
        self.result = Converter.convert(sum, self.currency)


class CustomDrop(DropDown):

    def choose_currency(self, text):
        """
        @param text:   a string representation of the selected name of currency in choice box
        @param root:   the object representation of the main layout
        """
        self.root.currency = text


class ConverterApp(App):

    def build(self):
        """
        @return:    the object representation of the main layout
        """
        Window.size = (400, 200)
        return ConvertorGridLayout()


if __name__ == '__main__':
    convApp = ConverterApp()
    convApp.run()

