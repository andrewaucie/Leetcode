from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.barLock = Lock()
        self.barLock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.fooLock.acquire(blocking=True)
            printFoo()
            self.barLock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barLock.acquire(blocking=True)
            printBar()
            self.fooLock.release()