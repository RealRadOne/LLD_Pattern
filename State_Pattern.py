from abc import ABC,abstractmethod

class TrafficLight:
    def __init__(self,duration):
        self.state = GreenLightState() 
        self.duration = duration 
        self.clock = 0
        self.emergency = False

    def set_state(self,new_state):
        self.state = new_state 

    def changeSignal(self):
        if self.emergency:
            self.set_state(GreenLightState())
            self.emergency = False
        else:
            self.state.signalChange()

    def gotEmergency(self):
        self.emergency = True
    
    def tick(self):
        self.clock+=1
        if(self.clock>=self.duration):
            self.changeSignal()
            self.clock = 0


class TrafficLightState(ABC):
    @abstractmethod
    def signalChange(self,signal:TrafficLight):
        pass 

    @abstractmethod
    def get_color(self):
        pass

class GreenLightState(TrafficLightState):
    def signalChange(self, traffic_light:TrafficLight):
        traffic_light.set_state(YellowLightState())

    def get_color(self):
        return 'Green'
    
class YellowLightState(TrafficLightState):
    def signalChange(self, traffic_light:TrafficLight):
        traffic_light.set_state(RedLightState())
    
    def get_color(self):
        return 'Yellow'
    
class RedLightState(TrafficLightState):
    def signalChange(self, traffic_light:TrafficLight):
        traffic_light.set_state(GreenLightState())
    
    def get_color(self):
        return 'Red'


if __name__ == "__main__":
    light1 = TrafficLight(duration=10)
    for i in range(30):
        light1.tick()

        if i==12:
            print("Ambulance passing")
            light1.gotEmergency()


    

        