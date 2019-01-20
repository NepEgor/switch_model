

class Counter:

    def __init__(self, number_of_clients):
        self.number_of_clients = number_of_clients
        # 0 - total number of tries, 1 - total number of successful connects
        self.tries = [[0 for x in range(number_of_clients)],
                      [0 for x in range(number_of_clients)]]

    def count(self, client, tries):
        assert client >= 0 and client < self.number_of_clients
        self.tries[0][client] += tries
        self.tries[1][client] += 1

    def avg(self):
        total_tries = sum(self.tries[0])
        success_tries = sum(self.tries[1])
        if success_tries == 0:
            return 0
        total_avg = total_tries / success_tries
        return [total_tries, success_tries, total_avg]
