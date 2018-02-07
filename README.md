# BD_Project - Taxi Price Prediction - by Luis and Jelena
The analytic goal of our big data project was to forecast the price of a future taxi ride using the NYC taxi data set. Therefore, we  set up a streaming data pipeline (consisting of Kafka and Spark) to eventually model the processed data in pyspark with the python libraries mentioned under "prerequisites". The focus of the project lies rather on the simulation of a data stream and the implementation of the tools to receive this data, than constructing a very accurate statistical estimation model. So the current standing of the analytics part leaves room for further improvement.

Our currently implemented architecture is documented in the uploaded JPEG with the grey elements not being fully implemented yet.

## Prerequisites
- Cloudera Quickstart VM 5.12
- We used the following services: 
  - Spark 1.6, Yarn and Zookeeper; already active on the VM 
  - CDH 5.12 and Kafka 3.0 had to be downloaded and activated as parcels
- Download and install Python2.7 and the Jupyter Notebook (or Anaconda, where jupyter and the needed libraries are included)
- If not working with anaconda make sure you have the following Python libraries installed: pandas, sklearn, numpya and kafka

- Set the following paths so you can use jupyter to work with pyspark:

```
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
export PATH=/home/cloudera/anaconda2/bin:$PATH
export PYSPARK_PYTHON=/home/cloudera/anaconda2/bin/python
```

You might want to set them directly in the Cloudera Manager under the Spark configuration in the field Configuration Snippet /spark-env.sh.

## Data used
The base of data consisted of the 

## Data Slicing and Kafka Producer
In order to simulate a real-time data stream, we pre

## Spark Consumer
We implemented the Spark consumer in various ways, so the messages could be displayed on the screen. Nevertheless, we did not manage to directly store the received data in Spark DataFrames, which our further code is based on. It turned out that there is a handy function coming with Spark Version 2.2+, so upgrading Spark or finding a workaround are options for improving the pipeline. 

## Spark DataFrames and Model creation
 For the time being we have to take the data from HDFS and pretend it came from a Spark Consumer.
 Place a file into the HDFS, read it out and continue with processing in Spark DataFrames.
 If you want to work with CSVs start pyspark with the following parameter: 
 '''
 $ pyspark --packages com.databricks:spark-csv_2.11:1.4.0
 ''' 
This will install the csv databricks package which helps reading in csv Data without formally inferring the underlying schema by hand.
