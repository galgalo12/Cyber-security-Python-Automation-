from ipywidgets import Dropdown, Button, Output, Layout, VBox
from IPython.display import display
from datetime import datetime
import json

# ==============================
# Model: Approved Users & Login Records
# ==============================
# username: approved list (case-insensitive)
usernames = ["keith", "john", "jimmy", "sarah"]
# Number of logins today
current_day_logins = [8, 7, 6, 9]
# Average login counts per day
average_day_logins = [4, 6, 1, 2]


# ==============================
# Helper function: Analyze logins
# ==============================
def analyze_login(username: str):
    """
    Analyzes the current day's login and compares with average login activity.
    Outputs results as JSON for SOC automation purposes.
    """
    username_lower = username.lower()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_event = {
        "username": username,
        "timestamp": timestamp,
        "user_approved": False,
        "current_day_logins": 0,
        "average_day_logins": 0,
        "login_ratio": 0,
        "anomaly_detected": False,
        "message": "",
    }

    if username_lower in [u.lower() for u in usernames]:
        ind = [u.lower() for u in usernames].index(username_lower)
        log_event["user_approved"] = True
        log_event["current_day_logins"] = current_day_logins[ind]
        log_event["average_day_logins"] = average_day_logins[ind]
        avg_day = average_day_logins[ind]

        # Calculate login ratio safely
        login_ratio = current_day_logins[ind] / avg_day if avg_day else 0
        log_event["login_ratio"] = round(login_ratio, 2)

        if login_ratio > 3:
            log_event["anomaly_detected"] = True
            log_event["message"] = "High login activity detected."
        else:
            log_event["message"] = "Login activity is within normal range."

    else:
        log_event["message"] = "User is not approved."

    # Print JSON output for automation
    print(json.dumps(log_event, indent=4))


# ==============================
# Widgets for SOC Automation
# ==============================
username_dropdown = Dropdown(
    options=usernames, description="Username:", layout=Layout(width="50%")
)
run_button = Button(description="Analyze Login", button_style="info", icon="check")
output_area = Output()


# Function to run when button is clicked
def on_button_click(b):
    output_area.clear_output()
    username = username_dropdown.value
    with output_area:
        analyze_login(username)


run_button.on_click(on_button_click)

# Display SOC automation panel
display(VBox([username_dropdown, run_button, output_area]))
