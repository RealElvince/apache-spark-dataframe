from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import pyspark.sql.functions as func


spark = SparkSession.builder\
        .master("local")\
        .appName("MySparkApp2")\
        .getOrCreate()



# create a schema
people_schema = StructType([
    StructField("UserId", StringType(), True),
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Number_of_friends", IntegerType(), True)
])


# create a DataFrame using the schema
people_df = spark.read.format("csv")\
    .option("header", "true")\
    .schema(people_schema)\
    .load("data/people.csv")


# Show the DataFrame
people_df.show()