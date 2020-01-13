from abc import ABC, abstractmethod
from Model import OrderBuilder, Order


class Command(ABC):
    """docstring for Command"""

    @abstractmethod
    def execute(self):
        pass


class CommandComposeOrder(Command):
    """docstring for CommandComposeOrder"""

    def __init__(self, order: OrderBuilder):
        super(CommandComposeOrder, self).__init__()
        #print(order)
        self.__order = order
        #print(self.__order)

    def execute(self):
        #print("Executing...")
        var = self.__order.build()
        return var

class CommandRevertOrder(Command):
    """docstring for CommandRevertOrder"""

    def __init__(self, order: Order):
        super(CommandRevertOrder, self).__init__()
        self.__order = order

    def execute(self):
        self.__order._product_list = []


class CommandChangeState(Command):
    """docstring for CommandChangeState"""

class CommandAddToMenu(Command):
    """docstring for CommandAddToMenu"""

class CommandRevertFromMenu(Command):
    """docstring for CommandRevertFromMenu"""


class Invoker:
    """docstring for Invoker"""

    # def __init__(self):
    #     self._command = command
    #
    # def store_command(self, command):
    #     self._commands.append(command)

    def execute_command(self, command: Command):
        #print("Executing...")
        return command.execute()
