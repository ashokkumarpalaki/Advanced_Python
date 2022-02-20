from abc import ABC, abstractmethod


class AbstractionTest(ABC):
    def __init__(self, ob1):
        self.ob1 = ob1
        print(ob1)

    def display(self):
        print("Helloworld")

    @classmethod
    def display1(cls):
        print("Helloworld")

    @abstractmethod
    def method01(self):
        pass


class Subtest(AbstractionTest):
    def __init__(self, ob1, ob2):
        super(Subtest, self).__init__(ob2)
        print(ob1 + ob2)

    @classmethod
    def display1(cls):
        print("I'm from subclass")
        AbstractionTest.display1()

    def method01(self):
        print("I'm abstract method")


if __name__ == '__main__':
    Subtest(10, 20).display()
    Subtest.display1()
    AbstractionTest.display1()
    Subtest(10, -5).method01()
