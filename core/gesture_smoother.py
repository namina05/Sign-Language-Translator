from collections import deque
from collections import Counter

class GestureSmoother:
    def __init__(self,history = 10):
        self.prediction_history = deque(maxlen=history)

    def smooth(self,prediction):
        self.prediction_history.append(prediction)
        most_common = Counter(self.prediction_history).most_common(1)

        return most_common[0][0]