# scraping_intermediate

This is the repository that has data scraping, extraction, conversion, organizing and etc. Please check the Usage part below for specific purpose of each code.

# Dependency
- Python 3
- Pandas

# Usage 

**[count_elements.py](https://github.com/Gegegegensan/scraping_intermediate/blob/master/count_elements.py)**

You could use this when you have lots of xlsx files with multiple tabs and want to extract a certain sheet's information consolidated as count.

- The first function **convert_to_csv()** works as xlsx => csv converter for the files in the directory.
- The second function **count_data()** works as consolidating a certain sheet's data into one csv file and split the data into two (or more if some code is added) based on the column on the consolidated csv file, and then make csv files with count info comparing to the Error_list.csv (tentative name) file.


# Author

[Gegegegensan](https://gegegegensan.com)

# Licence
This software is released under the MIT License.
