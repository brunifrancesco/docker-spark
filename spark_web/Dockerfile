FROM williamyeh/scala
RUN wget -c http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
RUN mkdir spark
RUN tar -xvf spark-2.1.0-bin-hadoop2.7.tgz -C spark
WORKDIR spark
CMD bash
