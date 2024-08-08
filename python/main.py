import threading


class ThreadLocalData:
    def __init__(self):
        self.local = threading.local()

    def set_data(self, key, value):
        setattr(self.local, key, value)

    def get_data(self, key):
        return getattr(self.local, key, None)


def thread_function(data_store, key, value):
    data_store.set_data(key, value)
    print(f"Thread {threading.current_thread().name} set {
          key} to {data_store.get_data(key)}")


def main():
    data_store = ThreadLocalData()

    # Create multiple threads
    thread1 = threading.Thread(target=thread_function, args=(
        data_store, 'data', 'value1'), name='Thread-1')
    thread2 = threading.Thread(target=thread_function, args=(
        data_store, 'data', 'value2'), name='Thread-2')

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
