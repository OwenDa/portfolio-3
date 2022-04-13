# pylint: global-statement, disable=invalid-name, broad-except
"""
Python program for data entry via terminal.
Once data is entered and validated, a sequence of statistical
operations are carried out.

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

test_records = SHEET.worksheet('test_records')  # Records sheet
records = test_records.get_all_values()  # Records values as nested lists

# STYLING
custom_theme = Theme(
    {"menu": "bright_green",
     "highlight": "bold bright_cyan",
     "error": "bright_red",
     "sample_separator": "bold bright_green", })
console = Console(theme=custom_theme)
# Console object for use with rich.console


# *** MENU FUNCTIONS ***

def get_menu_options(options_list):
    """
    Takes a menu_options list as parament.
    Prints menu options to body of menus.
    """
    for item in options_list:
        console.print(f"    {item}", style="menu")


def validate_menu_choice(choice, menu_options_list):
    """
    Error handling for menu option selection:
    Raises an error if user choice is not within range of menu
    options available in a given menu_options_list, is blank
    input or non-numeric. Otherwise, returns True.
    """
    try:
        option_range = len(menu_options_list)
        if len(choice) == 0:
            raise ValueError(f"{error_dict['blank_input']}")
        if not choice.isdigit():
            raise TypeError(f"{error_dict['menu_range']}")
        choice = int(choice)
        if choice < 1 or choice > option_range:
            raise ValueError(f"{error_dict['menu_range']}")
    except TypeError as e:
        format_error_message(e)
        return False
    except ValueError as e:
        format_error_message(e)
        return False
    return True


# - Main Menu -

main_menu_options = ["1. Help",
                     "2. Run Tests",
                     "3. View Records",
                     "4. Quit", ]


def show_main_menu():

    """
    Main Menu and welcome screen. Prints options available and awaits input.
    Calls validation func to ensure choice is within range. Throws error and
    terminates program if:
    - Menu cannot be presented or
    - valid choice cannot be processed for any reason.
    """
    while True:
        try:
            console.print("Ｔ－Ｔｅｓｔｅｒ", style="menu", justify="center")
            console.print("Main Menu", style="menu", justify="center")
            get_menu_options(main_menu_options)
            console.print("\n    At any time, press Ctrl+C/Cmd+C to quit.",
                          style="menu")
            choice = input(
                """    Enter a number to make a selection, and then press the "Enter" key:
                \n""")
            try:
                if validate_menu_choice(choice, main_menu_options):
                    choice = int(choice)
                    if choice == 1:
                        main_help_func()
                        break
                    elif choice == 2:
                        testing_mode()
                        break
                    elif choice == 3:
                        records_menu()
                        break
                    elif choice == 4:
                        quit_func()
                        break
                    else:
                        raise Exception
                else:
                    continue
            except Exception as e:
                except_str(e)
                quit_func()
        except Exception as e:
            except_str(e)
            quit_func()


def return_to_main_menu():
    """
    Guides user back to Main Menu screen when ready. Throws an error in the
    event of any input other than y/Y and re-prompts user. If these actions
    cannot run for any reason, terminates program via quit_func().
    """
    try:
        while True:
            try:
                choice = input("Returning to Main Menu. Press Y to confirm.\n")
                if choice.upper() == "Y":
                    show_main_menu()
                else:
                    raise ValueError
            except ValueError:
                msg = error_dict["no_other_operations"]
                format_error_message(msg)
                continue
    except Exception as e:
        except_str(e)
        quit_func()


# - Help Menu -

help_menu_options = ["1. Return to Main Menu",
                     "2. Running Tests in T-Tester",
                     "3. Viewing Records",
                     "4. Deleting Records",
                     "5. More information", ]

help_files = {"run_tests": "assets/help-docs/run-tests.txt",
              "view_records": "assets/help-docs/view-records.txt",
              "delete_records": "assets/help-docs/delete-records.txt",
              "more_info": "assets/help-docs/more-info.txt", }


def main_help_func():
    """
    Offers user instructions to use the Help docs and calls
    help_menu() to print list of help topics available.
    File will close when program exits the 'with' block.
    """
    with open("assets/help-docs/help-intro.txt",
              mode="r", encoding="utf-8") as f:
        contents = f.read()
        console.print(contents)
    help_menu()


def help_menu():
    """
    Calls get_menu_options() to print available menu options and requests
    user input to make selection. Then calls validate_menu_choice() to
    validate selection. Finally, passes choice to help_text().
    If these operations cannot be run, alerts user and exits to Main Menu.
    """
    try:
        while True:
            console.print("\nＯｐｔｉｏｎｓ", style="menu", justify="center")
            get_menu_options(help_menu_options)
            choice = input(
                """    Enter a number to make a selection, and then press the "Enter" key:
                \n""")
            if validate_menu_choice(choice, help_menu_options):
                choice = int(choice)
                if choice == 1:
                    show_main_menu()
                elif choice > 1:
                    topic = choice
                    help_text(topic)
            else:
                continue
    except Exception as e:
        except_str(e)
        return_to_main_menu()


def help_text(topic):
    """
    Used within help_menu() to determine the topic shown.
    Calls print_file() to output the contents of the correct file
    based on key:filepath value stored in help_files dict.
    Throws error if invalid selection is made or these actions
    cannot be run.
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
        format_error_message(e)
    try:
        print_file(file_path)
    except Exception as e:
        except_str(e)
        return_to_main_menu()


