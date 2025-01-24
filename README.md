OPC UA Data Monitor

This Python script connects to an OPC UA server, retrieves real-time data from a specified node, and logs the values into a CSV file when changes occur.

Features

Connects to an OPC UA server.

Monitors a specific node for value changes.

Saves timestamped values to a CSV file.

Implements error handling and logging.

Gracefully handles user interruptions.

Requirements

Python 3.x

opcua library (pip install opcua)

Installation

pip install opcua

Usage

Update SERVER_URL and NODE_ID in monitor_opcua.py.

Run the script:

python monitor_opcua.py

The script will continuously monitor and log changes to opcua_data.csv.

To stop, press Ctrl + C.

Configuration

Modify these variables as needed:

SERVER_URL = "opc.tcp://10.64.117.101:4840"
NODE_ID = "ns=1;s=/Default/Energy/ReadEnergy"
CSV_FILE = "opcua_data.csv"



