import asyncio
from bleak import BleakClient, BleakScanner
from typing import Optional
from utils.logger import logger


async def scan_and_connect(target_name: str) -> Optional[bool]:
    """
    Scans for Bluetooth devices and connects to the specified device by name.

    Args:
        target_name (str): The name of the Bluetooth device to connect to.

    Returns:
        Optional[bool]: True if the connection is successful, False otherwise.
    """
    logger.info("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()

    for device in devices:
        if device.name and device.name == target_name:
            logger.info(f"Found device: {device.name} ({device.address})")
            return await connect_to_device(device.address)

    logger.warning(f"No device named {target_name} found.")
    return None


async def connect_to_device(device_address: str) -> bool:
    """
    Connects to a Bluetooth device by its address.

    Args:
        device_address (str): The Bluetooth address of the device.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        async with BleakClient(device_address) as client:
            if client.is_connected:
                logger.info(f"Connected to {device_address}")
                return True
            else:
                logger.error(f"Failed to connect to {device_address}")
                return False
    except Exception as e:
        logger.exception(f"Error connecting to {device_address}:")
        return False


if __name__ == "__main__":
    asyncio.run(scan_and_connect("Nordic_Keyboard"))