def print_file(file_path):
    """
    Opens a given .txt file in read mode and outputs content.
    Calls show_menu() to provide option to show help menu when user
    is ready. Txt file will close upon exiting the 'with' block.
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        contents = f.read(None)
        console.print(contents)
        show_menu(help_menu)


def show_menu(menu_name):
    """
    Maximises available terminal display while reading Help docs by
    showing menu only after user input. Takes menu_name as parameter.
    This structure allows for reuse in case of future scaling.
    """
    console.print(("Finished reading? "
                   "Press Enter to show the menu."), style="highlight")
    show = input()
    if show:
        menu_name()


# - Records Menu -
records_menu_options = ["1. Return to Main Menu",
                        "2. Delete Last Record Shown", ]


def records_menu():
    """
    Calls functions to print Records menu options and to validate
    menu selection. For valid input, calls either main_menu or
    initiates process to delete last record.
    """
    try:
        while True:
            show_table()
            console.print("\nＯｐｔｉｏｎｓ", style="menu", justify="center")
            get_menu_options(records_menu_options)
            choice = input(
                """    Enter a number to make a selection, and then press the "Enter" key:
                \n""")
            if validate_menu_choice(choice, records_menu_options):
                choice = int(choice)
                if choice == 1:
                    show_main_menu()
                elif choice == 2:
                    delete_last_record()
            else:
                continue
    except Exception as e:
        except_str(e)
        return_to_main_menu()


def build_table():
    """
    Builds table from previous records stored in
    Google Sheets worksheet "test_records".
    """
    global test_records, records
    test_records = SHEET.worksheet('test_records')  # Google Sheet worksheet
    records = test_records.get_all_values()  # Records values as nested lists
    table = Table(title="Test Records")
    for heading in records[0]:
        table.add_column(f"{heading}", style="bright_cyan")
    for row in records[1::1]:
        table.add_row(*row)
    return table


def show_table():
    """ Retrieves table from build_table() and prints """
    table = build_table()
    console.print(table, style="bright_blue", justify="center")


def delete_last_record():
    """
    Allows user to delete the last record in table by typing a
    confirmation phrase OR exit without making changes.
    Throws error only in case of invalid (lowercase) confirmation phrase
    or if delete_rows() cannot be run. Provides feedback in all cases.
    """

    def exit_with_feedback(feedback):
        """ Returns to previous menu with ample warning to user """
        print(feedback)
        sleep(2.5)
        records_menu()

    console.print("\nCaution: Deletion cannot be undone.\n", style="highlight")
    print("You are about to delete the most current test record on the table.")
    while True:
        confirm_delete = input("To confirm this action, type 'DELETE'. "
                               "To exit, press Enter.\n")
        try:
            if confirm_delete == "delete":
                raise ValueError(error_dict["case_sensitive"])
        except ValueError as e:
            format_error_message(e)
            continue
        else:
            if confirm_delete == "DELETE":
                try:
                    test_records.delete_rows(len(records))
                    feedback = ("\nLast record successfully deleted.\n"
                                "Returning to previous menu...")
                    exit_with_feedback(feedback)
                except Exception as e:
                    msg = (f"Operation failed.\nError: {e}.")
                    format_error_message(msg)
                    feedback = "Exiting without making changes...\n"
                    exit_with_feedback(feedback)
            else:
                feedback = "Exiting without making changes...\n"
                exit_with_feedback(feedback)


# *** STATISTICAL TEST MODE ***
ALPHA = 0.05  # Standard significance level


def testing_mode():
    """
    Calls testing_main() function to enter program's testing
    mode, first alerting user and allowing time to read message.
    """
    console.print("Entering Testing Mode...\n", style="highlight")
    sleep(1)
    testing_main()


def testing_main():
    """
    Main statistical function to run all stats testing funcs.
    After calling all test funcs, provides appropriate output for test
    outcome. Calls update_test_records and finally exits to Main Menu.
    """
    tester_id = get_tester_id()
    console.print("\nSample A:", style="sample_separator")
    sample_a = collect_sample_data()
    console.print("\nSample B:", style="sample_separator")
    sample_b = collect_sample_data()
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
        print(("Levene's test was performed and homogeneity of "
               "variance was not found."))
    date_time = date_and_time()
    update_test_records(
            date_time[0], date_time[1], tester_id, mean_a, mean_b, outcome)
    return_to_main_menu()


# - Data Collection -


def get_tester_id():
    """
    Request user's name or organisational ID for records. Welcomes user
    by name/ID and returns the value for later use. Throws error if
    input is less than 2 characters or blank (empty). """
    while True:
        tester_id = input("Enter a username or ID of your choice: \n")
        try:
            if tester_id == "":
                raise ValueError(
                    "Username/ID required (eg. SamBeckett, User1, etc.)")
            if len(tester_id) < 2:
                raise ValueError("ID must be at least 2 characters in length.")
        except ValueError as e:
            format_error_message(e)
            continue
        else:
            print(f"\nWelcome, {tester_id}.\n")
            return tester_id


def collect_sample_data():
    """
    Main sample collection loop. Calls functions to gather subject quantity
    and sample values. Calls confirmation and validation functions. Returns
    only confirmed, validated data.
    """
    while True:
        qty = get_qty_subjects()
        if confirm_proceed(qty):
            pass
        else:
            continue
        sample = get_sample()
        if validate_sample_qty(sample, qty):
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
    and calls validation function to check the input. If these actions cannot
    be performed for any reason, throws error and returns to Main Menu.
    Note: qty MUST be cast as float after validation before converting to int.
    """
    while True:
        try:
            while True:
                console.print("Enter the number of subjects in this sample.",
                              style="highlight")
                qty = input(
                    "For example, enter '5' for a group with five subjects:\n")
                if validate_subject_qty(qty):
                    qty = float(qty)
                    qty = int(qty)
                    break
                else:
                    continue
            break
        except Exception as e:
            except_str(e)
            return_to_main_menu()
    return qty


