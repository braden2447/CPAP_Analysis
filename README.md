# CPAP Analysis Assignment

## Author: Braden Garrison

## Due: 9/28/21

## Program Instructions:

To run the CPAP Analysis module properly, a few specific files and file names are necessary.

First, the presence of an input .txt file containing the patient data to be analyzed must be present in the same folder as the cpap_database.py module.
This input file should be named "sample_data.txt" for the module to read in the data properly.
If the input file is named something different, the cpap_database.py module should be modified to change the "sample_data.txt" file name in the final "main" function.
Also, to ensure proper unit testing of one of the functions within the cpap_database.py module, a test text document named "testing_data_split.txt" must be present in the folder.
Both of these files must contain a final line containing some form of the word "End" to indicate the end of the file.

To run this program from the command line, type:

```python cpap_database.py```

The module will return nothing to the command line, but the processed patient CPAP data will be output to individual patient .json files within the folder on your local disk.

## CPAP Information

CPAP, or continuous positive airway pressure, machines are used to treat sleep apnea, a condition in which restrictive airways cause breathing to stop during sleep, awakening the affected individual.
CPAPs collect multiple sets of data throughout the night, including number of hours of use, amount of air leakage, and number of "events per hour."
These are the sets of data that are analyzed by this python module to provide a diagnosis of sleep disorders such as apnea, hypoxia, and hypoxia apnea.
More information on CPAP and these relevant diseases can be found at:
https://www.cpap.com/blog/hypoxia-hypoxemia-symptoms-causes-solutions/



