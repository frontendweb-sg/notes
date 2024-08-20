from concurrent.futures import ThreadPoolExecutor


def say_hi(name: str) -> None:
    print("Start....")
    print(name)


with ThreadPoolExecutor(max_workers=10) as exe:
    d = exe.submit(say_hi, 'pk')

    print('d', d._result)
