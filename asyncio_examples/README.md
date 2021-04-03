Asyncio
=======


Functions:
---------
1. **asyncio.run**(coro, *, debug=False): _Execute the coroutine coro and return the result._
   - This function cannot be called when another asyncio event loop is running in the same thread.
   - This function always creates a new event loop and closes it at the end. It should be used as a main entry point 
   for asyncio programs, and should ideally only be called once
2. **asyncio.create_task**(coro, *, name=None): _Wrap the coro coroutine into a Task and schedule its execution. 
   Return the Task object._
3. _coroutine_ **asyncio.sleep**(delay, result=None, *, loop=None): _Block for delay seconds_.
4. _awaitable_ **asyncio.gather**(*aws, loop=None, return_exceptions=False): _Run awaitable objects in the aws 
   sequence concurrently._
5. _coroutine_ **asyncio.wait_for**(aw, timeout, *, loop=None): _Wait for the aw awaitable to complete with a timeout._
6. _awaitable_ **asyncio.shield**(aw, *, loop=None): _Protect an awaitable object from being cancelled._
7. _coroutine_ **asyncio.wait**(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED):
    _Run awaitable objects in the aws iterable concurrently and block until the condition specified by return_when._
   - Returns two sets of Tasks/Futures: (done, pending).
   > done, pending = await asyncio.wait(aws)
   - this function does not raise `asyncio.TimeoutError`. Futures or Tasks that aren’t done when the timeout occurs are
     simply returned inside the second set.
   
        | Constant | Description  |
        | -------- | ------------ |
        | FIRST_COMPLETED | The function will return when any future finishes or is cancelled. |
        | FIRST_EXCEPTION | The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED. |
        | ALL_COMPLETED | The function will return when all futures finish or are cancelled. |
   - The explicit passing of coroutine objects to asyncio.wait() is deprecated.
8. **asyncio.as_completed**(aws, *, loop=None, timeout=None): _Run awaitable objects in the aws iterable concurrently. 
   Return an iterator of coroutines. Each coroutine returned can be awaited to get the earliest next result 
   from the iterable of the remaining awaitables._
9. _coroutine_ **asyncio.to_thread**(func, /, *args, **kwargs): _Asynchronously run function func in a separate thread._
    * New in version 3.9
    * This coroutine function is primarily intended to be used for executing IO-bound functions/methods that 
      would otherwise block the event loop if they were run in the main thread.
10. **asyncio.run_coroutine_threadsafe**(coro, loop): _Submit a coroutine to the given event loop. Thread-safe._
11. **asyncio.all_tasks**(loop=None): _Return a set of not yet finished Task objects run by the loop._
12. **asyncio.current_task**(loop=None): _Return the currently running Task instance, or None if no task is running._
13. _class_ **asyncio.Task**(coro, *, loop=None, name=None) _A Future-like object that runs a Python coroutine._
    - Not thread-safe.
    - asyncio.Task inherits from Future all of its APIs except Future.set_result() and Future.set_exception().
    - **cancel**(msg=None): Request the Task to be cancelled.
14. **asyncio.iscoroutine**(obj): _Return True if obj is a coroutine object._  
15. **asyncio.iscoroutinefunction**(func): _Return True if func is a coroutine function._

Awaitables:
----------
- An object is an awaitable object if it can be used in an await expression.
- There are three main types of awaitable objects: `coroutines`, `Tasks`, and `Futures`.
    - **Coroutines**:
        + Python coroutines are awaitables.
    - **Tasks**:
        + Tasks are used to schedule coroutines concurrently.
    - **Futures**:
        + A Future is a special low-level awaitable object that represents an eventual result of 
          an asynchronous operation.
        + Future objects in asyncio are needed to allow callback-based code to be used with async/await.
    

Streams:
-------

##### Stream Functions:
1. _coroutine_ **asyncio.open_connection**(host=None, port=None, *, loop=None, limit=None, ssl=None, family=0, proto=0, 
   flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None):
   - _Establish a network connection and return a pair of (reader, writer) objects._
   
2. _coroutine_ **asyncio.start_server**(client_connected_cb, host=None, port=None, *, loop=None, limit=None, 
   family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, 
   reuse_port=None, ssl_handshake_timeout=None, start_serving=True):
    - _Start a socket server._



