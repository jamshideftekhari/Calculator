from Models.EUTax import EUTax


class Calculator(object):

    total_price_ex_vat = 0
    total_price_in_vat = 0
    total_vat = 0

    def __init__(self):
        print('calculated object initiated')

    def calculate_price(self, price, number):
        self.total_price_ex_vat = price * number
        return self.total_price_ex_vat

    # 5 - echo EU Tax levels (Hard coded) and input area code
    def input_area_code(self):
        print("countries VAT: ")
        for co in EUTax:
            print(co.value)
        country_code = input("Please enter country code -> ")
        for cc in EUTax:
            if cc.value[0] == country_code.upper():
                country_tuple = cc
                print(f' country tuple: {country_tuple.value}')
                print(f' country tax value: {country_tuple.value[2]}')
                return country_tuple
        print("not found")
        return cc.NOTFound

    def calculate_vat(self, price, country_tuple):
        print(f'VAT for {country_tuple.value[1]} is {country_tuple.value[2]}%')
        self.total_vat = price * country_tuple.value[2] / 100
        return self.total_vat


