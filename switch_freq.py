import random
from pylibs.update_cfg import update_config_file
from pylibs.restart_service import restart_service


CONFIG_FILE_PATH = '/usr/local/etc/yate/ybts.conf'

# Frequency bands and corresponding ARFCN ranges
frequencies = {
    '850': (128, 251),
    '900': [(0, 124), (975, 1023)],  # Two ranges for EGSM900
    '1800': (512, 885),
    '1900': (512, 810)
}

def choose_arfcn(frequency):
    if frequency == '900':
        # EGSM900 has two ranges, choose randomly from one of them
        range_choice = random.choice(frequencies['900'])
        return random.randint(*range_choice)
    else:
        return random.randint(*frequencies[frequency])

def configure_yatebts():
    print("Choose a GSM frequency:")
    print("1. 850 MHz (GSM850)")
    print("2. 900 MHz (EGSM900)")
    print("3. 1800 MHz (DSC1800)")
    print("4. 1900 MHz (PCS1900)")

    choice = input("Enter the number corresponding to the frequency: ")

    frequency_map = {
        '1': '850',
        '2': '900',
        '3': '1800',
        '4': '1900'
    }

    if choice not in frequency_map:
        print("Invalid choice.")
        return

    frequency = frequency_map[choice]
    print(f"Selected frequency: {frequency} MHz")

    # Choose the ARFCN based on frequency
    arfcn = choose_arfcn(frequency)

    # Update the configuration file
    print(f"Setting Radio.Band={frequency} and Radio.C0={arfcn}")
    update_config_file(CONFIG_FILE_PATH, 'Radio.Band', frequency)
    update_config_file(CONFIG_FILE_PATH, 'Radio.C0', arfcn)

    # Restart the yatebts service if available
    restart_service('yatebts.service')


if __name__ == "__main__":
    configure_yatebts()
