import os 
import csv

csvpath = os.path.join('..', 'Resources','budget_data.csv')

months = []
profit_and_loss =[]
total_profit_loss = 0


#Open CSV file and call it budget_data_files
with open(csvpath) as budget_data_file: 
    
    csvreader= csv.reader(budget_data_file, delimiter=',')
    print(csvreader)

    #Skip first header row and save under csv_header variable
    csv_header = next(csvreader)
    
    #start loop to search through file 
    for row in csvreader:
        #Add months to months list 
        months.append(row[0])
        
        #Add profits and loss to profit_and_loss list and total up the total_profit_loss 
        profit_and_loss.append(int(row[1]))
        total_profit_loss += int(row[1])
        

    #Calculate total number of months in dataset and print this data. 
    total_months= len(months)
    
    #Calculuate change profit/losses over the entire period be subrating the end profit/loss with the first profit/loss 
    total_change = profit_and_loss[-1] - profit_and_loss[0]

    #Calculate the average change over time. 
    average_change = float(total_change)/ float(total_months-1)
    
    #Print Total months, Net total Amount Profit/Loss and Average Change. 
    print(f"Total months: {total_months}")
    print(f"Total: ${total_profit_loss}") 
    print(f"Average Change: ${round(average_change,2)}")
    
  
