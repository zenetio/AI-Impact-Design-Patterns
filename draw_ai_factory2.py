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

#factory_a = AIProductFactory(complexity="hard")
#product1 = factory_a.create_product()
#product1.display()

#factory_b = AIProductFactory(complexity="easy")
#product2 = factory_b.create_product()
#product2.display()


# 4. Illustration with Matplotlib

def draw_products(product_list):
    """Draws a figure showing the products based on their properties."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Products Created by AI Factory")
    ax.axis('off')  # Hide axes

    for i, product in enumerate(product_list):
        if isinstance(product, ProductA):
            ax.add_patch(plt.Rectangle((i*1.5, 0), 1, 1, facecolor='lightgray', edgecolor='black')) # A rectangle for the product
            ax.text(i*1.5 + 0.75, 0.5, f"Product A: {product.name}", ha='center', va='center')

        elif isinstance(product, ProductB):
            ax.add_patch(plt.Rectangle((i*1.5, 0), 1, 1, facecolor=product.color, edgecolor='black')) # Color for the product
            ax.text(i*1.5 + 0.75, 0.5, f"Product B: Color - {product.color}", ha='center', va='center')
    # Save figure to image directory
    plt.savefig("./images/factory_method_ai2.png")

    plt.show()


# Example Usage to draw the figure
products = [AIProductFactory(complexity="hard").create_product(), AIProductFactory(complexity="easy").create_product()]
draw_products(products)
