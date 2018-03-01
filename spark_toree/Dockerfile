FROM gettyimages/spark
RUN pip install toree jupyter
RUN jupyter toree install --user --spark_home $SPARK_HOME --spark_opts="--master spark://master:7077"
