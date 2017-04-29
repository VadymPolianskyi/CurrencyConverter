from service.web.parser import FixerParser


class Converter(object):
    CONVERTED_UNCORRECT_DATA = '0.0'

    @staticmethod
    def convert(sum, currency):
        """
        @param sum:        a string representation of count of money
        @param currency:   a string representation of currency name
        @param parser:     the object representation of the service to getting values of reference rates
        @param difference: a float representation of reference rate
        @return:           a string representation of the converted data or '0.0' if input data is incorrect
        """
        parser = FixerParser()
        try:
            difference = parser.get_current_value(currency)
            return str(float(sum) * difference)
        except ValueError:
            return Converter.CONVERTED_UNCORRECT_DATA
        except TypeError:
            return Converter.CONVERTED_UNCORRECT_DATA
