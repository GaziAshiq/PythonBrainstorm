import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a delay
    print("Data fetched!")

async def main():
    await asyncio.gather(fetch_data(), fetch_data())

# Run the async function
asyncio.run(main())
