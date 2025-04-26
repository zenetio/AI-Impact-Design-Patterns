class AIModelBuilder:
    def __init__(self):
        self.model = {}
    
    def set_layers(self, layers):
        self.model["layers"] = layers
        return self
    
    def set_optimizer(self, optimizer):
        self.model["optimizer"] = optimizer
        return self
    
    def build(self):
        return self.model

builder = AIModelBuilder()
model = builder.set_layers(3).set_optimizer("Adam").build()
print(model)