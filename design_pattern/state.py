from abc import ABCMeta, abstractclassmethod

class Water:

    def  __init__(self, state):
        self.__temperature = 25
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        self.__state = state

    def getTemperature(self):
        return self.__temperature
    
    def setTemperature(self, temperature):
        self.__temperature = temperature

    def riseTemperature(self,  step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)

class State(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractclassmethod
    def behavior(self, water):
        pass


class SolidState(State):

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print(water.getTemperature())