from datetime import datetime

# Approved users and their assigned devices
# username : device_id
approved_access = {
    "keith": "789uk",
    "john": "jfklsdjf",
    "jimmy": "9djflksf",
    "sarah": "342dfsf",
}


# Login logic
def login(username, device_id):

    # Make username case-insensitive
    username = username.lower()

    # Check if user is approved
    if username in approved_access:
        approval_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"✅ User '{username}' is approved.")
        print(f"🕒 Approved at: {approval_time}")

        # Validate device
        if device_id == approved_access[username]:
            print("✅ Access granted. Device is authorized.")
        else:
            print("❌ Access denied. Device is NOT authorized.")

    else:
        print("❌ Access denied. User is NOT approved.")


# Interactive input flow
def get_user_input():
    username = input("Enter username: ").lower()

    if username in approved_access:
        device_id = input("Enter your approved device ID: ")
        login(username, device_id)
    else:
        print("❌ Access denied. User is NOT approved.")


# ==========================
# Run interactive login
# ==========================
get_user_input()
