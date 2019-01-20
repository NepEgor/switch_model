from model_time.switch_class import Switch
from model_time.client_class import Client
from model_time.counter_class import Counter
from model_time.updater_class import Updater


def main():

    threads = []

    for i in range(510, 1010, 10):
        [updater,switch] = test(i)
        threads += [[updater.thread, switch]]

    for th in threads:
        print(th[1].number_of_clients)
        th[0].join()
        print(th[1].result())


def test(num):

    number_of_clients = num

    counter = Counter(number_of_clients)

    switch = Switch(number_of_clients, counter)
    clients = [Client(x, switch, counter) for x in range(number_of_clients)]

    updater = Updater(24*3600, clients)

    return [updater, switch]


if __name__ == '__main__':
    main()
