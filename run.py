# pylint: disable=invalid-name, broad-except
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
from rich.theme import Theme
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

# GLOBAL VARIABLE(S):
ALPHA = 0.05  # Standard significance level
test_records = SHEET.worksheet('test_records')  # Records sheet
records = test_records.get_all_values()  # Records values as nested lists
custom_theme = Theme(
    {"menu": "bright_green",
     "highlight": "bold bright_cyan",
     "error": "bright_red"})
console = Console(theme=custom_theme)
# Console object for use with rich.console


# MAIN MENU AND MAIN MENU OPTIONS:
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
    """ Main Menu and welcome screen. """
    while True:
        console.print("Ｔ－Ｔｅｓｔｅｒ", style="menu", justify="center")
        console.print("Main Menu", style="menu", justify="center")
        try:
            console.print("""
                        1. Help
                        2. Run Tests
                        3. View Records
                        4. Quit

                        At any time, press Ctrl+C/Cmd+C to quit.
                        """, style="menu")
            choice = int(input("""
                        Enter a number to make a selection,
                        and then press the "Enter" key:
        \n"""))
            if choice == 1:
                main_help_func()
                break
            elif choice == 2:
                testing_mode()
                break
            elif choice == (3):
                build_table()
                break
            elif choice == (4):
                quit_func()
                break
            else:
                raise ValueError
        except ValueError:
            msg = error_dict["menu_range"]
            error_wrapper(msg)
            continue
        except Exception as e:
            except_str(e)
            quit_func()


def return_to_main_menu():
    """ Guides user back to Main Menu screen when ready """
    while True:
        try:
            choice = input("Returning to Main Menu. Press Y to confirm.\n")
            if choice.upper() == "Y":
                main_menu()
            else:
                raise ValueError
        except ValueError:
            msg = error_dict["no_other_operations"]
            error_wrapper(msg)
            continue
        except Exception as e:
            except_str(e)
            quit_func()


# HELP SECTION:
help_files = {"run_tests": "help/run_tests.txt",
              "view_records": "help/view_records.txt",
              "delete_records": "help/delete_records.txt",
              "more_info": "help/more_info.txt", }


def print_file(file_path):
    """
    Opens a given txt file in read mode and outputs content.
    Offers user the option to show the help menu when ready.
    File will be closed upon exiting the with block.
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        contents = f.read(None)
        print(contents)
        show_menu(help_menu)


def show_menu(menu_name):
    """
    Maximise available terminal display while reading Help docs
    by showing menu only when asked.
    """
    console.print(("Finished reading? "
                   "Press Enter to show the menu."), style="highlight")
    show = input()
    if show:
        menu_name()


def help_text(topic):
    """
    Used within help_menu() to determine the help text shown.
    Uses print_file() to output the contents of the correct file.
    """
    try:
        if topic == 2:
            file_path = help_files["run_tests"]
        elif topic == 3:
            file_path = help_files["view_records"]
        elif topic == 4:
            file_path = help_files["delete_records"]
        elif topic == 5:
            file_path = help_files["more_info"]
        else:
            raise ValueError
    except ValueError as e:
        msg = e
        error_wrapper(msg)
    try:
        print_file(file_path)
    except Exception as e:
        except_str(e)
        return_to_main_menu()


def help_menu():
    """ Help Section Menu """
    while True:
        console.print("\nＯｐｔｉｏｎｓ", style="menu", justify="center")
        try:
            console.print("""
                        1. Return to Main Menu
                        2. Running Tests in T-Tester
                        3. Viewing Records
                        4. Deleting Records
                        5. More information""", style="menu")
            choice = int(input("""
                        Enter a number to make a selection,
                        and then press the "Enter" key:
        \n"""))
            if choice == 1:
                main_menu()
            elif choice > 1 and choice < 6:
                topic = choice
                help_text(topic)
            else:
                raise ValueError
        except ValueError:
            msg = error_dict["menu_range"]
            error_wrapper(msg)
            continue
        except Exception as e:
            except_str(e)
            return_to_main_menu()


def main_help_func():
    """ Offers user help in using the program """
    console.print("""[bold][bright_cyan]Welcome to T-Tester's Help section.[/][/]
This guide aims to instruct the user on the basic functions and processes of
the T-Tester program.

[bold][bright_cyan]To Exit the Program:[/][/]
Press Ctrl+C (Windows) or Cmd+C (Mac) at any time to quit the program.
Note that your work may not be saved. Alternatively, you may select the Quit
option from the Main Menu.

