class OldPredictionSystem:
    def classify(self, input_data):
        return "Old System Classification"

class AIAdapter:
    def __init__(self, old_system):
        self.old_system = old_system
    
    def predict(self, data):
        return self.old_system.classify(data)

old_system = OldPredictionSystem()
adapter = AIAdapter(old_system)
print(adapter.predict("input data"))