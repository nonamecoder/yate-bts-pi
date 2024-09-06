import re
import asyncio
import subprocess
from pylibs.update_cfg import update_config_file


HOST = "localhost"
PORT = 5038
CONFIG_FILE_PATH = "/usr/local/etc/yate/ybts.conf"
SERVICE_NAME = "yate"


def check_service_status(service_name):
    try:
        result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        status = result.stdout.decode('utf-8').strip()
        if status == 'active':
            return True
        else:
            return False

    except Exception as e:
        print(f"An error occurred while checking the service status: {e}")
        return False

def parse_scan_report(output):
    arfcn_list = []
    pattern = r"ARFCN (\d+) (\d+) dB, (\d+(\.\d+)?) MHz"
    matches = re.findall(pattern, output)
    for match in matches:
        arfcn = int(match[0])
        noise_db = int(match[1])
        frequency_mhz = float(match[2])
        arfcn_list.append((arfcn, noise_db, frequency_mhz))
    return arfcn_list

async def send_command(reader, writer, command):
    writer.write(command.encode('utf-8') + b"\n")
    await writer.drain()
    await asyncio.sleep(2)  # Wait time to ensure the server has time to process
    response = await reader.read(4096)  # Read a large chunk of data
    return response.decode('utf-8', errors='ignore')

async def telnet_session():
    try:
        reader, writer = await asyncio.open_connection(HOST, PORT)

        await send_command(reader, writer, "mbts scan start")

        while True:
            output = await send_command(reader, writer, "mbts scan report")

            # Check if the response is empty
            if not output.strip():
                print("Received empty response, waiting for scan data...")
                await asyncio.sleep(5)  # Wait longer before retrying
                continue

            if "Scan not yet ready" in output:
                # Extract the recommended waiting period from the output
                match = re.search(r"Try again in (\d+(\.\d+)?) seconds", output)
                if match:
                    wait_time = float(match.group(1))
                    print(f"Scan not ready. Waiting for {wait_time} seconds...")
                    await asyncio.sleep(wait_time)
            else:
                # Parse and display the scan report
                print("Scan complete. Parsing results...")
                arfcn_list = parse_scan_report(output)
                for arfcn, noise_db, frequency_mhz in arfcn_list:
                    print(f"ARFCN: {arfcn}, Noise: {noise_db} dB, Frequency: {frequency_mhz} MHz")

                # Update configuration with the best ARFCN
                if arfcn_list:
                    print("Updating configuration file with the best ARFCN...")
                    best_arfcn = arfcn_list[0][0]  # Best ARFCN is the first in the list
                    update_config_file(CONFIG_FILE_PATH, "Radio.C0", best_arfcn)
                else:
                    print("No ARFCN found in the scan report.")
                    print("Scan failed, please try again in a few seconds, radio wasn't ready.")
                break

        # Stop the ARFCN scan
        print("Stopping ARFCN scan...")
        await send_command(reader, writer, "mbts scan stop")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    if (check_service_status(SERVICE_NAME)):
        asyncio.run(telnet_session())
    else:
        print(f"Service {SERVICE_NAME} is not running. Please start the service and try again.")
