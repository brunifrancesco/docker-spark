FROM gettyimages/spark
RUN pip install jupyter
ENV PYSPARK_DRIVER_PYTHON jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS 'notebook --notebook-dir=/root/notebooks --ip=0.0.0.0 --port=8888' pyspark
RUN mkdir /root/notebooks
