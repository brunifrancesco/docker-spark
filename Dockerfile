FROM gettyimages/spark
RUN pip install jupyter bokeh pandas
RUN jupyter nbextension enable --py widgetsnbextension
ENV PYSPARK_DRIVER_PYTHON jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS 'notebook --notebook-dir=/tmp/data/notebooks --ip=0.0.0.0 --port=8888' pyspark
