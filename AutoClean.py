#!/usr/local/bin/python3

import asyncio
import os
from datetime import datetime

from pylitterbot import Account
from pylitterbot.enums import LitterBoxStatus

# Set email and password for initial authentication.
username = os.environ["LR_USERNAME"]
password = os.environ["LR_PASSWORD"]


async def main():
    # Create an account.
    account = Account()

    connected = False
    try:
        # Connect to the API and load robots.
        await account.connect(username=username, password=password, load_robots=True)
        connected = True

        if not account.robots:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] No robots found for this account.")
            return

        for robot in account.robots:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] Robot: {robot.name}")
            print(f"Status: {robot.status.text}")
            print(f"Power Status: {'On' if robot.is_online else 'Off'}")
            print(f"Litter Level: {robot.litter_level}%")
            print(f"Waste Drawer: {robot.waste_drawer_level}%")
            print(f"Firmware: {robot.firmware}")

            if robot.status == LitterBoxStatus.READY:
                print(f"[{now}] -> Starting cleaning cycle")
                await robot.start_cleaning()

    finally:
        # Disconnect from the API only if we actually connected.
        if connected:
            await account.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
