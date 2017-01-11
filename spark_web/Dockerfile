FROM gettyimages/spark
RUN pip install flask

CMD bin/spark-submit /tmp/data/server/server.py --master spark://172.17.0.8:7077
