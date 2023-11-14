class Econ:

    def __init__(self, state, avg_income, population):
        self.state = state
        self.avg_income = avg_income
        self.population = population
    
    def setState(self, state):
        self.state = state
    
    def setAvg_income(self, avg_income):
        self.avg_income = avg_income
    
    def setPopulation(self, population):
        self.population = population
    
class Good(Econ):

    def __init__(self, price, relative_price, ):
