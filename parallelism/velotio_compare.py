
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

import requests
from aiohttp import ClientSession


def fetch_url_data(pg_url):
    try:
        resp = requests.get(pg_url)
    except Exception as ex:
        print(f"Error occured during fetch data from url{pg_url}")
    else:
        return resp.content


def get_all_url_data(url, ntimes):
    url_list = [url] * ntimes
    with ProcessPoolExecutor() as executor:
        resp = executor.map(fetch_url_data, url_list)
    return resp


def run_multithread():
    url = "https://www.velotio.com/careers"
    for ntimes in [1, 10, 50, 100, 500]:
        start_time = time.time()
        responses = get_all_url_data(url, ntimes)
        print(f'Fetch total {ntimes} urls and process takes {time.time() - start_time} seconds')


async def async_fetch_url_data(session, url):
    try:
        async with session.get(url, timeout=60) as response:
            resp = await response.read()
    except Exception as ex:
        print(ex)
    else:
        return resp
    return


async def fetch_async(loop, r):
    url = "http://www.velotio.com/careers"
    tasks = []
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(async_fetch_url_data(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses


def run_asyncio():
    for ntimes in [1, 10, 50, 100, 500]:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(loop, ntimes))
        loop.run_until_complete(future)   # will run until it finish or get any error
        responses = future.result()
        print(f'Fetch total {ntimes} urls and process takes {time.time() - start_time} seconds')


if __name__ == '__main__':
    run_multithread()
    # run_asyncio()
