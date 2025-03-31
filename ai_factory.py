import random  # For simulating AI decision making (simplified)

class ProductA:
    def display(self):
        print("Product A")

class ProductB:
    def display(self):
        print("Product B")


class AbstractFactory:
    def create_product(self):
        raise NotImplementedError  # Abstract method - to be implemented by subclasses


class AIControlledFactory(AbstractFactory):
    def __init__(self, complexity_level="medium"):
        self.complexity_level = complexity_level

    def create_product(self):
        if self.complexity_level == "high":
            if random.random() < 0.7:  # Simulate AI choosing ProductA
                return ProductA()
            else:
                return ProductB()
        elif self.complexity_level == "low":
            return ProductA() #Simple case
        else:  # Default
            return ProductB()


class TraditionalFactory(AbstractFactory):
    def create_product(self):
        return ProductA()   # Always creates ProductA


# Usage
if __name__ == "__main__":

    #Traditional usage
    traditional_factory = TraditionalFactory()
    product = traditional_factory.create_product()
    product.display() # Output: Product A


    # AI-controlled factory
    ai_factory = AIControlledFactory(complexity_level="high")  # Experiment with different levels
    product = ai_factory.create_product()
    product.display()

    ai_factory2 = AIControlledFactory(complexity_level="low")
    product = ai_factory2.create_product()
    product.display()
