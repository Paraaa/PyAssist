import time
import threading


class ElapsedTimer(threading.Timer):
    started_at = None

    def start(self):
        self.started_at = time.time()
        threading.Timer.start(self)

    def elapsed(self):
        return time.time() - self.started_at

    def remaining(self):
        return self.interval - self.elapsed()
