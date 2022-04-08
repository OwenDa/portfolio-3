# pylint: disable=invalid-name
"""
Python program for data entry via terminal.
Once data is entered, a sequence of statistical
operations are carried out, until or unless:
  A) data is found unsuitable (input error, unequal variances),
  B) the expected flow of the program is completed,
  C) the user exits the program.
"""

# IMPORTS:
import datetime
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from rich.table import Table
from scipy import stats
from numpy import mean

# APIs and Google Sheets:
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pp3')


# MAIN MENU:

def help_func():
    """ Offers user help in using the program """
    print("Help text has yet to be added.")
    print("Please make another selection.")


def testing_mode():
    """
    Triggers testing_main() function when selected from Menu
    """
    print("Entering Testing Mode...\n")
    sleep(1)
    testing_main()


def quit_func():
    """ Quits program after a short delay of 1 second """
    print("Quitting program...")
    sleep(1)
    quit()


def main_menu():
    """ Experimental feature """
    while True:
        print("                          🆃-🆃🅴🆂🆃🅴🆁")
        print("- - - - - - - - - - - - - Main Menu - - - - - - - - - - - - -")
        try:
            choice = int(input("""
                        1. Help
                        2. Run Tests
                        3. Quit

                        Enter a number to make a selection,
                        and then press the "Enter" key:
        \n"""))
            if choice == 1:
                help_func()
            elif choice == 2:
                testing_mode()
            elif choice == (3):
                quit_func()
            else:
                raise ValueError
        except ValueError:
            msg = "Invalid Selection. Please choose 1, 2 or 3."
            error_wrapper(msg)
            continue


# GLOBAL VARIABLE(S):
ALPHA = 0.05  # Standard significance level
test_records = SHEET.worksheet('test_records')  # Records sheet


# EXPERIMENTAL AREA:


def build_table():
    """ Build table from previous records """
    records = test_records.get_all_values()
    table = Table(title="Test Records")
    print(table)
    for heading in records[0]:
        table.add_column(f"{heading}")
    for row in records[1::1]:
        i = range(len(records)-1)
        print(i)
        table.add_row(f"{row[0]}")
    console = Console()
    console.print(table)


# DATA COLLECTION:


def get_tester_id():
    """
    Request user's name or organisational ID for records.
    Currently allows any name; however, in professional environments,
    an organisation ID may be required. """
    while True:
        tester_id = input("Enter a username or ID of your choice: \n")
        if tester_id == "":
            msg = "Username or ID required (e.g. 'SamBeckett', 'User1' etc.)"
            error_wrapper(msg)
            continue
        elif len(tester_id) < 2:
            msg = "Username must be at least 2 characters in length."
            error_wrapper(msg)
            continue
        else:
            print(f"\nWelcome, {tester_id}.\n")
            return tester_id


def collect_data():
    """
    Collect sample values from user input
    """
    while True:
        qty = get_qty_subjects()
        if confirm_proceed(qty):
            pass
        else:
            continue
        sample = get_sample()
        if validate_data(sample, qty):
            pass
        else:
            continue
        if confirm_proceed(sample):
            pass
        else:
            continue
        return sample


def get_qty_subjects():
    """
    Requests the number of subjects (ie. expected number of values) in sample
    """
    while True:
        try:
            while True:
                qty = int(input(
                    "Enter the number of subjects in this sample: \n"))
                if qty < 5:
                    msg = "Five or more subjects required."
                    error_wrapper(msg)
                    continue
                break
        except ValueError:
            msg = "Must be numeric value. Try again."
            error_wrapper(msg)
            continue
        else:
            return qty


def confirm_proceed(last_input):
    """
    Generic function in which the user can:
    - confirm their last input if correct or
    - return to previous step.
    Deployed within loops:
    pass if correct, continue to repeat input.
    """
    while True:
        print(f"\nYou entered: {last_input}")
        answer = input("Is this correct? Y/N \n")
        if answer.upper() == "Y":
            print("\nProceeding to next step...\n")
            sleep(.5)
            return True
        elif answer.upper() == "N":
            print("\nReturning to previous step...\n")
            sleep(.5)
            return False
        else:
            msg = "Press Y if correct, or press N to re-enter the data."
            error_wrapper(msg)
            continue


