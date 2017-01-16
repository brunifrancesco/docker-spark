FROM gettyimages/spark
RUN pip install flask bokeh pandas
CMD bin/spark-submit  --packages org.mongodb.spark:mongo-spark-connector_2.10:2.0.0,org.apache.spark:spark-sql_2.10:2.0.2 /tmp/data/server/ciccio.py
