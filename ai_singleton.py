class AIModelSingleton:
    _instance = None

    def __new__(cls, model_name):
        if cls._instance is None:
            print("Loading AI model...")
            cls._instance = super(AIModelSingleton, cls).__new__(cls)
            cls._instance.model_name = model_name
        return cls._instance

model1 = AIModelSingleton("GPT-4")
model2 = AIModelSingleton("GPT-4")

print(model1 is model2)  # True