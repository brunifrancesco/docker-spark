
# spark

A `debian:jessie` based [Spark](http://spark.apache.org) container. Use it in a standalone cluster with the accompanying `docker-compose.yml`, or as a base for more complex recipes.

## docker example

To run `SparkPi`, run the image with Docker:

    docker run --rm -it -p 4040:4040 gettyimages/spark bin/run-example SparkPi 10

To start `spark-shell` with your AWS credentials:

    docker run --rm -it -e "AWS_ACCESS_KEY_ID=YOURKEY" -e "AWS_SECRET_ACCESS_KEY=YOURSECRET" -p 4040:4040 gettyimages/spark bin/spark-shell

To do a thing with Pyspark

    echo "import pyspark\nprint(pyspark.SparkContext().parallelize(range(0, 10)).count())" > count.py
    docker run --rm -it -p 4040:4040 -v $(pwd)/count.py:/count.py gettyimages/spark bin/spark-submit /count.py

## docker-compose example

To create a simplistic standalone cluster with [docker-compose](http://docs.docker.com/compose):

    docker-compose up --build

The SparkUI will be running at `http://${YOUR_DOCKER_HOST}:8080` with one worker listed. To run `pyspark`, exec into a container:

    docker exec -it spark_master /bin/bash
    bin/pyspark

To run `SparkPi`, exec into a container:

    docker exec -it spark_master /bin/bash
    bin/run-example SparkPi 10

To run `Jupyter notebook` with a running pyspark instance and connect it to MongoDB instance running on ${YOUR_MONGO_HOST}:
    
    docker exec -t -i spark_master bash
    cd bin
    ./pyspark --conf "spark.mongodb.input.uri=mongodb://172.17.0.2/measures.measure" \
            --packages org.mongodb.spark:mongo-spark-connector_2.10:2.0.0,org.apache.spark:spark-sql_2.10:2.0.2


To scale `N` further Spark workers (`N` must be greater of the created worker containers number):
   
   docker-compose scale worker=`N`

Please note that you cannot bind multiple containers to the same host port. To work this out, a reverse proxy needs to be used. 

To update the reverse proxy in order to check Spark workers Web UI:
   
    cd data/proxy/
    python proxier.py
    docker exec bash -c "nginx -s reload"

Pleas be sure *quik* and *docker-py* are installed to your host machine.

Spark worker web UIs are exposed at this URLs: `http://${YOUR_DOCKER_HOST}/workerN` where N in the index of the worker to be checked out (N starts from 0).

## license

MIT
