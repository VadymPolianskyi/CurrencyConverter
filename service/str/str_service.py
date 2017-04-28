import re


class RegularExpressionService(object):
    VALUE_SEARCH_PATTERN = '[0-9].+[0-9]'
    PAIR_CURRENCY_SEARCH_PATTERN = "':.*?,"

    def parse_json(self, json_str, currency_name):
        """
        @param json_str:   a string representation of the json response which include the reference rates
        @param pair:       a string representation of a pair "'name of currency': reference rate" of currency_name 
        @return:           a string value of the reference rates
        """
        pair = self.__search_elements(currency_name + self.PAIR_CURRENCY_SEARCH_PATTERN, json_str)
        return self.__search_elements(self.VALUE_SEARCH_PATTERN, pair)

    def __search_elements(self, pattern, text):
        """
        @param element:    the representation of found string by the pattern
        @return:           an str representation of a pair "'name of currency': reference rate"
        """
        for element in re.finditer(pattern, text):
            return element.group()
