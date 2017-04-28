import requests
from service.str.str_service import RegularExpressionService


class FixerParser(object):
    HTTP_GET_REQEST = 'http://api.fixer.io/latest?base=USD'

    def get_current_value(self, name):
        """
        @param name:            a string representation of name of currency
        @param json_response:   a string representation of the json response which include the reference rates
        @return:                a float representation of reference rate
        """
        json_response = self.__parse_currency()

        str_service = RegularExpressionService()
        return float(str_service.parse_json(json_response, name))

    def __parse_currency(self):
        """
        @param r:       a object response from get-request
        @return:        a string representation of the json response which include the reference rates according to USD
        """
        r = requests.get(self.HTTP_GET_REQEST, auth=('user', 'pass'))
        return str(r.json())
