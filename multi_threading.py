#Multi threading is aphenomenon where multiple threads are defined in one process
# and performs all the threads simultaneously is a called multi-threading

import threading
def add(number):
    print(number+8)

def subtract(number):
    print(number-8)


if __name__ == "__main__":
    thread1 = threading.Thread(target=add,args=(45,))
    thread2 = threading.Thread(target=subtract,args=(45,))

    thread1.start()
    thread2.start()