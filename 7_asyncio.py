import time
import asyncio

# simple task function
async def simple_task(number):
    # sleep 1 second
    await asyncio.sleep(1)
    # return number
    return number

# cancel task function
async def cancel_task(task):
    # wait 0.2 second
    await asyncio.sleep(0.2)
    # cancel task
    was_canceled = task.cancel()
    # print cancel task
    print(f'{time.ctime()} canceled: {was_canceled}')

# coroutine function
async def main():
    # create simple task
    coro = simple_task(1)
    # create a task for simple task
    task = asyncio.create_task(coro)
    # create the shielded task
    shielded = asyncio.shield(task)
    # create the task to cancel
    asyncio.create_task(cancel_task(shielded))
    # handle cancel
    try:
        # await shielded task
        result = await shielded
        print(f'{time.ctime()} > got: {result}')
    except asyncio.CancelledError:
        print(f'{time.ctime()} shielded was cancel')
    # sleep 1 second
    await asyncio.sleep(1)
    # print time task
    print(f'{time.ctime()} shielded: {shielded}')
    print(f'{time.ctime()} task: {task}')

# start
asyncio.run(main())

#
# Mon Jul 17 22:28:36 2023 canceled: True
# Mon Jul 17 22:28:36 2023 shielded was cancel
# Mon Jul 17 22:28:37 2023 shielded: <Future cancelled>
# Mon Jul 17 22:28:37 2023 task: <Task finished name='Task-2' coro=<simple_task() done, defined at /Users/tawankriangkraiwanich/Desktop/asyncio_class/7_asyncio.py:5> result=1>
#