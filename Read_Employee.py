import csv

def main():
    try:
        with open('employee_data.csv', 'r') as employees:
            csv_file = csv.reader(employees, delimiter=',')
            next(csv_file) 

            with open('employee_pay_report.txt', 'w') as outfile:
                outfile.write('EMPLOYEE PAY REPORT\n')
                outfile.write('=' * 30 + '\n')

                for row in csv_file:
                    id = row[0]
                    name = row[1]
                    # Total Pay Calculation: (Salary * Bonus) + Salary
                    total_pay = (int(row[3]) * float(row[7])) + int(row[3])
                    team = row[6]

                    outfile.write(f'ID: {id}\n')
                    outfile.write(f'Name: {name}\n')
                    outfile.write(f'Total Pay: ${total_pay:,.2f}\n')
                    outfile.write(f'Team: {team}\n')
                    outfile.write('-' * 20 + '\n')

        print("Successfully created 'employee_pay_report.txt'")
    except FileNotFoundError:
        print("Error: 'employee_data.csv' not found.")

if __name__ == "__main__":
    main()