import random


class Client:

    load = 360  # sec = 0.1 erl
    connect_wait_time = 15  # sec
    call_delay_time = 3600  # sec

    def __init__(self, id, switch, counter):
        self.switch = switch
        self.counter = counter
        self.channel = -1  # -1 for disconnected

        self.id = id

        self.__try_number = 0
        self.__stage = 0
        self.__stages = [self.__delay, self.__try, self.__call]
        self.__wait_for = 0

    # True if retry again, False if give up
    @staticmethod
    def retry(try_number):
        if try_number == 0:
            return True
        rnd = random.random()
        if try_number < 3:
            return rnd <= 0.9
        if try_number < 5:
            return rnd <= 0.75
        return rnd <= 0.6

    def update(self, time):
        if time < self.__wait_for:
            return

        delta = self.__stages[self.__stage]()
        # print(self.__stage, delta)
        self.__wait_for = time + delta

    def __delay(self):  # 0
        self.channel = self.switch.disconnect(self.channel)
        self.__try_number = 0

        self.__stage = 1
        return random.random() * Client.call_delay_time

    def __try(self):  # 1
        if Client.retry(self.__try_number):
            self.channel = self.switch.connect()
            self.__try_number += 1
            if self.channel != -1:
                # print('connected')
                self.__stage = 2
                return 0

            # print('try again')
            return Client.connect_wait_time

        # print('give up')
        self.__stage = 2
        return 0

    def __call(self):  # 2
        time = Client.load
        if self.channel == -1:
            time = 0

        self.counter.count(self.id, self.__try_number)

        self.__stage = 0
        return time
