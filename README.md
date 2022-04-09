Ｔ－Ｔｅｓｔｅｒ

T-Tester is a simple and adaptable tool that runs in the terminal and can be adapted to any number of business needs and other scenarios.  

## Contents
1. [Overview](#overview)  
2. [User Stories](#user-stories)
    + [Sample Datasets](#sample-datasets)
3. [Tech Stack](#tech-stack)  
4. [Features](#features)
    + [Future Features](#future-features)
5. [Testing](#testing)
6. [Deployment](#deployment)  
7. [Acknowledgements](#acknowledgements) 
  
## Overview  
As the name may suggest, the primary function of T-Tester is to carry out the statistical test known as a t-test. While there are several forms of t-test, also known as Student's t-test, perhaps the most commonly used is the independent t-test.  
  
Developed by William Sealy Gossett, publishing under the pseudonym Student, t-tests are frequently implemented to check the reliability and generalisability of an apparent difference in mean averages.  As a brief example, one might imagine a survey in which the heights of 100 people from two different regions are recorded. The mean average height from Region A is unlikely to be identical to that of Region B. However, such a difference may result from either random chance or be reflective of a real-world difference. In this scenario, the researcher's objective is to assess the reliability of this difference via statistical analysis. A difference that meets the test's criteria to be considered reliable can be referred to as a statistically significant difference.  
  
Other examples where a t-test might be deployed include:  
- Comparing the mean average weekly (or other interval) sales within two branches of a store chain.  
- Comparing the mean average weekly (or other interval) sales of one store from two different years or quarters.  
- Comparing batches of consumable goods for consistency and quality control.  
- Quality control of any goods where mean averages can be used for assessment; for example, ensuring that each batch of household paint produced contains consistent amounts of all chemicals used in manufacturing.  
- Comparing customer satisfaction scores between agents or representatives providing services on behalf of a company.  
- Expenditure comparisons; for example, average monthly expenditure for two office branches.   
- Cost comparisons; for example, comparing the average amount billed by two different service utility providers over a given period where bills are not a fixed monthly amount.
- Time comparison, such as in comparing the average time taken to perform a given task.  
  
T-Tester then is an adaptable tool that can be deployed to almost any scenario in which a t-test may be used. Although discussed in more detail in the [Features](#features) section, T-Tester's functions, in brief, include:  

- Help menu allowing the user to access instructions for use within the program itself.  
- Gathering sample data for two samples.
- Carrying out pre-test checks:  
    + Ensuring the number of data points (subjects) in each sample is adequate for testing.
    + Testing for homogeneity of variance, an assumption of the t-test which, if not met, may mean the data is not suitable for a t-test.  
- Executing an independent t-test and outputting the result to the user in a simplified format, for example:  
    + No statistically significant difference found 
    + Statistically significant difference. The mean average of Sample A (3.44) was greater than that of Sample B (2.88).  
- Saving results to a spreadsheet alongside the time and date of the test as well as the name or organisational ID of the user conducting the test.
- Allowing the user to view previous records in a formatted table within the terminal.  
- Allowing the user to delete the last record shown within the table; for example, where a test is erroneously carried out twice.  
  
To explore these features with sample data, see [Sample Datasets](#sample-datasets) below.  
  
## User Stories  
  
### Sample Datasets:  
To test different outcomes, the reader may wish to make use of the sample datasets below. 

**How to Use Sample Datasets:**  
Keeping this README document open for reference, [launch the program](https://t-tester.herokuapp.com/). Select "Run Tests" from the menu by pressing the associated number in the menu (e.g. 2) on your keyboard. When entering input, you must then use the Enter key on your keyboard to submit your input.  
  
You will be asked to enter a username or ID of your choosing. This must be two or more characters in length. Type your chosen username and again press Enter.  
  
When prompted, enter the number of subjects in the first sample of your chosen dataset. This must be entered as an integer (ie. "5", not "five" or "5.0"). After pressing enter, you will be asked to confirm by submitting either Y or N.  

You will now be asked to input the values within the sample. You may type these individually or simply copy-and-paste the values from the dataset below. Submit the information by pressing Enter and confirm. You will be prompted to repeat the relevant steps for the second sample.  The program will proceed according to the outcome described for each sample dataset.
  
  
| Dataset 1| Subjects |  Values                        |
|----------|----------|--------------------------------|
| Sample A |     5    |  100,2000,30000,400000,5000000 |
| Sample B |     5    |  1,2,3,4,5                     |  
  
**Outcome: Data Unsuitable**  
In *Dataset 1*, the two samples collected from the user are unsuitable for an independent t-test and will fail when the program checks for homogeneity of variances (Levene's Test), causing the program to bypass the t-test. This can be verified by inputting the same numbers to an online Levene's Test tool, such as [SocSciStatistics.com](https://www.socscistatistics.com/tests/levene/default.aspx).
  
  
| Dataset 2| Subjects |  Values    |
|----------|----------|------------|
| Sample A |     5    |  8,7,3,9,5 |
| Sample B |     5    |  3,5,7,3,5 |  
  
**Outcome: No Statistically Significant Difference**  
In *Dataset 2*, the samples are suitable for an independent t-test and the program will proceed to carry it out. Again, this can be verified by inputting the same numbers to an online Levene's Test tool, such as [SocSciStatistics.com](https://www.socscistatistics.com/tests/levene/default.aspx).

Once carried out, the independent t-test will return no statistically significant difference between the samples in this dataset. This can be verified using an online t-test calculator, such as that available from [GraphPad](https://www.graphpad.com/quickcalcs/ttest1.cfm). 


### Invalid Input  
Attempting to enter following values in response to their respective input requests will show an error message and prompt the user to correct the error by trying again.  
  
**Menus**
| Request                | Invalid Value Type               | Error Message                                                   |  
|------------------------|----------------------------------|-----------------------------------------------------------------| 
| Main Menu Selection    | Blank                            | Invalid Selection. Please choose 1, 2, 3 or 4.                  |
| Main Menu Selection    | Letter/symbol(s)                 | Invalid Selection. Please choose 1, 2, 3 or 4.                  |  
| Main Menu Selection    | Number out of option range       | Invalid Selection. Please choose 1, 2, 3 or 4.                  |
| Help Menu Selection    | Blank                            | Invalid Selection. Please choose from the numbers shown.        |  
| Main Menu Selection    | Letter/symbol(s)                 | Invalid Selection. Please choose from the numbers shown.        |  
| Main Menu Selection    | Number out of option range       | Invalid Selection. Please choose from the numbers shown.        |  
| Records Menu Selection | Blank                            | Invalid Selection. Please choose 1 or 2.                        |  
| Records Menu Selection | Letter(s)/Symbol(s)              | Invalid Selection. Please choose 1 or 2.                        |  
| Records Menu Selection | Number out of option range       | Invalid Selection. Please choose 1 or 2.                        |  


**Running Tests**
| Request             | Invalid Value Type    | Error Message                                                              |  
|---------------------|-----------------------|----------------------------------------------------------------------------| 
| Request  | Invalid Value Type               | Error Message                                                              |
| Username | Blank                            | Username or ID required (e.g. SamBeckett, User1, etc.)                     |  
| Username | Single character                 | Username must be at least 2 characters in length                           |  
| Subjects | Blank                            | Must be numeric value. Try Again.                                          |  
| Subjects | Letter(s)                        | Must be numeric value. Try Again.                                          |  
| Subjects | Number below 5                   | Five or more subjects required. Try Again.                                 |  
| Subjects | Negative number                  | Five or more subjects required. Try Again.                                 |  
| Subjects | Float, e.g. 5.2                  |                                                                            |  
| Y/N      | Blank                            | Press Y if correct, or press N to re-enter the data.                       |  
| Y/N      | Letter other than Y/N*           | Press Y if correct, or press N to re-enter the data.                       |  
| Y/N      | Number                           | Press Y if correct, or press N to re-enter the data.                       |   
| Sample   | Blank**                          | 0 values entered. Expected [subjects]. Please begin this sample again.     |    
| Sample   | Comma(s) only**                  | 0 values entered. Expected [subjects]. Please begin this sample again.     |  
| Sample   | Number of values != [subjects]   | [x] values entered. Expected [subjects]. Please begin this sample again.   |    
| Sample   | Letter(s), e.g. "G", "1,2,3,r,5" | Non-numeric value(s) detected. Try again.                                  |  
| Sample   | Punctuation, other than as float | Non-numeric value(s) detected. Try again.                                  |  
| Sample   | Multiple decimals e.g. "5..2"    | Non-numeric value(s) detected. Try again.                                  |  
| Y        | Any other letter                 | No other operations available at this time. Press Y to return to Main Menu.|  

*Note that a lowercase y/n is handled automatically and does not require user-intervention.  
** Note that multiple commas or spaces within an otherwise valid sample (1  ,2, , 3 , 4,,,5) are automatically corrected.  
  
  
**Deleting Records**
| Request                               | Invalid Value Type| Error Message                                |  
|---------------------------------------|-------------------|----------------------------------------------| 
| "DELETE" or                           | "delete"          | "This option is case-sensitive.              |  
|  Enter to cancel or                   |                   | To delete, type 'DELETE'                     |
|  any key followed by Enter to cancel  |                   | To exit, press any other key and hit Enter." |
  


  
Data for testing significant/non-significant sets:  
non_sig_a = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88  
non_sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88  
sig_a = [83.70, 81.50, 80.60, 83.90, 84.40]  # Test data // m = 82.82  
sig_b = [66.1, 69.9, 67.7, 69.6, 71.1]  # Test data // m = 68.88  
  
## Tech Stack  
1. Languages:
  + Python  
2. Main Libraries & Modules:
  + google auth
  + gspread
  + numpy
  + scipy
  + rich

## Features
  
### Future Features  
  
## Testing  
  
## Deployment  
  

## Acknowledgements 
1. Levene's Test as carried out in Python is covered in this [Statology Article](https://www.statology.org/levenes-test-python/).  
2. Independent t-tests are covered in this [Data Camp video](https://www.youtube.com/watch?v=YpZlT64kFGA).  
3. The Main Menu function is partly based on that designed within this [How To Create a Menu in Python video](https://www.youtube.com/watch?v=P6azEyNIQDQ), with particular reference to the use of [sleep function](https://www.programiz.com/python-programming/time/sleep).  
4. ASCII-Art was generated via [fsymbols.com](https://fsymbols.com/text-art/).  
  