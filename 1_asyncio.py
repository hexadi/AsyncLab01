# coroutine task
import asyncio

# sub coroutine function
async def custom_coro():
    # sleep 1 second
    await asyncio.sleep(1)

# main coroutine function
async def main():
    # execute sub coroutine function
    await custom_coro()

# start
asyncio.run(main())