def get_sample():
    """
    Requests values contained within sample. Calls format_sample_data()
    to format input. Throws error and alerts user if data invalid.
    """
    while True:
        console.print(("Enter the values or scores within this sample, "
                      "separated by commas"),
                      style="highlight")
        raw_data = input("For example: 2, 4.5, 13, 21, 26 \n\n")
        try:
            sample = format_sample_data(raw_data)
        except ValueError:
            msg = error_dict["non_numeric_detected"]
            format_error_message(msg)
            continue
        except Exception as e:
            except_str(e)
            return_to_main_menu()
        else:
            return sample

# Subsection: Sample Validation


def validate_subject_qty(qty):
    """
    Checks number of subjects as input by user. Raises specific
    errors if input is blank, decimal number that cannot be
    made whole without change of numeric value, non-numeric text,
    negative number or less than 5. Otherwise, returns True.
    """
    try:
        if qty == "":
            raise ValueError(f"{error_dict['blank_input']}")
        if not qty.isdigit():
            try:
                qty = float(qty)
            except Exception:
                raise ValueError(f"{error_dict['non_numeric_detected']}")
            else:
                if qty % 1 != 0:
                    raise ValueError(f"{error_dict['subject_int']}")
                else:
                    qty = int(qty)
        qty = int(qty)
        if qty < 0:
            raise ValueError(f"{error_dict['negative_number']}")
        if qty < 5:
            raise ValueError(f"{error_dict['subject_qty']}")
    except Exception as e:
        format_error_message(e)
        return False
    else:
        return True


def format_sample_data(data):
    """ Format input and remove errant characters """
    data = data.replace(" ", "")
    data = data.replace(",,", ",")
    data = data.split(",")
    data = list(filter(None, data))
    data = [float(i) for i in data]
    return data


