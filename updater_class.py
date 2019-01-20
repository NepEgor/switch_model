import threading


class Updater:

    def __init__(self, max_time, updatables):
        self.max_time = max_time
        self.updatables = updatables

        self.time = 0

        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while self.time <= self.max_time:

            for updatable in self.updatables:
                updatable.update(self.time)

            self.time += 1
