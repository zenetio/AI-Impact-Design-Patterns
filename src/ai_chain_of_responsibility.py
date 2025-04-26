# ai_chain_of_responsibility.py

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.can_handle(request):
            return f"Handled by {self.__class__.__name__}"
        elif self.successor:
            return self.successor.handle(request)
        return "Request not handled"

    def can_handle(self, request):
        raise NotImplementedError()

class ConcreteHandlerA(Handler):
    def can_handle(self, request):
        return request < 10

class ConcreteHandlerB(Handler):
    def can_handle(self, request):
        return 10 <= request < 20

class ConcreteHandlerC(Handler):
    def can_handle(self, request):
        return request >= 20

# Traditional usage
if __name__ == "__main__":
    handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC()))
    for r in [5, 15, 25, 35]:
        print(f"Request: {r} -> {handler_chain.handle(r)}")

# AI-Enhanced usage
import random

class AIHandler:
    def __init__(self, handlers):
        self.handlers = handlers

    def handle(self, request):
        # AI predicts which handler can actually process the request
        capable = [h for h in self.handlers if h.can_handle(request)]
        # If no handler matches, fallback to full list
        pool = capable if capable else self.handlers
        # Dummy scoring: replace with real ML model prediction
        selected = max(pool, key=lambda h: random.random())
        return f"AI selected {selected.__class__.__name__} -> {selected.handle(request)}"

if __name__ == "__main__":
    handlers = [ConcreteHandlerA(), ConcreteHandlerB(), ConcreteHandlerC()]
    ai_handler = AIHandler(handlers)
    for r in [5, 15, 25, 35]:
        print(f"AI Request: {r} -> {ai_handler.handle(r)}")
