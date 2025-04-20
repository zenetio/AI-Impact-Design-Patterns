class Observer:
    def update(self, event_data):
        pass

class SecuritySystem:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, event_data):
        if AIThreatAnalyzer.is_real_threat(event_data):
            for observer in self._observers:
                observer.update(event_data)

class SecurityAlert(Observer):
    def update(self, event_data):
        print(f"Security Alert: {event_data}")

class AIThreatAnalyzer:
    @staticmethod
    def is_real_threat(event_data):
        return "malware" in event_data.lower()
    
# Example usage
if __name__ == "__main__":
    # 1. Initialize the security system and attach an alert observer
    security_system = SecuritySystem()
    alert = SecurityAlert()
    security_system.add_observer(alert)

    # 2. Send an event without a real threat — no output expected
    event_data = "User login successful"
    security_system.notify_observers(event_data)

    # 3. Send an event indicating malware — triggers the alert
    event_data = "Malware detected in system scan"
    security_system.notify_observers(event_data)