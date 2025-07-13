from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import pyspark.sql.functions as func

# spark session
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



# show all transformations
transformed_df = people_df.select(
    people_df.UserId,
    people_df.Name,
    people_df.Age,
    people_df.Number_of_friends
).where(people_df.Age > 30)\
 .withColumn("insert_ts", func.current_timestamp())\
 .orderBy(people_df.UserId)

# Show the DataFrame
transformed_df.show()

# count the number of rows of the trnsformed DataFrame

print("The number of rows:",transformed_df.count())

