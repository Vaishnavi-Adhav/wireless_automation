# Bluetooth and WiFi Scanner Project

This project provides Python scripts for scanning Bluetooth and WiFi devices and utilities to facilitate logging and network operations. The project is structured into modules for easy management and scalability.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Bluetooth Scanner](#bluetooth-scanner)
  - [WiFi Scanner](#wifi-scanner)
- [Testing](#testing)
- [Utilities](#utilities)
  - [Logger](#logger)
  - [Network Utilities](#network-utilities)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project includes the following functionalities:

- **Bluetooth Scanner:** A script that scans for nearby Bluetooth devices and attempts to connect to a specific device.
- **WiFi Scanner:** A script to scan for nearby WiFi networks.
- **Utilities:** Helper functions for logging and network operations.

## Directory Structure
```
project_root/
│
├── src/
│ ├── bt_scanner.py # Bluetooth scanner script
│ ├── wifi_scanner.py # WiFi scanner script
│ ├── main.py # Main entry point for the project
│ └── utils/ # Utility functions and modules
│ ├── logger.py # Logging utility
│ └── network_utils.py # Network-related utilities
│
├── tests/
│ └── test_hello.py # Unit tests for the project
│
├── README.md # Project documentation
└── requirements.txt # Python dependencies
```


## Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- Virtual environment (recommended)

### Steps

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Vaishnavi-Adhav/wireless_automation.git
   cd project-name
   
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```
   
3. Install the required dependencies:
   ```bash
       pip install -r requirements.txt
   ```
   
## Usage
### Bluetooth Scanner
To run the Bluetooth scanner:

```bash
python src/bt_scanner.py
```
This script will scan for nearby Bluetooth devices and attempt to connect to a device with a specified name.

### WiFi Scanner
To run the WiFi scanner:

```bash
python src/wifi_scanner.py
```
This script will scan for nearby WiFi networks and display the list of available networks.

### Run entire framework
To run the entire automation framework

```bash
python src/main.py
```
This will run both Wi-Fi and Bluetooth scanners.

## Testing
The project includes unit tests located in the tests/ directory.

To run the tests, use:

```bash
pytest tests/
```
This will execute the test suite and provide feedback on code correctness.