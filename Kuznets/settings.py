class Settings():
    """ A class to store all settings for EconSim"""

    def __init__(self):

        # Initial economy settings. Households >= firms
        self.init_households = 20
        self.init_firms = 3
        self.init_interest_rate = 1.01

        # Initial household settings
        self.init_hh_savings = 20
        self.init_MPC = 0.95
        self.init_human_capital = 100

        # Initial firm settings
        self.init_production = int(100) # 10 * self.init_households
        self.init_labour_productivity = 1.3 # output per labour input

        # Initial government settings
        self.init_govt_revenue = 0
        self.init_govt_expenditure = 0
        self.init_govt_debt = 0
