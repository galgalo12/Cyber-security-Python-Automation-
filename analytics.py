from ipywidgets import widgets, Layout
from IPython.display import display
from csv import reader

# Widget 2
from ipywidgets import Dropdown, Button, Output, VBox
from IPython.display import display

# Model 1: Lists of approved users, current day logins, and average day logins
usernames = ["keith", "john", "jimmy", "sarah"]
current_day_logins = [8, 7, 6, 9]
average_day_logins = [4, 6, 1, 2]


# Define a function to analyze logins
def logins(username, current_day, average_day):
    # Check if the username is in the list of approved usernames
    if username in usernames:
        print(f"The user {username} is approved.")

        # Find the index of the username in the list
        ind = usernames.index(username)

        # Check if the current day and average day logins match the records
        if current_day_logins[ind] == current_day:
            print("Username has been active for", current_day, "days today.")
        else:
            print("Current day login record for", username, "is not valid.")

        if average_day_logins[ind] == average_day:
            # what is index? it is the position of the username in the list, which we use to access the corresponding current day and average day logins.
            print("On average, the user has been active for", average_day, "days.")
        else:
            print("Average day login record for", username, "is not valid.")
    else:
        print("The username", username, "is not approved to access the system.")


# Test the function with various inputs
logins("keith", 8, 4)
logins("john", 7, 6)
logins("jimmy", 6, 1)
# Case sensitivity issue
logins("Jimmy", 8, 7)  # This will print not approved because of case sensitivity
# Incorrect login records
logins("keith", 9, 5)

# ==============================

# Define the widgets
username_widget = widgets.Dropdown(
    options=usernames, description="Username:", layout=Layout(width="40%")
)
output = widgets.Output()

# Display the widget
display(username_widget, output)


# Define the update function to display login details
def update_login_details(change):
    output.clear_output()  # Clear the previous output
    username = change["new"]  # Get the new username
    if username in usernames:
        ind = usernames.index(username)  # Find the index of the username
        current_day = current_day_logins[ind]
        average_day = average_day_logins[ind]
        with output:
            print(f"Username: {username}")
            print(f"Current Day Logins: {current_day}")
            print(f"Average Day Logins: {average_day}")
    else:
        with output:
            print("Please select a valid username.")


# Attach the update function to the username widget
username_widget.observe(update_login_details, names="value")


# Model 2: Refined login function
def analyze_logins(username, current_day, average_day):
    if username in usernames:
        print("The user", username, "is approved.")
        ind = usernames.index(username)
        print(f"Username: {username}")

        if current_day == current_day_logins[ind]:
            print(f"Current Day Logins: {current_day}")
        else:
            print(
                f"Current day login record for {username} does not match. Expected: {current_day_logins[ind]}, Provided: {current_day}"
            )
            return  # Exit the function early if current day doesn't match

        print(f"Average Day Logins: {average_day_logins[ind]}")

        if average_day == average_day_logins[ind]:
            login_ratio = current_day / average_day
            print(f"Login Ratio: {login_ratio:.2f}")
            if login_ratio > 3:
                print("This account has MORE login activity than normal.")
    else:
        print("The username", username, "is not approved to access the system.")


# Test the refined function
analyze_logins("john", 7, 6)
analyze_logins("jimmy", 6, 1)
analyze_logins("sarah", 9, 2)
analyze_logins("Sarah", 8, 3)
analyze_logins("sarah", 9, 1)
analyze_logins("sarah", 3, 2)

# Create widgets for Model 2
username_dropdown = Dropdown(options=usernames, description="Username:")
run_button = Button(description="Analyze Logins", button_style="", icon="check")
output_area = Output()


def display_login_details(username):
    with output_area:
        output_area.clear_output()
        if username in usernames:
            ind = usernames.index(username)
            current_day = current_day_logins[ind]
            average_day = average_day_logins[ind]
            login_ratio = current_day / average_day if average_day else 0

            print(f"Username: {username}")
            print(f"Current Day Logins: {current_day}")
            print(f"Average Day Logins: {average_day}")
            if average_day:
                print(f"Login Ratio: {login_ratio:.2f}")
                if login_ratio > 3:
                    print("This account has more login activity than normal.")
            else:
                print("Cannot calculate login ratio due to zero average day logins.")
        else:
            print("Username not found in the approved list.")


# Button event
def on_run_button_clicked(b):
    display_login_details(username_dropdown.value)


run_button.on_click(on_run_button_clicked)

# Display the widgets
display(VBox([username_dropdown, run_button, output_area]))
