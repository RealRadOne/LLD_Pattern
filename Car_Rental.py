import time
import random 
import datetime
import uuid
from abc import ABC,abstractmethod
class Car:
    def __init__(self,platenumber:int,model:str,year:int):
        self._Platenumber = platenumber
        self._Model = model
        self._Year = year
        self._Price = 0
        self._Status = 'available'

    @property
    def Price(self):
        return self._Price
    
    @Price.setter
    def Price(self,price:int):
        self._Price = price 

    @property
    def Status(self):
        return self._Status
    
    @Status.setter
    def Status(self,status:str):
        self._Status = status

class Customer:
    def __init__(self,CID:int,Name:str):
        self._CID = CID
        self._Name = Name 

    @property
    def CID(self):
        return self._CID
    
    @property
    def Name(self):
        return self._Name
        
class Reservation:
    def __init__(self,RID:int,startDate,endDate):
        self._RID = RID
        self._Car = None 
        self._Customer = None 
        self._StartDate = startDate
        self._EndDate = endDate

    @property
    def Customer(self):
        return self._Customer
    
    @Customer.setter
    def Customer(self,customer):
        self._Customer = customer
    
    @Car.setter
    def Car(self,car: Car):
        self._Car = car 

    @property
    def Car(self):
        return self._Car

    @property
    def EndDate(self):
        return self._EndDate
    
    @property
    def StartDate(self):
        return self._StartDate
    
    @EndDate.setter
    def EndDate(self,endDate):
        self._EndDate = endDate

class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass 

class CreditCard(Payment):
    def make_payment(self):
        return "Payment processed"
    
class PayPal(Payment):
    def make_payment(self):
        return "Payment Processed"

class RentalSystem:
    def __init__(self):
        self._Reservations = {}
        self._Cars = {}

    def addCar(self,plateNumber:int,model:str,year:int):
        if plateNumber in self._Cars:
            return "This car has been registered before"
        if not isinstance(model,str):
            raise TypeError
        car_info = Car(plateNumber,model,year)
        self._Cars[plateNumber] = car_info 
    
    def get_CarByModel(self,model:str):
        car = None 
        for plateNumber in self._Cars:
            if self._Cars[plateNumber].model == model:
                car = plateNumber[car]
        if car==None:
            return "Sorry, we don't have this model"
        elif car.Status == 'Occupied':
            return "Sorry these models are no longer available"
        else:
            return car

    def makeReservation(self,model:str):
        try:
            car = self.get_CarByModel(model)
        except Exception:
            raise AttributeError
        RID = uuid.uuid4
        startDate = datetime.date
        endDate = startDate+30
        current = Reservation(RID,startDate,endDate)
        current.Car = car
        current.Car.Status = 'Occupied'
        self._Reservations[RID] = current
        return RID 
    
    def makePayment(self,RID:int,amount:int,mode:str):
        current = self._Reservations[RID]
        cost = current.Car.Price*(current.endDate-current.startDate)
        self._Reservations.pop(RID)
        if mode=='Paypal':
            PayPal().make_payment(cost)
        else:
            CreditCard().make_payment(cost)

if __name__ == "__main__":
    machine = RentalSystem()
    machine.addCar(1228,model='Mazda',year=2025)
    machine.addCar(1330,model='Subaru',year=2024)
    machine.addCar(1456,model='Denali',year=2024)
    r1 = machine.makeReservation(model='Subaru')
    r2 = machine.makeReservation(model='Denali')
    machine.makePayment(r1)
    
 