def validate_sample_qty(sample, qty):
    """
    Ensures correct number of values per sample by comparing to previously
    entered input (qty). Throws error and returns False if values do not
    match. This will also catch empty input as "0" values cannot match qty.
    """
    try:
        if len(sample) != qty:
            raise ValueError(f"{len(sample)} values entered. Expected {qty}."
                             f" Please begin this sample again.")
    except ValueError as e:
        format_error_message(e)
        return False
    return True


# - Statistical Operations -


def describe(sample):
    """ Returns descriptive stats (mean average) of sample """
    mean_avg = round(mean(sample), 2)
    return mean_avg


def homogeneity_of_variance_check(a, b):
    """
    Performs Levene's Test to check data's suitability for t-test.
    True (p = > ALPHA) = Suitable: null hypothesis cannot be rejected
    and equality of variance assumed.
    False = Unsuitable, reject null hypothesis: data is too
    heterogenous to meet assumptions of ind. t-test.
    """
    result = stats.levene(a, b, center='mean')
    if result[1] > ALPHA:
        return True
    else:
        return False


def t_test(first_sample, second_sample):
    """
    Runs independent t-test on samples given.
    Compares sig value (p-value) to ALPHA to output results of
    t-test to terminal in terms of significance.
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


# - Update Test Records -


def update_test_records(*args):
    """
    Updates test records stored in Google Sheets and informs
    user.. Currently uses *args for flexible development.
    """
    console.print("\nUpdating test records...\n", style="highlight")
    test_records.append_row(args)
    sleep(.5)
    print("Record successfully updated.")
    print("You can view this record in the \n"
          "'View Records' section from the Main Menu.")


def date_and_time():
    """ Get time and date of test completion for records """
    now = datetime.datetime.now()
    test_time = now.strftime("%H:%M")
    test_date = now.strftime("%d.%m.%y")
    return test_date, test_time


# *** ERROR HANDLING & ERROR MESSAGES ***
error_dict = {
    "menu_range":
        "Invalid Selection. Please enter a number from the options shown.",
    "no_other_operations":
        """No other operations available at this time.
    Press Y to return to Main Menu.""",
    "subject_int":
        """Enter an integer (e.g. '7', not '7.2')).
    Please try again.""",
    "subject_qty":
        "Five or more subjects required. Try again.",
    "non_numeric_detected":
        "Non-numeric characters detected. Try again.",
    "case_sensitive":
        "This option is case-sensitive. To delete, type 'DELETE'",
    "blank_input":
        "Cannot be left blank. Please enter your input and press Enter.",
    "negative_number": "Enter a positive number, eg. 7 or 128.", }


def format_error_message(msg):
    """ Wraps around error messages for greater legibility """
    console.print(("\n- - - - - - - - - - - - - - - - - Error - "
                  "- - - - - - - - - - - - - - - - - "), style="error")
    console.print(msg, style="highlight")
    console.print(("- - - - - - - - - - - - - - - - - - - - - - - -"
                   " - - - - - - - - - - - - - -\n"), style="error")


def except_str(e):
    """
    Formatted feedback for Exceptions. Does not interfere with BaseException.
    In use, paired with quit_func() or return_to_main_menu() depending on
    failure (ie. failure to load Main Menu vs failure to load Help menu).
    """
    print("Sorry, something went wrong.")
    print(f"Error: {e}.")
    sleep(1)


# *** GENERIC FUNCTIONS & MAIN ***


def confirm_proceed(last_input):
    """
    Generic function in which the user can:
    - confirm their last input if correct or return to previous step.
    Displays error and prompts re-input in case of input other than Y/y/N/n.
    Deployed within loops elsewhere:
    - pass if True, continue to repeat input if False.
    """
    while True:
        console.print(f"\nYou entered: {last_input}")
        answer = input("Is this correct? Y/N \n")
        try:
            answer = answer.upper()
            if answer == "Y":
                console.print("\nProceeding to next step...\n",
                              style="green")
                sleep(.5)
                return True
            elif answer == "N":
                console.print("\nReturning to previous step...\n",
                              style="highlight")
                sleep(.5)
                return False
            else:
                raise ValueError("Press Y if correct, "
                                 "or press N to re-enter the data.")
        except ValueError as e:
            format_error_message(e)
            continue


def quit_func():
    """
    Quits program after alerting the user and providing a 1-second delay.
    If this fails for any reason, terminates program without further action.
    """
    try:
        print("Quitting program...")
        sleep(1)
        quit()
    except Exception:
        quit()


def main():
    """
    Main Function: Initiates the main menu which acts as
    welcome screen and provides options from which all other
    parts of the program can be accessed and operated.
    """
    show_main_menu()


main()
