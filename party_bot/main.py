import logging
import asyncio
from bot_app import *

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    asyncio.run(get_all_person())
