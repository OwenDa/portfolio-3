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

data = SHEET.worksheet('data')

past_data = data.get_all_values()
print(past_data)  # Testing sheet


# Data for testing significant/non-significant sets:
non_sig_a = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88
non_sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88
sig_a = [83.70, 81.50, 80.60, 83.90, 84.40]  # Test data // m = 82.82
sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88


# Levene's Test Data and Testing Area:

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


levene_result = homogeneity_of_variance_check(sig_a, sig_b)
print(levene_result)


# Standard Variables:
ALPHA = 0.05  # significance level
sample_a = []
sample_b = []


def collect_data(sample):
    """
    Collect sample values from user input
    """
    while True:
        qty = int(input("Enter the number of subjects in this sample: "))
        for i in range(0, qty):
            num = float(input("Enter a value and press Enter: "))
            sample.append(num)
        print(sample)
        confirmation = input("Is this data correct? Y/N ")
        if confirmation.upper() == "Y":
            print("Move on to next collection.")
            break
        elif confirmation.upper() == "N":
            print("Repeat this collection.")
        else:
            print("Error: Incorrect input.")
            break
    return sample


collect_data(sample_a)
collect_data(sample_b)
print(f"Sample A: {sample_a}")
print(f"Sample B: {sample_b}")

t_test_result = stats.ttest_ind(sample_a, sample_b)
mean_a = round(mean(sample_a), 3)
mean_b = round(mean(sample_b), 3)
print(f"Sample A mean = {mean_a}.")
print(f"Sample B mean = {mean_b}.")


def output_result():
    """
    Outputs results of t-tests to terminal in terms of significance
    """
    if t_test_result[1] < ALPHA:
        print("Statistically significant difference")
    else:
        print("No statistically significant difference")


output_result()


# Reminder: Expect a terminal of 80 characters wide and 24 rows high.
