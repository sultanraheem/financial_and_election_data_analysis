import os
import csv

file = r'PyBank\Resources\budget_data.csv'

with open(file, 'r') as f:
    csvreader = csv.reader(f, delimiter=",")
    csvheaderrow = next(csvreader)
# Setting variables
    total_months = 0
    total = 0
    average_change = 0
    great_inc = ["", 0]
    great_dec = ["", 9999999999999999999]  # Initial value set to a large number
    dates = []
    profits = []

    first_row = next(csvreader) # First row data includes header
    total_months += 1
    total += int(first_row[1]) # Need ignore (1)
    prev_profit = int(first_row[1])

    for row in csvreader: #How data wanted from source iterator
        total_months += 1
        total += int(row[1])

        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        average_change += profit_change
        dates.append(row[0])
        profits.append(int(row[1]))

        if profit_change > great_inc[1]: # Calculation for crtieria between what is gratest increase
            great_inc[0] = row[0] # Above parameter we have set here
            great_inc[1] = profit_change

        if profit_change < great_dec[1]: #Calculation for crtieria between what is gratest decrease
            great_dec[0] = row[0]
            great_dec[1] = profit_change
    # Calculation for average change
    average_change /= total_months - 1

print('Financial Analysis')
print('----------------------------')
print('Total Months:', total_months)
print('Total:', total)
print('Average Change:', round(average_change, 2))
print('Greatest Increase in Profits:', great_inc[0], "($", great_inc[1], ")")
print('Greatest Decrease in Profits:', great_dec[0], "($", great_dec[1], ")")

#f = open("financial_analysis.txt", "w")
#print >>f, ('Financial Analysis')
#print >>f, ('----------------------------')
#print >>f, ('Total Months:', total_months)
#print >>f, ('Total:', total)
#print >>f, ('Average Change:', round(average_change, 2))
#print >>f, ('Greatest Increase in Profits:', great_inc[0], "($", great_inc[1], ")")
#print >>f, ('Greatest Decrease in Profits:', great_dec[0], "($", great_dec[1], ")")"""
# https://stackoverflow.com/questions/13794873/how-to-export-all-print-to-a-txt-file-in-python
#file = "pybank.txt"

file_path = r'PyBank\Analysis'
with open("financial_analysis.txt", "a") as f:
    print('Financial Analysis', file=f)
    print('----------------------------', file=f)
    print('Total Months:', total_months, file=f)
    print('Total:', total, file=f)
    print('Average Change:', round(average_change, 2), file=f)
    print('Greatest Increase in Profits:', great_inc[0], "($", great_inc[1], ")", file=f)
    print('Greatest Decrease in Profits:', great_dec[0], "($", great_dec[1], ")", file=f)
# In running this print code, I learn that it is only for output in a text file, there is nothing for the terminal
    # I have ran it a few times and the text file has the same output over and over again, not sure what to do about it
    # ^ That is inside the text file, every time this runs it prints a new rendition of the print output

#f = open("txt file.txt", 'w')
#print >>f, "Financial Analysis"

#with open("financial_analysis.txt", "a") as z:
#    z.write('Financial Analysis\n')
 #   z.write('----------------------------\n')
   # z.write('Total Months: {}\n'.format(total_months))
  #  z.write('Total: {}\n'.format(total))
    #z.write('Average Change: {:.2f}\n'.format(average_change))
    #z.write('Greatest Increase in Profits: {} (${})\n'.format(great_inc[0], great_inc[1]))
    #z.write('Greatest Decrease in Profits: {} (${})\n'.format(great_dec[0], great_dec[1]))

    



