import abc

class FlyBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self) -> None:
        raise NotImplementedError()

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("飛びます")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("飛びません")

class QuackBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self) -> None:
        raise NotImplementedError

class Quack(QuackBehavior):
    def quack(self):
        print("カーカー")

class Squeak(QuackBehavior):
    def quack(self):
        print("キューキュー")

class Duck(metaclass=abc.ABCMeta):
    _fly_behavior = None
    _quack_behavior = None

    @property
    def fly_behavior(self):
        return self._fly_behavior
    
    @fly_behavior.setter
    def fly_behavior(self, fly_behavior):
        self._fly_behavior = fly_behavior
    
    @property
    def quack_behavior(self):
        return self._quack_behavior
    
    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        self._quack_behavior = quack_behavior
    
    @abc.abstractmethod
    def perform_fly(self):
        self.fly_behavior.fly()
    
    @abc.abstractmethod
    def perform_quack(self):
        self.quack_behavior.quack()


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()
    
    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()
    


def simulator():
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

if __name__ == "__main__":
    simulator()


