FROM apache/spark:4.0.2

# Install Python packages
COPY requirements.txt /opt/requirements.txt

RUN apt-get update && \
    pip3 install --no-cache-dir -r /opt/requirements.txt && \
    apt-get clean

# Install hadoop-aws and aws-java-sdk-bundle
ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/4.0.2/hadoop-aws-4.0.2.jar /opt/spark/jars/
ADD https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar /opt/spark/jars/
