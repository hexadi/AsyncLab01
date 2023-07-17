from random import random
import asyncio
import time

# task coroutine function
async def task_coro(arg):
    # generate value 0-1 with plus 1
    value = 1 + random()
    # print time and random value
    print(f'{time.ctime()} > task got {value}')
    # sleep for random value
    await asyncio.sleep(value)
    # print task done
    print(f'{time.ctime()} > task done')

# main coroutine function
async def main():
    # create a task
    task = task_coro(1)
    # execute the task and wait for timeout
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print(f'{time.ctime()} Gave up waiting, task canceled')
    
# start
asyncio.run(main())

#
# Mon Jul 17 22:28:14 2023 > task got 1.4967384413946299
# Mon Jul 17 22:28:14 2023 Gave up waiting, task canceled
#