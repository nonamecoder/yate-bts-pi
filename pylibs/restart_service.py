import subprocess


def restart_service(service_name):
    try:
        # Check if the service exists
        status = subprocess.run(['systemctl', 'is-active', '--quiet', service_name])
        if status.returncode == 0:
            print(f"Service {service_name} is active, restarting...")
            subprocess.run(['sudo', 'systemctl', 'restart', service_name])
            print(f"Service {service_name} restarted successfully.")
        else:
            print(f"Service {service_name} is not active or not found.")
    except Exception as e:
        print(f"Failed to restart service: {e}")
