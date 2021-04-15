# from data.data import resources, FORMAT
# from resource import Resource


class Cashier:
    """This class calculate the bills for the user.
    ...
    Methods
    -------
    get_total():
        adds all the number of notes the user put in,
    confirming_payment():
        check if the money put in by the user is less than the actual cost,
        it also checks if the money is greater than the actual cost if it is change is being returned
    """
    def __init__(self, biyar, faiba, muri, wazobia):
        self.wazobia = wazobia
        self.muri = muri
        self.faiba = faiba
        self.biyar = biyar

    def get_total(self):
        total = (self.wazobia * 50) + (self.muri * 20) + (self.faiba * 10) + (self.biyar * 5)
        return total

    def confirming_payment(self, resource):
        bill = resource.calculate_bill()
        total = self.get_total()

        if total < bill:
            return "Sorry that’s not enough money. Money refunded"
        elif total > bill:
            change = total - bill
            return f"\nHere is your ₦{change} in change.\nHere is your work!!!"
        else:
            return f'\nHere is your work!!!'
