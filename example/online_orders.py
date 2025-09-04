import asyncio
import time
import random
import multiprocessing as mp

# Function asynchronous
async def check_invetory(item):
    print(f'Checking invetory to {item}...')
    await asyncio.sleep(random.randint(3,6))
    print(f'Verify invetory to {item}')
    # Product availability
    return random.choice([True, False])

# Function asyn to processing the pay
async def process_payment(order_id):
    print(f'Processing payment to {order_id}...')
    # Simulate time to await what have a service of pay
    await asyncio.sleep(random.randint(3,6))
    print(f'Payment processing to {order_id}')
    return True

# Function the intencibe in CPU to calculate the total cost the order
def calculate_total(items):
    print(f'Calculating total of {len(items)} items...')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f'Cost total calculated is {total}')
    return total

async def process_order(order_id, items):
    print(f'Start processing order to {order_id}...')
    # Verify inventory to every order
    inventory_checks = [check_invetory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)

    if not all(inventory_results):
        print(f'Order processing failed for {order_id}')

    with mp.Pool() as pool:
        total = pool.apply(calculate_total, (items,))

    # Processing the pay async
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f'Payment processing succeeded for {order_id}\nTotal: {total}')
    else:
        print(f'Error processing payment for {order_id}')

async def main():
    orders = [
        {
            'order_id': 1,
            'items': [
                {'name': 'Laptop', 'price': 1000},
                {'name': 'Mouse', 'price': 100}
            ]
        },
        {
            'order_id': 2,
            'items': [
                {'name': 'Smartphone', 'price': 800},
                {'name': 'Headphones', 'price': 150}
            ]
        },
        {
            'order_id': 3,
            'items': [
                {'name': 'Monitor', 'price': 300},
                {'name': 'Keyboard', 'price': 120},
                {'name': 'Mousepad', 'price': 20}
            ]
        },
        {
            'order_id': 4,
            'items': [
                {'name': 'Tablet', 'price': 600}
            ]
        },
        {
            'order_id': 5,
            'items': [
                {'name': 'Printer', 'price': 250},
                {'name': 'Ink Cartridge', 'price': 60}
            ]
        }
    ]
    # Processing the multiples orders
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)

# Create the event loop
if __name__ == '__main__':
    asyncio.run(main())

