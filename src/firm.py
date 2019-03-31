""" Class for all information about an individual firm """
import random

class Firm():

    def __init__(self, settings):
        self.product_name = 'A'
        self.inventory = int(1) # stock of inventory (units of output)
        self.expected_production = settings.init_production
        self.production = 0#self.expected_production # flow of production (one cycle)

        self.product_price = 1 + (random.random() - 0.5) * 0.2

        self.labour_productivity = settings.init_labour_productivity # output per labour input
        self.capital_investment = 0.1 * settings.init_production
        self.debt = self.capital_investment
        self.revenue = 0 # flow of revenue (one cycle)

        self.workers = {} # hhID, worker dictionary
        self.owners = {} # hhID, owner dictionary

    def update_hiring_intentions(self):
        # Update firm's expected revenue based on sales
        if self.inventory == 0: # Ran out of inventory
            self.product_price *= 1.1
            self.expected_production *= 1.1
        elif self.inventory > 0.5 * self.expected_production: # too much inventory
            self.product_price *= 0.9
            self.expected_production *= 0.95
        else:
            self.product_price *= 1.02
            self.expected_production *= 1.02
        if self.product_price < 0: self.product_price = 0.01

        expected_revenue = self.expected_production * self.product_price
        expected_production_spending = expected_revenue - self.debt * 0.05
        expected_labour_spending = expected_production_spending/self.labour_productivity
        expected_additional_labour_spending = expected_labour_spending
        for hhID, household in self.workers.items():
            expected_additional_labour_spending -= household.expected_wages

        if expected_additional_labour_spending < 0:
            return 0
        else:
            return expected_additional_labour_spending

    def update_production(self, labour_cost):
        self.production += labour_cost * self.labour_productivity
        self.debt += labour_cost #+ self.capital_investment
        return 1

    # Adds sales to firm's revenue.
    # Returns sales fulfilled
    def update_revenue(self, sales):
        quantity = sales/self.product_price
        if self.inventory > quantity: # firm fulfils all sales
            self.inventory -= quantity
            self.revenue += sales
            return sales
        elif self.inventory > 0: # firm partially fulfils order, returns unfilled amount
            sales = self.inventory * self.product_price
            self.revenue += sales
            self.inventory = 0
            return sales
        elif self.inventory == 0: # firm out of stock, return sales
            return 0

    def update_financial(self, interest_rate):
        self.debt -= self.revenue
        self.debt *= interest_rate
        self.revenue = 0

        return 0

    def status(self):
        status = "Inventory: " + str(round(self.inventory,2)) + " production: " + str(round(self.production,2)) + " revenue: " + str(round(self.revenue,2)) + " debt: " + str(round(self.debt,2))
        return status
