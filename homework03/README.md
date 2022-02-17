# Water-Analysis

## Overview
This homework dealt with the analysis of water quality and state whether the samples are safe for observation

## How to Download Water Data
1)Use this link https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
2)Log into isp
3)open COE332 Directory
4)open COE332-hw and then homework03
5)use wget followed by the link to download

## Python Scripts
There are 2 files: 'test_water.py', 'test_test_water.py'.
-test_water.py contains two functions and a main. Function one calculates turbidity, function 2 calculates minimum time for water to reach below a safe level.
-test_test_water.py has unit tests to test things like math and type errors in the code. All tests pass so code is running as expected.

## How to run the code
After the json file is downloaded, use "python3 test_water.py' to find the turbidity data. The turbidity should be outputted, along with a message on whether the water is safe or not, and minimum time until it is below a safe level.
Then, use "pytest test_test_water.py" to ensure that the first code file passes all unit tests, if it fails then a message saying what failed should display.
