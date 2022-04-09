Ｔ－Ｔｅｓｔｅｒ

T-Tester is a simple and adaptable tool that runs in the terminal and can be adapted to any number of business needs and other scenarios.  

## Contents
1. [Problem Statement](#problem-statement)  
2. [User Stories](#user-stories)
    + [Sample Datasets](#sample-datasets)
3. [Tech Stack](#tech-stack)  
4. [Features](#features)
    + [Future Features](#future-features)
5. [Testing](#testing)
6. [Deployment](#deployment)  
7. [Acknowledgements](#acknowledgements) 

## Problem Statement  

## User Stories  
  
### Sample Datasets:  
To test different outcomes, the reader may wish to make use of the following datasets.  
  
Dataset:  
5 Subjects: [100,2000,30000,400000,5000000]  
5 Subjects: [1,2,3,4,5]  

Outcome:  
In this case, the two samples collected from the user are unsuitable for an independent t-test and will fail when the program checks for homogeneity of variances (Levene's Test), causing the program to bypass the t-test. This can be verified by inputting the same numbers to an online Levene's Test tool, such as [SocSciStatistics.com](https://www.socscistatistics.com/tests/levene/default.aspx).

Dataset:  
5 Subjects: [8,7,3,9,5]  
5 Subjects: [3,5,7,3,5]  

Outcome:  
Here, the samples are suitable for an independent t-test and the program will proceed to carry it out. Again, this can be verified by inputting the same numbers to an online Levene's Test tool, such as [SocSciStatistics.com](https://www.socscistatistics.com/tests/levene/default.aspx).

Once carried out, the independent t-test will return no statistically significant difference between the samples in this dataset. This can be verified using an online t-test calculator, such as that available from [GraphPad](https://www.graphpad.com/quickcalcs/ttest1.cfm).  
  
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
1. Levene's Test as carried out in Python is covered on this [Statology Article](https://www.statology.org/levenes-test-python/).  
2. Independent t-tests (also known as Student's t-test) is covered in this [Data Camp video](https://www.youtube.com/watch?v=YpZlT64kFGA).  
3. The Main Menu function is partly based on that designed within this [How To Create a Menu in Python video](https://www.youtube.com/watch?v=P6azEyNIQDQ), with particular reference to the use of [sleep function](https://www.programiz.com/python-programming/time/sleep).  
4. ASCII-Art was generated via [fsymbols.com](https://fsymbols.com/text-art/).  
  