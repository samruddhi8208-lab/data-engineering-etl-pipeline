from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum
import os


OUTPUT_DIR = "data/processed"


def create_spark_session():
    return (
        SparkSession.builder
        .appName("ETL Data Processing Pipeline")
        .master("local[*]")
        .getOrCreate()
    )


def process_data(spark):

    # Create output folder
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    employees = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv("data/raw/employees.csv")
    )

    orders = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv("data/raw/orders.csv")
    )

    orders = orders.withColumn(
        "total_amount",
        col("quantity") * col("price")
    )

    joined_data = employees.join(
        orders,
        on="employee_id",
        how="inner"
    )

    department_summary = (
        joined_data
        .groupBy("department")
        .agg(
            sum("total_amount").alias("total_order_amount")
        )
    )

    department_summary.show()

    # Save Spark output
    output_path = os.path.join(
        OUTPUT_DIR,
        "spark_department_summary"
    )

    department_summary.coalesce(1).write \
        .mode("overwrite") \
        .option("header", True) \
        .csv(output_path)

    print(f"Spark output saved to: {output_path}")

    return department_summary


if __name__ == "__main__":

    spark = create_spark_session()

    process_data(spark)

    spark.stop()
