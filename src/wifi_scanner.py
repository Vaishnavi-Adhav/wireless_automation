import subprocess
import plistlib
from typing import Dict, Any
from tabulate import tabulate
from utils.logger import logger


class WiFiScanner:
    """
    Class to scan, display, and connect to Wi-Fi networks using macOS system profiler.
    """

    def __init__(self) -> None:
        self.networks: Dict[str, Dict[str, Any]] = {}
        self.raw_data: Any = None

    def scan(self) -> None:
        """
        Scans for available Wi-Fi networks using the system profiler and parses the results.
        """
        cmd = ["system_profiler", "SPAirPortDataType", "-xml"]
        try:
            output = subprocess.check_output(cmd)
            self.raw_data = plistlib.loads(output)
            logger.info("Raw data obtained successfully.")
            self.parse_wifi_info()
        except subprocess.CalledProcessError as e:
            logger.error(f"Error scanning networks: {e}")
        except Exception as e:
            logger.exception("Unexpected error during scanning:")

    def parse_wifi_info(self) -> None:
        """
        Parses the Wi-Fi information from the raw data obtained during scanning.
        """
        if not self.raw_data or not isinstance(self.raw_data, list) or len(self.raw_data) == 0:
            logger.warning("No valid raw data to parse.")
            return

        try:
            wifi_data = self.raw_data[0].get('_items', [])
            if not wifi_data:
                logger.warning("No Wi-Fi data found in raw data.")
                return

            for item in wifi_data:
                interfaces = item.get('spairport_airport_interfaces', [])
                for interface in interfaces:
                    if 'spairport_airport_local_wireless_networks' in interface:
                        self.parse_other_networks(interface['spairport_airport_local_wireless_networks'])

            if self.networks:
                self.display_networks()
            else:
                logger.warning("No networks found after parsing.")
        except Exception as e:
            logger.exception("Error parsing Wi-Fi info:")

    def parse_other_networks(self, other_networks: Any) -> None:
        """
        Parses the networks and stores them in the networks dictionary.
        """
        for network in other_networks:
            ssid = network.get('_name', 'Unknown')
            self.networks[ssid] = {
                'channel': network.get('spairport_network_channel', 'Unknown'),
                'phymode': network.get('spairport_network_phymode', 'Unknown'),
                'security': network.get('spairport_security_mode', 'Unknown'),
                'signal_noise': network.get('spairport_signal_noise', 'Unknown')
            }

    def display_networks(self) -> None:
        """
        Displays the scanned Wi-Fi networks in a tabular format.
        """
        headers = ["SSID", "Channel", "PHY Mode", "Security", "Signal/Noise"]
        table_data = [
            [ssid, info['channel'], info['phymode'], info['security'], info['signal_noise']]
            for ssid, info in self.networks.items()
        ]
        logger.info("\n" + tabulate(table_data, headers, tablefmt="grid"))

    def connect_to_network(self, ssid: str, password: str) -> bool:
        """
        Connects to a Wi-Fi network by SSID using the given password.

        Args:
            ssid (str): The SSID of the Wi-Fi network.
            password (str): The password of the Wi-Fi network.

        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        if ssid not in self.networks:
            logger.warning(f"SSID '{ssid}' not found in scanned networks.")
            return False

        cmd = ["networksetup", "-setairportnetwork", "en0", ssid, password]
        try:
            subprocess.check_call(cmd)
            logger.info(f"Successfully connected to {ssid}.")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Error connecting to {ssid}: {e}")
            return False
        except Exception as e:
            logger.exception("Unexpected error during connection:")
            return False


if __name__ == "__main__":
    scanner = WiFiScanner()
    scanner.scan()
