import random
import asyncio
import time

# task coroutine function
async def task_coro(arg):
    # generate value 0-1
    value = random.random()

    # sleep from random
    await asyncio.sleep(value)

    # print task finish and time
    print(f'{time.ctime()} > task {arg} done with {value}')

# main coroutine function
async def main():
    # create 10 coroutine tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait all tasks completed
    done,pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # print time finish
    print(f'{time.ctime()} All done')

# start
asyncio.run(main())

#
# Mon Jul 17 22:27:59 2023 > task 6 done with 0.0822813408202423
# Mon Jul 17 22:28:00 2023 > task 3 done with 0.25530962538066826
# Mon Jul 17 22:28:00 2023 > task 9 done with 0.37094097269178095
# Mon Jul 17 22:28:00 2023 > task 2 done with 0.3914572427117584
# Mon Jul 17 22:28:00 2023 > task 5 done with 0.4500511730061245
# Mon Jul 17 22:28:00 2023 > task 4 done with 0.6469590062613823
# Mon Jul 17 22:28:00 2023 > task 1 done with 0.6645639053775061
# Mon Jul 17 22:28:00 2023 > task 8 done with 0.7579154929953257
# Mon Jul 17 22:28:00 2023 > task 7 done with 0.8127686195119902
# Mon Jul 17 22:28:00 2023 > task 0 done with 0.8863148863806385
# Mon Jul 17 22:28:00 2023 All done
#