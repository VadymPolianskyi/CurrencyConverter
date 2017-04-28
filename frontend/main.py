from kivy.app import App
from kivy.core.window import Window

from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout

from service.web.parser import FixerParser


class ConvertorGridLayout(GridLayout):
    currency = StringProperty()
    result = StringProperty()

    def open_drop(self):
        """
        @param drop_down:   a object representation of the choice box
        """
        self.drop_down = CustomDrop()
        self.drop_down.open(self.ids.butt)
        self.drop_down.root = self

    def convert(self, sum):
        """
        @param sum:        a string representation of input data
        @param parser:     the object representation of the service to getting values of reference rates
        @param difference: a float representation of reference rate
        @param result:     a string representation of the converted data
        """
        parser = FixerParser()
        try:
            difference = parser.get_current_value(self.currency)
            self.result = str(float(sum) * difference)
        except ValueError:
            self.result = '0.0'


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