[bold][bright_cyan]To Use this Guide:[/][/]
Select a topic from the options below, and a brief guide will be displayed.
At the end of each topic, you will be prompted to return here when ready.""")
    help_menu()


# RECORDS & BUILD TABLE AREA:
def build_table():
    """ Build table from previous records """
    table = Table(title="Test Records")
    for heading in records[0]:
        table.add_column(f"{heading}", style="bright_cyan")
    for row in records[1::1]:
        table.add_row(*row)
    console.print(table, style="bright_blue", justify="center")
    records_menu()


def records_menu():
    """ Records Area Menu """
    while True:
        console.print("\nＯｐｔｉｏｎｓ", style="menu", justify="center")
        try:
            console.print("""
                        1. Return to Main Menu
                        2. Delete Last Record Shown
                        """, style="menu")
            choice = int(input("""
                        Enter a number to make a selection,
                        and then press the "Enter" key:
        \n"""))
            if choice == 1:
                main_menu()
            elif choice == 2:
                delete_last_record()
            else:
                raise ValueError
        except ValueError:
            msg = error_dict["menu_range"]
            error_wrapper(msg)
            continue
        except Exception as e:
            except_str(e)
            return_to_main_menu()


def delete_last_record():
    """
    Allows the user to delete the last record shown on the table
    or exit without making changes should they wish to abort.
    """

    def exit_with_feedback(feedback):
        """ Returns to previous menu with ample warning to user """
        print(feedback)
        sleep(2.5)
        records_menu()

    console.print("\nCaution: Deletion cannot be undone.\n", style="highlight")
    print("You are about to delete the most current test record on the table.")
    while True:
        confirm_delete = input("To confirm this action, type 'DELETE'."
                               "To exit, press any other key and hit Enter.\n")
        if confirm_delete == "delete":
            msg = error_dict["case_sensitive"]
            error_wrapper(msg)
            continue
        elif confirm_delete == "DELETE":
            try:
                test_records.delete_rows(len(records))
                feedback = ("Last record successfully deleted. "
                            "Returning to previous menu...")
                exit_with_feedback(feedback)
            except Exception as e:
                msg = (f"Operation failed.\nError: {e}.")
                error_wrapper(msg)
                feedback = "Exiting without making changes...\n"
                exit_with_feedback(feedback)
        else:
            feedback = "Exiting without making changes...\n"
            exit_with_feedback(feedback)


# DATA COLLECTION:
def get_tester_id():
    """
    Request user's name or organisational ID for records.
    Currently allows any name; however, in professional environments,
    an organisation ID may be required. """
    while True:
        tester_id = input("Enter a username or ID of your choice: \n")
        if tester_id == "":
            msg = "Username or ID required (e.g. SamBeckett, User1, etc.)"
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
                    msg = error_dict["subject_qty"]
                    error_wrapper(msg)
                    continue
                break
        except ValueError:
            msg = error_dict["subject_int"]
            error_wrapper(msg)
            continue
        except Exception as e:
            except_str(e)
            return_to_main_menu()
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
        console.print(f"\nYou entered: {last_input}")
        answer = input("Is this correct? Y/N \n")
        if answer.upper() == "Y":
            console.print("\nProceeding to next step...\n", style="highlight")
            sleep(.5)
            return True
        elif answer.upper() == "N":
            console.print(
                "\nReturning to previous step...\n", style="highlight")
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
            msg = error_dict["non_numeric_detected"]
            error_wrapper(msg)
            continue
        except Exception as e:
            except_str(e)
            return_to_main_menu()
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
        msg = (f"{len(sample)} values entered. "
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
    return_to_main_menu()


# DATA HANDLING:
def update_test_records(*args):
    """
    Updates test records stored in Google Sheets
    Currently uses *args for flexible development
    """
    console.print("\nUpdating test records...\n", style="highlight")
    test_records.append_row(args)
    sleep(.5)
    print("Record successfully updated.")
    print("You may need to re-start the program to view this "
          "record in the 'View Records' section.")


def date_and_time():
    """ Get time and date of test for records """
    now = datetime.datetime.now()
    test_time = now.strftime("%H:%M")
    test_date = now.strftime("%d.%m.%y")
    return test_date, test_time


# ERROR HANDLING & FORMATTING:
error_dict = {
    "menu_range":
        "Invalid Selection. Please enter a number from the options shown.",
    "no_other_operations":
        """No other operations available at this time.
    Press Y to return to Main Menu.""",
    "subject_int":
        """Must be numeric value. Whole numbers only (e.g. '7', not '7.2').
    Please try again.""",
    "subject_qty":
        "Five or more subjects required. Try again.",
    "non_numeric_detected":
        "Non-numeric characters detected. Try again.",
    "case_sensitive":
        "This option is case-sensitive. To delete, type 'DELETE'", }


def error_wrapper(msg):
    """ Wraps around error messages for greater legibility """
    console.print("\n- - - - - - - - - - - Error - - - - - - - - - - - - ",
                  style="error")
    console.print(msg, style="highlight")
    console.print("- - - - - - - - - - - - - - - - - - - - - - - - - - \n",
                  style="error")


def except_str(e):
    """
    Formatted feedback for Exceptions.
    Does not interfere with BaseException.
    """
    print("Sorry, something went wrong.")
    print(f"Error: {e}.")
    sleep(1)


# MAIN AS MAIN_MENU
main_menu()
