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

sample_a = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data
sample_b = [83.7, 81.5, 80.6, 83.9, 84.4]  # Test data

result = stats.ttest_ind(sample_a, sample_b)

ALPHA = 0.05  # significance level


def output_result():
    """
    Outputs result of t-test to terminal in terms of significance
    """
    if result[1] < ALPHA:
        print("significance")
    else:
        print("non stat-sig")


output_result()
# Reminder: Expect a terminal of 80 characters wide and 24 rows high.
