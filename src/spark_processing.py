from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum


def create_spark_session():
    return (
        SparkSession.builder
        .appName("ETL Data Processing Pipeline")
        .master("local[*]")
        .getOrCreate()
    )


def process_data(spark):

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

    return department_summary


if __name__ == "__main__":

    spark = create_spark_session()

    process_data(spark)

    spark.stop()
