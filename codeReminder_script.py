import time
from plyer import notification
import gmailConfig

def remind_to_code():
    notification_title = "Coding Reminder"
    notification_message = "It's 7:00 AM! Time to start coding!"
    notification_timeout = 10  # Notification will stay for 10 seconds

    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout
    )

if __name__ == "__main__":
    # Set the time for the reminder (7:00 AM)
    reminder_time = "07:00"

    while True:
        # Get the current time
        current_time = time.strftime("%H:%M")

        # Check if it's time to remind
        if current_time == reminder_time:
            gmailConfig(remind_to_code)
            print("Email sent!")

        # Sleep for a minute before checking again
        time.sleep(60)
