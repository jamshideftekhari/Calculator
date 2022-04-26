# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1 - Hello world
# 2 - input/echo number of items
# 3 - input/echo price of items
# 4 - calculate price without tax
# 5 - echo Tax levels Hard coded
# 6 - receive to letter state codes echo and show tax level
# 7 - Calculate price
# 8 - List hard coded discount values
# 9 - calculate discount value based on Order.py value
# 10 - calculate total price with discount included.
# 11 - add tax levels to file/DB
# 12 - add discount values to file/DB

from Models.EUTax import EUTax
from Services.tax_calculator import Calculator


# 1 - Hello world
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 2 - input/echo number of items
def input_number():
    item_nr = int(input("Please enter the number of items yo want to buy -> "))
    print("You entered: " + str(item_nr))
    return item_nr


# 3 - input/echo price of items
def input_price():
    price = int(input("please enter the price of the item you buy -> "))
    print("you entered: " + str(price))
    return price


# 4 - calculate price without tax
def calculate_price(price, number):
    total = price*number
    return total


# 5 - echo EU Tax levels (Hard coded) and input area code
def input_area_code():
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


def calculate_tax(price, country_tuple):
    print(f'VAT for {country_tuple.value[1]} is {country_tuple.value[2]}%')
    tax = price * country_tuple.value[2]/100
    return tax


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to calculator')
    nr = input_number()
    pr = input_price()

    # calculate tax using methods
    print('***************calculate total price using methods******************')
    price_ex_tax = calculate_price(pr, nr)
    print(f'total price exclusive tax is: {price_ex_tax}')
    cc = input_area_code()
    ta = calculate_tax(pr, cc)
    print(f'VAT =  {ta}')
    price_in_tax = price_ex_tax + ta
    print(f'total price inclusive tax is: {price_in_tax}')

    print('***************calculate total price using calculate object******************')
    my_cal = Calculator
    price_ex_tax = my_cal.calculate_price(pr, nr)
    print(f'total price exclusive tax is: {price_ex_tax}')
    cc = my_cal.input_area_code()
    ta = my_cal.calculate_vat(pr, cc)
    print(f'VAT =  {ta}')
    price_in_tax = price_ex_tax + ta
    print(f'total price inclusive tax is: {price_in_tax}')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

