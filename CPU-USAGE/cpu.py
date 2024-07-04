import psutil
import time
from plyer import notification  # Import the notification module from plyer

def send_notification(cpu_usage):
    """Sends a desktop notification when CPU usage exceeds the threshold."""
    notification.notify(
        title='High CPU Alert',
        message=f'Your CPU usage is at {cpu_usage}%. Please check your system.',
        timeout=10  # Notification disappears after 10 seconds
    )

def monitor_cpu_usage(alert_threshold, check_interval):
    """Monitors the CPU usage and sends a desktop notification if the threshold is exceeded."""
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"Current CPU usage: {cpu_usage}%")  # Still printing to console for logs
        if cpu_usage > alert_threshold:
            print(f"CPU usage exceeded {alert_threshold}%. Sending alert...")
            send_notification(cpu_usage)
        time.sleep(check_interval)

if __name__ == "__main__":
    try:
        alert_threshold = float(input("Enter the CPU usage percentage threshold for alerts: "))
        check_interval = float(input("Enter how often to check the CPU usage (in seconds): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

    monitor_cpu_usage(alert_threshold, check_interval)
