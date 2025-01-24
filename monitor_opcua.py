import time
import csv
import logging
from opcua import Client, ua

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configuration
SERVER_URL = "opc.tcp://10.64.117.101:4840"
NODE_ID = "ns=1;s=/Default/Energy/ReadEnergy"
CSV_FILE = "opcua_data.csv"

def main():
    client = Client(SERVER_URL)
    client.timeout = 10  # Set timeout to 10 seconds
    try:
        logging.info("Connecting to OPC UA server...")
        client.connect()
        logging.info("Successfully connected to the OPC UA server.")

        node = client.get_node(NODE_ID)
        logging.info(f"Monitoring node: {NODE_ID}")

        # Initialize the previous value
        previous_value = None

        # Open the CSV file to store data
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            
            # Write headers if the file is empty
            if file.tell() == 0:
                writer.writerow(["Timestamp", "Value"])

            # Monitor node value in a loop
            while True:
                try:
                    data_value = node.get_value()
                    if data_value != previous_value:
                        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                        writer.writerow([timestamp, data_value])
                        logging.info(f"Data saved: {timestamp} - {data_value}")
                        previous_value = data_value
                    time.sleep(1)
                except ua.UaError as e:
                    logging.error(f"Error reading value: {e}")
                    time.sleep(1)  # Pause before retrying

    except KeyboardInterrupt:
        logging.info("Script interrupted by user.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    finally:
        try:
            logging.info("Disconnecting from OPC UA server...")
            client.disconnect()
            logging.info("Successfully disconnected.")
        except Exception as e:
            logging.error(f"Error during disconnection: {e}")

if __name__ == "__main__":
    main()
