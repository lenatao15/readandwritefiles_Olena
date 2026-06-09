import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers,delimiter=',')

next(csv_file)

total_customer = 0
outfile = open('customer_country.csv', 'w', newline ='')

writer = csv.writer(outfile)

fields = ['First Name', 'Last Name', 'Country']
writer.writerow(fields)
for row in csv_file:
    
    new_row = [row[1],row[2], row[4]]
    writer.writerow(new_row)
   

    total_customer+=1

print('Total number of customers read from the file is:',total_customer)

    

    