import subprocess


def test_connectivity(hostname: str = "8.8.8.8") -> bool:
    """
    Tests network connectivity by pinging a specified hostname.

    Args:
        hostname (str): The hostname or IP address to ping.

    Returns:
        bool: True if the ping is successful, False otherwise.
    """
    cmd = ["ping", "-c", "4", hostname]
    try:
        subprocess.check_call(cmd)
        print("Connectivity test passed. Ping successful.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Connectivity test failed: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error during connectivity test: {e}")
        return False
