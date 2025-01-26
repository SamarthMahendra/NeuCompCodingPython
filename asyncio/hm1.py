import asyncio

async def fetch_data1():
    print("Fetching data 1...")
    await asyncio.sleep(2)
    print("Data 1 fetched!")

async def fetch_data2():
    print("Fetching data 2...")
    await asyncio.sleep(1)  # Oops! Missing something here?
    print("Data 2 fetched!")

async def main():
    await asyncio.gather(fetch_data1(), fetch_data2())  # Oops! Missing something here?

asyncio.run(main())
