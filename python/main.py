import asyncio
import api
import time
from concurrent.futures.thread import ThreadPoolExecutor


async def print_n(name: str) -> str:
    return name


async def main():
    # tasks = [api.fetch_data(i) for i in range(1, 100+1)]
    # await asyncio.sleep(2)
    # await asyncio.gather(*tasks)
    # print('done')
    # tasks = []
    for i in range(1, 100+1):
        api.fetch_data(i)
    #     tasks.append(api.fetch_post(i))
    # await asyncio.sleep(2)s
    # results = await asyncio.gather(*tasks)

    # print(f"Both tasks have completed now: {results}")


if __name__ == "__main__":
    t1 = time.perf_counter()
    asyncio.run(main())
    # main()
    t2 = time.perf_counter()

    print(f"time taken: {(t2-t1)}")
