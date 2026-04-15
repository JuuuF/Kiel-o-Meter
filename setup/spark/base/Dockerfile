FROM apache/spark:4.0.2

USER root

# Install hadoop-aws and aws-java-sdk-bundle
ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar /opt/spark/jars/
ADD https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar /opt/spark/jars/

# Install Python packages
COPY requirements.txt /opt/requirements.txt

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r /opt/requirements.txt && \
    apt-get clean

# Set working directory
WORKDIR /opt/spark

# Set Environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH=${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${PATH}

# Set user to "spark"
USER spark
