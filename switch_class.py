

class Switch:

    number_of_channels = 6
    load_threshold = 0.8

    def __init__(self, number_of_clients, counter):
        self.number_of_clients = number_of_clients
        self.counter = counter

        self.channels = [False for x in range(self.number_of_channels)]
        self.load = 0

    def connect(self):
        for i in range(Switch.number_of_channels):
            if not self.channels[i]:
                if i < Switch.number_of_channels:
                    self.channels[i] = True
                    self.load = sum(self.channels) / Switch.number_of_channels
                    return i
                else:
                    if self.load >= Switch.load_threshold:
                        self.channels[i] = True
                        self.load = sum(self.channels) / Switch.number_of_channels
                        return i
        return -1

    def disconnect(self, channel):
        assert channel in range(-1,Switch.number_of_channels)
        if channel != -1:
            self.channels[channel] = False
        return -1

    def update(self, time):
        print(self.load, sum(self.channels), self.counter.avg())

    def result(self):
        return [self.load, sum(self.channels), self.counter.avg()]
