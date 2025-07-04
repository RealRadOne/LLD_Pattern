from abc import ABC,abstractmethod

# Coffee will be an interface, we will define 
# behaviors i.e. one type where cream is missing, 
# other where sugar is, one where milk is
class Coffee(ABC):
    @abstractmethod
    def add_sugar(self):
        pass 

    @abstractmethod
    def add_cream(self):
        pass 

    @abstractmethod
    def add_milk(self):
        pass 

    @abstractmethod
    def add_coffee(self):
        pass 

    @abstractmethod
    def add_flavor(self):
        pass 

class Espresso(Coffee):

    def add_sugar(self,sugar):
        return sugar

    def add_coffee(self,coffee):
        return coffee
    
    def add_milk(self,milk):
        return milk

    def add_cream(self):
        pass

    def add_flavor(self,flavor:str):
        return flavor
    
    def get_price(self):
        return self.price

class Latte(Coffee):
    def __init__(self):
        self.sugar = 0
        self.coffee = 0
        self.milk = 0
        self.flavor = None 
        self.price = 10

    def add_sugar(self,sugar):
        self.sugar = sugar

    def add_coffee(self,coffee):
        self.coffee = coffee

    def add_milk(self,milk):
        self.milk = milk

    def add_flavor(self,flavor:str):
        self.flavor = flavor
    
    def add_cream(self):
        return super().add_cream()
    
    def get_price(self):
        return self.price
    
class Payment(ABC):
    def get_balance(self):
        pass

    def make_payment(self):
        pass 

class BankPayment(Payment):
    def __init__(self,balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def make_payment(self,amount):
        if(amount>=self.balance):
            return "Insufficient Balance"
        else:
            self.balance-=amount
            return "Payment Processed"


class Machine:
    def __init__(self,sugar,milk,cream,coffee,flavors):
        self.sugar = sugar
        self.milk = milk
        self.cream = cream
        self.coffee = coffee
        self.flavors = flavors

    def make_payment(self,amount):
        mode = BankPayment()
        mode.make_payment(amount=amount)

    def make_order(self,cur_item,flavor):
        if cur_item == 'Latte':
            try:
                if self.sugar>=2 and self.coffee>=5 and self.milk>=3:
                    item = Latte()
                    item.add_flavor(flavor=flavor)
                    self.sugar-=2
                    self.coffee-=5
                    self.milk-=3
                    self.make_payment(item.price)
            except:
                return "Not enough ingredients"
        elif cur_item == 'Espresso':
            try:
                if self.sugar>=2 and self.coffee>=10:
                    item = Espresso()
                    self.sugar-=2
                    self.coffee-=10
                    self.make_payment(item.price)
            except:
                return "Not enough ingredients"
            
        
if __name__ == "__main__":
    m = Machine(20,10,15,30,['Cinnamon','Hazelnut'])
    m.push_order('Latte')
    m.make_payment()
