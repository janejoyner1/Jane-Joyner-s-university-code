import csv

with open('monthly spendings chart.py') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    line_count = 0 
    for row in csv_reader:
        if line_count == 0:
            print (f'The chart shows the {", ".join(row)}')
            line_count += 1
        
        else:
            print(f'\t{row[0]} monthly income is {row[1 ]}, his total expenses are {row[2]}, so his total savings are{row[3]}.')
            line_count += 1
            
    
    
    
import csv
     
with open( 'monthly spendings chart 2.py') as csv_file :
    csv_reader = csv.reader(csv_file, delimiter= ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'The chart shows the {", ".join(row)}')
            line_count += 1
            
        else:
            print(f'\t{row[0]} monthly income is {row[1 ]}, her total expenses are {row[2]}, so her total savings are {row[3]}.')
            line_count += 1
            
    
    
    
import csv

with open('monthly spendings chart 3.py') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=  ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f' The chart shows the {",".join(row)}')
            line_count += 1
            
        else:
            print(f'\t{row[0]} monthly income is {row[1 ]}, his total expenses are {row[2]}, so his total savings are {row[3]}.')
            line_count += 1
            
            
            
            print('Accoring to the charts, Bob makes the highest savings overall. ')
            
            print('The total income of all 3 indivuals is £10,372 ')
        
            
           
            
           
            
            print('This is a list of expenses unique to each individual.')       
      
import csv

with open ('expense list.py') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))
        
    
            
            
    
        

           