import gspread
from google.oauth2.service_account import Credentials
from scipy import stats

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

non_sig_a = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data
non_sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data
sig_a = [83.70, 81.50, 80.60, 83.90, 84.40]
sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]

sig_result = stats.ttest_ind(sig_a, sig_b)
non_sig_result = stats.ttest_ind(non_sig_a, non_sig_b)

ALPHA = 0.05  # significance level


def output_result():
    """
    Outputs results of t-tests to terminal in terms of significance
    """
    if non_sig_result[1] < ALPHA:
        print("Statistically significant difference")
    else:
        print("No statistically significant difference")
    if sig_result[1] < ALPHA:
        print("Statistically significant difference")
    else:
        print("No statistically significant difference")


output_result()
# Reminder: Expect a terminal of 80 characters wide and 24 rows high.