def get_sample():
    """
    Requests values contained within sample
    """
    while True:
        raw_data = input("Enter the values separated by commas: \n")
        try:
            sample = format_data(raw_data)
        except ValueError:
            msg = "Non-numeric value(s) detected. Try again."
            error_wrapper(msg)
            continue
        else:
            return sample


def format_data(data):
    """ Format data and remove errant characters """
    data = data.replace(" ", "")
    data = data.replace(",,", ",")
    data = data.split(",")
    data = list(filter(None, data))
    data = [float(i) for i in data]
    return data


def validate_data(sample, qty):
    """
    Ensures correct number of values per sample
    """
    if len(sample) == qty:
        return True
    else:
        msg = (f"{len(sample)} values entered."
               f"Expected {qty}.\nPlease begin this sample again.")
        error_wrapper(msg)
        return False


# STATISTICAL OPERATIONS:
def describe(sample):
    """ Output descriptive stats (mean and values) """
    mean_avg = round(mean(sample), 2)
    return mean_avg


def homogeneity_of_variance_check(a, b):
    """
    Performs Levene's Test to check suitability of data for t-test
      True = Suitable (p = >.05), null hypothesis cannot be rejected
      and equality of variance assumed.
      False = Unsuitable (p = <.05), reject null hypothesis,
      data is too heterogenous meet assumptions of ind. t-test.
    """
    result = stats.levene(a, b, center='mean')
    if result[1] > .05:
        return True
    else:
        return False


def t_test(first_sample, second_sample):
    """
    Outputs results of t-tests to terminal in terms of significance
    """
    test_values = stats.ttest_ind(first_sample, second_sample)
    if test_values[1] < ALPHA:
        t_test_result = "Statistically significant difference."
    else:
        t_test_result = "No statistically significant difference."
    return t_test_result


def output_means(a, b):
    """ Outputs mean averages in order of precedence """
    if a > b:
        print(f"The mean average of Sample A ({a}) \n"
              f"was greater than Sample B ({b}).")
    else:
        print(f"The mean average of Sample B ({b}) \n"
              f"was greater than Sample A ({a}).")


# DATA HANDLING:
def update_test_records(*args):
    """
    Updates test records stored in Google Sheets
    Currently uses *args for flexible development
    """
    print("\nUpdating test records...\n")
    test_records.append_row(args)
    sleep(.5)
    print("Record successfully updated.")


def date_and_time():
    """ Get time and date of test for records """
    now = datetime.datetime.now()
    test_time = now.strftime("%H:%M")
    test_date = now.strftime("%d.%m.%y")
    return test_date, test_time


# ERROR FORMATTING:
def error_wrapper(msg):
    """ Wraps around error messages for greater legibility """
    print("\n- - - - - - - - - - - Error - - - - - - - - - - - - ")
    print(msg)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - \n")


def testing_main():
    """
    Main test-mode function to run all other test-related functions
    """
    tester_id = get_tester_id()
    sample_a = collect_data()
    sample_b = collect_data()
    mean_a = describe(sample_a)
    mean_b = describe(sample_b)
    levene_result = homogeneity_of_variance_check(sample_a, sample_b)
    if levene_result:
        outcome = t_test(sample_a, sample_b)
        print(outcome)
        if outcome == "Statistically significant difference.":
            output_means(mean_a, mean_b)
    else:
        outcome = "T-test not conducted due to unequal variance."
        print("Data is unsuitable for t-test.")
        print("Reason: Lacks homogeneity of variance.")
    date_time = date_and_time()
    update_test_records(
            date_time[0], date_time[1], tester_id, mean_a, mean_b, outcome)


build_table()


# main_menu()


# Reminder: Expect a terminal of 80 characters wide and 24 rows high.
