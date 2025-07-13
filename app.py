
from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local")\
        .appName("MySparkApp")\
        .getOrCreate()
        
        
# data         
data = [
        
        ("Elisha","Otieno","1998-10-23","M",4000),
        ("Wince","Ogola","1997-09-30","F",8000),
        ("Osbon","Odhiambo","1999-12-31","M",7000),
        ("Meshack","Otieno","1996-10-19","M",3500)
        ]

# Define schema
columns = ["FirstName","LastName","DOB","Gender","Salary"]


df = spark.createDataFrame(data=data,schema=columns)

df.show()
print(df.printSchema())