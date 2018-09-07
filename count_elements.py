import os
from pandas import DataFrame
import pandas as pd
import csv
# import glob
# import numpy as np 
# import openpyxl

# If running the code on your terminal, run this code below first on the particular directory
# import os
# os.getcwd()

# Converting xlsx files to csv files
def convert_to_csv():
	path = "<the path to your directory>"
	files = os.listdir(path)
	filenames = [f for f in files if os.path.isfile(os.path.join(path, f))]
	for filename in filenames:
		if "<particular string>" in filename:
			print ("Converting.. Please wait.")
			data = pd.read_excel('{}'.format(filename), '<sheet name>', index_col=None, header=None)
			data.to_csv('{}'.format(filename) + '.csv', encoding='utf-8', header=None)
			print (filename + " converted.")
		else:
			pass 

# Extract particular columns of all the csv files and put them onto one single csv file
# Separate the csv file into to based on the column and count the strings on Error_list.csv
# Create two csv files that show the count on each string on Error_list.csv
def count_data():
	path = "<the path to your directory>"
	files = os.listdir(path)
	files = [f for f in files if os.path.isfile(os.path.join(path, f))]
	data_list = [] 
	machine_1 = [] # column 17
	machine_2 = [] # column 4
	for csv_file in files:
		if "<particular string>" in csv_file:
			try:
				csv_input = pd.read_csv(filepath_or_buffer="<the path to the directory>/{}".format(csv_file), usecols=[4, 17], encoding="utf-8", delimiter=",", header=None)
				data_list.append(csv_input)
			except:
				continue
			frame = pd.concat(data_list)
			frame.to_csv("<the path to the directory>/<file name>")
	csv_input_1 = pd.read_csv(filepath_or_buffer="<the path to the directory>/<file name>", usecols=[2], nrows=200, encoding="utf-8", delimiter=",", header=None)
	machine_1.append(csv_input_1)
	csv_input_2 = pd.read_csv(filepath_or_buffer="<the path to the directory>/<file name>", usecols=[1], nrows=200, encoding="utf-8", delimiter=",", header=None)
	machine_2.append(csv_input_2)
	frame_1 = pd.concat(machine_1)
	frame_2 = pd.concat(machine_2)
	error = pd.read_csv(filepath_or_buffer="<the path to the directory>/Error_list.csv", encoding="utf-8", delimiter=",")
	counts = frame.stack().value_counts().to_frame('<column label>').loc[error.error]
	counts.to_csv("<the path to the directory>/<file name>")
	counts_1 = frame_1.stack().value_counts().to_frame('<column label>').loc[error.error]
	counts_1.to_csv("<the path to the directory>/<file name 1>")
	print("<file name 1> is created")
	counts_2 = frame_2.stack().value_counts().to_frame('<column label>').loc[error.error]
	counts_2.to_csv("<the path to the directory>/<file name 2>")
	print("<file name 2> is created")

if __name__ == '__main__':
	convert_to_csv()
	count_data()

