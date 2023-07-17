import asyncio
import time

# main coroutine function
async def main():
    # print to know the main coroutine started
    print(f'{time.ctime()} main coroutine started')
    # get current task
    task = asyncio.current_task()
    # print the current task
    print(f'{time.ctime()} {task}')

# start
asyncio.run(main())

#
# Mon Jul 17 22:26:24 2023 main coroutine started
# Mon Jul 17 22:26:24 2023 <Task pending name='Task-1' coro=<main() running at /Users/tawankriangkraiwanich/Desktop/asyncio_class/2_asyncio.py:11> cb=[_run_until_complete_cb() at /opt/homebrew/Cellar/python@3.9/3.9.16/Frameworks/Python.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py:184]>
#