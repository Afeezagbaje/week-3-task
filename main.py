from assets import art
from resource import Resource
from cashier import Cashier


class Printer:
    """This class act like a printer which the users interact with
    """
    print(art.logo)
    print('Welcome to automated printer')

    @classmethod
    def printer_machine(cls):
        resource = Resource()

        while True:
            user_input = input("\nWhat format would you like 'coloured' or 'greyscale'?\n")

            while user_input.lower() not in ['coloured', 'greyscale', 'report', 'off']:
                user_input = input("Invalid!!!! Please put in 'coloured' or 'greyscale'\n")

            while user_input == 'report':
                print(resource.report())
                user_input = input("\nWhat format would you like 'coloured' or 'greyscale'?\n")

            # This switch off the printer if 'off' is been typed
            if user_input == 'off':
                return 'Thanks for using our service Bye.....'

            number_of_pages = input("How many pages?\n")

            while number_of_pages.isnumeric() is not True:
                print("You've entered an invalid number")
                number_of_pages = input("How many pages?\n")

            # This checks if there is enough resource to print the pages the users want.
            # If No the printer tells the user no enough resources but if yes then the
            # monies(currencies) is being asked from users
            ink_and_price = resource.check_resource(user_input, number_of_pages)
            if ink_and_price != True:
                print(ink_and_price)
            else:
                print(f'Your price is ₦{resource.calculate_bill()}')
                print("Please insert Monies.")

                # This catches an error if the user type in a string instead of a number
                try:
                    biyar = int(input('How many Biyar: '))
                    faiba = int(input('How many Faiba: '))
                    muri = int(input('How many Muri: '))
                    wazobia = int(input('How many Wazobia: '))
                except ValueError:
                    print("You've entered an invalid input")
                    Printer.printer_machine()

                # This add all the currencies payed by the user
                calculate_money = Cashier(biyar, faiba, muri, wazobia)
                calculate_money.get_total()

                # This confirm the payment if it is less than or greater than the actual cost
                print(calculate_money.confirming_payment(resource))

                # This update the resources after printing the pages
                resource.deduct_resource()
                print('Thanks for using our Printing service. Hope you enjoyed it!!')
                print("===================================================================")


print(Printer.printer_machine())
