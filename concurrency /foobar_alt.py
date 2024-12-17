import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_turn = True
        self.condition = threading.Condition()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.condition:
                while not self.foo_turn:
                    self.condition.wait()

                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.foo_turn = False
                self.condition.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.condition:
                while self.foo_turn:
                    self.condition.wait()
                printBar()
                self.foo_turn = True
                self.condition.notify()  