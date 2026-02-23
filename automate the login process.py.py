from datetime import datetime
import json

# Approved users and their assigned devices
approved_access = {
    "keith": "789uk",
    "john": "jfklsdjf",
    "jimmy": "9djflksf",
    "sarah": "342dfsf",
}


def login(username, device_id):
    username = username.lower()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_event = {
        "username": username,
        "device_id": device_id,
        "timestamp": timestamp,
        "user_approved": False,
        "device_authorized": False,
        "access_granted": False,
        "status": "DENIED"
    }

    if username in approved_access:
        log_event["user_approved"] = True

        if device_id == approved_access[username]:
            log_event["device_authorized"] = True
            log_event["access_granted"] = True
            log_event["status"] = "GRANTED"

    # Print formatted JSON
    print(json.dumps(log_event, indent=4))


def get_user_input():
    username = input("Enter username: ")
    device_id = input("Enter device ID: ")
    login(username, device_id)


get_user_input()
