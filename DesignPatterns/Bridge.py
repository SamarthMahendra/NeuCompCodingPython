# The Bridge design pattern allows you to separate the abstraction from the implementation. It is a structural design pattern.


# Without Bridge Pattern:

# abstract class Pizza - deliver()
# PepperoniPizza extends Pizza - deliver()
# VeggiePizza extends Pizza - deliver()

# now add two types -> american and italian
# AmericanPepperoniPizza extends Pizza - deliver()
# AmericanVeggiePizza extends Pizza - deliver()
# ItalianPepperoniPizza extends Pizza - deliver()
# ItalianVeggiePizza extends Pizza - deliver()

# here american and italian are two independant dimentions

from abc import ABC, abstractmethod

class Pizza(ABC):

    def __init__(self, sauce, topping, crust):
        self.sauce = sauce
        self.topping = topping
        self.crust = crust

    @abstractmethod
    def deliver(self):
        pass



class AmericanPepperoniPizza(Pizza):

        def __init__(self, sauce, topping, crust):
            super().__init__(sauce, topping, crust)

        def deliver(self):
            print(f"Delivering American Pepperoni Pizza with {self.sauce} sauce, {self.topping} topping and {self.crust} crust.")


class AmericanVeggiePizza(Pizza):

            def __init__(self, sauce, topping, crust):
                super().__init__(sauce, topping, crust)

            def deliver(self):
                print(f"Delivering American Veggie Pizza with {self.sauce} sauce, {self.topping} topping and {self.crust} crust.")


class ItalianPepperoniPizza(Pizza):

                def __init__(self, sauce, topping, crust):
                    super().__init__(sauce, topping, crust)

                def deliver(self):
                    print(f"Delivering Italian Pepperoni Pizza with {self.sauce} sauce, {self.topping} topping and {self.crust} crust.")


class ItalianVeggiePizza(Pizza):

                def __init__(self, sauce, topping, crust):
                    super().__init__(sauce, topping, crust)

                def deliver(self):
                    print(f"Delivering Italian Veggie Pizza with {self.sauce} sauce, {self.topping} topping and {self.crust} crust.")


# With Bridge Pattern:

# abstract class Pizza - deliver()

class Pizza(ABC):

    def __init__(self, sauce, topping, crust):
        self.sauce = sauce
        self.topping = topping
        self.crust = crust

    @abstractmethod
    def deliver(self):
        pass


class PizzaType(ABC):

    @abstractmethod
    def deliver(self):
        pass

class American(PizzaType):

        def deliver(self):
            print("Delivering American Pizza")

class Italian(PizzaType):

            def deliver(self):
                print("Delivering Italian Pizza")


class PepperoniPizza(Pizza):

        def __init__(self, pizza_type: PizzaType, sauce, topping, crust):
            super().__init__(sauce, topping, crust)
            self.pizza_type = pizza_type

        def deliver(self):
            self.pizza_type.deliver()
            print(f"Delivering Pepperoni Pizza with {self.sauce} sauce, {self.topping} topping and {self.crust} crust.")


class VeggiePizza(Pizza):

        def __init__(self, pizza_type: PizzaType, sauce, topping, crust):
            super().__init__(sauce, topping, crust)
            self.pizza_type = pizza_type

        def deliver(self):
            self.pizza_type.deliver()
            print(f"Delivering Veggie Pizza with {self.sauce} sauce, {self.topping} topping and {self.crust} crust.")




if __name__ == '__main__':


    american_pepperoni = PepperoniPizza(American(), "Tomato", "Pepperoni", "Thin")
    american_pepperoni.deliver()

    italian_veggie = VeggiePizza(Italian(), "Pesto", "Mushrooms", "Thick")
    italian_veggie.deliver()




