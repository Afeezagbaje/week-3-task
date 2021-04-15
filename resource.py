from data.data import resources, FORMAT


class Resource:
    """This class takes care of the resources of the printer i.e the available resources in the printer like
    amount of inks, paper and profit.
    ....

    Methods
    -------
    report() returns the available resources,
    check_resources() checks if there is enough resources to print user's number of pages,
    calculate_bill() calculate the cost of printing the amount of pages the user want to print,
    deduct_resource() update the resources after printing the number of page a user wants to print
    """

    def __init__(self):
        self.inks = resources['ink']
        self.papers = resources['paper']
        self.profit = resources['profit']

    def report(self):
        return f'Ink: {self.inks}ml \nPaper: {self.papers}pcs \nProfit: ₦{self.profit}'

    def check_resource(self, user_input, pages):
        self.user_input = user_input
        self.pages = int(pages)
        self.ink_quantity = FORMAT[self.user_input]['materials']['ink']
        self.price = FORMAT[self.user_input]['price']
        self.ink_needed = int(self.pages) * int(self.ink_quantity)

        if self.ink_needed > self.inks:
            return f'Sorry, there is not enough ink to print {self.pages} pages'
        elif self.pages > self.papers:
            return 'Sorry, there is not enough paper'
        else:
            return True

    def calculate_bill(self):
        self.bill = int(self.price) * int(self.pages)
        return self.bill

    def deduct_resource(self):
        self.profit += self.bill
        self.inks -= self.ink_needed
        self.papers -= self.pages

