import re

def update_config_file(cfg_file, key, value, create_if_missing=False):
    try:
        with open(cfg_file, 'r') as file:
            lines = file.readlines()

        # Prepare to find both commented and uncommented versions of the key
        uncommented_pattern = re.compile(r'^\s*' + re.escape(key) + r'\s*=\s*.+', re.IGNORECASE)
        commented_pattern = re.compile(r'^\s*;\s*' + re.escape(key) + r'\s*=\s*.+', re.IGNORECASE)

        updated = False

        with open(cfg_file, 'w') as file:
            for line in lines:
                if uncommented_pattern.match(line):
                    file.write(f"{key}={value}\n")
                    updated = True
                elif commented_pattern.match(line):
                    # If key is commented out, uncomment and update
                    file.write(f"{key}={value}\n")
                    updated = True
                else:
                    file.write(line)

            if not updated:
                if create_if_missing:
                    # If the key is not found and creation is allowed, add it at the end
                    print(f"{key} not found in configuration file. Adding it at the end.")
                    file.write(f"\n{key}={value}\n")
                else:
                    print(f"Error: {key} not found and creation is disabled.")

        if updated or create_if_missing:
            print(f"Updated {key} to {value} in {cfg_file}")
        print("Restart Yate service to apply the changes.")

    except Exception as e:
        print(f"Failed to update configuration file: {e}")
