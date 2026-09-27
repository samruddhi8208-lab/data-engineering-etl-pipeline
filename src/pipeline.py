from extract import extract_employees, extract_orders
from transform import clean_employees, clean_orders
import os


EMPLOYEE_FILE = "data/raw/employees.csv"
ORDERS_FILE = "data/raw/orders.csv"
OUTPUT_DIR = "data/processed"


def main():

    # Create output folder
    os.makedirs(OUTPUT_DIR, exist_ok=True)

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

    # Save output
    output_file = os.path.join(
        OUTPUT_DIR,
        "department_summary.csv"
    )

    department_summary.to_csv(
        output_file,
        index=False
    )

    print(f"Output saved to: {output_file}")


if __name__ == "__main__":
    main()
