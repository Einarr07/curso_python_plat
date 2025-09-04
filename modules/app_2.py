from reports import generate_sales_report, generate_expenses_report

if __name__ == '__main__':
    print(generate_sales_report('February', 2000))
    print(generate_expenses_report('January', 9856))