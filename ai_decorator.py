class BaseClassifier:
    def classify(self, data):
        return "Base classification"

class AIEnhancedClassifier:
    def __init__(self, classifier):
        self.classifier = classifier
    
    def classify(self, data):
        base_result = self.classifier.classify(data)
        return f"{base_result} with AI Enhancement"

classifier = BaseClassifier()
ai_classifier = AIEnhancedClassifier(classifier)
print(ai_classifier.classify("data"))