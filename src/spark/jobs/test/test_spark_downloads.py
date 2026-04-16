"""
Test code to check if data can be read from MinIO using spark-native code.
"""

from pyspark.sql import SparkSession

# ------------------------------------------------------------------------
# Initialize spark session
builder = SparkSession.builder.appName("Test Sparquet Download")

# Init MinIO connectivity
#fmt: off
builder = builder \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")

builder = builder \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescencePartitions.enabled", "true")
# fmt: on

spark = builder.getOrCreate()

# ------------------------------------------------------------------------
# Debug code to get entries in bucket

hadoop_conf = spark._jsc.hadoopConfiguration()
fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(
    spark._jvm.java.net.URI("s3a://processed-data"), hadoop_conf
)

# List everything in the bucket
print("--- LISTING BUCKET CONTENTS ---")
path = spark._jvm.org.apache.hadoop.fs.Path("/")
files = fs.listFiles(path, True)
found = False
while files.hasNext():
    found = True
    print(f"Hadoop sees: {files.next().getPath().toString()}")

if not found:
    print("Hadoop sees NOTHING in this bucket. Check endpoint/credentials.")
print("-------------------------------")

# ------------------------------------------------------------------------
# Read some data in a sparkonic way

df = (
    spark.read.format("parquet")
    .option("mergeSchema", "false")
    .option("pathGlobFilter", "arrivals_*.parquet")
    .load("s3a://processed-data/processed/date=2026-04-07/")
)
df.show()
