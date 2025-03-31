import matplotlib.pyplot as plt

# 1. The Factory Method Pattern (Basic Example)

class ProductA:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Product A: {self.name}")


class ProductB:
    def __init__(self, color):
        self.color = color

    def display(self):
        print(f"Product B: Color - {self.color}")


class AbstractFactory:
    def create_product(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteFactoryA(AbstractFactory):
    def create_product(self):
        return ProductA("Item A")

class ConcreteFactoryB(AbstractFactory):
    def create_product(self):
        return ProductB("Red")


# 2. Enhancing with AI -  Dynamic Product Creation based on Input

import random

class AIProductFactory(AbstractFactory):
    def __init__(self, complexity="medium"):
        self.complexity = complexity # Let's assume "easy", "medium", or "hard"

    def create_product(self):
        if self.complexity == "easy":
            return ProductA("Simple Item")  # Easy product
        elif self.complexity == "medium":
            return ProductB("Blue") # Medium complexity product
        elif self.complexity == "hard":
            # Simulate AI decision making (e.g., based on some data)
            if random.random() < 0.7:  # 70% chance of a complex product
                return ProductA("Complex Item")
            else:
                return ProductB("Green") # Other wise, return another B
        else:
            print(f"Unknown complexity level: {self.complexity}. Defaulting to medium.")
            return ProductB("Blue")


# 3. Usage Example

factory_a = AIProductFactory(complexity="hard")
product1 = factory_a.create_product()
product1.display()

factory_b = AIProductFactory(complexity="easy")
product2 = factory_b.create_product()
product2.display()


