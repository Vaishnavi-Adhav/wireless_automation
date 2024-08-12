# // TODO: Add unit tests for wifi_scanner.py and bt_scanner.py

def get_wireless_quote() -> str:
    return "The best wireless signal is the one you don't even notice."


def test_get_wireless_quote():
    expected_quote = "The best wireless signal is the one you don't even notice."
    assert get_wireless_quote() == expected_quote
