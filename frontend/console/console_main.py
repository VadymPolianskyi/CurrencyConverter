from service.converter.converter import Converter


class ConverterApp(object):

    @staticmethod
    def check_to_exit(sum, currency):
        """
        @return:   the boolean representation of available exit comand
        """
        return sum == 'e' or currency == 'e'

    @staticmethod
    def run():
        """
        @param currency:  a string representation of currency name
        @param sum:       a string representation of count of money
        """
        print '''Welcome!
Enter sum and currency to convert to USD
or 'e' to exit'''
        while True:

            sum = raw_input('Sum> ')
            currency = raw_input('To currency> ')

            if ConverterApp.check_to_exit(sum, currency):
                break

            print sum, 'USD is', Converter.convert(sum, currency), currency
            print '\nWrite again: \n'
        print 'Bye!'


if __name__ == '__main__':
    ConverterApp.run()