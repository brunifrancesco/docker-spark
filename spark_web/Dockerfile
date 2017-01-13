FROM gettyimages/spark
RUN pip install flask

CMD bin/spark-submit /tmp/data/server/server.py --packages org.mongodb.spark:mongo-spark-connector_2.10:2.0.0,org.apache.spark:spark-sql_2.10:2.0.2
