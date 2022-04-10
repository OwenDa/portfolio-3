Ｔ－Ｔｅｓｔｅｒ

T-Tester is a simple and adaptable tool that runs in the terminal and can be adapted to any number of business needs and other scenarios.  
  
## Contents
1. [Overview](#overview)  
2. [Tech Stack](#tech-stack)  
3. [User Stories](#user-stories)
4. [Features](#features)
    + [Future Features](#future-features)
5. [Testing](#testing)
    + [Test Cases](#test-cases)
        - Invalid Input
        - Sample Datasets
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
  
  
## Tech Stack  
1. Languages:  
    + Python  
2. Main Libraries & Modules:  
    + [google-auth 2.6.3](https://pypi.org/project/google-auth/)
    + [gspread 5.3.0](https://pypi.org/project/gspread/)
    + [numpy 1.22.3](https://pypi.org/project/numpy/)
    + [scipy 1.8.0](https://pypi.org/project/scipy/)
    + [rich 12.2.0](https://pypi.org/project/rich/) 
    
## User Stories  
As a user, I want to...  
  
- Understand how to use the program  
    + Brief instructions on each of the program's functionalities can be easily accessed from the Main Menu. These are divided by topic, allowing the user to access the most relevant information to their situation. A link to more in-depth information, provided in this README document, is also provided.  
  
- Ascertain the suitability of my data for use in the program  
    + T-Tester checks for homogeneity of variance, an important consideration when conducting independent t-tests. T-Tester also ensures that each sample contains at least five subjects. A famously robust test in this regard, the indepenent t-test can accomodate small sample sizes. However, T-Tester cannot assess methodological issues such as sampling method and representivity. It does not, at the time of writing, provide information on distribution such as skewness and kurtosis.  
  
- Compute the mean averages of two samples  
    + T-Tester calculates the mean average for each sample provided but does not relay non-significant data within the terminal as this could be misleading. Instead, the mean averages are relayed within the terminal only for statistically significant results. However, a record of all means is kept within the associated Google Sheets spreadsheet, should an organisation have other uses for this information.  
  
- Compare the means of two samples, if suitable  
    + T-Tester's primary function is to carry out an indepenent t-test, comparing the means of two samples and determining the statistical significance of any difference identified.
  
- See the results of the analysis  
    + Resuls of any tests conducted (Levene's test, indepenent t-test) are relayed within the terminal in terms of significance.
    
        | Possible Outputs                                                                                                   |  
        |--------------------------------------------------------------------------------------------------------------------|  
        | T-test not conducted due to unequal variance. Data is unsuitable for t-test. Reason: Lacks homogeneity of variance.|  
        | No statistically significant difference found                                                                      |  
        | Statistically significant difference. The mean average of Sample A (3.44) was greater than that of Sample B (2.88).|  
  
- Read records of past test results  
    + The Main Menu provides an option to "View Records" which allows the user to view a table of past test results within the program. Records can also be viewed in the related Google Sheet. 
    
- Create a new record for each new test conducted  
    + A new record is added for each test process, recording the time and date of the test's completion, the user's name, username or ID, the mean average for each sample used within the test(s) and one of the three possible outputs in the table above.  
  
- Store records in a manner that makes them easy to share  
    + While accessible as a table within the program, records are stored in a Google Sheets spreadsheet, meaning they could be easily shared within an organisation or to other parties if desired. This also means that records are accessible on multiple devices and when the program is closed or the user does not have access to the program.  

- Update the externally-stored records automatically   
    + Newly created records are added to the connected Google Sheet rather than the program itself. This is also true when deleting data; it is the Google Sheet which is being updated. The program simply retrieves this information from the Google Sheet in order to display records in a convenient manner within the terminal. Changes to the Google Sheet are, therefore, reflected within the program, although it may be necessary to restart the program in order to see the most recent version of the available records.  
  
- Store records in a manner that allows me or others to copy, extract, manipulate or delete data  
    + Records are stored in a Google Sheet spreadsheet which not only makes their content more accessible in many ways but also means that either selected data or the entire worksheet can be copied. Individual records or fields can be extracted for use in other programs. Data can also be deleted from the spreadsheet or a copy of the spreadsheet. For instance, one colleague may need access only to statistically significant results, and may wish to store these in a separate spreadsheet, file or other program.  
  
- Delete a record if created in error  
  + The last shown record within the records table can be deleted by the user. This enables duplicate tests to be removed immediately upon realising the error, or in the event that a test was carried out on an dataset containing an error, it can be removed immediately. Records older than this can only be changed from within the Google Sheets spreadsheet. To minimise the risk of accidental deletion, a warning is displayed and confirmation is required. To confirm deletion, the user is instructed to type "DELETE" in capitals. Simultaneously, the user is told the pressing Enter will cancel deletion. If a request to delete a record is aborted in this manner, the user will be directed away from the deletion screen and back to the preceeding menu. A lowercase response ("delete") will prompt a message informing the user that the option is case sensitive and asking them to try again.  
  
- Navigate through the program  
    + Menus allow for easy and relatively intuitive navigation. Instructions are provided alongside menus, informing the user how to make a selection. T-Tester also enables the user to return to the previous menu where relevant; for example, after cancelling the deletion or a file or after reading a help topic.  
  
- Minimise the risk of entering incorrect data  
    + Invalid data is handled through error messages, automatic re-formatting and prompts to the user; however, valid data can nevertheless be incorrect data, largely due to ommission, typo or other user error.
    
    To minimise the risk of omitting a value within a sample, the user is asked to specify the number of values they expect to be entering (ie. the number of subjects within a sample), and this is compared to the actual number of values entered when the user submits the sample.  
      
    To ensure this comparison works as efficiently as possible, confirmation is required for both inputs. The following example cases explain how these checks are applied:  
      
    **Case 1: The user erroneously enters "13" as the number of subjects for a sample which actually contains 14 values.**  
    T-Tester will display the message, "You entered: 13. Is this correct? Y/N", requesting confirmation that this number is correct. As it is incorrect, the user enters "N" and is offered the opportunity to re-enter the number.  
      
    **Case 2: The user correctly inputs "14" as the number of subjects, but subsequently enters only 13 of these values due to a typo, omission or copy/paste error.**  
    T-Tester will alert the user of the disparity and restart collection of that particular sample.  
      
    **Case 3: The user enters the correct number of values for the sample, but the input contains a typo.**  
    T-Tester relays the values for a sample back to the user in a message such as, "You entered: [1, 2, 3, 4, 6]. Is this correct? Y/N".  The values shown in this message have been automatically formatted, making them easy to read and increasing the user's ability to spot any typos. For example, the data above may have originally been entered by the user as "1,,,, 2,3,  4, 6,,", but the program has formatted it in a more consistent and readable manner. If the data does contain a typo, the user will respond "N" to decline confirmation and be asked to enter the values again.

- Avoid crashing/restarting the program if I inadvertantly enter incorrect input  
    + When invalid input is entered, a helpful message is displayed prompting the user to amend their input and allowing them to continue from the relevant step of the process. In most cases, this is the previous step within a given process.  
    
    Where an as yet unforeseen error arises, the program will attempt to return the user to the Main Menu. If, for any reason, this fails, or where the error arises within the Main Menu, the program will close though its own quit process. T-Tester's quit process informs the user, "Sorry, something went wrong. [error message]. Quitting program..." before quitting with Python's built-in quit function. A slight delay is added between the phrases of this message to ensure the reader is not unduly alarmed and has time to take in the message. If, for any reason, the T-Teminal's quit process cannot run as intended, it will simply use the built-in Python quit function without any communication to the user. Ctrl+C/Cmd+C will terminate the program and therefore does not allow further activity or communication from the program itself.  
    
- Receive feedback in case of erroneous input  
    + Helpful and descriptive error messages and prompts are used wherever possible within the program whenever invalid data is entered. The user is then offered the opportunity to re-enter this data without needing to restart the program or even restart the testing process if using the program's testing functions.  
  
- Correct invalid or erroneous input without restarting the program  
    + As described elsewhere, a response in Y/N format is required to confirm inputs when running tests. If the user responds "N", T-Tester provides the opportunity to re-enter the input. Where invalid data is entered, the user is shown a descriptive error message and then offered the opportunity to re-enter this data without needing to restart the program.  
  
- Exit the program easily  
    + The user can exit the program from the Main Menu. In this event, the program will inform the user with a simple "Quitting program..." message. A slight delay is added between this message and exiting the program, ensuring the user has time to read the message.  
    + Ctrl+C/Cmd+C will terminate the program and therefore does not allow further activity or communication from the program itself.  
  
Further test cases, with particular reference to individual error messages, are discussed in [Test Cases: Invalid Input](#test-cases-invalid-input).  
  
Additionally, the [Sample Datasets](##sample-datasets) provided function as test cases for sample entry in T-Tester's testing mode.
  
## Features  
  
  
### Future Features  
It debatable whether deletion of records beyond the last shown record is a desirable feature. Deletion of the last shown record may be useful when a user realises, shortly after conducting a test, that the test was already carried out, used an incomplete or incorrect dataset and so on. For more selective deletion of records, access to the related Google Sheets spreadsheet is required. This limitation of the program may actually represent a useful feature in and of itself, as Google Sheets' permissions and access options allow for precise control of who may carry out such selective deletion. Nevertheless, it is possible that the program may expand its deletion options in the future.  
  
Currently, the program does not assess skewness and kurtosis. These features could be added for a more rounded and thorough set of pre-test checks.  

Additional inputs could be added to the program's testing feature, such as a "Tester Notes" input. This input could then be added as an additional field to the records kept. The usefulness of such a feature may depend on how the program is being used. The optimal design would be one in which the user can configure which fields are needed within their records and which fields are unecessary. To be truly useful, these settings would need to be stored in a lasting manner. Only the necessary inputs would then be requested during the testing process.  
    
    
## Testing  
Manual testing, including exploratory testing, was carried out throughout development. New features were tested as they were added and before committing changes. Certain features were pushed and tested within the deployed environment to ensure that rendering was as intended.  
  
### Test Cases
<details><summary>
Invalid Input
</summary></br>  
Attempting to enter following values in response to their respective input requests shows an error message and prompts the user to correct the error by trying again.  
  
  
**Menus**
| Request                | Invalid Value Type               | Error Message                                                   |  
|------------------------|----------------------------------|-----------------------------------------------------------------| 
| Main Menu Selection    | Blank                            | Invalid Selection. Please enter a number from the options shown.|
| Main Menu Selection    | Letter/symbol(s)                 | Invalid Selection. Please enter a number from the options shown.|  
| Main Menu Selection    | Number out of option range       | Invalid Selection. Please enter a number from the options shown.|
| Help Menu Selection    | Blank                            | Invalid Selection. Please enter a number from the options shown.|  
| Main Menu Selection    | Letter/symbol(s)                 | Invalid Selection. Please enter a number from the options shown.|  
| Main Menu Selection    | Number out of option range       | Invalid Selection. Please enter a number from the options shown.|  
| Records Menu Selection | Blank                            | Invalid Selection. Please enter a number from the options shown.|  
| Records Menu Selection | Letter(s)/Symbol(s)              | Invalid Selection. Please enter a number from the options shown.|  
| Records Menu Selection | Number out of option range       | Invalid Selection. Please enter a number from the options shown.|  


**Running Tests**
| Request  | Invalid Value Type               | Error Message                                                              |  
|----------|----------------------------------|----------------------------------------------------------------------------| 
| Username | Blank                            | Username or ID required (e.g. SamBeckett, User1, etc.)                     |  
| Username | Single character                 | Username must be at least 2 characters in length                           |  
| Subjects | Blank                            | Enter an integer, e.g. '7' (Not '7.2' or 'seven'). Please try again.       |  
| Subjects | Letter(s)                        | Enter an integer, e.g. '7' (Not '7.2' or 'seven'). Please try again.       |  
| Subjects | Number below 5                   | Five or more subjects required. Try Again.                                 |  
| Subjects | Negative number                  | Five or more subjects required. Try Again.                                 |  
| Subjects | Float, e.g. 5.2                  | Enter an integer, e.g. '7' (Not '7.2' or 'seven'). Please try again.       |  
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
</details>  
  
<details><summary>  
Sample Datasets  
</summary></br>  
The following sample datasets can be used to test different outcomes of T-Tester's testing mode.  
  
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
   
**Additional Datasets**  
  
| Dataset 3 | Subjects |  Values                       | Mean  | Outcome          |
|-----------|----------|-------------------------------|-------|------------------|
| Sample A  |     5    |  66.1, 69.9, 67.7, 69.6, 71.1 | 68.88 | Non-significant  |
| Sample B  |     5    |  66.1, 69.9, 67.7, 69.6, 71.1 | 68.88 | Non-significant  |
  
In *Dataset 3*, the values entered are identical. The mean average returned for each sample is therefore identical and no statistically significant difference is found.

| Dataset 4 | Subjects |  Values                            | Mean  | Outcome     |
|-----------|----------|------------------------------------|-------|-------------|
| Sample A  |     5    |  83.70, 81.50, 80.60, 83.90, 84.40 | 82.82 | Significant |
| Sample B  |     5    |  66.1, 69.9, 67.7, 69.6, 71.1      | 68.88 | Significant | 

In *Dataset 4*, differing mean averages are calculated for each sample. Homogeneity of variances is confirmed and an indepenent t-test is carried out accordingly. A statistically significant difference is found, with the mean of Sample A being greater than that of Sample B.  
</details>  
    
## Deployment  
  
  
## Acknowledgements 
1. Levene's Test as carried out in Python is covered in this [Statology Article](https://www.statology.org/levenes-test-python/).  
2. Independent t-tests are covered in this [Data Camp video](https://www.youtube.com/watch?v=YpZlT64kFGA).  
3. The Main Menu function is partly based on that designed within this [How To Create a Menu in Python video](https://www.youtube.com/watch?v=P6azEyNIQDQ), with particular reference to the use of [sleep function](https://www.programiz.com/python-programming/time/sleep).  
4. ASCII-Art was generated via [fsymbols.com](https://fsymbols.com/text-art/).  
  