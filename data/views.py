from django.shortcuts import render

# Create your views here.
import numpy as np
import pandas as pd
from obspy import read
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os, csv
import json
from decimal import Decimal

cat_directory = '../data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
data = []


def moon_data(request):
    # Initialize an empty dictionary, list, and row counter
    data_dict = {}
    fifth_column_array = []
    row_count = 0
    # New dictionary to hold the transformed values
    transformed_dict = {}
    # Open the CSV file
    with open('./output.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row if your CSV has one
        header = next(csv_reader)
        
        # Iterate through the rows in the CSV
        for row in csv_reader:
            row_count += 1  # Increment the row counter
            
            # Extract the 2nd, 4th, and 5th columns (index 1, 3, 4)
            key = row[0]  # Assuming the 2nd column is the key
            value = (row[2], row[3])  # Tuple of 4th and 5th columns
            data_dict[key] = value

            # Iterate through the original dictionary
    #        for key, value in data_dict.items():
     #           transformed_dict[key] = {
      #              'magnitude': value[0],
       #             'value': value[1]
                #}

            # Output the transformed dictionary
            #print(transformed_dict)
                        
            # Append the 5th column to the array
            fifth_column_array.append(row[3])

    # Print the resulting dictionary, array, and row count
    #print("Dictionary:", data_dict)
    #print("Array of 5th column:", fifth_column_array)
    #print("Number of rows in the CSV file:", row_count)


    # Print the resulting    
    return render(request, "data/moon.html", {'dataa':json.dumps(fifth_column_array), "length":row_count , 'all_data':transformed_dict})


def mars_data(request):
    # Initialize an empty dictionary, list, and row counter
    data_dict = {}
    fifth_column_array = []
    row_count = 0
    # New dictionary to hold the transformed values
    transformed_dict = {}
    # Open the CSV file
    with open('./output2.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row if your CSV has one
        header = next(csv_reader)
        
        # Iterate through the rows in the CSV
        for row in csv_reader:
            row_count += 1  # Increment the row counter
            
            # Extract the 2nd, 4th, and 5th columns (index 1, 3, 4)
            key = row[0]  # Assuming the 2nd column is the key
            value = (row[2], row[3])  # Tuple of 4th and 5th columns
            data_dict[key] = value

            # Iterate through the original dictionary
    #        for key, value in data_dict.items():
     #           transformed_dict[key] = {
      #              'magnitude': value[0],
       #             'value': value[1]
                #}

            # Output the transformed dictionary
            #print(transformed_dict)
                        
            # Append the 5th column to the array
            fifth_column_array.append(row[3])

    # Print the resulting dictionary, array, and row count
    #print("Dictionary:", data_dict)
    #print("Array of 5th column:", fifth_column_array)
    #print("Number of rows in the CSV file:", row_count)


    # Print the resulting    
    return render(request, "data/mars.html", {'dataa':json.dumps(fifth_column_array), "length":row_count , 'all_data':transformed_dict})


def index(request):
    return render(request, 'data/main.html')


def features(request):
    return render(request, 'data/features.html')
