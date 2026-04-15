from pyspark.sql import SparkSession


def create_spark_session() -> SparkSession:
    builder = SparkSession.builder.appName("MinIO Connectivity Test")

    spark = builder.getOrCreate()
    return spark


spark = create_spark_session()
