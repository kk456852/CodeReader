from abc import ABCMeta, abstractclassmethod
import time

class GameRole:

    STEP = 5

    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def leftMove(self):
        self.__x -= self.STEP
        
    def rightMove(self):
        self.__x += self.STEP

    def upMove(self):
        self.__y += self.STEP

    def downMove(self):
        self.__y -= self.STEP

    def jumpMove(self):
        self.__z += self.STEP

    def squatMove(self):
        self.__z -= self.STEP

    def attack(self):
        print(f"{self.name} 发动攻击  哒哒哒哒")
    
    def showPosition(self):
        print(f"呼叫总部，我现在位于x :{self.__x} y :{self.__y} z :{self.__z}")


class GameCommand(metaclass=ABCMeta):

    def __init__(self, role):
        self._role = role

    def setRole(self, role):
        self._role = role

    @abstractclassmethod
    def execute(self):
        pass


class Left(GameCommand):

    def execute(self):
        self._role.leftMove()
        self._role.showPosition()


class Right(GameCommand):

    def execute(self):
        self._role.upMove()
        self._role.showPosition()


class Down(GameCommand)"

    def execute(self):
        self._role.downMove()
        self._role.showPosition()


class MacroCommand(GameCommand):

    def __init__(self, role = None):
        super.__init__(role)
        self.__commands = []

    def addCommand(self, command):
        self.__commands.append(command)

    def removeCommand(self, command):
        self.__commands.remove(command)

    def execute(self):
        for command in self.__commands
            command.execute()


class GameInvoker:

    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command

    def action(self):
        if self.__command is not None:
            self.__command.execute()



            
             