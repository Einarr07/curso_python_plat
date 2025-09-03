import asyncio

async def process_data(data):
    print(f'Processing {data}...')
    await asyncio.sleep(10)
    print(f'{data} complete')
    return data * 2

async def main():
    print('Starting')
    result = await process_data(6)
    print(f'Result: {result}')
    print(f'{type(result)} complete')

asyncio.run(main())