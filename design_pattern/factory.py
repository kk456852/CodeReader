from abc import ABCMeta, abstractclassmethod

class Coffee(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractclassmethod
    def getTaste(self):
        pass

class LatteCaffe(Coffee):

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "轻柔而香醇"

class MochaCoffee(Coffee):

    def __init__(self, name):
        super.__init__(name)

    def getTaset(self):
        return "丝滑与醇厚"


