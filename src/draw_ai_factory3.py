import matplotlib.pyplot as plt
from ai_factory3 import AIProductFactory

def draw_factory_system():
    """Draws a comprehensive visualization of the AI Enhanced Factory system."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title("AI Enhanced Factory System", pad=20)
    ax.axis('off')

    # Draw Factory Components
    factory_box = plt.Rectangle((0.1, 0.6), 0.8, 0.3, facecolor='lightblue', edgecolor='black')
    ax.add_patch(factory_box)
    ax.text(0.5, 0.75, "AI Factory", ha='center', va='center', fontsize=12)

    # Draw AI Analysis Components
    ai_box = plt.Rectangle((0.1, 0.3), 0.3, 0.2, facecolor='lightgreen', edgecolor='black')
    ax.add_patch(ai_box)
    ax.text(0.25, 0.4, "AI Analyzer", ha='center', va='center', fontsize=10)

    # Draw Product Creation Components
    product_box = plt.Rectangle((0.6, 0.3), 0.3, 0.2, facecolor='lightyellow', edgecolor='black')
    ax.add_patch(product_box)
    ax.text(0.75, 0.4, "Product Creator", ha='center', va='center', fontsize=10)

    # Draw Connections
    ax.annotate('', xy=(0.4, 0.65), xytext=(0.25, 0.35),
               arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.65, 0.65), xytext=(0.75, 0.35),
               arrowprops=dict(arrowstyle='->', color='black'))

    # Draw Input/Output
    input_box = plt.Rectangle((0.1, 0.8), 0.1, 0.1, facecolor='white', edgecolor='black')
    ax.add_patch(input_box)
    ax.text(0.15, 0.85, "Input", ha='center', va='center', fontsize=8)

    output_box = plt.Rectangle((0.8, 0.8), 0.1, 0.1, facecolor='white', edgecolor='black')
    ax.add_patch(output_box)
    ax.text(0.85, 0.85, "Output", ha='center', va='center', fontsize=8)

    # Draw Example Products
    ax.text(0.15, 0.15, "Example Products:", fontsize=10)
    
    factory = AIProductFactory()
    
    # Create example products with different requirements
    products = [
        factory.create_product(["High performance", "Fast response"]),
        factory.create_product(["Energy efficient", "Low power"])
    ]

    for i, product in enumerate(products):
        x = 0.15 + i * 0.4
        ax.text(x, 0.1, product.display(), fontsize=8)

    # Save figure
    plt.savefig("./images/factory_method_ai3.png")
    plt.show()

# Run the visualization
draw_factory_system()