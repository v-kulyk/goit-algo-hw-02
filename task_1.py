from queue import Queue

queue = Queue()

def generate_request():
    request = input("Введіть заявку: ")

    if request:
        queue.put(request)

def process_request():
    if queue.qsize() > 0:
        request = queue.get()

        print("Обробляємо заявку: " + request)
    else:
        print("Черга пуста")


def main():
    try:
        while (True):
            generate_request()
            process_request()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()