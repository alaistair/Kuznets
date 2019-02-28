class Settings():
    """ A class to store all settings for EconSim"""

    def __init__(self):

        # Initial economy settings. Households >= firms
        self.init_households = 100
        self.init_firms = 3
        self.init_interest_rate = 1.03

        # Initial household settings
        self.init_hh_savings = 100
        self.init_MPC = 0.9
        self.init_human_capital = 100

        # Initial firm settings
        self.init_firm_expected_revenue = 10 * self.init_households
        self.init_firm_debt = 3 * self.init_firm_expected_revenue
        self.init_productivity = 1.1 # output per input

        # Initial government settings
        self.init_govt_revenue = 0
        self.init_govt_expenditure = 0
        self.init_govt_debt = 0
