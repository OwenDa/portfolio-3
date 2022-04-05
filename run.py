"""
Python program for data entry via terminal.
Once data is entered, a sequence of statistical
operations are carried out, until or unless:
  A) data is found unsuitable (input error, unequal variances),
  B) the expected flow of the program is completed,
  C) the user exits the program.
"""

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

data_sheet = SHEET.worksheet('data')

# past_data = data.get_all_values()
# print(past_data)  # Testing sheet


# Data for testing significant/non-significant sets:
non_sig_a = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88
non_sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88
sig_a = [83.70, 81.50, 80.60, 83.90, 84.40]  # Test data // m = 82.82
sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88


# Standard Variables:
ALPHA = 0.05  # significance level


# INPUT AREA:
def collect_data():
    """
    Collect sample values from user input
    """
    while True:
        qty = int(input("Enter the number of subjects in this sample: "))
        if confirm_proceed(qty):
            pass
        else:
            continue
        raw_data = input("Enter the values separated by commas: ")
        sample = format_data(raw_data)
        if validate_data(sample, qty):
            pass
        else:
            continue
        if confirm_proceed(sample):
            pass
        else:
            continue
        return sample


def confirm_proceed(last_input):
    """
    Generic function in which the user can confirm their last input if correct.

    Deployed within loops:
    pass if correct, continue to repeat input.
    """
    while True:
        print(f"You entered: {last_input}")
        answer = input("Is this correct? Y/N ")
        if answer.upper() == "Y":
            print("Proceeding to next step...")
            return True
        elif answer.upper() == "N":
            print("Returning to previous step...")
            return False
        else:
            print("- - - - - - - - - - - Error - - - - - - - - - - - - ")
            print("Press Y if correct, or press N to re-enter the data.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")
            continue


def format_data(data):
    """ Format data and remove errant characters """
    data = data.replace(" ", "")
    data = data.replace(",,", ",")
    data = data.split(",")
    data = list(filter(None, data))
    data = [int(i) for i in data]
    return data


def validate_data(sample, qty):
    """
    Ensures correct number of values per sample
    """
    if len(sample) == qty:
        return True
    else:
        print("- - - - - - - - - - - Error - - - - - - - - - - - - ")
        print("Number of values entered does not match the number of")
        print("subjects expected. Please begin this sample again.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")
        return False


# OPERATIONS AREA:
def describe(sample):
    """ Output descriptive stats (mean and values) """
    mean_avg = round(mean(sample), 3)
    return mean_avg


def homogeneity_of_variance_check(a, b):
    """
    Performs Levene's Test and prints result
    """
    result = stats.levene(a, b)
    if result[1] < .05:
        print("Equal not variance assumed.")
    else:
        print("Equal variance assumed.")
    return result


# OUTPUT AREA:
def output_result(first_sample, second_sample):
    """
    Outputs results of t-tests to terminal in terms of significance
    """
    t_test_result = stats.ttest_ind(first_sample, second_sample)
    if t_test_result[1] < ALPHA:
        print("Statistically significant difference")
    else:
        print("No statistically significant difference")


#  def main():
    """
    Main function to run all other functions in appropriate order
    """
    #  sample_a = collect_data()
    #  sample_b = collect_data()
    #  mean_a = describe(sample_a)
    #  mean_b = describe(sample_b)
    #  levene_result = homogeneity_of_variance_check(sig_a, sig_b)
    #  print(levene_result)
    #  output_result(sample_a, sample_b)


sample_a = collect_data()
sample_b = collect_data()
mean_a = describe(sample_a)
mean_b = describe(sample_b)
print(mean_a, mean_b)

# Reminder: Expect a terminal of 80 characters wide and 24 rows high.
