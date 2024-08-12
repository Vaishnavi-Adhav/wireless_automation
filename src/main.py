from wifi_scanner import WiFiScanner
import asyncio
from bt_scanner import scan_and_connect


def main():
    # Wi-Fi Scanning and Connection
    wifi_scanner = WiFiScanner()
    wifi_scanner.scan()

    target_ssid = "Sanavi Forever"
    wifi_password = "Vaish@123"

    if target_ssid in wifi_scanner.networks:
        print(f"Network '{target_ssid}' found. Attempting to connect...")
        if wifi_scanner.connect_to_network(target_ssid, wifi_password):
            from utils.network_utils import test_connectivity
            test_connectivity()
        else:
            print("Failed to connect to the network.")
    else:
        print(f"Network '{target_ssid}' not found in the scan.")

    # Bluetooth Scanning and Connection
    target_device_name = "Nordic_Keyboard"
    asyncio.run(scan_and_connect(target_device_name))


if __name__ == "__main__":
    main()
