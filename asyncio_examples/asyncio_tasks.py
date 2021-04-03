import asyncio
import time
from datetime import datetime


async def hello_world():
    print("hello")
    await asyncio.sleep(1)
    print("world")


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def hello_world2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    print(f"after hello at {time.strftime('%X')}")
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


async def hello_world3():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f} at {time.strftime('%X')}")
    return f


async def try_gather():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


async def try_gather2():
    # Schedule three calls *concurrently*:
    tasks = [
        asyncio.create_task(factorial("A", 2), name="fac2"),
        asyncio.create_task(factorial("B", 3), name="fac3"),
        asyncio.create_task(factorial("C", 4), name="fac4")
    ]
    await asyncio.gather(*tasks)

    return tasks


async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')


async def check_timeout():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')


async def foo():
    return 42


async def test_failed_wait():
    coro = foo()
    done, pending = await asyncio.wait({coro})

    if coro in done:
        print(coro)
        # This branch will never be run!


async def test_wait_passed():
    task = asyncio.create_task(foo())
    done, pending = await asyncio.wait({task})

    if task in done:
        print(f"{task.done()} result:{task.result()} is done")
        # Everything will work as expected now.


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(2)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def check_thread():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1),
        hello_world3()
    )

    print(f"finished main at {time.strftime('%X')}")


async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def check_cancel_me():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


async def check_thread_safe():
    loop = asyncio.get_event_loop()
    timeout = 3

    # Create a coroutine
    coro = asyncio.sleep(1, result=3)

    # Submit the coroutine to a given loop
    future = asyncio.run_coroutine_threadsafe(coro, loop)

    # Wait for the result with an optional timeout argument
    try:
        result = future.result(timeout)
    except asyncio.TimeoutError:
        print('The coroutine took too long, cancelling the task...')
        future.cancel()
    except Exception as exc:
        import traceback
        traceback.print_exc()
        print(f'The coroutine raised an exception: {exc!r}')
    else:
        print(f'The coroutine returned: {result!r}')


def run_coroutine1():
    # asyncio.run(hello_world())
    # asyncio.run(hello_world2())
    # asyncio.run(hello_world3())
    # asyncio.run(display_date())
    resp = asyncio.run(try_gather2())
    for x in resp:
        print(dir(x))
        print(x)
        print(x.result())
    # asyncio.run(check_timeout())
    # asyncio.run(test_failed_wait())
    # asyncio.run(test_wait_passed())
    # asyncio.run(check_cancel_me())
    # asyncio.run(check_thread())
    # asyncio.run(check_thread_safe())


if __name__ == '__main__':
    # hello world
    run_coroutine1()
    # print(hello_world())
    # Throws RuntimeWarning: coroutine 'hello_world' was never awaited
