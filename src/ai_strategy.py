# Example of Strategy Pattern with AI enhancement:
# Each strategy could leverage user_data (e.g., prefs) to produce tailored recommendations.

class Strategy:
    def recommend(self, user_data):
        # In a real AI-driven strategy, inspect user_data and apply ML models or heuristics
        pass

class ContentBased(Strategy):
    def recommend(self, user_data):
        # Would use user_data["prefs"] to match content features to user interests
        return "Content-based recommendation"

class CollaborativeFiltering(Strategy):
    def recommend(self, user_data):
        # Would use user_data across many users to find similar taste profiles
        return "Collaborative filtering recommendation"

# How to use:
if __name__ == "__main__":
    user_data = {"prefs": ["action", "drama"]}
    # In this stub, prefs are not consumed, but real strategies would analyze them.
    strat1 = ContentBased()
    print("ContentBased:", strat1.recommend(user_data))
    strat2 = CollaborativeFiltering()
    print("CollaborativeFiltering:", strat2.recommend(user_data))