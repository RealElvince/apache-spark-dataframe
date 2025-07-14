from pyspark.sql.types import *

schema = StructType([
    StructField("Author", StringType(), True),
    StructField("Title", StringType(), True),
    StructField("Year", IntegerType(), True),
    StructField("Price", FloatType(), True),
    StructField("Publisher", StringType(), True)
])