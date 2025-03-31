import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

class ProductA:
    def __init__(self, name, complexity, ai_score):
        self.name = name
        self.complexity = complexity
        self.ai_score = ai_score

    def display(self):
        return f"Product A: {self.name}\nComplexity: {self.complexity}\nAI Score: {self.ai_score:.2f}"


class ProductB:
    def __init__(self, color, features, confidence):
        self.color = color
        self.features = features
        self.confidence = confidence

    def display(self):
        return f"Product B: Color - {self.color}\nFeatures: {', '.join(self.features)}\nConfidence: {self.confidence:.2f}"


class AbstractFactory:
    def create_product(self):
        raise NotImplementedError("Subclasses must implement this method")


class AIProductFactory(AbstractFactory):
    def __init__(self, data_analyzer=None):
        self.data_analyzer = data_analyzer if data_analyzer else DataAnalyzer()

    def create_product(self, requirements):
        analysis = self.data_analyzer.analyze(requirements)
        
        if analysis['complexity'] <= 0.3:
            return self._create_simple_product(analysis)
        elif analysis['complexity'] <= 0.7:
            return self._create_medium_product(analysis)
        else:
            return self._create_complex_product(analysis)

    def _create_simple_product(self, analysis):
        return ProductA(
            name="Simple Component",
            complexity="Low",
            ai_score=analysis['confidence']
        )

    def _create_medium_product(self, analysis):
        return ProductB(
            color=self._choose_color(analysis['features']),
            features=analysis['features'][:2],
            confidence=analysis['confidence']
        )

    def _create_complex_product(self, analysis):
        return ProductB(
            color=self._choose_color(analysis['features']),
            features=analysis['features'],
            confidence=analysis['confidence']
        )

    def _choose_color(self, features):
        # Simple AI color selection based on features
        if 'performance' in features:
            return 'red'
        elif 'efficiency' in features:
            return 'green'
        return 'blue'


class DataAnalyzer:
    def analyze(self, requirements):
        # Simulate AI analysis
        complexity = self._calculate_complexity(requirements)
        confidence = self._calculate_confidence(requirements)
        features = self._extract_features(requirements)
        
        return {
            'complexity': complexity,
            'confidence': confidence,
            'features': features
        }

    def _calculate_complexity(self, requirements):
        # Simulate complexity calculation
        return sum(len(req) for req in requirements) / (len(requirements) * 10)

    def _calculate_confidence(self, requirements):
        # Simulate confidence calculation
        return min(1.0, sum(len(req) for req in requirements) / 100)

    def _extract_features(self, requirements):
        # Simulate feature extraction
        features = []
        for req in requirements:
            if 'performance' in req.lower():
                features.append('performance')
            if 'efficiency' in req.lower():
                features.append('efficiency')
            if 'quality' in req.lower():
                features.append('quality')
        return features


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
    plt.savefig("./images/factory_method_ai2.png")
    plt.show()

# Run the visualization
draw_factory_system()