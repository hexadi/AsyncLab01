import asyncio
import time

# task coroutine
async def task_coro(value):
    # print task executing
    print(f'{time.ctime()} task {value} executing')
    # sleep 1 second
    await asyncio.sleep(1)

# main coroutine function
async def main():
    # print time started
    print(f'{time.ctime()} main starting.')
    # create 10 coroutines
    coros = [task_coro(i) for i in range(10)]
    # run tasks gather
    await asyncio.gather(*coros)
    # print when it done
    print(f'{time.ctime()} main done')

# start
asyncio.run(main())

#
# Mon Jul 17 22:27:37 2023 main starting.
# Mon Jul 17 22:27:37 2023 task 0 executing
# Mon Jul 17 22:27:37 2023 task 1 executing
# Mon Jul 17 22:27:37 2023 task 2 executing
# Mon Jul 17 22:27:37 2023 task 3 executing
# Mon Jul 17 22:27:37 2023 task 4 executing
# Mon Jul 17 22:27:37 2023 task 5 executing
# Mon Jul 17 22:27:37 2023 task 6 executing
# Mon Jul 17 22:27:37 2023 task 7 executing
# Mon Jul 17 22:27:37 2023 task 8 executing
# Mon Jul 17 22:27:37 2023 task 9 executing
# Mon Jul 17 22:27:38 2023 main done
#