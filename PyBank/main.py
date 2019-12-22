import os
import csv

# open a list for storing data
total_months = []
profit_loss = []

# to make a csv path to get data

budget_data = os.path.join('..','Resources', 'budget_data.csv')

# opening csv folders

with open(budget_data, newline='') as csvfile:
    budget_read = csv.reader(csvfile, delimiter=',')

# need to skip header, so here is skipper

    next(budget_read)

# addtl or continuous writings in csv

    for row in budget_read:
        total_months.append(row[0])
        profit_loss.append(float(row[1]))

main_total_months = (len(total_months))

main_total_amounts = sum(profit_loss)

main_avrg = main_total_amounts / main_total_months

# biggest profit 
main_max_profit = max(profit_loss)  # max number
index_main_max = profit_loss.index(main_max_profit) # max number's address;month
max_month = total_months[index_main_max] # take it to my months' list

# biggest loss
main_min_profit = min(profit_loss)  # lowest number
index_main_min = profit_loss.index(main_min_profit) # lowest number's address;month
min_month = total_months[index_main_min] # take it to my months' list


financial_analysis = (f'''Financial Analysis
--------------------------------------------
Total Months:{main_total_months}
Total: ${main_total_amounts:.2f}
Average Change: {main_avrg:.2f}
Greatest Increase in Profits: {max_month} {main_max_profit:.2f}
Greatest Decrease in Profits: {min_month} {main_min_profit:.2f}''')

print(financial_analysis)

analysis = open('financial_analysis.txt', 'w') # to write the anlysis in txt format
analysis.write(financial_analysis)
analysis.close()




