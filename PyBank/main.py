import os 
import csv

csvpath = os.path.join('..', 'Resources','budget_data.csv')

months = []
profit_and_loss =[]
total_profit_loss = 0

greatest_increase  = 0 
greatest_decrease = 0
previous_value = 0
current_value = 0 

#Open CSV file and call it budget_data_files
with open(csvpath) as budget_data_file: 
    csvreader= csv.reader(budget_data_file, delimiter=',')
    print(csvreader)

    #Skip first header row and save under csv_header variable
    csv_header = next(csvreader)
    
    #Start loop to search through file 
    for row in csvreader:
        #Add months to months list 
        months.append(row[0])
        
        #Add profits and loss to profit_and_loss list and total up the total_profit_loss 
        profit_and_loss.append(int(row[1]))
        total_profit_loss += int(row[1])
        
        #at row 2, store value from first row as previous_value if you cannot 
        current_value = row[1]
    
        #deterimne change by using current_value minus previous_value 
        change = int(current_value) - int(previous_value)
                
        if change > greatest_increase: 
            greatest_increase = change 
            greatest_increase_month = str(row[0])
    
        if change < greatest_decrease: 
            greatest_decrease = change 
            greatest_decrease_month = str(row[0])
    
        previous_value = row[1] 

        #Calculate total number of months in dataset and print this data. 
    total_months= len(months)
    
    #Calculuate change profit/losses over the entire period be subrating the end profit/loss with the first profit/loss 
    total_change = profit_and_loss[-1] - profit_and_loss[0]

    #Calculate the average change over time. 
    average_change = float(total_change)/ float(total_months-1)
    
    #Print Total months, Net total Amount Profit/Loss and Average Change. 
    
    print("-------------------------------------------------------------------")
    print(f"Total months: {total_months}")
    print(f"Total: ${total_profit_loss}") 
    print(f"Average Change: ${round(average_change,2)}")
    
    print(f"Total Profit/Loss: {total_profit_loss}")
    print(f"Greatest Increase in Profits: {greatest_increase_month}: (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month}: (${greatest_decrease})")
    print("-------------------------------------------------------------------")


output_path = os.path.join("..",'Analysis','output_pybank.txt')

with open(output_path,'a') as txtfile:
    
    txtfile.write('Financial Analysis\n')
    txtfile.write("-------------------------------------------------------------------\n")
    txtfile.write(f"Total months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n") 
    txtfile.write(f"Average Change: ${round(average_change,2)}\n")
    
    txtfile.write(f"Total Profit/Loss: {total_profit_loss}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month}: (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month}: (${greatest_decrease})\n")
    txtfile.write("-------------------------------------------------------------------")
