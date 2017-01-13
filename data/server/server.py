from flask import Flask
app = Flask(__name__)

from pyspark.sql import SparkSession
print("Creating the SPARK SESSION")

spark = SparkSession.builder \
     .master("spark://master:7077") \
     .appName("Vediamo") \
     .config("spark.mongodb.input.uri", "mongodb://mongodb/measures.measure") \
     .getOrCreate()

print("SPARK Session created")


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8889)
