from extract import extract_employees, extract_orders
from transform import clean_employees, clean_orders


EMPLOYEE_FILE = "data/raw/employees.csv"
ORDERS_FILE = "data/raw/orders.csv"


def main():

    # Extract
    employees = extract_employees(EMPLOYEE_FILE)
    orders = extract_orders(ORDERS_FILE)

    # Transform
    employees = clean_employees(employees)
    orders = clean_orders(orders)

    # Join
    merged_data = employees.merge(
        orders,
        on="employee_id",
        how="inner"
    )

    # Department summary
    department_summary = (
        merged_data
        .groupby("department")["total_amount"]
        .sum()
        .reset_index()
    )

    print("Department Summary:")
    print(department_summary)


if __name__ == "__main__":
    main()
