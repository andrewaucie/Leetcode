from threading import Condition
class FooBar:
    def __init__(self, n):
        self.n = n
        self.cond = Condition()
        self.fooCount = 0
        self.barCount = 0
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.cond:
                self.cond.wait_for(lambda: self.fooCount == self.barCount)
                printFoo()
                self.fooCount += 1
                self.cond.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.cond:
                self.cond.wait_for(lambda: self.fooCount-1 == self.barCount)
                printBar()
                self.barCount += 1
                self.cond.notify()

