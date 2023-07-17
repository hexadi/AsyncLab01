import asyncio
import time

# task coroutine function
async def task_coroutine(value):
    # report a message
    print(f'{time.ctime()} task {value} is running')
    # block for a moment
    await asyncio.sleep(1)

# main coroutine function
async def main():
    # print time and started
    print(f'{time.ctime()} main coroutine started')
    # start 10 tasks coroutine
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    # sleep 0.1 second
    await asyncio.sleep(0.1)
    # check all tasks
    tasks = asyncio.all_tasks()
    # print all tasks running
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name()}, {task.get_coro()}')
    for task in started_tasks:
        await task

# start
asyncio.run(main())

#
# Mon Jul 17 22:26:50 2023 main coroutine started
# Mon Jul 17 22:26:50 2023 task 0 is running
# Mon Jul 17 22:26:50 2023 task 1 is running
# Mon Jul 17 22:26:50 2023 task 2 is running
# Mon Jul 17 22:26:50 2023 task 3 is running
# Mon Jul 17 22:26:50 2023 task 4 is running
# Mon Jul 17 22:26:50 2023 task 5 is running
# Mon Jul 17 22:26:50 2023 task 6 is running
# Mon Jul 17 22:26:50 2023 task 7 is running
# Mon Jul 17 22:26:50 2023 task 8 is running
# Mon Jul 17 22:26:50 2023 task 9 is running
# Mon Jul 17 22:26:51 2023 > Task-9, <coroutine object task_coroutine at 0x1051f54c0>
# Mon Jul 17 22:26:51 2023 > Task-2, <coroutine object task_coroutine at 0x1051d4940>
# Mon Jul 17 22:26:51 2023 > Task-7, <coroutine object task_coroutine at 0x1051f53c0>
# Mon Jul 17 22:26:51 2023 > Task-4, <coroutine object task_coroutine at 0x10489e740>
# Mon Jul 17 22:26:51 2023 > Task-1, <coroutine object main at 0x1051d4540>
# Mon Jul 17 22:26:51 2023 > Task-10, <coroutine object task_coroutine at 0x1051f5540>
# Mon Jul 17 22:26:51 2023 > Task-3, <coroutine object task_coroutine at 0x1051d49c0>
# Mon Jul 17 22:26:51 2023 > Task-8, <coroutine object task_coroutine at 0x1051f5440>
# Mon Jul 17 22:26:51 2023 > Task-5, <coroutine object task_coroutine at 0x1051f52c0>
# Mon Jul 17 22:26:51 2023 > Task-11, <coroutine object task_coroutine at 0x1051f5640>
# Mon Jul 17 22:26:51 2023 > Task-6, <coroutine object task_coroutine at 0x1051f5340>
#