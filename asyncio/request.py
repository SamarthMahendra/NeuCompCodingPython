

import aiohttp
import asyncio



url = 'https://www.google.com'


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async  with session.get(url) as response:
            if (p:=response.status)==200:
                data =await response.text()
                print(data[:500])
            else:
                print("status code:", p)



# Wrap the call in a main coroutine
async def main():
    await make_request(url)

# Run the main coroutine
asyncio.run(main())
