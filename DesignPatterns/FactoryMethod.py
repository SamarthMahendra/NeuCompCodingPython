class CaneItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price}'

    def prepare(self):
        pass

class Size:

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'{self.size}'

    def get_size(self):
        return self.size


class Small(Size):

        def __init__(self):
            super().__init__('small')


class Medium(Size):

        def __init__(self):
            super().__init__('medium')

class Large(Size):

        def __init__(self):
            super().__init__('large')




class ChickenFingers(CaneItem):

    def __init__(self, size:Size =Small()):
        super().__init__('Chicken Fingers', 5.0)
        self.size = size

    def prepare(self):
        print(f'Preparing {self.name} of size : {self.size}.')

class CrinkleCutFries(CaneItem):

    def __init__(self, size:Size =Small()):
        super().__init__('Crinkle Cut Fries', 2.0)
        self.size = size

    def prepare(self):
        print(f'Preparing {self.name} of size : {self.size}.')


class TexasToast(CaneItem):

    def __init__(self, size:Size =Small()):
        super().__init__('Texas Toast', 1.0)
        self.size = size

    def prepare(self):
        print(f'Preparing {self.name} of size : {self.size}.')

class Coleslaw(CaneItem):

    def __init__(self, size:Size =Small()):
        super().__init__('Coleslaw', 1.0)
        self.size = size

    def prepare(self):
        print(f'Preparing {self.name} of size : {self.size}.')

# Create an abstract class RaisingCanesOrder with an abstract method createMenuItem(itemType: str) -> MenuItem.

from abc import ABC, abstractmethod

class RaisingCanesOrder(ABC):

        @abstractmethod
        def createMenuItem(self, itemType: str, size: Size) -> CaneItem:
            pass

class SimpleOrder(RaisingCanesOrder):

    def createMenuItem(self, itemType: str, size:Size = Small()) -> ChickenFingers | CrinkleCutFries | TexasToast | Coleslaw | None:
        if itemType == 'chicken_fingers':
            return ChickenFingers(size)
        elif itemType == 'fries':
            return CrinkleCutFries(size)
        elif itemType == 'texas_toast':
            return TexasToast(size)
        elif itemType == 'coleslaw':
            return Coleslaw(size)
        else:
            return


class ComboOrder(SimpleOrder):
    def createCombo(self, comboType: str):
        if comboType == "box_combo":
            return [
                self.createMenuItem("chicken_fingers", Size("medium")),
                self.createMenuItem("fries", Size("medium")),
                self.createMenuItem("texas_toast", Size("small")),
                self.createMenuItem("coleslaw", Size("small"))
            ]
        elif comboType == "caniac_combo":
            return [
                self.createMenuItem("chicken_fingers", Size("large")),
                self.createMenuItem("fries", Size("large")),
                self.createMenuItem("texas_toast", Size("medium")),
                self.createMenuItem("coleslaw", Size("medium"))
            ]
        else:
            raise ValueError(f"Unknown combo type: {comboType}")


# Client Code
def main():
    # Create a ComboOrder instance
    combo_order = ComboOrder()

    # Order a 'Box Combo'
    print("Ordering Box Combo:")
    box_combo_items = combo_order.createCombo("box_combo")
    for item in box_combo_items:
        item.prepare()

    print("\nOrdering Caniac Combo:")
    # Order a 'Caniac Combo'
    caniac_combo_items = combo_order.createCombo("caniac_combo")
    for item in caniac_combo_items:
        item.prepare()

if __name__ == "__main__":
    main()


