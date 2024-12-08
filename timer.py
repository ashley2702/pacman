import time

class Timer:
    def __init__(self, limit):
        self.limit = limit
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def remaining_time(self):
        elapsed = time.time() - self.start_time
        return max(0, self.limit - elapsed)
