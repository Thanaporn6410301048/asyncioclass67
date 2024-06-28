# Before python 3.7 we manually create/get event loop and then schedule our task
import asyncio

async def some_async_task():
    print("sleeping for 1 seconds")
    await asyncio.sleep(1)
    print("done")

# Get the current event loop.
loop = asyncio.get_event_loop()

# Run until the coroutine is completed.
loop.run_until_complete(some_async_task())
