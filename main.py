import asyncio
from fast import fast
from agents import manual_agent, wdio_agent

# from agents import bulk_wdio_agent


async def main():
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
