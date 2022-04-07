# pylint: disable=invalid-name
"""
Python program for data entry via terminal.
Once data is entered, a sequence of statistical
operations are carried out, until or unless:
  A) data is found unsuitable (input error, unequal variances),
  B) the expected flow of the program is completed,
  C) the user exits the program.
"""

import datetime
import gspread
from google.oauth2.service_account import Credentials
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


# Data for testing significant/non-significant sets:
non_sig_a = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88
non_sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88
sig_a = [83.70, 81.50, 80.60, 83.90, 84.40]  # Test data // m = 82.82
sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88


# Standard Variables:
ALPHA = 0.05  # significance level


# INPUT AREA:
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
            print(f"Welcome, {tester_id}.")
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
    Generic function in which the user can confirm their last input if correct.
    Deployed within loops:
    pass if correct, continue to repeat input.
    """
    while True:
        print(f"You entered: {last_input}")
        answer = input("Is this correct? Y/N \n")
        if answer.upper() == "Y":
            print("Proceeding to next step...")
            return True
        elif answer.upper() == "N":
            print("Returning to previous step...")
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
        msg = (f"{len(sample)} values entered. Expected {qty}.\nPlease begin this sample again.")
        error_wrapper(msg)
        return False


# OPERATIONS AREA:
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
        print(f"The mean average of Sample A ({a}) \nwas greater than Sample B ({b}).")
    else:
        print(f"The mean average of Sample B ({b}) \nwas greater than Sample A ({a}).")


# DATA HANDLING:
def update_test_records(*args):
    """
    Updates test records stored in Google Sheets
    Currently uses *args for flexible development
    """
    print("Updating test records...")
    test_records = SHEET.worksheet('test_records')
    test_records.append_row(args)
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
    print("- - - - - - - - - - - Error - - - - - - - - - - - - ")
    print(msg)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")


def main():
    """
    Main function to run all other functions in appropriate order
    """
    print("  🆃-🆃🅴🆂🆃🅴🆁")
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


main()


# Reminder: Expect a terminal of 80 characters wide and 24 rows high.
