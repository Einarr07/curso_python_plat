import reports

sales_report = reports.generate_sales_report('October', 10000)

expenses_report = reports.generate_expenses_report('October', 5000)

if __name__ == '__main__':
    print(sales_report)
    print(expenses_report)