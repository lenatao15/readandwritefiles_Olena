import csv

with open('sales.csv', 'r') as sales_report:
    csv_file = csv.reader(sales_report,delimiter=',')

    fields = next(csv_file)

    with open('salesreportFINAL.csv', 'w', newline ='') as outfile:

        writer = csv.writer(outfile)


        writer.writerow(['Customer ID', 'Total'])
        
        previous_custID =''
        rowTotal = 0
        customer_total = 0
        for row in csv_file:
            current_custID = row[0]
            row[3] = float(row[3])
            row[4] = float(row[4])
            row[5] = float(row[5])

            rowTotal = row[3]+row[4]+row[5]
            if previous_custID == current_custID:
                customer_total += rowTotal
            else:
                if previous_custID != '':
                    new_row = [previous_custID, f'{customer_total:.2f}']
                    writer.writerow(new_row)
                    
                previous_custID = current_custID
                customer_total = rowTotal
            
        if previous_custID != '':
            writer.writerow([previous_custID, f'{customer_total:.2f}'])

    