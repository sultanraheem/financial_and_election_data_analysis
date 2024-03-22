# Module_3_Challenge
Module 3 Challenge 

# NOTE
This challenge was completed with a team consisting of Rob Molenda, Muneeb Samad, Lucas Perez, and Jelena Raonic who provided further assistance through Zoom and Slack.
A complete work cited will be provided at the end of the README.
 

# Correctly Reads in the CSV (10 points)
The code reads CSVs for both PyBank and PyPoll using Python and Successfully stores the header row

In main.py:

import os
import csv

file = r'PyBank\Resources\budget_data.csv'

with open(file, 'r') as f:
    csvreader = csv.reader(f, delimiter=",")
    csvheaderrow = next(csvreader)

In main1.py:

import os
import csv

file = r'PyPoll\Resources\election_data.csv'

with open(file, 'r') as f:
    csvreader = csv.reader(f, delimiter=",")
    # Skip header row
    next(csvreader)

    Sources used:
    https://stackoverflow.com/questions/60190232/how-to-access-csv-file-using-os-module
    https://stackoverflow.com/questions/16823695/how-to-use-delimiter-for-csv-in-python
    https://note.nkmk.me/en/python-csv-reader-writer/#read-csv-files-csvreader
    
  # Results Printed out to correctly to terminal (40 points)

    3 attempts were used to print the results, only the working print is non-commented and sourced within the main.py file for sources

    print('Financial Analysis')
print('----------------------------')
print('Total Months:', total_months)
print('Total:', total)
print('Average Change:', round(average_change, 2))
print('Greatest Increase in Profits:', great_inc[0], "($", great_inc[1], ")")
print('Greatest Decrease in Profits:', great_dec[0], "($", great_dec[1], ")")

Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates_votes_count.items():
    percentage = candidates_percentage[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

Sources:
https://note.nkmk.me/en/python-csv-reader-writer/#read-csv-files-csvreader
https://stackoverflow.com/questions/55064657/python-print-output-instead-of-formula

# Code Runs Error Free (10 points)

I ran the code in my terminal, this is my first time using the terminal and GitHub to get my codes to run
In my experience, I am sure this will run on any machine but I am not able to confirm this

# Exports results to text file (30 points)

file_path = r'PyBank\Analysis'
with open("financial_analysis.txt", "a") as f:
    print('Financial Analysis', file=f)
    print('----------------------------', file=f)
    print('Total Months:', total_months, file=f)
    print('Total:', total, file=f)
    print('Average Change:', round(average_change, 2), file=f)
    print('Greatest Increase in Profits:', great_inc[0], "($", great_inc[1], ")", file=f)
    print('Greatest Decrease in Profits:', great_dec[0], "($", great_dec[1], ")", file=f)

  This is the only method I was able to use to print into a text file and I had a lot of trouble with the path of my file

Direct comment from VSCode: running this print code, I learn that it is only for output in a text file, there is nothing for the terminal
    # I have ran it a few times and the text file has the same output over and over again, not sure what to do about it
    # ^ That is inside the text file, every time this runs it prints a new rendition of the print output

    I do not know how to stop it from printing again and again when it is ran, you will see in the text file that the results will already have been 
    printed a handful of times, that is every time I ran it to test its functionality in my VSCode

    Sources:
    https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
    
    An additional source from source code used for my understanding: 
    https://stackoverflow.com/questions/13794873/how-to-export-all-print-to-a-txt-file-in-python

  # Code is cleaned and commented (10 points)

  I understand that the code needs to be cleaned, I have included two aspects for the printing functions

  They are as follows:

  #f = open("financial_analysis.txt", "w")
#print >>f, ('Financial Analysis')
#print >>f, ('----------------------------')
#print >>f, ('Total Months:', total_months)
#print >>f, ('Total:', total)
#print >>f, ('Average Change:', round(average_change, 2))
#print >>f, ('Greatest Increase in Profits:', great_inc[0], "($", great_inc[1], ")")
#print >>f, ('Greatest Decrease in Profits:', great_dec[0], "($", great_dec[1], ")")"""
#source: https://stackoverflow.com/questions/13794873/how-to-export-all-print-to-a-txt-file-in-python
#file = "pybank.txt"

AND

#f = open("txt file.txt", 'w')
#print >>f, "Financial Analysis"

#with open("financial_analysis.txt", "a") as z:
    #z.write('Financial Analysis\n')
    #z.write('----------------------------\n')
    #z.write('Total Months: {}\n'.format(total_months))
    #z.write('Total: {}\n'.format(total))
    #z.write('Average Change: {:.2f}\n'.format(average_change))
    #z.write('Greatest Increase in Profits: {} (${})\n'.format(great_inc[0], great_inc[1]))
    #z.write('Greatest Decrease in Profits: {} (${})\n'.format(great_dec[0], great_dec[1]))

    These have simply been included to show my work and include an aforementioned source that aided my understanding
    To me, this is useful information

  # Submission

  To understand how GitHub works, I have spoken to the instructor, and classmates, along with a video to help

  Video: https://www.youtube.com/watch?v=xmK1Q5uzH4w
